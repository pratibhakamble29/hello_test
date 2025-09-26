#WAP to print number between 1 to 500 skipping numbers which are ending with digit wither 0 , 5 , 9

num = 1

while num <= 500:
    last_digit = num % 10

    if last_digit == 0 or last_digit == 5 or last_digit == 9:
        num += 1
    else:
        print(num , end = " ")

    num += 1
