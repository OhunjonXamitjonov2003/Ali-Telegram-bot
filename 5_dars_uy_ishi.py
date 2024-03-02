from collections import namedtuple


Book = namedtuple("Book","avtor name rangi varoqlar_soni")

book = ("Imomi Zarnujiy","Ilim olish sirlar","qizil","66 bet")

bo = Book(*book)

print(*bo)