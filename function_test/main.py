from random import randint


def my_function (user:str, friend:str):
    print (f"Hi {user}. Nice to meet you!")
    print (f"I've heard you are a friend of {friend}")
    print (f"")

def add_nums (A:int, B:int):
    return int((A+B))

my_function("Samia","Foez")
my_function("Foez","Abida")
my_function("Abida","Hasma")
my_function("Hasma", "Samia")

print(f"SUM:{add_nums(5,6)}")
