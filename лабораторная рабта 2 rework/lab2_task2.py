import math

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
debt = 0
current_spend = spend
for i in range (1,months+1):

    if i == 1:
        current_spend = spend
    else:
        current_spend = current_spend * (1 + increase)  # текущие расходы увеличиваются на +0.03%

    diff = salary - current_spend #долг за тек. месяц (тк salary < spend)

    debt += diff #общий долг

money_capital = math.ceil(abs(debt)) #запасы (всего), которые мы тратим на каждый лишний месячный долг





print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
