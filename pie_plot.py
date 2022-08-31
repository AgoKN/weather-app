# Agostin Kolëndrekaj
import json
import matplotlib.pyplot as plt

f = open("data.json")  # hapim file-n qe ka te dhenat meteorologjike
# inicializojme variblin data me te dhenat e files data.json
data = json.load(f)
f.close()  # mbyllim file-n

lista_per_eren = []  # liste boshe qe do mbaje te dhenat per eren qe kemi ne json
for items in data:  # cikel qe te mbushim listen me te dhenat per eren
    # te dhenat "Era" nga file i json ja kalojme var. era nje nga nje
    era = items["Era"]
    # vendosim ne listen boshe cdo te dhene nga var. "era"
    lista_per_eren.append(era)

# cikel qe te shtoje njesine e matjes se eres per cdo te dhene
era_me_kmh = []
for items in lista_per_eren:
    items = str(items) + " km/h"
    era_me_kmh.append(items)

ditet_e_javes = []  # liste boshe qe do mbaje ditet e javes qe kemi ne json
for items in data:  # cikel qe te mbushim listen me te dhenat per ditet e javes
    # te dhenat "Dita" nga file i json ja kalojme var. ditet nje nga nje
    ditet = items["Dita"]
    # vendosim ne listen boshe cdo te dhene nga var. "ditet"
    ditet_e_javes.append(ditet)

plt.title("Era (km/h) per javen (10/1/2022 - 16/1/2022)",
          fontweight="bold", color="#ab1c4d")  # Personalizojme titullin
# vendosim se cfare dona te afishojme
plt.pie(lista_per_eren, labels=ditet_e_javes)

# te legjenda vendosim te dhenat bashk me njesine e matjes
plt.legend(era_me_kmh)
plt.show()  # shfaqim grafikun
