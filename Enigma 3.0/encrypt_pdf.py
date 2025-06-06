"""
- Not going to rewrite the whole code
- Will use encrypt_plain.py for encryption of text
- Will take out text from PDF file
- Will put it into encrypt_plain.py function
- Will save the text in Word file
- Then make a copy of that word file in PDF format
- Will save a lot of time
"""

# Importing modules
import encrypt_plain  # File for encryption
import pdfplumber
import docx
from docx2pdf import convert


"""
Modules -
- pdfplumber will take out text
- docx will save and make the Word file
- docx2pdf will be used for converting Word file to PDF
"""



# Making the function for the whole process
# It will encrypt and give you decryption token
def encryption_pdf(filename_pdf, saving_name_doc, saving_name_pdf, checking_version_office):
    """
    - First, Going to handle correction
        - Check whether file name ends with proper extension (.pdf) or not
        - If not then will add
        - If there, then pass
        - Then the code for taking out text from file
        - Will take out text
        - Will encrypt it
        - Will save it in word file
        - Will covert it into PDF
        - As we can't write text in pdf
        """



    """Here we will check further for version of microsoft word 
    of user as our docx2pdf is better module but it don't work 
    in microsoft version 2009 or before, and we will not provide
    services for microsoft version 2009 or before."""




    # Correction handling, correcting the user input
    if not filename_pdf.endswith(".pdf"):
        # Adding .pdf to filename_pdf if it's not present
        filename_pdf += ".pdf"

    if not saving_name_pdf.endswith(".pdf"):
        # Adding .pdf to saving file name if it's not there
        saving_name_pdf += ".pdf"

    if not saving_name_doc.endswith(".docx"):
        # Adding .docx to saving file name if it's not there
        saving_name_doc += ".docx"


    # Opening the file and taking text
    full_text = []
    file_out = pdfplumber.open(filename_pdf)  # Opening PDF
    length = len(file_out.pages)
    for x in range(length):
        page = file_out.pages[x]
        text = page.extract_text()
        full_text.append(text)

    #closing the PDF
    file_out.close()


    # Taking text and putting the text into a single variable
    full_text_final = "\n".join(full_text)


    # Encrypting the message
    token_msg_pdf = encrypt_plain.encryption_plain(full_text_final)

    # Token and message as the encryption_plain func returns in tuple
    token_doc = token_msg_pdf[0]
    encrypted_msg = token_msg_pdf[1]

    # Saving the msg in a Word file
    saving_file = docx.Document()
    saving_file.add_paragraph(encrypted_msg)
    saving_file.save(saving_name_doc)

    #Saving the same file as PDF (converting that word file to PDF)
    #Saving the file depending on a version of microsoft
    if checking_version_office == "n":
        convert(saving_name_doc, saving_name_pdf)
        """A reminder to be given that this program only works for word 2010+ 
        Microsoft Word, because docx2pdf only works for 2010+ versions"""

    elif checking_version_office == "y":
        print("""Sorry this program is not suitable for Microsoft version 2009 or before :( But 
your docx form of this module is saved :)""")

    # Telling user the file saved successfully
    print("File saved successfully!!!")

    # Returning the token as a message is already saved to the file
    return token_doc


if __name__ == "__main__":
    print("Testing the method")
    trial01 = input("Kindly enter the pdf file name : ")
    trial02 = input("Kindly enter the name by which you want to save docx file : ")
    trial03 = input("Kindly enter the name by which you want to save pdf : ")
    checking_version = input("Version : ")
    print(encryption_pdf(trial01, trial02, trial03, checking_version))