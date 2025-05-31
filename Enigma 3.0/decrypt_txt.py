"""- Not going to rewrite the whole code
- Will use decrypt_plain.py for decryption of text
- Will take out text from txt file
- Will put it into decrypt_plain.py module and function
- Then will take the message and will save it as it was given
- Will save a lot of time"""

#Importing python module
import decrypt_plain
import colours as c

# Making the function for taking out text from the .txt file
def decryption_txt(filename_txt, saving_name_txt, token):
    """- First, Going to handle correction
    - Check whether file name end with proper extension (.txt) or not
    - If not then will add
    - If there then pass
    - Then the code for taking out text from file
    - Then will put the text into decryption_plain function
    - Will make a file wit same format
    - Will save the text in it
    - Not going to handle error here, will have a special module for it"""

    #Correction handling, correcting the user input
    if not filename_txt.endswith(".txt"):
        # Adding .txt to filename_txt if it's not present
        filename_txt += ".txt"

    if not saving_name_txt.endswith(".txt"):
        # Adding .txt to saving file name if it's not there
        saving_name_txt += ".txt"


    #Taking out text
    with open(filename_txt, "r", encoding="utf-8") as file_out:
        msg_txt = file_out.read()



    #Putting the text into function to decrypt it
    final_msg = decrypt_plain.decryption_plain(token, msg_txt)

    #Saving the msg to file the user wants
    with open(saving_name_txt, "w", encoding="utf-8") as file_in:
        file_in.write(final_msg)

    #Telling user the file saved successfully
    print(f"{c.salmon}File saved successfully!!!{c.end}")


if __name__ == "__main__":
    print("Just some testing")
    trial1 = input("Enter the file name : ")
    trial2 = input("Enter the file name you want to save it with : ")
    code = input("Kindly enter the decryption token : ")
    decryption_txt(trial1, trial2, code)