#Importing modules
import sys

#Assigning letters
dict0 = {
    'A': 'M', 'B': 'Q', 'C': 'W', 'D': 'E', 'E': 'R', 'F': 'T', 'G': 'Y', 'H': 'U', 'I': 'I', 'J': 'O', 'K': 'P', 'L': 'A',
    'M': 'S', 'N': 'D', 'O': 'F', 'P': 'G', 'Q': 'H', 'R': 'J', 'S': 'K', 'T': 'L', 'U': 'Z', 'V': 'X', 'W': 'C', 'X': 'V',
    'Y': 'B', 'Z': 'N', '0': '9', '1': '8', '2': '7', '3': '6', '4': '5', '5': '4', '6': '3', '7': '2', '8': '1', '9': '0',
    ' ': '#', '.': ',', ',': '.', '!': '?', '?': '!', '-': '_', '_': '-', '(': ')', ')': '(', '[': ']', ']': '[', '{': '}',
    '}': '{', '<': '>', '>': '<', '@': '$', '$': '@', '%': '^', '^': '%', '&': '*', '*': '&', '+': '=', '=': '+', '/': '\\',
    '\\': '/', '|': ';', ';': '|', ':': "'", "'": ":", '"': '`', '`': '"'
}
#making its reverse dictionary

reverse_dict0 = dict(zip(dict0.values(), dict0.keys()))

# Encoder func.

def encoder(x):
    ux1 = list(x)
#    print(type(ux1))
    for n in range(len(ux1)):
        something = ux1[n]
#        print('this is ux1 -',ux1, type(ux1))
#        print('its n-',n, type(n))
#        print('this is something -',something, type(something))
#        print('this is dict0 -',dict0, type(dict0))
        ux1[n] = dict0.get(something, something)
    encoded_message = ''.join(ux1)
    print("Your encoded message is - ",encoded_message, "\n")
    
    
#Decoder func.

def decoder(x):
    ux1 = list(x)
    for n in range(len(ux1)):
        something = ux1[n]
        ux1[n] = reverse_dict0.get(something, something)
    decoded_message = ''.join(ux1)
    print("Your decoded message is - ", decoded_message, "\n")
    





#Final execution
while True:
    request = input("Enter the message : ").upper()
    while True:
        enorden = input("""So what do you want to do with the message ?
        a. Encode
        b. Decode
        c. End program
        Choose one of the option(a/b/c) - """)
        if enorden.lower() == 'a':
            encoder(request)
            break
        elif enorden.lower() == 'b':
            decoder(request)
            break
        elif enorden.lower() == 'c':
            print('\nThank You for using our application, I hope you come back soon :-)'.center(100 ,' '))
            sys.exit()
        else:
           print("Kindly choose a valid option\n\n")
           
        
            
        
            
