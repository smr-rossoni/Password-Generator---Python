# Password Generator in Python

import random
import string

def gerar_senha(tamanho=12):
    # Conjunto de caracteres
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    # Todos os caracteres juntos
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos

    # Gera a senha aleatória
    senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))
    return senha

def main():
    print("=== GERADOR DE SENHAS ===")
    tamanho = input("Digite o tamanho da senha (padrão 12): ")
    
    if tamanho.isdigit():
        tamanho = int(tamanho)
    else:
        tamanho = 12

    senha = gerar_senha(tamanho)
    print(f"Sua senha gerada: {senha}")

if __name__ == "__main__":
    main()
