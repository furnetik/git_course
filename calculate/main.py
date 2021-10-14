import math

import mysum

def main():

    while True:
        
        # Выводим сообщение какие действия есть
        print("Выберите действие которое хотите сделать:\n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"
              "Выйти: q\n")

        action = input("Действие: ")
        if action == "q":
            # Выводим сообщение
            print("Выход из программы")
            # Выходим из цикла
            break

        if action in ('+', '-', '*', '/'):

            x = float(input("x = "))

            y = float(input("y = "))

            if action == '+':

                print('%.2f + %.2f = %.2f' % (x, y, x+y))
            # Если action равен - то
            elif action == '-':

                print('%.2f - %.2f = %.2f' % (x, y, x-y))
            # Если action равен * то
            elif action == '*':

                print('%.2f * %.2f = %.2f' % (x, y, x*y))
            # Если action равен / то
            elif action == '/':
                # Если y не равен нулю то
                if y != 0:

                    print('%.2f / %.2f = %.2f' % (x, y, x/y))
                else: # Иначе

                    print("Деление на ноль!")

if __name__ == "__main__":
    main()
