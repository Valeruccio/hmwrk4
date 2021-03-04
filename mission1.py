def sal():
    try:
        time = float(input('Выработка в минутах '))
        salary = int(input('Ставка в бакса '))
        bonus = int(input('Премия в бакса '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {round(res)}  бакса')
    except ValueError:
        return print('Not a number')
sal()
