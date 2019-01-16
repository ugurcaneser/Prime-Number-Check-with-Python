def isPrime(number):
    if (number == 1):
        return False
    elif (number == 2):
        return True
    else:
        for i in range(2, number):
            if (number % i == 0):
                return False
        return True
while True:
    number = input("Enter a number: ")
    if (number == "q"):
        break
    else:
        number = int(number)
        if (isPrime(number)):
            print(number, "is a prime number!")
        else:
            print(number, "is NOT a prime number!")
