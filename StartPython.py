#STEP1
#Get your name, last name and age
#Example: name lastname is age years old.
name = input("Please, write your name: ")
last_name  = input("Please, write your surname: ")
age = input("How old are you?: ")
print(f"{name} {last_name} is {age} years old.")

print ("*******************************************************************")
#STEP2
#Creating an e-mail address using first and last name in all small letters
#and print it on the screen.
name = name.lower()
last_name = last_name.lower()
web_site = input("Please, enter your website:")
mail_adres = print(f"{name}.{last_name}@{web_site}")
email = name.lower() + "." + last_name.lower() + "@" + web_site
print(email)

print ("*******************************************************************")
#STEP3
#Print on the screen the total number of characters of the name
#and surname information received from the user.

length = len(name+last_name)
print(f"Your name and last name length is:{length}")




                 
