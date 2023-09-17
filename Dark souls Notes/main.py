def notes():
    pass
# def merchants():
#
# def bosses():

def main():
    while True:
        print("Что вы хотите сделать?\n1 Написать Заметку\n2 Записать Торговца\n3 Записать Босса")
        choice = input("Введите цифру")

        if choice == "1":
            notes()
        # if choice == "2":
        #     merchants()
        # if choice == "3":
        #     bosses()
        else:
            print("Вы написали число вне списка")


