"""
VaiNaWeb - Desafio 1 - Tayná Goes de Sousa
"""

# BEGIN [Verifica se um aluno foi aprovado com base na nota.
def verificar_aprovacao(nota: float) -> str:
    if not 0 <= nota <= 10:
        return "Nota inválida! Digite um valor entre 0 e 10."
    return "Aprovado" if nota >= 6 else "Reprovado"
# END [Verifica se um aluno foi aprovado com base na nota.

# BEGIN [Verifica se uma pessoa pode votar com base na idade.
def verificar_idade(idade: int) -> str:
    if idade < 0:
        return "Idade inválida!"
    return "Você pode votar." if idade >= 16 else "Você não pode votar."
# END [Verifica se uma pessoa pode votar com base na idade. 

# BEGIN [Classifica a nota do aluno em uma escala de A a F.
def classificar_nota(nota: float) -> str:
    if not 0 <= nota <= 100:
        return "Nota inválida! Digite um valor entre 0 e 100."
    
    classificacoes = {
        (90, 100): "Parabéns, você tirou A!",
        (80, 90): "Muito bem, você tirou B.",
        (70, 80): "Bom trabalho, você tirou C.",
        (60, 70): "Fique atento, você tirou D.",
        (0, 60): "Estude um pouco mais, você tirou F."
    }
    
    for (min_, max_), mensagem in classificacoes.items():
        if min_ <= nota < max_:
            return mensagem
    return "Nota inválida!"
# END [Classifica a nota do aluno em uma escala de A a F.

# BEGIN [Soma dois números.
def somar_numeros(num1: float, num2: float) -> float:
    return num1 + num2
# END [Soma dois números.

# BEGIN [Verifica se a senha está correta.
def verificar_senha(senha: str) -> bool:
    return senha == "Python123"
# END [Verifica se a senha está correta.

# BEGIN [Exibe os números de 1 a 10.
def exibir_numeros() -> None:
    for i in range(1, 11):
        print(i)
# END [Exibe os números de 1 a 10.

# BEGIN [Organiza uma lista de números em ordem crescente.
def organizar_lista() -> list:
    numeros = [8, 3, 10, 1, 5]
    return sorted(numeros)
# END [Organiza uma lista de números em ordem crescente.

# BEGIN [Acessa os registros de alunos.
def acessar_registros() -> tuple:
    alunos = ("Tayna", "Gabriel", "Luana", "Davi", "João", "Maria", "Pedro", "Ana", "Bruno", "Carla")
    return alunos[0], alunos[-1]
# END [Acessa os registros de alunos.

# BEGIN [Calcula o dobro de um número.
def calcular_dobro(numero: float) -> float:
    return numero * 2
# END [Calcula o dobro de um número.

# BEGIN [Conta o número de letras em um nome.
def contar_letras(nome: str) -> int:    
    return len(nome.strip())
# END [Conta o número de letras em um nome.

# BEGIN [Exibe o menu de opções.
def exibir_menu() -> None:
    print("\n" + "="*50)
    print("SISTEMA DE GERENCIAMENTO ESCOLAR".center(50))
    print("="*50)
    print("\nEscolha uma opção:")
    print("1. Verificar Aprovação")
    print("2. Verificar Elegibilidade para Votar")
    print("3. Classificar Nota")
    print("4. Somar Números")
    print("5. Verificar Senha")
    print("6. Exibir Números de 1 a 10")
    print("7. Organizar Lista")
    print("8. Acessar Registros de Alunos")
    print("9. Calcular Dobro")
    print("10. Contar Letras")
    print("0. Sair")
    print("="*50)
# END [Exibe o menu de opções.

# BEGIN [Função principal que gerencia o menu do programa.
def menu() -> None:
    while True:
        exibir_menu()
        
        try:
            escolha = input("\nDigite o número da opção desejada: ").strip()
            
            if escolha == "0":
                print("\nObrigado por usar o sistema! Até logo!")
                break
                
            elif escolha == "1":
                nota = float(input("Digite a nota do aluno (0-10): "))
                print(verificar_aprovacao(nota))
                
            elif escolha == "2":
                idade = int(input("Digite sua idade: "))
                print(verificar_idade(idade))
                
            elif escolha == "3":
                nota = float(input("Digite a nota do aluno (0-100): "))
                print(classificar_nota(nota))
                
            elif escolha == "4":
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print(f"A soma é: {somar_numeros(num1, num2)}")
                
            elif escolha == "5":
                senha = input("Digite a senha: ")
                print("Senha correta! Acesso permitido." if verificar_senha(senha) else "Senha incorreta! Acesso negado.")
                
            elif escolha == "6":
                print("\nNúmeros de 1 a 10:")
                exibir_numeros()
                
            elif escolha == "7":
                print("\nNúmeros organizados:", organizar_lista())
                
            elif escolha == "8":
                primeiro, ultimo = acessar_registros()
                print(f"\nPrimeiro aluno: {primeiro}")
                print(f"Último aluno: {ultimo}")
                
            elif escolha == "9":
                numero = float(input("Digite um número: "))
                print(f"O dobro de {numero} é {calcular_dobro(numero)}")
                
            elif escolha == "10":
                nome = input("Digite um nome: ")
                print(f"O nome '{nome}' tem {contar_letras(nome)} letras.")
                
            else:
                print("\nOpção inválida! Por favor, escolha uma opção válida.")
                
        except ValueError:
            print("\nErro: Por favor, digite um valor numérico válido.")
        except Exception as e:
            print(f"\nOcorreu um erro: {str(e)}")
            
        input("\nPressione Enter para continuar...")
# END [Função principal que gerencia o menu do programa.

# BEGIN [Executa o programa.
if __name__ == "__main__":
    menu()
# END [Executa o programa.

# END [Desafio 1 - Tayná Goes de Sousa]
