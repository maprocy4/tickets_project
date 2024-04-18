#!/usr/bin/python

def main():
    tickes_num = None
    discount = None
    final_price = 0

    tickets_num = int(input("Сколько вы хотите приобрести билетов? - "))

    final_price = 0
    for i in range(tickets_num):
        age = int(input("Введите возраст посетителя: "))

        if age>18 and age<=25:
            final_price += 990
        elif age>25:
            final_price += 1390

    if tickets_num > 3:
        final_price *= 0.9

    print("К оплате: %d руб." % final_price)

if __name__ == "__main__":
    main()
