# Funcionalidades básicas:Distância entre dois pontos, Ponto médio entre dois pontos, Verificar se três pontos estão alinhados (colineares), Encontrar a equação da reta que passa por dois pontos, Verificar se duas retas são paralelas ou perpendiculares

def main():
    while True:
        entrada = input("CALCULADORA GEOMÉTRICA\nDigite ___ para:\n1. Calcular a DISTÂNCIA ENTRE DOIS PONTOS NA RETA\n 2. Calcular o PONTO MÉDIO ENTRE DOIS PONTOS NA RETA\n3. Calcular os PONTOS COLINEARES\n4. Calcular a EQUAÇÃO GERAL DA RETA\n5. Verificar SE AS RETAS SÃO PARALELAS OU PERPENDICULARES\n")
        if entrada =="1":
            distancia_dois_pontos()
        elif entrada == "2":
            ponto_medio()
        elif entrada == "3":
            pontos_colineares()
        elif entrada == "4":
            equacao_da_reta()
        elif entrada =="5":
            verifica_reta()
        else:
            print("Digite corretamente o que deseja fazer de acordo com o menu")
            continue

main()