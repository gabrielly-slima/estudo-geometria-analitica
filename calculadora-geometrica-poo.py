import math
import numpy as np

class Reta:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def mostrar_valores(self):
        print(f"Sua reta será composta pelos pontos:A= ({self.x1} , {self.y1}) e B= ({self.x2} , {self.y2})")
    
    def distancia_dois_pontos(self):
        calculo_distancia = math.sqrt(((self.x2)-(self.x1))**2 + ((self.y2)-(self.y1))**2)
        print(f"A distância entre dois pontos na sua reta é de {calculo_distancia}\n")
    
    def ponto_medio(self):
        ponto_medio_x = ({self.x1}+{self.x2})/2
        ponto_medio_y = ({self.y1})+{self.y2}/2
        print(f"O ponto médio do eixo 'x' da reta é {ponto_medio_x} e do eixo 'y' é {ponto_medio_y}")

def main():
    while True:
        entrada = input("CALCULADORA GEOMÉTRICA\nDigite ___ para:\n1. Calcular a DISTÂNCIA ENTRE DOIS PONTOS NA RETA\n2. Calcular o PONTO MÉDIO ENTRE DOIS PONTOS NA RETA\n3. Calcular os PONTOS COLINEARES\n4. Calcular a INCLINAÇÃO DA RETA\n0. Para ENCERRAR\n")
        if entrada =="1":
            reta_criada = entrada_valores()
            reta_criada.distancia_dois_pontos()
        elif entrada == "2":
            reta_criada = entrada_valores()
            reta_criada.ponto_medio()

def entrada_valores():
    x1 = float(input("Digite o x do ponto A"))
    y1 = float(input("Digite o y do ponto A"))
    x2 = float(input("Digite o x do ponto B"))
    y2 = float(input("Digite o y do ponto B"))
    
    criacao_reta = Reta(x1,y1,x2,y2)
    criacao_reta.mostrar_valores()
    return criacao_reta

main()

        