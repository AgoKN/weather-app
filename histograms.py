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

plt.xlabel("Temperatura (°C)", fontsize="17", color="orange",
           fontweight="bold")  # Personalizojme "x label"
plt.ylabel("Nr i Ditve", fontsize="17", color="orange",
           fontweight="bold")  # Personalizojme "y label"
# Personalizojme titullin
plt.title("Sa dite ne jave jane me te njejten temperature \n(10/1/2022 - 16/1/2022)", color="#ab1c4d")

# vendosim se cfare dona te afishojme
plt.hist(lista_per_temperaturat, edgecolor="black", color="red")
plt.show()  # shfaqim grafikun
