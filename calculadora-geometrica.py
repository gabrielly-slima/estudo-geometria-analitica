import math
import numpy as np

def pedir_valores(eixo):
    while True:
        valores = input(f"Digite duas coordenadas do eixo {eixo} separando-as por espaços\n").split()
        if len(valores) > 2:
            print("Você digitou coordenadas a mais, digite apenas DUAS")
            continue
        elif len(valores) > 1:
            try:
                converter_coordenadas = [float(num) for num in valores]
                return converter_coordenadas
            except ValueError:
                print(f"As coordenadas de {eixo} devem ser números válidos")
        else:
            print("Digite mais uma coordenada")

def mostrar_valores(coordenadas_x,coordenadas_y):
    '''
    Exibe as coordenadas inseridas pelo usuário.

    Parâmetros:
    coordenadas_x (list[float]): Coordenadas do eixo X.
    coordenadas_y (list[float]): Coordenadas do eixo Y.
    '''
    print(f"Sua reta será composta pelos pontos: A = ({coordenadas_x[0]}, {coordenadas_y[0]}), B = ({coordenadas_x[1]}, {coordenadas_y[1]})")

def distancia_dois_pontos(coordenadas_x,coordenadas_y):
    calculo_distancia = math.sqrt(((coordenadas_x[1])-(coordenadas_x[0]))**2 + ((coordenadas_y[1])-(coordenadas_y[0]))**2)
    print(f"A distância entre dois pontos na sua reta é de {calculo_distancia}\n")

def ponto_medio(coordenadas_x,coordenadas_y):
    ponto_medio_x = (coordenadas_x[0]+coordenadas_x[1])/2
    ponto_medio_y = (coordenadas_y[0]+coordenadas_y[1])/2
    print(f"O ponto médio do eixo 'x' da reta é = {ponto_medio_x} e do eixo 'y' é {ponto_medio_y}\n")

def pedir_3_valores(eixo):
     while True:
        valores = input(f"Digite três coordenadas do eixo {eixo} separando-as por espaços\n").split()
        if len(valores) > 3:
            print("Você digitou coordenadas a mais, digite apenas TRÊS")
            continue
        elif len(valores) > 1:
            try:
                converter_coordenadas = [float(num) for num in valores]
                return converter_coordenadas
            except ValueError:
                print(f"As coordenadas de {eixo} devem ser números válidos")
        else:
            print("Digite mais duas coordenadas")

def pontos_colineares(coordenadas_x,coordenadas_y):
    matriz = np.array([[coordenadas_x[0],coordenadas_y[0],1],
                       [coordenadas_x[1],coordenadas_y[1],1],
                       [coordenadas_x[2],coordenadas_y[2],1]])
    determinante = np.linalg.det(matriz)
    if determinante == 0:
        print("Os pontos são colineares, ou seja, estão alinhados na mesma reta")
    else:
        print("Os pontos não são colineares")

def inclinacao_reta(coordenadas_x,coordenadas_y):
    if coordenadas_x[0] == coordenadas_x[1]:
        print("Inclinação indefinida (divisão por zero = reta vertical)")
    else:
        inclinacao = (coordenadas_y[1]-coordenadas_y[0])/(coordenadas_x[1]-coordenadas_x[0])
        print(f"A inclinação da reta (coeficiente angular) é dada por (y2 - y1) / (x2 - x1) = {inclinacao}")
        print(f"A inclinação da reta é de ({coordenadas_y[1]} - {coordenadas_y[0]}) / ({coordenadas_x[1]} - {coordenadas_x[0]}) = {inclinacao}")

def calcular_distancia_dois_pontos():
    coordenadas_x = pedir_valores("X")
    coordenadas_y = pedir_valores("Y")
    mostrar_valores(coordenadas_x,coordenadas_y)
    distancia_dois_pontos(coordenadas_x,coordenadas_y)

def calcular_ponto_medio():
    coordenadas_x = pedir_valores("X")
    coordenadas_y = pedir_valores("Y")
    mostrar_valores(coordenadas_x,coordenadas_y)
    ponto_medio(coordenadas_x,coordenadas_y)

def calcular_pontos_colineares():
    coordenadas_x = pedir_3_valores("X")
    coordenadas_y = pedir_3_valores("Y")
    pontos_colineares(coordenadas_x,coordenadas_y)

def calcular_inclinacao_reta():
    coordenadas_x = pedir_valores("X")
    coordenadas_y = pedir_valores("Y")
    mostrar_valores(coordenadas_x,coordenadas_y)
    inclinacao_reta(coordenadas_x,coordenadas_y)

def main():
    while True:
        entrada = input("CALCULADORA GEOMÉTRICA\nDigite ___ para:\n1. Calcular a DISTÂNCIA ENTRE DOIS PONTOS NA RETA\n2. Calcular o PONTO MÉDIO ENTRE DOIS PONTOS NA RETA\n3. Calcular os PONTOS COLINEARES\n4. Calcular a INCLINAÇÃO DA RETA\n0. Para ENCERRAR\n")
        if entrada =="1":
            calcular_distancia_dois_pontos()
        elif entrada == "2":
            calcular_ponto_medio()
        elif entrada == "3":
            calcular_pontos_colineares()
        elif entrada == "4":
            calcular_inclinacao_reta()
        elif entrada == "0":
            print("Encerrando...")
            break
        else:
            print("Digite corretamente o que deseja fazer de acordo com o menu\n")
            continue

main()