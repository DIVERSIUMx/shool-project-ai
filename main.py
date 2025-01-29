from scanner import check
from cam import shot

shot()

if check():
    print("ok")
else:
    print("ЧТО ВЫ ЗАБЫЛИ НА БОЛОТЕ!?")
