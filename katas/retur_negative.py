#In this simple assignment you are given a number and have to make it negative. 
#But maybe the number is already negative?

def make_negative( number ):
     int(f"-{number}")if number > 0 else number



print(make_negative(5))
print(make_negative(-5))