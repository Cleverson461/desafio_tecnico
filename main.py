# Técnica:

""" 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código; """

def is_fibonacci(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

# Teste com um número
num = int(input("Digite um número: "))
if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")


""" 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre. 

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
"""
def count_letter_a(s):
    return s.lower().count('a')

# Teste com uma string
string = input("Digite uma string: ")
count = count_letter_a(string)
print(f"A letra 'a' aparece {count} vez(es) na string.")




""" 3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA? """
indice = 12
soma = 0
k = 1

while k < indice:
    k = k + 1
    soma = soma + k 

print(soma)


""" 4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___ # O próximo número é 9

b) 2, 4, 8, 16, 32, 64, ____ # O próximo número é 128

c) 0, 1, 4, 9, 16, 25, 36, ____ # O próximo número é 49

d) 4, 16, 36, 64, ____ # O próximo número é 100

e) 1, 1, 2, 3, 5, 8, ____ # O próximo número é 13

f) 2,10, 12, 16, 17, 18, 19, ____ # O próximo número é 20
 """

""" 5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  

## RESPOSTA ###
-> Ligue o primeiro interruptor e deixe-o ligado por alguns minutos.
-> Depois, desligue o primeiro interruptor e ligue o segundo.
-> Vá até as salas das lâmpadas:
    -> A lâmpada quente será a controlada pelo primeiro interruptor (pois estava ligada por mais tempo).
    -> A lâmpada acesa será a controlada pelo segundo interruptor.
    -> A lâmpada apagada e fria será a controlada pelo terceiro interruptor.


"""




# NÃO SE ESQUEÇA DE INSERIR O LINK DO SEU REPOSITÓRIO NO GITHUB COM O CÓDIGO FONTE QUE VOCÊ DESENVOLVEU.