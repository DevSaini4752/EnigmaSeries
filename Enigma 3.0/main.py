"""
So this will be the final module and
this will the motherboard of the
whole project which will connect all
the modules.
"""

"""This module is divide into some function -
function 1 - Encryption() - Will handle whole 
encryption part - Plain Text, txt, docx, pdf

function 2 - Decryption() - Will handle whole 
decryption part - Plain text, txt, docx, pdf

function 3 - Main() - Will handle function 1 
and function 2 and remaining things like 
documentation, my_journey, and exit"""

#Importing the internal and external modules
#For Normal Work
import os
import docx
import sys
from animations import type_write
from time import sleep as delay
import colours as c
import errors
import error_handler
from saving_token import store_token

#For Decryption
import decrypt_plain
import decrypt_txt
import decrypt_doc
import decrypt_pdf

#For Encryption
import encrypt_plain
import encrypt_txt
import encrypt_doc
import encrypt_pdf

#-----------Interactive text in vars for user-----------#

# ASCII art for welcoming user
welcome = f"""
{c.light_red}                ███████╗███╗   ██╗██╗ ██████╗ ███╗   ███╗ █████╗     ██████╗     ██████╗ 
{c.end}{c.light_yellow}                ██╔════╝████╗  ██║██║██╔════╝ ████╗ ████║██╔══██╗    ╚════██╗   ██╔═████╗
{c.end}{c.light_green}                █████╗  ██╔██╗ ██║██║██║  ███╗██╔████╔██║███████║     █████╔╝   ██║██╔██║
{c.end}{c.light_cyan}                ██╔══╝  ██║╚██╗██║██║██║   ██║██║╚██╔╝██║██╔══██║     ╚═══██╗   ████╔╝██║
{c.end}{c.light_blue}                ███████╗██║ ╚████║██║╚██████╔╝██║ ╚═╝ ██║██║  ██║    ██████╔╝██╗╚██████╔╝
{c.end}{c.pink}                ╚══════╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═╝ ╚═════╝ 

        {c.end}

{c.light_cyan}
Welcome to Enigma 3.0 - A master piece forged with passion, precision, 
and purpose. This is the place where innovation meets security.

Get ready to experience like never before...!!!"""

# ASCII art to see off user
see_off = (f"""
{c.cyan}████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗███████╗       ██╗    ██╗███████╗    ██╗  ██╗ ██████╗ ██████╗ ███████╗       {c.end}
{c.cyan}╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝██╔════╝       ██║    ██║██╔════╝    ██║  ██║██╔═══██╗██╔══██╗██╔════╝       {c.end}
{c.cyan}   ██║   ███████║███████║██╔██╗ ██║█████╔╝ ███████╗       ██║ █╗ ██║█████╗      ███████║██║   ██║██████╔╝█████╗         {c.end}
{c.light_blue}   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗ ╚════██║       ██║███╗██║██╔══╝      ██╔══██║██║   ██║██╔═══╝ ██╔══╝    {c.end}     
{c.light_blue}   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗███████║▄█╗    ╚███╔███╔╝███████╗    ██║  ██║╚██████╔╝██║     ███████╗       {c.end}
{c.light_blue}   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝     ╚══╝╚══╝ ╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝       {c.end}

{c.light_green}██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗██╗     ██╗         ██████╗ ███████╗████████╗██╗   ██╗██████╗ ███╗   ██╗    {c.end}
{c.light_green}╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║██║     ██║         ██╔══██╗██╔════╝╚══██╔══╝██║   ██║██╔══██╗████╗  ██║    {c.end}
{c.light_green} ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██║     ██║         ██████╔╝█████╗     ██║   ██║   ██║██████╔╝██╔██╗ ██║    {c.end}
{c.light_yellow}  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║     ██║         ██╔══██╗██╔══╝     ██║   ██║   ██║██╔══██╗██║╚██╗██║    {c.end}
{c.light_yellow}   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║███████╗███████╗    ██║  ██║███████╗   ██║   ╚██████╔╝██║  ██║██║ ╚████║    {c.end}
{c.light_yellow}   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   {c.end} 

{c.pink}                                ███████╗ ██████╗  ██████╗ ███╗   ██╗                                             {c.end}       
{c.pink}                                ██╔════╝██╔═══██╗██╔═══██╗████╗  ██║                                            {c.end}        
{c.pink}                                ███████╗██║   ██║██║   ██║██╔██╗ ██║                                             {c.end}       
{c.red}                                ╚════██║██║   ██║██║   ██║██║╚██╗██║                                             {c.end}       
{c.red}                                ███████║╚██████╔╝╚██████╔╝██║ ╚████║                                             {c.end}       
{c.red}                                ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝     {c.end}""")



#-----------------Encryption Part----------------#

#Funtion 1 - Encryption Part

def encryption():
    """Here we will only cover encryption-

    - First we will ask for an input method

    - Then we will execute things depending
    on the user's choice that whether they
    want to encrypt their text via plain text,
    text document, Word or PDF

    - After executing 1 option function will
    end."""

    while True:
        try:
            # Asking for an input type for encryption
            enc_input = (input(f"""{c.cyan}So what do you want to encrypt...?
        
a. Plain text
b. Text Document (.txt)
c. Microsoft Office Word (.docx)
d. PDF

Kindly choose one of the option letter (a/b/c/d) : {c.end}""").lower())

            #Executing the conditions based on user input (enc_input)
            #Condition 1 - a. Plain Text
            if enc_input == "a":#Plain Text
                #input
                message_enc = input(f"""{c.light_green}        
Kindly enter the message you want to encrypt : {c.end}""")

                #Checking for errors
                error_handler.validate_inputs(msg=message_enc)


                #Final output for user
                token_n_msg = encrypt_plain.encryption_plain(message_enc)
                print(f"""{c.red}
Kindly copy the message properly - Only copy the message in purple only otherwise you might end up having a wrong message!!
Here is your message....in purple..
Message - {c.end}{c.purple}
{token_n_msg[1]}{c.end}
""")
                #Storing token
                store_token(token_n_msg[0])

                #Pausing the program for 2 seconds
                #To make user experience better
                delay(2)
                break

            #Condition 1 is done, now shifting to condition 2
            elif enc_input == "b":# Text document
                #Taking inputs
                enc_input_b_file = input(f"{c.light_blue}Kindly enter the filename or path : {c.end}")
                enc_input_b_save_file = input(f"{c.light_green}Kindly enter the name by which you want to save it : {c.end}")

                #Checking for errors :|
                error_handler.validate_inputs(filename=enc_input_b_file, saving_name=enc_input_b_save_file, filetype=".txt")


                #Output
                token = encrypt_txt.encryption_txt(enc_input_b_file, enc_input_b_save_file)

                #Saving token
                store_token(token)

                #Delaying for user experience
                delay(2)
                break

                #Condition 2 ends

            elif enc_input == "c": # Word file
                #Taking inputs
                filename_enc_doc = input(f"{c.light_yellow}Kindly enter the filename : {c.end}")
                saving_name_doc = input(f"{c.light_blue}Kindly enter the name you want to save with : {c.end}")

                #Checking for errors :)
                error_handler.validate_inputs(filename=filename_enc_doc, saving_name=saving_name_doc, filetype=".docx")

                #Execution
                token_doc = encrypt_doc.encryption_doc(filename_enc_doc, saving_name_doc)

                #Output :)
                print(f"{c.bold_green}File saved successfully....!!!{c.end}")

                #Storing token
                store_token(token_doc)

                #Delaying for user experience
                delay(2)
                #Done :)
                break

            elif enc_input == "d": #PDF file

                # Warning user
                print(f"""{c.bold_red}Important Notice: This software supports only simple PDFs. PDFs with 
complex formatting, special fonts, or encrypted content may cause errors during encryption 
or decryption. Please ensure the PDF is a basic text document to avoid any issues.{c.end}""")

                #Taking inputs :|
                filename_pdf = input(f"{c.teal}Kindly enter file name : {c.end}")
                saving_pdf_doc = input(f"{c.sky_blue}Kindly enter the name with which you want to save your Word file : {c.end}")
                saving_pdf_pdf = input(f"{c.yellow}{c.green}Kindly enter the name with which you want to save your PDF file : {c.end}")
                while True:
                    version = input(f"{c.red}Is your microsoft version 2009 or before (y/n) : ").lower()
                    if version == "y" or version == "n":
                        break
                    else:
                        print(f"{c.red}Warning: Kindly tell (y/n), no other option is there{c.end}")

                #Checking for errors
                error_handler.validate_inputs(filename=filename_pdf, saving_name=saving_pdf_pdf, filetype=".pdf")

                #Execution :)
                token = encrypt_pdf.encryption_pdf(filename_pdf, saving_pdf_doc, saving_pdf_pdf, version)

                #Output :):)
                print(f"{c.light_green}File saved successfully...!!!{c.end}")

                #Storing token
                store_token(token)

                #Delaying.....
                delay(2)

                break
                #Done:)

            else:
                #If a user puts an invalid option
                print(f"""\n{c.red}Invalid input, kindly enter a option
(a/b/c/d){c.end}\n""")


        #Handling all errors (custom as well as built-in)

        # Error how length of token
        except errors.LengthException as len_ex:
            print(len_ex)
            break

        # Error for no msg
        except errors.NoMsgError as no_msg:
            print(no_msg)
            break

        # Error for an empty file
        except errors.EmptyFileException as empty:
            print(empty)
            break

        # Error for invalid name
        except errors.InvalidFileNameException as invalid_ex:
            print(invalid_ex)
            break

        # Error - UserFileNotFoundException
        except errors.UserFileNotFoundException as file_not_found:
            print(file_not_found)
            break

        # Error - FileAlreadyExistsException
        except errors.FileAlreadyExistsException as already_exists:
            print(already_exists)
            break

            # If person has entered wrong word file name
        except docx.opc.exceptions.PackageNotFoundError as ex:
            try:
                description = f"""{c.red}
Warning!!! : 

Kindly check whether the file path and name
is correct or not as we can't 
find the file/path which you gave. Kindly keep
these points in mind while inserting the 
path/file name -

-   If you are just putting file name
then confirm that file exist at same 
location as this program file exists

-   Kindly check for upper and lower case
letters in the path/filename as they are
common because of human error

-   Kindly take path or file name from
properties of the file only as it reduces 
the chances of human error significantly

Kindly check above points and retry{c.end}

{c.blue}{ex}{c.end}"""

                raise errors.UnexpectedError(description)
            except Exception as unexpected_error:
                print(unexpected_error)
                break


        # General Exception
        except Exception as ex:
            try:
                raise errors.UnexpectedError(ex)
            except errors.UnexpectedError as uex:
                print(uex)
                break

#---------------------Decryption Part---------------------#

def decryption():
    """Here we will execute everything
    such as input output adn exceptions

    Here is the path

    - Input
    - Decryption
    - Find errors
    - Tell errors to user (if there is)
    - Give out put"""

    #Keeping code in while True to re-execution
    while True:
        #Try and except for error handling
        try:
            dec_input = input(f"""{c.lime}Kindly choose what do you want to decrypt - 

a. Plain Text
b. Text Document (.txt file)
c. Word Document (.docx)
d. PDF

Kindly type the option (a/b/c/d) : {c.end}""").lower()

            #Executing options
            if dec_input == "a":#For plain text

                #Taking msg and token from user
                msg_dec_a = input(f"{c.blue}Kindly enter your message : {c.end}")
                token_dec_a = input(f"{c.purple}Kindly enter your token : {c.end}")

                #Checking for errors
                error_handler.validate_inputs(token=token_dec_a, msg=msg_dec_a)

                #Execution of decryption
                decrypted_msg_a = decrypt_plain.decryption_plain(token_dec_a, msg_dec_a)

                #Giving msg to user
                print(f"""{c.pink}Congratulation!!! Message decrypted successfully....
Your message - {decrypted_msg_a}{c.end}""")

                #Ending the loop :)
                break

            elif dec_input == "b":#For text document
                #Taking inputs
                filename_dec_b = input(f"{c.blue}Kindly enter your filename or path : {c.end}")
                saving_dec_b = input(f"{c.gold}Kindly enter name from which you want to save the file : {c.end}")
                token_dec_b = input(f"{c.purple}Kindly enter the decryption token : {c.end}")

                #Cheking for errors
                error_handler.validate_inputs(token=token_dec_b, filename=filename_dec_b, saving_name=saving_dec_b, filetype=".txt")

                #Executing a decryption process
                decrypt_txt.decryption_txt(filename_dec_b, saving_dec_b, token_dec_b)

                #Ending, bye :)
                break

            elif dec_input == "c":#For Word decryption
                #Takimg inputs
                filename_dec_c = input(f"{c.blue}Kindly enter the filename or path : {c.end}")
                saving_dec_c = input(f"{c.gold}Kindly enter the filename from which you want to save it : {c.end}")
                token_dec_c = input(f"{c.purple}Kindly enter the decryption token : {c.end}")

                #Chekcing for errors
                error_handler.validate_inputs(token=token_dec_c, filename=filename_dec_c, saving_name=saving_dec_c, filetype=".docx")

                #Executing a process
                decrypt_doc.decryption_doc(filename_dec_c, saving_dec_c, token_dec_c)

                #Ending process :)
                break

            elif dec_input == "d":#For PDF

                #Warning user
                print(f"""{c.bold_red}Important Notice: This software supports only simple PDFs. PDFs with 
complex formatting, special fonts, or encrypted content may cause errors during encryption 
or decryption. Please ensure the PDF is a basic text document to avoid any issues.{c.end}""")

                #Taking input
                filename_dec_d = input(f"{c.blue}Kindly enter the file name : {c.end}")
                saving_dec_d_doc = input(f"{c.olive}Kindly enter the filename with which you want to save it's word form : {c.end}")
                saving_dec_d_pdf = input(f"{c.teal}Kindly enter the filename with which you want to save it's PDF form : {c.end}")
                token_dec_d = input(f"{c.gold}Kindly enter the decryption token : {c.end}")
                while True:
                    version = input(f"{c.light_cyan}Is your microsoft version 2009 or before (y/n) : {c.end}").lower()
                    if version == "y" or version == "n":
                        break
                    else:
                        print(f"{c.red}Warning: Kindly tell y/n, no other option is there{c.end}")

                #Checking for errors
                error_handler.validate_inputs(token=token_dec_d, filename=filename_dec_d, saving_name=saving_dec_d_pdf, filetype=".pdf")

                #Checking for a docx file also, as one filetype at a time is there
                error_handler.validate_inputs(saving_name=saving_dec_d_doc, filetype=".docx")

                #Executing the process
                decrypt_pdf.decryption_pdf(filename_dec_d, saving_dec_d_doc, saving_dec_d_pdf, version, token_dec_d)

                #Ending the process :)
                break

            else:#Wrong input
                print(f"{c.red}\nInvalid input!!! Kindly enter correct in option (a/b/c/d) !!!\n")


        # Handling all errors (custom as well as built-in)

        # Error how length of token
        except errors.LengthException as len_ex:
            print(len_ex)
            break

        # Error for no msg
        except errors.NoMsgError as no_msg:
            print(no_msg)
            break

        # Error for an empty file
        except errors.EmptyFileException as empty:
            print(empty)
            break

        # Error for invalid name
        except errors.InvalidFileNameException as invalid_ex:
            print(invalid_ex)
            break

        # Error - UserFileNotFoundException
        except errors.UserFileNotFoundException as file_not_found:
            print(file_not_found)
            break

        # Error - FileAlreadyExistsException
        except errors.FileAlreadyExistsException as already_exists:
            print(already_exists)
            break

            # If person has entered wrong word file name
        except docx.opc.exceptions.PackageNotFoundError as ex:
            try:
                description = f"""{c.red}
        Warning!!! : 

        Kindly check whether the file path and name
        is correct or not as we can't 
        find the file/path which you gave. Kindly keep
        these points in mind while inserting the 
        path/file name -

        -   If you are just putting file name
        then confirm that file exist at same 
        location as this program file exists

        -   Kindly check for upper and lower case
        letters in the path/filename as they are
        common because of human error

        -   Kindly take path or file name from
        properties of the file only as it reduces 
        the chances of human error significantly

        Kindly check above points and retry{c.end}

        {c.blue}{ex}{c.end}"""

                raise errors.UnexpectedError(description)
            except Exception as unexpected_error:
                print(unexpected_error)
                break


        # General Exception
        except Exception as ex:
            try:
                raise errors.UnexpectedError(ex)
            except errors.UnexpectedError as uex:
                print(uex)
                break

#----Decryption and Encryption Function Ends :) Now Main function----#

def main():
    """Here we will execute final things and this method can be used
    anywhere. Here we are -
    - Welcoming user with some text
    - Giving options to user
    - Executing those things"""

    #Welcoming user with some effects
    type_write(welcome)

    #Keeping code in loop to keep it running
    while True:
        #Taking input
        user_request = input(f"""{c.light_purple}
So what do you want to do...?

a. Encryption
b. Decryption 
c. Feedback
d. Exit 

Kindly choose one of the option (a/b/c/d/e/f) : {c.end}""").lower()

        #Executing user's need
        #Encryption
        if user_request == "a":
            encryption()

        elif user_request == "b":
            decryption()


        elif user_request == "c":
            print(f"""{c.light_yellow}
            We value your feedback to keep making Enigma 3.0 better!
            {c.light_cyan}Feel free to share your thoughts, suggestions, or issues.
            {c.light_red}~ Dev Saini
            {c.end}""")

        elif user_request == "d":
            # Sending off user with some beautiful text
            type_write(see_off, wait=0.001)

            print("Thank you for using our services and We hope you will return soon....:)")
            sys.exit()

        else:
            print(f"""{c.red}Invalid option!!!
Kindly choose and type the option only (a/b/c/d/e/f)""")


if __name__ == "__main__":
    main()
    delay(7)#So that cmd don't close immediately after the process ends
    print("Bye-Bye...!!!")

#---Officially ending --- Journey - 11 April 2025 to 28 April 2025---#
