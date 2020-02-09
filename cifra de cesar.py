#Afabeto para que o programa reconheça os caracteres que serão digitados
alfabeto = ' !.,?AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzâäàåÄÅáÁÂÀãÃéêëèÉÊËïîìíÍÎÏÌôöòÖóÔÓÒõÕüûùÜúÚÛÙÇçñÑýÝ1234567890'

#Rotação que será executada pelo programa para realizar a criptografia
ROT = 13

print()



print("1 cifrar")
print("2 decifrar")
print("3 sair do programa")


print("")


#função input utilizada para o usuario escolher entre cifrar ou decifrar
modo = int(input("escolha umas das opções acima: "))

print()

def escolha():
    if modo == 1:
        
        cifrar()
    if modo == 2:
        
        decifrar()
    if modo == 3:
        print ("fim do programa, muito obrigado!")


def cifrar():
    texto = str(input('insira o texto a ser criptografado: ')) #texto que será criptografado
    m = ''
    for c in texto:
        c_index = alfabeto.index(c) #variavel utilizada para encontrar a posição de cada letra do texto
        m += alfabeto[(c_index + ROT) % len (alfabeto)] #algoritimo de conversão para criptografar
    print("Seu texto criptografado é: (" + m + ")") #resultado da mensagem criptografada


def decifrar():
    texto = str(input('insira o texto a ser criptografado: ')) #texto que será criptografado
    m = ''
    for c in texto:
        c_index = alfabeto.index(c) #variavel utilizada para encontrar a posição de cada letra do texto
        m += alfabeto[(c_index - ROT) % len (alfabeto)] #algoritimo de conversão para criptografar
    print("Seu texto criptografado é: ("+ m +")") #resultado da mensagem criptografada


def main():
    escolha()


main()
