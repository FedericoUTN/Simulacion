import numpy as np
import random
import matplotlib.pyplot as plt

tiradas = 1500
cant_nro = 37
frecuencias = []
muestra = []
promedios = []
desvios = []
varianzas = []

x = list(range(cant_nro))


def calcula_frecuencia(total):
    fr = np.bincount(muestra) / total
    fr = fr.tolist()
    while len(fr) < cant_nro:
        fr.append(int(0))
    frecuencias.append(fr)


def ruleta():
    for i in range(1, tiradas + 1):
        muestra.append(random.randint(0, cant_nro))
        calcula_frecuencia(i)
        promedios.append(np.mean(muestra))
        desvios.append(np.std(muestra))
        varianzas.append(np.var(muestra))


def plot_promedios():
    plt.figure('PROMEDIOS')
    plt.plot(promedios, 'r-', label='Promedio')
    prom_esp = (cant_nro * (cant_nro + 1)) / 2 / cant_nro
    plt.axhline(prom_esp, label='Promedio espeado')
    plt.xlabel('n numero de tiradas')
    plt.legend()
    plt.show()


def plot_desvios():
    plt.figure('DESVIOS')
    plt.plot(desvios, 'r-', label='Desvio')
    desv_esp = np.std(x)
    plt.xlabel('n numero de tiradas')
    plt.axhline(desv_esp, label='Desvio esperado')
    plt.legend()
    plt.show()


def plot_varianza():
    plt.figure('VARIANZA')
    plt.plot(varianzas, 'r-', label='Varianza')
    var_esp = np.var(x)
    plt.xlabel('n numero de tiradas')
    plt.axhline(var_esp, label='Varianza esperada')
    plt.legend()
    plt.show()


def plot_frecuencias(nro):
    fr = []
    for i in frecuencias:
        fr.append(i[nro])
    plt.figure('FRECUENCIA RELATIVA')
    plt.xlabel('n numero de tiradas')
    plt.title('Frecuencia Relativa del nro ' + str(nro))
    plt.plot(fr, 'r-', label='Frecuencia Relativa')
    plt.axhline(1 / 37, label='Frecuencia Relativa esperada')
    plt.legend()
    plt.show()


# Main
ruleta()
plot_promedios()
plot_desvios()
plot_varianza()
bolilla = input("Ingrese un numero del 0 al 36: ")
plot_frecuencias(int(bolilla))
