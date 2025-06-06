"""Here we will have decryption of text
- The Same logic will be applied which was applied at encryption_plain.py
- The Only difference would be that -
    - Will use decryption token to make keys
    - We will make reversed key
- Ultimately we will make reversed dict of what used during encryption"""

#Importing modules
import string
import sympy


# Making a function for decryption
"""Just to remind -
- This functions structure should be similar to encryption_plain()
- Because this will be used in a same way it was used
- Will save a lot of time as we will not need to write whole code again"""

def decryption_plain(decryption_token, message):
    """Work done by it -
    - Will make key from decryption token
    - Will have the same conditions as it had in encrypt_plain.py
    - Just the keys will be reversed
    - At the end it will return the decrypted message"""

    """To covert decrypted token to keys -
    - We will make a list of characters 
    - This list will be kept in value side
    - As the code will be referring to them
    - So when we will put letters (from decryption token) in key 
    then they will match with the chars to whom they are 
    referring to in encrypted message
    - And we will use that dict for decryption"""

    #Making dict of decryption_token
    # Making keys of the dicts

    token = decryption_token.split("key0000")

    #Extracting keys
    key1 = list(token[0])
    key2 = list(token[1])
    key3 = list(token[2])
    key4 = list(token[3])
    key5 = list(token[4])
    key6 = list(token[5])

    # Making vars of characters
    letters = string.ascii_letters
    punctuation_for_list = string.punctuation
    digits = string.digits

    # Making value part of dicts
    var_for_values = list(letters + punctuation_for_list + digits + " ")

    # Making dict which will be the key for decryption
    # (connecting keys and values to make dicts)
    dict_key1 = dict(zip(key1, var_for_values))
    dict_key2 = dict(zip(key2, var_for_values))
    dict_key3 = dict(zip(key3, var_for_values))
    dict_key4 = dict(zip(key4, var_for_values))
    dict_key5 = dict(zip(key5, var_for_values))
    dict_key6 = dict(zip(key6, var_for_values))


    # These vars will be used further for different work
    msg_list = list(message)
    length = len(msg_list)
    final_msg = [] #All encrypted letters will be stored here

    # Now our dictionaries and all variables are ready, they will be used for decryption
    for num in range(length):
        char = msg_list[num]
        index = num + 1


        if (not sympy.isprime(index)) or (index == 1):
            #Will check for prime and 1

            if (index == 1) or (not index % 4 == 0 and not index % 5 == 0 and not index %2 == 0):
                # This will be checking for key 1(Composite and 1)

                final_msg.append(dict_key1.get(char, char))



            elif index %2 == 1 and not index %4 == 0 and not index %5 == 0:
                #Key2 check
                #This will check for odd and composite number

                final_msg.append(dict_key2.get(char, char))



            elif index %4 == 0 and not index %5 == 0 and not index %2 == 1:
                #Key 3 check
                #Divisible by four

                final_msg.append(dict_key3.get(char, char))



            elif index %5 == 0 and not index %4 == 0:
                #Key-4 check, divisible by 5 or not

                final_msg.append(dict_key4.get(char, char))


            else:
                #All the overlapping conditions will be covered here
                final_msg.append(dict_key5.get(char, char))


        elif sympy.isprime(index):

            final_msg.append(dict_key6.get(char, char))


    decrypted_msg = "".join(final_msg)

    print("Message decrypted successfully.....!!!!")
    return decrypted_msg

if __name__ == "__main__":
    decryption_key = input("Kindly enter the token : ")
    message_ = input("Kindly enter the message :) : ")
    print(decryption_plain(decryption_key, message_))