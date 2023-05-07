# Create a program that asks the user for a number and then
#     prints out a list of all the divisors of that number.
#

number = int(input("Podaj liczbe "))
divisors = []

for element in range(1, number + 1):
    if number % element == 0:
        divisors.append(element)
#
# print('Divisors of ', number, 'are ', divisors)
print('Divisors of {} are {}'.format(number, divisors))
