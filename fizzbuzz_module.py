'''
def fizzbuzz(number_1, number_2):
    for i, item in enumerate(number_1):
        j = i
        if item != 'Fizz' and number_2[j] == 'Buzz':
           number_1[i] = 'Buzz'
        if item == 'Fizz' and number_2[j] == 'Buzz':
           number_1[i] = 'FizzBuzz'
    return number_1

def fizz(number_1):
    for i, item in enumerate(number_1):
        if not (item % 3):
            number_1[i] = 'Fizz'

def buzz(number_2):
    for i, item in enumerate(number_2):
        if not (item % 5):
            number_2[i] = 'Buzz'

def main():
    number_1 = list(range(1, 101))
    number_2 = list(range(1, 101))
    fizz(number_1)
    buzz(number_2)
    fizzbuzz(number_1, number_2)
    print(number_1)
'''

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        number = 'FizzBuzz'
    elif number % 3 == 0:
        number = 'Fizz'
    elif number % 5 == 0:
        number = 'Buzz'
    return number

def main():
    numbers = list(range(1, 101))
    for i in range(0, 100):
        number = numbers[i]
        number = fizzbuzz(number)
        numbers[i] = number
    print(numbers)


if __name__ == '__main__':
    main()
