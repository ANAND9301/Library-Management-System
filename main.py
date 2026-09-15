import json 
import random
import string 
from pathlib import Path 
from datetime import datetime

class Library:
    database = "library.json"

    data = {"books" :[],"members" :[]}

    #load Existing data to json 

    if Path(database).exists() :
        with open(database,"r") as fs :
            content = fs.read()
            if content :
                data = json.loads(content)
    else :

        with open(database,"w") as fs :
            json.dump(data,fs,indent=4)


    @classmethod
    def save_data(cls):
        with open(cls.database,"w") as f:
            json.dump(cls.data,f,indent = 4 , default = str)

    


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

        Library.data['books'].append(book)
        Library.save_data()


    def list_books(self):
        if not Library.data['books']:
            print("NO Books available")

        for b in Library.data['books']:
            print(f"{b['id'][:12]:20}{b['title'][:24]:25} {b['author'][:19]:20}{b['total_copies']}/{b['available_copies']}")


    def add_member(self):
        name = input("Enter your name:  ")
        email = input("Enter your email_id:   ")

        member = {
            "id" : Library.gen_id("M"),
            "name" : name,
            "email" : email,
            "borrowed" : []
        }

        Library.data['members'].append(member)
        Library.save_data()
        print("Member added successfully!!!")

    def list_members(self):
        if not Library.data['members']:
            print("NO members available")
        
        for m in Library.data['members']:
            print(f"{m['id']:20}{m['name'][:24]:25} {m['email'][:29]:30}")
            print(f"Borrowerd books :: {m['borrowed']}")

    def borrow_book(self):
        member_id = input("Enter the member ID : ").strip()
        members = [m for m in Library.data['members'] if m['id'] == member_id]
        if not members:
            print("No Such ID exists! ")

            return
        member = members[0]



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

if choice == "2":
    hello.list_books()

if choice == "3":
    hello.add_member()

if choice == "4":
    hello.list_members()

if choice == "5":
    hello.borrow_book()
