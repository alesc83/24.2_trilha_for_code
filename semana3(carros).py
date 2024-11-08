import pandas as pd
from os import system

system('cls')

csv_car = pd.read_csv('abobrinha\mt_cars.csv')

aux = []
for i in list(csv_car["mpg"]):
    i = float(i)
    aux.append(i)
csv_car['mpg'] = aux

econ = csv_car[csv_car["mpg"] <= 15]
econ = econ.sort_values(by = 'mpg', ascending=True)


print("------------Top 5 mais Econômicos------------")
print(econ[['model','mpg']].head())

print("\n------------Top 5 mais Potentes------------")
pot = csv_car[csv_car["hp"] > 200]
pot = pot.sort_values(by = "hp", ascending=False)
print(pot[['model','hp']].head())

print("\n------------Top 5 mais Rápidos------------")
rapidinhos = csv_car[csv_car["qsec"] <= 20]
rapidinhos = rapidinhos.sort_values(by = 'qsec', ascending=True)
print(rapidinhos[['model','qsec']].head())

econ_list = list(econ['model'].head())
pot_list = list(pot['model'].head())
rap_list = list(rapidinhos['model'].head())


des = []
for i in econ_list:
    if i in pot_list:
        if i in rap_list:
            des.append(i)

print(f'\nOs únicos carros que figuram nos três rankings são: {des.pop(0)} e {des.pop(0)}')
