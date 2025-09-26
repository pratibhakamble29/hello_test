bank_account_number = int(input("Enter bank account number :"))
account_holder_name = input("Enter account holder name : ")
gender = input("Enter gender : ")
birth_date = input("Enter birth date : ")
city = input("Enter your city : ")
opening_balance = int(input("Enter opening balance :"))

interest_amount = (opening_balance * (3/100))
print("interest Amount : ", interest_amount)

total_available_balance = (interest_amount + opening_balance)
print("Total available balance is :",total_available_balance)
