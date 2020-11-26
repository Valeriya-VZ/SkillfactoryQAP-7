# Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров.
# Вам необходимо написать программу, которая позволяла бы составлять список нескольких гостей.
# Решите задачу с помощью метода конструктора и примените один из принципов наследования.
# При выводе в консоль вы должны получить:  “Иван Петров, г.Москва, статус "Наставник"

# Создаим класс InvitationList в файле InvitationClass
# Выполним импорт класса InvitationList из InvitationClass:

from InvitationClass import InvitationList
ivanpetrov = InvitationList(name='Иван', surname='Петров', address='г.Москва', status='Наставник')
ivanivanov = InvitationList(name='Иван', surname='Иванов', address='г.Москва', status='Участник')

print(ivanpetrov.getinvitation())
print(ivanivanov.getinvitation())
