import random
import string

while True:
    code = input("Kindly enter the message (With at least 3 characters) : ") # Ask user for message, He/she want to code
    print("a. Code")
    print("b. Decode")
    print("c. exit")
    choice = input("What do you want : ") # Allow user to choose to code or decode
    if choice == "a": # The system will work depending on the user's choice of coding or decoding the message
        code = code[::-1] # Will reverse the string(message)
        for _ in range(3): # Will add 4 random characters at starting and ending
            code = (random.choice(string.ascii_letters)) + code + (random.choice(string.ascii_letters)) # ascii_letters is a function of string module containing all alphabets in both upper and lower case
        code = code.replace(" ", "rgmvooyorqe") # Will put random characters from options at the place of space
        print("Here is your coded message : ", code)# Gives you final codr
    
    elif choice == "b":
        code = code.replace("rgmvooyorqe", " ")#Decodes the whole message, reversing all methods of codind
        code = code[3:-3]
        code = code[::-1]
        print(code)
    
    elif choice == "c":#Closes the program
        print("Thank you for using me")
        break
    
    else:
        print("Kindly enter from the following options")#If written something else then instead of error it gives a try