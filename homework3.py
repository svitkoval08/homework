Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> print("---Кафе “У Монті”---")
---Кафе “У Монті”---
>>> dishes = input("Введіть список страв, що треба подати до вечері(розділені комами): ")
Введіть список страв, що треба подати до вечері: 
>>> dishes = dishes.split(',')
>>> total_price = 0
>>> for dish in dishes:
...     price = random.randint(1, 5000)
...     print("{:<15}{:>5} грн".format(dish, price))
...     total_price += price
... print("Всього {:>5} грн".format(total_price))
SyntaxError: invalid syntax
>>> print("Всього {:>5} грн".format(total_price))
Всього     0 грн
