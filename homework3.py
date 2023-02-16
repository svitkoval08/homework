import random
print("---Кафе “У Монті”---")
dishes = input("Введіть список страв, що треба подати до вечері(розділені комами): ")
dishes = [dish.strip() for dish in dishes.split(',')]
total_price = 0
for dish in dishes:
    price = random.randint(1, 5000)
    print("{:<15}{:>5} грн".format(dish, price))
    total_price += price
print("Всього {:>5} грн".format(total_price))

