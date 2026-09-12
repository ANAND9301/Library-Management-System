import json 
import random
import string 
from pathlib import Path 
from datetime import datetime

class Library:
    def gen_id(Prefix="B"):
        random_id = " "
        for i in range(5):
            random_id += random.choices(string.ascii_uppercase + string.digits)[0]

        return Prefix + "-" + random_id





    def add_book(self):
        title = input("Enter Book title : ")
        author = input("Enter Book author : ")
        copies = int(input("Enter no. of Copies : "))

        book = {
            "id" : Library.gen_id(),
            "title" : title,
            "author" : author,
            "total_copies" : copies,
            "available_copies" : copies,
            "added_on" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        print(book)

hello = Library()

#Functionalities 
print("="*50)
print("Library Management System")
print("="*50)

print("1. Add book")
print("2. List book")
print("3. To add Member")
print("4. List members")
print("5. Borrow book")
print("6. Return book")
print("0. Exit the portal")

print("-"*50)

choice = input("What you Want to DO :  ")

if choice == "1":
    hello.add_book()