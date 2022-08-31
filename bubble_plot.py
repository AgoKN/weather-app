# Agostin Kolëndrekaj
import json
import matplotlib.pyplot as plt

f = open("data.json")  # hapim file-n qe ka te dhenat meteorologjike
# inicializojme variblin data me te dhenat e files data.json
data = json.load(f)
f.close()  # mbyllim file-n

# liste boshe qe do mbaje te dhenat per lageshtine qe kemi ne json
lista_per_lageshtine = []
for items in data:  # cikel qe te mbushim listen me te dhenat per lageshtine
    # te dhenat "Lageshtia" nga file i json ja kalojme var. lageshtia nje nga nje
    lageshtia = items["Lageshtia"]
    # vendosim ne listen boshe cdo te dhene nga var. "lageshtia"
    lista_per_lageshtine.append(lageshtia)

ditet_e_javes = []  # liste boshe qe do mbaje ditet e javes qe kemi ne json
for items in data:  # cikel qe te mbushim listen me te dhenat per ditet e javes
    # te dhenat "Dita" nga file i json ja kalojme var. ditet nje nga nje
    ditet = items["Dita"]
    # vendosim ne listen boshe cdo te dhene nga var. "ditet"
    ditet_e_javes.append(ditet)

lista_per_reshjet = []  # liste boshe qe do mbaje te dhenat per reshjet qe kemi ne json
for items in data:  # cikel qe te mbushim listen me te dhenat per reshjet
    # te dhenat "Probabiliteti i Reshjeve" nga file i json ja kalojme var. reshjet nje nga nje
    reshjet = items["Probabiliteti i Reshjeve"]
    # vendosim ne listen boshe cdo te dhene nga var. "reshjet"
    lista_per_reshjet.append(reshjet)

plt.xlabel(  # Personalizojme "x label"
    "Ditet",
    fontsize="15",
    color="#ab1c4d",
    fontweight="bold",
)
plt.ylabel("Perqindja (%)", fontsize="15", color="green",
           fontweight="bold")  # Personalizojme "y label"
plt.title(  # Personalizojme titullin
    "Lageshtia (red color) dhe Reshjet (blue color) \nper javen (10/1/2022 - 16/1/2022)",
    fontweight="bold",
)
plt.xticks(rotation=25)  # rrotullojme te dhenat ne boshtin e x 25 grade
# vendosim se cfare dona te afishojme
plt.scatter(
    ditet_e_javes, lista_per_lageshtine,  edgecolors="red", c="white"
)
plt.scatter(
    ditet_e_javes, lista_per_reshjet,  edgecolors="blue", c="white"
)
plt.show()  # shfaqim grafikun
