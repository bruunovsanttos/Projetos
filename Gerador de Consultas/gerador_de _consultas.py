import datetime

#1. Definição das Estruturas de Dados

#Crie uma lista para armazenar os pacientes cadastrados.
pacientes = []
#Crie uma lista para armazenar as consultas agendadas.
consultas = []


#3. Cadastrar um Paciente
#Peça ao usuário para inserir o nome e o telefone.
#Verifique se o telefone já está cadastrado na lista de pacientes.
#Se o telefone não estiver cadastrado, adicione o paciente à lista de pacientes e exiba uma mensagem de sucesso.
#Se o telefone já estiver cadastrado, exiba uma mensagem de erro e retorne ao menu principal.
def cadastro_paciente():
    nome = input("Digite o nome do paciente:")
    telefone = input("insira um numero de Telefone sem traços ou parenteses ex 999999999: ")

    for paciente in pacientes:
        if paciente["telefone"] == telefone:
            print("Esse telefone já tem cadastro...")
            return

    novo_paciente = {"nome": nome, "telefone": telefone}
    pacientes.append(novo_paciente)
    print("Paciente cadastrado com sucesso")

#4. Marcar uma Consulta
#Exiba a lista numerada de pacientes cadastrados.
def listar_pacientes():
    for indice, paciente in enumerate(pacientes):
        print(f"{indice}: {paciente["nome"],paciente["telefone"]}")




def marcar_consulta():
    # Peça ao usuário para escolher um paciente a partir da lista.
    listar_pacientes()
    paciente_escolhido = int(input("Escolha um paciente para marcar consulta:"))
    confirmacao = int(input(f"O paciente escolhido foi {paciente_escolhido}? 1 - Sim 2 - Não"))

    if confirmacao == 1:
        # Solicite a data, hora e especialidade desejada.
        data = input("Para qual data deseja marcar consulta? ex:dd-mm-aaaa: ")
        hora = input("Qual o hórario desejado?(para hórarios depois do meio dia utilizar 13:00): ")
        especialidade = input("Qual a especialidade desejada?: ")

        # Verifique se a data e hora são válidas (não no passado).
        data_consulta = datetime.datetime.strptime(f"{data} {hora}", "%d-%m-%Y %H:%M")

        if data_consulta <= datetime.datetime.now():
            print("Não é possivel marcar pois você marcou uma data retoativa, tente novamente...")
            return

        # Verifique se a data e a hora já estão ocupadas para qualquer paciente.
        elif data_consulta == datetime.datetime.now():
            print("ja temos consulta marcada no mesmo horário, tente outro horário.")


        # Se estiverem disponíveis e válidas, adicione o agendamento à lista de consultas e exiba uma mensagem de sucesso.
        elif data_consulta > datetime.datetime.now():
            consultas.append({
                "paciente": paciente_escolhido,
                "data": data,
                "hora": hora,
                "especialidade": especialidade
            })
            print("Consulta marcada com sucesso.")

    elif confirmacao == 2:
        print("não foi possivel agendar, tente novamente.")
        return






def cancelar_consulta():
    pass
#5. Cancelar uma Consulta
#Exiba a lista numerada de agendamentos existentes.
#Peça ao usuário para escolher um agendamento a partir da lista.
#Exiba os detalhes da consulta selecionada.
#Pergunte ao usuário se ele deseja cancelar a consulta.
#Se sim, remova o agendamento da lista e exiba uma mensagem de confirmação.
#Se não, retorne ao menu principal.


#2. Menu Principal

#Crie um loop while que exibirá o menu principal e permitirá ao usuário escolher uma das opções:

while True:

    menu = int(input("""
-------------Clínica Agil Agendamentos-------------

1 - Cadastrar paciente
2 - Marcar Consulta
3 - Cancelar Consulta
4 - Sair

---------------------------------------------------

Digite sua resposta:
"""))

    # Cadastrar um paciente.
    if menu == 1:
        cadastro_paciente()
    # Marcar uma consulta.
    elif menu == 2:
        marcar_consulta()
    # Cancelar uma consulta.
    elif menu == 3:
        cancelar_consulta()

    # 6. Sair
    # Encerre o loop while e finalize o programa.
    elif menu == 4:
        print("Obrigado por utilizar nossos serviços")
        break


