# Agostin Kolëndrekaj
import json
import matplotlib.pyplot as plt

f = open("data.json")  # hapim file-n qe ka te dhenat meteorologjike
# inicializojme variblin data me te dhenat e files data.json
data = json.load(f)
f.close()  # mbyllim file-n

lista_per_temperaturat = []  # liste boshe qe do mbaje temp. qe kemi ne json
for items in data:  # cikel qe te mbushim listen me te dhenat per temperaturen
    # te dhenat "Temperatura" nga file i json ja kalojme var. temperaturat nje nga nje
    temperaturat = items["Temperatura"]
    # vendosim ne listen boshe cdo te dhene nga var. "temperaturat"
    lista_per_temperaturat.append(temperaturat)

ditet_e_javes = []  # liste boshe qe do mbaje ditet e javes qe kemi ne json
for items in data:  # cikel qe te mbushim listen me te dhenat per ditet e javes
    # te dhenat "Dita" nga file i json ja kalojme var. ditet nje nga nje
    ditet = items["Dita"]
    # vendosim ne listen boshe cdo te dhene nga var. "ditet"
    ditet_e_javes.append(ditet)

plt.grid(True)  # to make the graph have grid view
plt.xlabel("Ditet", fontsize="17", color="orange",
           fontweight="bold")  # Personalizojme "x label"
plt.ylabel("Temperatura (°C)", fontsize="17",  # Personalizojme "y label"
           color="orange", fontweight="bold")
plt.title("Temperatuarat per javen (10/1/2022 - 16/1/2022)",
          fontweight="bold", color="#ab1c4d")  # Personalizojme titullin

# vendosim se cfare dona te afishojme
plt.plot(
    ditet_e_javes,
    lista_per_temperaturat,
    "ro",  # "r" for red and "o" for circle markers
    ditet_e_javes,
    lista_per_temperaturat,
    "r--",  # "r" for red and "--" for dashed lines
)
plt.show()  # shfaqim grafikun
