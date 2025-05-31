"""This module is to be used for
opening and printing the text of
documentation of the project."""

#Importing Module
import sys
import os
import os.path
import time

def documentation_open():
    """Here we will just open the text
    file of documentation, before it, we
    will find its relative path which
    will be useful in .exe file because
    it can't access the files easily as
    it put them in a temporary folder"""

    #Getting the path and other necessary things
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    final_path = os.path.join(base_path, "Documentation.txt")

    #Printing the text
    with open(f"{final_path}", "r") as file:
        data = file.read()
        print(data)
        print("Wait for 3 seconds for file.....")


    #delaying
    time.sleep(3)


    #Opening the file
    os.system(f"start {final_path}")




if __name__ == "__main__":
    print("Testing....")
    documentation_open()