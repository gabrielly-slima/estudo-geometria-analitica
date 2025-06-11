# Funcionalidades básicas:Distância entre dois pontos, Ponto médio entre dois pontos, Verificar se três pontos estão alinhados (colineares), Encontrar a equação da reta que passa por dois pontos, Verificar se duas retas são paralelas ou perpendiculares
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
    print(f"Sua reta será composta das seguintes coordenadas: X(a,b) = {coordenadas_x[0]},{coordenadas_x[1]} Y(a,b) = {coordenadas_y[0]},{coordenadas_y[1]}")

def distancia_dois_pontos(coordenadas_x,coordenadas_y):
    calculo_distancia = math.sqrt(((coordenadas_x[1])-(coordenadas_x[0]))**2 + ((coordenadas_y[1])-(coordenadas_y[0]))**2)
    print(f"A distância entre dois pontos na sua reta é de {calculo_distancia}\n")

def ponto_medio(coordenadas_x,coordenadas_y):
    calculo_ponto_medio = ((coordenadas_x[0]+coordenadas_x[1]/2)+(coordenadas_y[0]+coordenadas_y[1]/2))
    print(f"O ponto médio da reta é = {calculo_ponto_medio}\n")

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

    
def main():
    while True:
        entrada = input("CALCULADORA GEOMÉTRICA\nDigite ___ para:\n1. Calcular a DISTÂNCIA ENTRE DOIS PONTOS NA RETA\n2. Calcular o PONTO MÉDIO ENTRE DOIS PONTOS NA RETA\n3. Calcular os PONTOS COLINEARES\n4. Calcular a EQUAÇÃO GERAL DA RETA\n5. Verificar SE AS RETAS SÃO PARALELAS OU PERPENDICULARES\n")
        if entrada =="1":
            coordenadas_x = pedir_valores("X")
            coordenadas_y = pedir_valores("Y")
            distancia_dois_pontos(coordenadas_x,coordenadas_y)
        elif entrada == "2":
            coordenadas_x = pedir_valores("X")
            coordenadas_y = pedir_valores("Y")
            ponto_medio(coordenadas_x,coordenadas_y)
        elif entrada == "3":
            coordenadas_x= pedir_3_valores("X")
            coordenadas_y= pedir_3_valores("Y")
            pontos_colineares(coordenadas_x,coordenadas_y)
        else:
            print("Digite corretamente o que deseja fazer de acordo com o menu")
            continue

main()