def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} - Fizz_Buzz")
        elif i % 3 == 0:
            print(f"{i} - Fizz")
        elif i % 5 == 0:
            print(f"{i} - Buzz")
        else:
            print(i)


number = int(input("Введите число: "))
fizz_buzz(number)
