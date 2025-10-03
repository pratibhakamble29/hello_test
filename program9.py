'''
write menu driven applications pythin code to handle bank accpunt transictions 
1. Open Account
2. Show Account
3. Deposite Account
4. Withdraw Account
5. Exist
'''
import os

while True:
    print("1. open account ")
    print("2. show account ")
    print("3. deposite account")
    print("4. withdraw account")
    print("5. exist")

    choice = int(input("Enter your choice :"))
    os.system("cls")

    if choice == 1:
        accountnum = int(input("Enter your account number : "))
        accname = input("Enter account holder name :")
        balance = int(input("Enter opening balance :"))
        print(f"hello {accname} your Bank Account opened successfully :")

    elif choice == 2:
        user_acno = int(input("Enter your account number to show account :"))
        if user_acno == accountnum:
            damt = int(input("Enter Amount :"))
            balance += damt
            print(f"Rs.{damt} Credited to your account")
        else:
            print("Account number is invalid.")

    elif choice == 3:
        user_acno = int(input("Enter your account number to depostie amount:"))
        if user_acno == accountnum:
            print(f"Account Details : {accountnum} \t {accname} \t Rs.{balance}")
            print("------------------------------ ~ ------------------------------")
        else:
            print("Account Number invalid.")


    elif choice == 4:
        user_acno = int(input("Enter your account number to withdraw amount : "))
        if user_acno == accountnum:
            wamt = int(input("Enter Amount : "))

            if wamt <= balance:
                print(f"Rs.{wamt} debited from your account.")
                balance -= wamt
            else:
                print("Less balance to withdraw amount.")
        else:
            print("Account number is invalid.")

    elif choice == 5:
        break

    else:
        print("Invalid choice Enter Correct.")

