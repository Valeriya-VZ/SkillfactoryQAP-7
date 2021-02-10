# Напишите программу, которая будет записывать и кэшировать номера ваших друзей.
# Программа должна уметь воспринимать несколько команд: записать номер,
# показать номер друга в консоли при вводе имени или же удалить номер друга по имени.
# Кэширование надо производить с помощью Redis.
# Ввод и вывод информации должен быть реализован через консоль (с помощью функций input() и print()).
import redis
red = redis.Redis(
    host='redis-12927.c44.us-east-1-2.ec2.cloud.redislabs.com',
    port=12927,
    password='GPzfvdiWVA8IVZ8LE88tNwX1ynk3kHnB'
)

cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break