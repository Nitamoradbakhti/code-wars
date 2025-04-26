# #Your job is to write a simple password validation function, as seen on many websites.

# The rules for a valid password are as follows:

#     There needs to be at least 1 uppercase letter.
#     There needs to be at least 1 lowercase letter.
#     There needs to be at least 1 number.
#     The password needs to be at least 8 characters long.

# Your function takes a string argument and returns whether it is a valid password, as a boolean.
# Examples:

# "Abcd1234" ===> true
# "Abcd123" ===> false
# "abcd1234" ===> false
# "AbcdefGhijKlmnopQRsTuvwxyZ1234567890" ===> true
# "ABCD1234" ===> false
# "Ab1!@#$%^&*()-_+={}[]|\:;?/>.<," ===> true;
# "!@#$%^&*()-_+={}[]|\:;?/>.<," ===> false;

#Solutions:
def password(password_input):
 
    upper = any(st.isupper() for st in password_input)
    lower = any(st.islower() for st in password_input)
    digit = any(st.isdigit() for st in password_input)
    length = len(password_input) > 7
    return upper and lower and digit and length