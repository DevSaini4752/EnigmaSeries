"""This module is to open developers journey document"""

#Importing Module
import sys
import os
import os.path
import time
import colours as c

def journey_doc_open():
    """Here we will just open the Word file,
    before it, we will find its relative
    path which will be useful in .exe
    file because it can't access the files
    easily as it put them in a temporary folder"""

    print(f"""{c.light_red}The file which will be opened in 5 seconds, This 
is my whole journey of making this whole project and 
my efforts and emotions are defined in it and I will 
be thankful to you if you read it properly{c.end}""")

    #Giving time to user to read the above message
    time.sleep(5)

    #Getting the path and other necessary things
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    final_path = os.path.join(base_path, "Enigma_3.0_journey.docx")


    #Opening the file
    os.system(f"start {final_path}")


if __name__ == "__main__":
    print("Testing....")
    journey_doc_open()