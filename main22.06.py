

a = int(input())
b = int(input())
d = int(input())
c = [a, b, d]

for i in c:
    with open('text20.06.txt', 'a+', encoding="utf8") as file:
        file.write(str(i) + '\n')
unpacking = open('text20.06.txt', 'r')
n = [i.strip() for i in unpacking]

num = map(lambda)
print(n)

#next_stage

my_list = []

def inputs():
    cycle = True
    while cycle:
        a = input()
        if a != "end" and len(a) > 0:
            my_list.append(a)

        elif len(a) == 0:
            continue

        else:
            cycle = False
            write_on_file()

def write_on_file():
    with open("test22.06.txt", "w+", encoding='utf8') as file:
        file.write(str(my_list))
    read_file()

def read_file():
    with open("test20.06.txt", "r+", encoding='utf8') as file:
        my_str = file.read().replace("'", '')
        new_list = my_str.strip("[]").split('', '')
        try:
            T3 = list(map(int, new_list))
            print(type(T3[1]))

        except ValueError:
            print(T3)
            print('AAAA!')

inputs()


'''
Калькулятор
'''


class Calculator():

#attr
    def __init__(self, x, y):
        try:
            self.x = int(x)
            self.y = int(y)
        except ValueError:
            self.x = x
            self.y = y

#method
    def sum(self):
        return self.x + self.y

    def mult(self):
        return self.x * self.y

    def division(self):
        try:
            return self.x / self.y
        except ZeroDivisionError:
            return f'Вы пытались разделить на ноль {self.x}'




calc = Calculator(3, 0)
print(calc.division())

#Регулярные выражения, модуль

import re

some_text = "Достать сслыку на картинку <img scr='bg.jpg'> в тексте </p>"

match = re.findall(r"<img.*?>", some_text)
print(match)
print(len(match))

# База данных, создание

import sqlite3 as sql

connector = sql.connect('cats.db')
cursor = connector.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS cats (
        poroda TEXT,
        age INTEGER,
        color TEXT


    )


    """
)

connector.close()