# В проекте «Дом питомца» скоро появится новая услуга: электронный кошелек.
# То есть система будет хранить данные о своих клиентах и об их финансовых операциях.
# Вам нужно написать программу, обрабатывающую данные,
# и на выходе в консоль получить следующее:
# Клиент "Иван Петров". Баланс: 50 руб.
class OnlineWallet:
    def __init__(self, clientname, clientsurname, balance):
        self.clientname = clientname
        self.clientsurname = clientsurname
        self.balance = balance

    def getinfoclient(self):
        return f'''Клиент "{self.clientname} {self.clientsurname}". Баланс: {self.balance} руб.'''


ivanpetrov = OnlineWallet(clientname='Иван', clientsurname='Петров', balance=50)

print(ivanpetrov.getinfoclient())
