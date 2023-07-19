import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

def payment(request):
    if request.method == 'POST':
        # Get the amount from the form
        amount = int(request.POST.get('amount'))  # Assuming the amount is in cents

        # Get the credit card token submitted by the form
        token = request.POST.get('stripeToken')

        try:
            # Create a charge using the Stripe API with the provided amount
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description='Example charge',
                source=token,
            )
        except stripe.error.CardError as e:
            # If the charge is declined, display an error message
            return render(request, 'payment.html', {'error': e})

        # Payment successful; do something here, e.g., save the order in the database

        return redirect('payment_success')

    return render(request, 'payment.html')
