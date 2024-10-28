
money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
total_money = money_capital
current_spend = 0
count = 1

while total_money > current_spend:

    total_money += salary #к текущим деньгам прибавляется зарплата в 1 день

    if count == 1:
        current_spend = spend
    else:
        current_spend = current_spend*(1+increase) #текущие расходы увеличиваются на +0.05%
    total_money -= current_spend #остаток денег под конец месяца
    count += 1



print("Количество месяцев, которое можно протянуть без долгов:", count)
