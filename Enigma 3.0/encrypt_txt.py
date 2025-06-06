"""- Not going to rewrite the whole code
- Will use encrypt_plain.py for encryption of text
- Will take out text from txt file
- Will put it into encrypt_plain.py function
- Then will take the message and will save it as it was given
- Will save a lot of time"""

#Importing python module
import encrypt_plain

# Making the function for taking out text from the .txt file
def encryption_txt(filename_txt, saving_name_txt):
    """- First, Going to handle correction
    - Check whether file name end with proper extension (.txt) or not
    - If not then will add
    - If there then pass
    - Then the code for taking out text from file
    - Then will put the text into encryption_plain function
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



    #Putting the text into function to encrypt it
    token_n_msg = encrypt_plain.encryption_plain(msg_txt)
    token = token_n_msg[0]
    final_msg = token_n_msg[1]

    #Saving the msg to file the user wants
    with open(saving_name_txt, "w", encoding="utf-8") as file_in:
        file_in.write(final_msg)

    #Telling user the file saved successfully
    print("File saved successfully!!!")

    #Returning the token as a message is already saved to the file
    return token

if __name__ == "__main__":
    print("Just some testing")
    trial1 = input("Enter the file name : ")
    trial2 = input("Enter the file name you want to save it with : ")
    decryption_token = encryption_txt(trial1, trial2)
    print(f"So here is your decryption_token - {decryption_token}")