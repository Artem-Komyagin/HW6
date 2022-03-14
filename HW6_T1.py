# 1. Создать класс TrafficLight (светофор).
#
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
# на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение
# и завершать скрипт.


from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def start(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(1)
            i += 1


t = TrafficLight()
t.start()






# class Book:
#     count=0
#
#
#     def __init__(self, title, author, year=2000):
#         self.title= title
#         self._author = author
#         self.__year = year
#         Book.count+=1
#
#
#     def get_full_name(self):
#         return f'{self.title} - {self._author} [{self.__year}]'
#
# print(Book.count)
# my_book_1= Book( 'Sherlock Holmes', 'Doyal A.K.')
# my_book_2= Book( '1984', 'Orwell J.')
# print(Book.count)
#
# print(my_book_1._author)
# # print(my_book_1.__year)
#
# print(my_book_1.get_full_name())
# print(my_book_2.get_full_name())
# print(my_book_1.get_full_name())
