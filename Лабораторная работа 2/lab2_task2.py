salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
total_money = money_capital
current_spend = spend
count = 0
win = 0
ndiff = 0
min = 999999
for money_capital in range (1000,90000,1):
    '''print("start money", money_capital)'''
    total_money = money_capital
    for i in range(1, 99):

        if i == 1:
            current_spend = spend
        else:
            current_spend = current_spend * (1 + increase)  # текущие расходы увеличиваются на +0.05%
        diff = salary - current_spend
        total_money += diff
        if total_money < 0:
            break
        count = i
        '''print("total = ", total_money, "cur_spend = ", current_spend, "i = ", i)'''


    if count == 10:
        '''print("count= ", count)'''
        '''print("WINNER", money_capital)'''
        win = money_capital
        if win<min:
            min = win

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", min-1)
