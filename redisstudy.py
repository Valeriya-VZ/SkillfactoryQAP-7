import redis


# Создаем объект класса Redis
red = redis.Redis(
    host='redis-12927.c44.us-east-1-2.ec2.cloud.redislabs.com',
    port=12927,
    password='GPzfvdiWVA8IVZ8LE88tNwX1ynk3kHnB'
)
# в терминале прописываем python -i чтобы интерпретатор не выключался когда скрипт выполнится до конца.
# и имя файла, т.е.: python -i redisstudy.py
# дальше обращаемся к нашей переменной - прописывая red
# попытаемся сохранить строку в базу данных в терминате прописываем red.set('var1', 'value')
# чтобы получить значение прописываем red.get('var1')