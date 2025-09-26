'''
Write a python program to validate the details provided by a user as part of registering to a web application. 
Write a function validate_name(name) to validate the user name 
Name should not be empty, name should not exceed 15 characters 
Name should contain only alphabets 
Write a function validate_phone_no(phoneno) to validate the phone number 
Phone number should have 10 digits 
Phone number should not have any characters or special characters 
All the digits of the phone number should not be same. 
Example: 9999999999 is not a valid phone number 
Write a function validate_email_id(email_id) to validate email Id 
It should contain one '@' character and '.com' 
'.com' should be present at the end of the email id. 
Domain name should be either 'gmail', 'yahoo' or 'hotmail' 
Note: Consider the format of email id to be username@domain_name.com 
All the functions should return true if the corresponding value is valid. Otherwise, it should return false. 
Write a function validate_all(name,phone_no,email_id) which should invoke appropriate functions to validate the arguments 
passed to it and display appropriate message. Refer the comments provided in the code. 
Note: You may use str.isalpha(), str.isdigit() methods to check whether a string contains alphabets or digits alone.t
'''

def validate_name (name:str):
    if not name:
        return false
    if len(name) > 15:
        return false
    if not name.isalpha():
        return false
    return True

def validate_phone_no(phoneno:str):
    if len(phoneno) != 10:
        return false
    if not phoneno.isdigit():
        return flase
    if len(set(phoneno)) == 1:
        return false
    return True

def validate_email_id(email_id :str) -> bool:
    if email_id.count("@") != 1:
        return false
    if not email_id.endswith(".com"):
        return false

    username , domain_part = email_id.split("@")

    domain_name = domain_part[:-4]

    if domain_name not in ["gmail" , "yahoo", "hotmail"]:
        return false
    if not username:
        return false
    return True

def validate_all(name:str , phoneno : str , email_id : str):
    if not validate_name(name):
        print("Invalide name! Name should br alphabates only, no empty, max 15 char")
    else:
        print("Name is valid")

    if not validate_phone_no(phoneno):
        print("Invaide phone number! phone number should be 10 digit, all digit, and all digit should not be same.")
    else:
        print("Phone number is valid.")

    if not validate_email_id(email_id):
        print("Invalide email id ! Email should be in format username@domain.com where domain is gmail, yahoo or hotmail.")
    else:
        print("Email Id is valid.")

name_input = "pratibhakamble"
phone_number_input = "1234456895"
email_id_input = "pratukamble5@gmail.com"

validate_all(name_input, phone_number_input, email_id_input)


