"""This module is made to analyze
the codes and inputs of user in
main.py and will find normal and
custom errors for errors module,
this will raise them and will guide
the user if any exception occurs"""

"""
- There will be optional parameters
- And they will be checked for correction
for e.g. if a token para is there then it 
will be checked for 605 digits

- The "try" and "except" will be in this 
module only so that it will be raised 
automatically and if the error is raised 
then user will be asked for inputs again
"""
#Importing errors
import errors
import pdfplumber
import docx
import os
import colours as c


#Making a module :)
def validate_inputs(token=None, filename=None, saving_name=None, filetype=None, msg=None):

    try:
        #Asking user for filetype if
        #user gives the filename
        if (filename is not None or saving_name is not None) and filetype is None:
            raise ValueError(f"""{c.red}
Warning :
If you are putting filename 
or saving_name then it's 
mandatory to give value 
of filetype !!!
{c.end}""")



        # Checking for errors
        #Token check
        if not token is None:
            # Token length check

            if not len(token) == 605:
                raise errors.LengthException(str(len(token)))

        if not filename is None:

            #Correction in filename
            if not filename.endswith(filetype):
                filename += filetype

            #Cheking whether file exists or not
            #Also checking whether the file is empy or not

            if filetype == ".txt":
                file = open(filename, "r")
                text = file.read()
                file.close()
                #Raising error if a file is empty
                if text == "":
                    raise errors.EmptyFileException

            if filetype == ".pdf":
                text = pdfplumber.open(filename)
                empty_check = any(page.extract_text() for page in text.pages)
                if not empty_check:
                    raise errors.EmptyFileException
                text.close()

            if filetype == ".docx":
                text = docx.Document(filename)
                empty_check = any(page.text for page in text.paragraphs)
                if not empty_check:
                    raise errors.EmptyFileException



        if not saving_name is None:
            #Correction in saving name
            if not saving_name.endswith(filetype):
                saving_name += filetype


            #Checking for invalid name
            for char in saving_name:
                if char == "/" or char == ":" or char == "*" or char == "?" or char == "<" or char == ">" or char == "|" or char == "`":
                    raise errors.InvalidFileNameException(saving_name)



            #Cheking whether a file already exists or not
            y_or_n = os.path.exists(saving_name)
            if y_or_n:
                raise FileExistsError

        #Checking is there is no msg or empty str
        if msg == "":
            raise errors.NoMsgError


    #Handling some Errors others to be handled in main.py
    #Error for File not found
    except FileNotFoundError:
        raise errors.UserFileNotFoundException(filename)

    #Error for a file already exists
    except FileExistsError:
        raise errors.FileAlreadyExistsException(saving_name)

    #Handling errors for telling user about error
    """Here we not going to handle 
    all error because we can't break 
    the loop of main.py so controlling 
    those exceptions there only"""





#Testing and debugging side
if __name__ == "__main__":
    help(docx.opc.exceptions.PackageNotFoundError)
