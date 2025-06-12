import math
import numpy as np

class Reta:
    def __init__(self,x1,y1,x2,y2,x3,y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    
    def mostrar_valores(self):
        print(f"Sua reta será composta pelos pontos:A= ({self.x1} , {self.y1}) e B= ({self.x2} , {self.y2})")
    
    def distancia_dois_pontos(self):
        calculo_distancia = math.sqrt(((self.x2)-(self.x1))**2 + ((self.y2)-(self.y1))**2)
        print(f"A distância entre dois pontos na sua reta é de {calculo_distancia}\n")
    
    def ponto_medio(self):
        ponto_medio_x = ((self.x1)+(self.x2))/2
        ponto_medio_y = ((self.y1)+(self.y2))/2
        print(f"O ponto médio do eixo 'x' da reta é {ponto_medio_x} e do eixo 'y' é {ponto_medio_y}")

    def pontos_colineares(self):
        matriz = np.array([[self.x1,self.y1,1],[self.x2,self.y2,1],[self.x3,self.y3,1]])
        determinante = np.linalg.det(matriz)
        if determinante == 0:
            print("Os pontos são colineares, ou seja, estão alinhados na mesma reta")
        else:
            print("Os pontos não são colineares")
    
    def inclinacao_reta(self):
        if self.x1 == self.x2:
            print("Inclinação indefinida (divisão por zero = reta vertical)")
        else:
            inclinacao = ((self.y2)-(self.y1))/((self.x2)-(self.x1))
            print(f"A inclinação da reta (coeficiente angular) é dada por (y2 - y1) / (x2 - x1) = {inclinacao}")
            print(f"A inclinação da reta é de ({self.y2}-{self.y1}/{self.x2}-{self.x1}) = {inclinacao}")

def entrada_2_valores():
    while True:
            x1 = float(input("Digite o x do ponto A\n"))
            y1 = float(input("Digite o y do ponto A\n"))
            x2 = float(input("/Digite o x do ponto B\n"))
            y2 = float(input("Digite o y do ponto B\n"))

            criacao_reta = Reta(x1,y1,x2,y2)
            criacao_reta.mostrar_valores()
            return criacao_reta
        
def entrada_3_valores():
    while True:
        try:
            x1 = float(input("Digite o x do ponto A\n"))
            y1 = float(input("Digite o y do ponto A\n"))
            x2 = float(input("Digite o x do ponto B\n"))
            y2 = float(input("Digite o y do ponto B\n"))
            x3 = float(input("Digite o x do ponto C\n"))
            y3 = float(input("Digite o y do ponto C\n"))

            criacao_reta = Reta(x1,y1,x2,y2,x3,y3)
            criacao_reta.mostrar_valores()
            return criacao_reta
    
        except ValueError:
            print("Caractere inválido! Digite um número")
            continue

def main():
    while True:
        try:
            entrada = int(input("CALCULADORA GEOMÉTRICA\nDigite ___ para:\n1. Calcular a DISTÂNCIA ENTRE DOIS PONTOS NA RETA\n2. Calcular o PONTO MÉDIO ENTRE DOIS PONTOS NA RETA\n3. Calcular os PONTOS COLINEARES\n4. Calcular a INCLINAÇÃO DA RETA\n0. Para ENCERRAR\n"))
            if entrada == 1:
                reta_criada = entrada_2_valores()
                reta_criada.distancia_dois_pontos()
            elif entrada == 2:
                reta_criada = entrada_2_valores()
                reta_criada.ponto_medio()
            elif entrada == 3:
                reta_criada = entrada_3_valores()
                reta_criada.pontos_colineares()
            elif entrada == 4:
                reta_criada = entrada_2_valores
                reta_criada.inclinacao_reta()
            elif entrada == 0:
                print("Encerrando...")
                break

            else:
                print("Digite um número válido!")
                continue

        except ValueError:
            print("Caractere inválido! Digite o que deseja fazer de acordo com o MENU\n")

main()

        