class Test:
    def __init__(self):
        self.my_class_variable = 30
        self.name = "Unknown"


    def set_name(self,name):
        self.name = name


    def increase_var(self,n):
        self.my_class_variable += n


def function():
    test_obj = Test()
    print(f"Before increasing: {test_obj.my_class_variable}")
    n = int(input("Введите число, на которое вы хотите увеличить число: "))
    test_obj.increase_var(n)
    print(f"After increasing: {test_obj.my_class_variable}")
    print(f"Name: {test_obj.name}")
    name = input("Enter user's name: ")
    test_obj.set_name(name)
    print(f"Name after change: {test_obj.name}")


function()