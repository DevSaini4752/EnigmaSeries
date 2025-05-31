"""So here we are going to make all
the custom errors -
•	Length not matching error – Here we
 will check for length of token, if it
 doesn’t match with the necessary length which
 is 605, then we will ask user for token
 again.

•	File is not found error
•	File already exists error
•	No message error – If there is
no message then we will give this
error, like if user gives unexpected

•	Unexpected error – This will be
for all the other errors that can be
there, so that if I left with any error,
 then it can control or manage it.

•	EmptyFileError
•   InvalidFileNameException - So there 
are some rules of naming the files in 
windows and other, and I'm designing this
project for windows only and some symbols 
are there i.e. \\/:*?<>|` So there
will be an error that will be raised if 
any of these symbols is there.

"""
#Importing colors to give color to description of bug
import colours as c



# Error for length check
class LengthException(Exception):
    """If the decryption token's length
    is not 605, then this error will be
    thrown :) """

    def __init__(self, value):
        self.value = value
        description = (f"""{c.red}Kindly enter correct decryption token,
the decryption token has a length of {c.end}{c.light_cyan}605{c.end}{c.red} digit 
and the length of your token is : {c.end}{c.light_cyan}{self.value}{c.end}""")
        super().__init__(description)


# FileNotFoundError
class UserFileNotFoundException(Exception):
    """So I'm making this custom exception
    as I want a custom behavior of error
    and real one doesn't give me that much
    custom message power"""

    def __init__(self, filename):
        msg_file_not_found = (f"""{c.red}
Warning!!! : 

Kindly check whether the file path and name{c.end}{c.cyan} 
({filename}){c.end}{c.red} is correct or not as we can't 
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

Kindly check above points and retry{c.end}""")
        super().__init__(msg_file_not_found)


# FileExistsException
class FileAlreadyExistsException(Exception):
    """So I'm making this custom exception
        as I want a custom behavior of error
        and real one doesn't give me that much
        custom message power"""
    """This error is for if the user wants to 
    save the file, but another file exists 
    with same name and type then this error 
    would be raised."""

    def __init__(self, filename):
        msg_file_exists = (f"""{c.red}
Warning!!! : 

The filename with which you want to 
save the file {c.end}{c.cyan}({filename}){c.end}{c.red} already 
exists with same format in the location
which you gave so kindly do one of
the step - 

1. Change file name
2. Change file location

Kindly keep this thing in mind!!!{c.end}""")

        super().__init__(msg_file_exists)


#NoMsgError
class NoMsgError(Exception):
    """So this exception will be for
    the condition where the user doesn't
    put any text in plain text input"""

    def __init__(self):
        msg_no_msg = f"""{c.red}
Warning!!! : 

Kindly put some text in the plain text
input which we can encrypt, your input
doesn't contain any text, so kindly put 
a message in it.{c.end}"""

        super().__init__(msg_no_msg)


#UnexpectedException
class UnexpectedError(Exception):
    """Just for the condition if any
    exception occurs which is not in our
    system"""

    def __init__(self, exception_name):
        msg_unexpected = f"""{c.red}
Sorry to inform you but some unexpected 
error occurred and we are extremely sorry
to you :( 

Exception : 
{c.end}{c.light_blue}
{exception_name}{c.end}"""

        super().__init__(msg_unexpected)


#EmptyFileError
class EmptyFileException(Exception):
    """To inform user that no text is
    there in the file which they are
    asking for"""

    def __init__(self):
        msg_no_text = f"""{c.red}
Warning :

There is no text in the file you are
asking for. So, kindly check for the 
file properly then try again later!!!
{c.end}"""
        
        super().__init__(msg_no_text)
        
        
#InvalidFileNameException
class InvalidFileNameException(Exception):
    """To inform user about restricted symbols
    in the filename which they want to save with"""
    
    def __init__(self, filename):
        msg_invalid_filename = f"""{c.red}
Warning : 

The symbols which you are using in the 
name of the file {c.end}{c.cyan}({filename}){c.end}{c.red} are 
restricted in the windows environment 
so you can't use them. The symbols are - 
 \\ / : * ? < > | ` 
So kindly correct the name and Try Again!!!

:)
{c.end}"""
        super().__init__(msg_invalid_filename)






if __name__ == "__main__":
    try:
        user = int(input("Enter : "))
        if user == 1:
            raise LengthException(value=user)
        elif user == 2:
            raise UserFileNotFoundException("Filename/path")
        elif user == 3:
            raise FileAlreadyExistsException("Filename/ path")
        elif user == 4:
            raise UnexpectedError

    except Exception as e:
        print(e)
