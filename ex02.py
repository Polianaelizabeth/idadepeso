idade = int(input("Idade: "))
peso = float(input("Peso(kg): "))

if idade < 20:
    if peso < 60:
        print("grupo de risco: 9")
    elif 60 <= peso <= 90:
        print("grupo de risco: 8")
    else:
        print("grupo de risco: 7")
elif 20 <= idade <= 50:
    if peso < 60:
        print("grupo de risco: 6")
    elif 60 <= peso <= 90:
        print("grupo de risco: 5")
    else:
        print("grupo de risco: 4")
else:
    if peso < 60:
        print("grupo de risco: 3")
    elif 60 <= peso <= 90:
        print("grupo de risco: 2")
    else:
        print("grupo de risco: 1")

