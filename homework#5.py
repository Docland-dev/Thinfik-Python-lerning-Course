"""Python Easy Online class,
Homework #5: Basic Loops"""

#looping through numbers from 1 - 100
for number in range(100): #checking if number is divisible by both 3 and 5
        if (number % 3 == 0) and (number % 5 == 0):
            print('FizzBuzz')
            continue
        if number%3 == 0: #checking if number is divisible by 3
            print('Fizz')
            continue
        if number%5 == 0: #checking if number is divisible by 5
            print('Buzz')
            continue
        for i in range(2, number): #checking if number is a prime number
            if number % i == 0:
                break
        else:
            print('Prime')
            continue
        print(number)
    

    
    