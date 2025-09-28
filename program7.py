#WAP to input total amount, required no . of years, age of person check wether following condition to determine wether a person eligible for loan or not
'''1) age is more than 50 sthen person is eligible for macimum loan of 5 lakhs
2) if age is between 30 and 50 then person is eligible for maximum loan of 3 lakhs
3) if age is between 20 and 30 then person is eligible for maximum loan of lakhs
4) if age is bellowed 20 the person is not eligible'''

total_amount= int(input("Enter total amount : "))
no_of_years = int(input("Enter number of year : "))
age = int(input("Enter age : "))

if age > 50:
    print("Person is eligible for maximum loan of 5 lakhs ")
elif age > 30 and age < 50:
    print("Person is eligible for maximum loan of 3 lakhs ")
elif age > 20 and age < 30:
    print("Person is eligible for maximum loan of 2 lakhs ")     
elif age < 20:
    print("person is not eligible")

