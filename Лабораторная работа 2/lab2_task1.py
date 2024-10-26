from multiprocessing.dummy import current_process

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
total_money = money_capital
current_spend = 0
count = 0 #кол во месяцев

for i in range (1,99):

    total_money += salary #к текущим деньгам прибавляется зарплата в 1 день

    if i == 1:
        current_spend = spend
    else:
        current_spend = current_spend*(1+increase) #текущие расходы увеличиваются на +0.05%
    if total_money < current_spend:
        break
    count = i
    '''print("total = ", total_money, "cur_spend = ", current_spend, "i = ", i)'''
    total_money -= current_spend #остаток денег под конец месяца
    '''print("last total = ", total_money, "i=", i)'''



print("Количество месяцев, которое можно протянуть без долгов:", count)
