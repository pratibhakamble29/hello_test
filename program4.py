# WAP to print numbers between 50 to 100 except those number which are not palindrome

num = 50

while num <= 100:
    first_digit = (num // 10) % 10
    last_digit = num % 10

    if first_digit == last_digit:
        num += 1
    else:
        print(num , end = " ")

    num += 1
