# Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров.
# Вам необходимо написать программу, которая позволяла бы составлять список нескольких гостей.
# Решите задачу с помощью метода конструктора и примените один из принципов наследования.
# При выводе в консоль вы должны получить:  “Иван Петров, г.Москва, статус "Наставник"
class InvitationList:
    def __init__(self, name, surname, address, status):
        self.name = name
        self.surname = surname
        self.address = address
        self.status = status

    def getinvitation(self):
        return f'''{self.name} {self.surname}, {self.address}, статус "{self.status}"'''

# Далее продолжим работу в файле 16.9.4
