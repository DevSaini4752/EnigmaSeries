"""This will save the token in a text document which will
make it safe and easy to store otherwise coping the token
directly from a console can cause human error. It will save
the token with time stamp in name"""

#Importing modules
import time
import os.path
import colours as c

#Making the function
def store_token(token):
    #Putting time stamp in var
    time_ = time.strftime("%d-%m-%Y %I-%M %p")

    #Title of the file
    title = f"Token-{time_}.txt"

    #Making and saving file
    with open(f"{title}", "w") as file:
        file.write(f"""
This file contains the decryption token for your message or file. Please ensure that you store it securely, as it is necessary to decrypt your content.

**Important Notes:**

1. **Do not alter the token in any way.** Editing any part of the token may render the decryption process invalid.
2. When copying the token, **be sure to copy the entire line**. Any omission or modification could prevent successful decryption.

Here is your unique decryption token for the file:

{token}

Please copy the entire token above, and keep it safe. It is critical for decrypting your content.

**Disclaimer:**

- The token is generated with high security and should be kept private. 
- Sharing or modifying the token may compromise its security and the integrity of your file/message.

Thank you for using our service. If you have any questions or issues, feel free to reach out.

Kind Regards,  
Dev Saini
""")

    #Telling user about the file
    print(f"""{c.red}
Important note!!! - 

Your token is saved in a file in the same location of this file i.e. {c.gold}{os.path.abspath(title)}{c.end}{c.red}.
So you can find and use it whenever you want to decrypt your message :){c.end}""")

