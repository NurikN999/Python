# Class name should have first letter capitalized
# PascalCase


class User:

    def __init__(self):
        self.id = 1
        self.name = "Unknown"
        self.surname = "Unknown"

    def set_name_and_surname(self,name,surname):
        self.name = name
        self.surname = surname

    def set_id(self,id):
        self.id = id


    def print_info(self):
        print(f"Name: {self.name} \nSurname: {self.surname} \nID: {self.id}")



user_1 = User()
user_1.set_name_and_surname(input("Enter user's name: "),input("Enter user's surname: "))
user_1.set_id(int(input("Enter user's id: ")))

user_1.print_info()