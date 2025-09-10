"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами. Решите используя sys.argv и argparse
"""
import argparse


def calculation(production, price_hour, bonus):
    return production * price_hour + bonus

def main():
    parser = argparse.ArgumentParser(description="Расчет")
    parser.add_argument("production", type=float, help='выработка в часах')
    parser.add_argument("price_hour", type=float, help='ставка в час')
    parser.add_argument("bonus", type=float, help='размер премии')
    args = parser.parse_args()


    calculation_ = calculation(args.production, args.price_hour, args.bonus)
    print(calculation_)


if __name__ == "main":
    main()
