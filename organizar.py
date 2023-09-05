# Exemplo de definicao de funçao no Python

def soma(a, b):
    resultado = a + b
    return resultado
s = soma (1,2)
print(s)

# Outro exemplo ainda de definicao de funçao no Python sem colocar parÃ¢metros

print(' -'*30)
print('          Vinheria Agnello')
print(' -'*30)
print('')
print(' -'*30)
print('          PromoÃ§Ã£o de vinhos - queima de estoque')
print(' -'*30)


def linha_separacao():
    return print(' -'*30)
linha_separacao()

print('          PromoÃ§Ã£o de vinhos - queima de estoque')    

linha_separacao()

print('          PromoÃ§Ã£o de vinhos - Queima de Estoque')
linha_separacao()

# Exercicio 1 - Crie uma funçao para calcular o dobro de um numero

def dobrar_numero():
    numero = float(input("Digite um numero: "))
    resultado = numero * 2
    return resultado
print(' O dobro do numero:   ',dobrar_numero())

#  Exercicio 2 - Crie uma funçao que soma dois numeros inteiros 

def somar_numeros():
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    resultado = numero1 + numero2
    return resultado
print(' A soma dos numeros:   ',somar_numeros())

#  Exercicio 3 - Crie uma funçao que forneça o modulo do numero

def valor_absoluto():
    numero = float(input("Digite um nÃºmero:  "))
    resultado = abs(numero)
    return resultado
print(' O modulo do numero Ã©:  ',valor_absoluto())

#  Exercicio 4 - Crie uma funçao que forneça o quadrado do numero

def quadrado_de_n():
    numero = float(input("Digite um nÃºmero: "))
    resultado = numero ** 2
    return resultado
print(' O modulo do numero Ã©:  ',quadrado_de_n())

 #  Exercicio 5 - Crie um codigo para calcular o Fatorial de um numero

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)
n = int(input('Digite o numero que vc quer calcular o fatorial:  '))

print("O fatorial de", n, "Ã©", fatorial(n))


#  Exercicio 6 - Crie uma funÃ§Ã£o que retorna o maior entre dois nÃºmeros:
    
def busca_maior():
    numero1 = float(input("Digite o primeiro nÃºmero: "))
    numero2 = float(input("Digite o segundo nÃºmero: "))
    if numero1 > numero2:
        return numero1
    else:
        return numero2
print(' O maior numero Ã©:  ',busca_maior())

#  Exercicio 7 - Crie uma funÃ§Ã£o que retorne o antecessor do numero

def buscar_antecessor():
    numero = float(input("Digite um nÃºmero: "))
    antecessor = numero - 1
    return antecessor
print(' O antecessor Ã©:  ',buscar_antecessor())

#  Exercicio 8 - Crie uma funÃ§Ã£o que retorna o menor entre dois nÃºmeros

def buscar_menor():
    numero1 = float(input("Digite o primeiro nÃºmero: "))
    numero2 = float(input("Digite o segundo nÃºmero: "))
    if numero1 < numero2:
        return numero1
    else:
        return numero2
print('o numero menor Ã©: ', buscar_menor())

#  Exercicio 9 - Crie uma funÃ§Ã£o que verifica se um nÃºmero Ã© par:

def verificar_par():
    numero = int(input("Digite um nÃºmero: "))
    if numero % 2 == 0:
        return print('O numero Ã© par!')
    else:
        return print('O numero Ã© impar!')
print(verificar_par())

#  Exercicio 10 - Crie uma funÃ§Ã£o para calcular a raiz quadrada de um numero:
import math

def calcular_raiz_quadrada():
    numero = float(input("Digite um nÃºmero: "))
    raiz_quadrada = math.sqrt(numero)
    return raiz_quadrada
print('A raiz quadrada Ã©: ',calcular_raiz_quadrada())
      
# Exercicio 11 - Crie um codigo para somar dois numeros complexos

def somar_numeros_complexos(num1, num2):
    real = num1[0] + num2[0]
    imaginaria = num1[1] + num2[1]
    resultado = (real, imaginaria)
    return resultado

# Solicita as partes real e imaginÃ¡ria do primeiro nÃºmero complexo ao usuÃ¡rio
real1 = float(input("Digite a parte real do primeiro nÃºmero complexo: "))
imaginaria1 = float(input("Digite a parte imaginÃ¡ria do primeiro nÃºmero complexo: "))

# Solicita as partes real e imaginÃ¡ria do segundo nÃºmero complexo ao usuÃ¡rio
real2 = float(input("Digite a parte real do segundo nÃºmero complexo: "))
imaginaria2 = float(input("Digite a parte imaginÃ¡ria do segundo nÃºmero complexo: "))

# Cria as representaÃ§Ãµes dos nÃºmeros complexos como tuplas (parte real, parte imaginÃ¡ria)
num1 = (real1, imaginaria1)
num2 = (real2, imaginaria2)

# Realiza a soma dos nÃºmeros complexos
soma = somar_numeros_complexos(num1, num2)

# Exibe o resultado
print("A soma dos nÃºmeros complexos Ã©:", soma)

