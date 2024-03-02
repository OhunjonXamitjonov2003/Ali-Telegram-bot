from collections import namedtuple
# #
# # User = namedtuple("User","id name lastname age email")
# # users = [
# #     (1,"Tohi","Tohirov",20,"tohi@gmail.com"),
# #     (2,"Tohi","Valiyev",21,"aliyev@gmail.com"),
# #     (3,"Sobir","Tohirov",22,"sobir@gmail.com")
# # ]
# #
# # for user in users:
# #     us = User(*user)
# #     print(us.id,us.name,us.lastname,us.age,us.email)
# #       print(*us)
# Car = namedtuple("Car","name color tezligi price orindiqlar_soni boshqaruvi")
#
# car = ("Malibu","red","300km/h",20000,4,"Avtomat")
#
#
# ca = Car(*car)
# print(*ca)

Book = namedtuple("Book","avtor name rangi varoqlar_soni")

book = ("Imomi Zarnujiy","Ilim olish sirlar","qizil","66 bet")

bo = Book(*book)

print(*bo)

