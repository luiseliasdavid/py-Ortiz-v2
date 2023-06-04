my_number = 324324
my_list = [int(digit) for digit in str(my_number)]

while len(my_list) > 1:
    result = 0
    for number in my_list:
        result += number
    my_list = [int(digit) for digit in str(result)]

print(my_list)

def digital_root(n):
    while n > 9:
        digit_list = [int(digit) for digit in str(n)]
        n = sum(digit_list)
    return n

print(digital_root(324324))


a = [0,1]
b= sum(a)
print(b)