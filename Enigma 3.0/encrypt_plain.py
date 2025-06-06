#Importing modules
import sympy
#This ^ module will allow us to check for prime and composite number
import mydata

"""So here for this encryption we will have 6 dynamic keys which we will import from "mydata.py".
So there will be six condition for the encryption, as we have poly alphabetic encryption so here
we will replace the character based on its index, and there will be 6 condition which will be
applied to index and the character will change based on which condition do it fulfills, so here
is our conditions -
	Key 1 – If index == composite num and "1" will also be here
	Key 2 – If index == composite and odd
	Key 3 – If index == composite and divisible by 4
	Key 4 – If index == composite and divisible by 5
	Key 5 – If index == overlapping condition e.g. composite, odd and divisible by 5
	Key 6 – If index == Prime number
"""

def encryption_plain(text): #So here I have put "text" as a parameter
    # which will the message who has to be encrypted
    """But…..before making the keys and conditions for index of character,
    we have to make the message to list and make the thing such that
    it can be placed into those conditions.

    It will use a for loop. And the process will be like this –

1.	Message to list
2.	For loop will take the character one by one and passing them through the conditions, and after it
changes it will be placed into an empty list
3.	At last that list will be converted into a message and will be returned
4.	By the time this process ends, we will save all the keys as a decryption token in a variable.
5.	At the end of the module, it will return a tuple containing message and decryption token.
6.  First element of tuple - Decryption Token
7.  Second element of a tuple - Encrypted message
"""
# defining the variable to be used further
    msg_list = list(text)
    length = len(msg_list)
    final_msg = [] #All encrypted letters will be stored here

    # So here these are all the functions for keys from "mydata.py" and we are
    # executing it as well as saving the key in variables which were returning from
    # those functions
    dict_key1 = mydata.key1()
    dict_key2 = mydata.key2()
    dict_key3 = mydata.key3()
    dict_key4 = mydata.key4()
    dict_key5 = mydata.key5()
    dict_key6 = mydata.key6()



    # Now using for loop and will put all keys and condition in it so that it can be applied to every character
    for num in range(length):
        char = msg_list[num]
        index = num + 1

        #The conditions which will put the character for different keys

        if (not sympy.isprime(index)) or (index == 1):
            #Will check for composite and 1

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


# So now we are making the decryption token where all the keys will be connected with
# "key0000" and it will be used in decryption

    # These are the keys, we are joining them for decryption token
    token1 = "".join(dict_key1.values())
    token2 = "".join(dict_key2.values())
    token3 = "".join(dict_key3.values())
    token4 = "".join(dict_key4.values())
    token5 = "".join(dict_key5.values())
    token6 = "".join(dict_key6.values())

    #Making final token
    all_tokens = [token1, token2, token3, token4, token5, token6]
    decryption_token = "key0000".join(all_tokens)

    #Making and returning the whole message
    final_msg_returning = "".join(final_msg)

    """Here we are returning two variables, first one is token 
    and second is message, so they must be accessed accordingly :)"""

    return decryption_token, final_msg_returning

if __name__ == "__main__":
    print("Just some testing")
    user_msg = input("Enter : ")
    testing = encryption_plain(user_msg)
    print(testing[0])
    print(testing[1])