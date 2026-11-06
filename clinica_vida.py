#!/usr/bin/env python3
# Clínica Vida+ — cadastro de pacientes no terminal
# Dados fictícios para fins acadêmicos.

pacientes = []


def ler_idade():
    while True:
        entrada = input("Idade: ").strip()
        try:
            idade = int(entrada)
            if 0 <= idade <= 130:
                return idade
            print("Digite uma idade entre 0 e 130.")
        except ValueError:
            print("Idade inválida. Use apenas números inteiros.")


def cadastrar_paciente():
    print("\n--- Cadastro de paciente ---")
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome não pode ficar vazio.")
        return
    idade = ler_idade()
    telefone = input("Telefone: ").strip()
    if not telefone:
        print("Telefone não pode ficar vazio.")
        return
    pacientes.append({"nome": nome, "idade": idade, "telefone": telefone})
    print(f"Paciente {nome} cadastrado com sucesso!")


def ver_estatisticas():
    print("\n--- Estatísticas ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    idades = [paciente["idade"] for paciente in pacientes]
    mais_novo = min(pacientes, key=lambda paciente: paciente["idade"])
    mais_velho = max(pacientes, key=lambda paciente: paciente["idade"])
    print(f"Total cadastrado: {len(pacientes)}")
    print(f"Idade média: {sum(idades) / len(idades):.1f} anos")
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")


def buscar_paciente():
    print("\n--- Buscar paciente ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    termo = input("Nome para busca: ").strip().lower()
    encontrados = [p for p in pacientes if termo in p["nome"].lower()]
    if not encontrados:
        print("Nenhum paciente encontrado.")
        return
    for paciente in encontrados:
        print(f"- {paciente['nome']} | {paciente['idade']} anos | {paciente['telefone']}")


def listar_pacientes():
    print("\n--- Todos os pacientes ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    for indice, paciente in enumerate(pacientes, start=1):
        print(f"{indice}. {paciente['nome']} | {paciente['idade']} anos | {paciente['telefone']}")


def menu():
    while True:
        print("\n===== CLÍNICA VIDA+ =====")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente pelo nome")
        print("4. Listar todos os pacientes")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            ver_estatisticas()
        elif opcao == "3":
            buscar_paciente()
        elif opcao == "4":
            listar_pacientes()
        elif opcao == "5":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Escolha de 1 a 5.")


if __name__ == "__main__":
    menu()
