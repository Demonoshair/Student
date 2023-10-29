win=1
action = 0
day = 1
dayNorm = 365
money = 50
study = 100
stamina = 100
name = input("Назовите своего студента: ")
print("Вашего студента зовут", name)
while(day < dayNorm + 1):
    print(day)
    money = money
    stamina = stamina + 20
    if stamina > 100:
        stamina = 100
    if money > 100:
        money = 100
    if study > 100:
        study = 100
    if money > 15 and study > 10 and action == 0:
        money = money-10
        study = study-10
        stamina = stamina+20
        print("студент сегодня отдыхал")
        action = 1
    elif stamina > 10 and money > 10 and action == 0:
        study = study+15
        stamina = stamina-30
        print("студент сегодня учился")
        action = 1
    elif stamina > 10 and study > 10 and action == 0:
        money = money+15
        study = study-10
        stamina = stamina-30
        print("студент сегодня работал")
        action = 1
    if stamina > 100:
        stamina = 100
    if money > 100:
        money = 100
    if study > 100:
        study = 100
    if stamina < 10:
        money = money-10
        study = study-20
        stamina = stamina+40
        print("Студент Екстренно отдохнул")
    print("Усталость студента", 100-stamina)
    print("Деньги студента", money)
    print("Успеваемость студента", study)
    if study < 1 or money < 1 or action == 0:
        print("Simulation Over")
        break
        win=0
    day = day+1
    action = 0
if win==1:
    print("Поздравляю,",name,"Прожил целый год!")
