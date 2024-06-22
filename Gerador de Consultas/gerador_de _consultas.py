import datetime

pacientes = []
consultas = []

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

def listar_pacientes():
    for indice, paciente in enumerate(pacientes):
        print(f"{indice}: {paciente["nome"],paciente["telefone"]}")

def marcar_consulta():
    listar_pacientes()
    paciente_escolhido = int(input("Escolha um paciente para marcar consulta:"))
    confirmacao = int(input(f"O paciente escolhido foi {paciente_escolhido}? 1-Sim 2-Não"))

    if confirmacao == 1:
        data = input("Para qual data deseja marcar consulta? ex:dd-mm-aaaa: ")
        hora = input("Qual o hórario desejado?(para hórarios depois do meio dia utilizar 13:00): ")
        especialidade = input("Qual a especialidade desejada?: ")

        data_consulta = datetime.datetime.strptime(f"{data} {hora}", "%d-%m-%Y %H:%M")

        if data_consulta <= datetime.datetime.now():
            print("Não é possivel marcar pois você colocou uma data retroativa, tente novamente...")
            return

        for consulta in consultas:
            consulta_data_hora = datetime.datetime.strptime(f"{consulta['data']} {consulta['hora']}", "%d-%m-%Y %H:%M")
            if consulta_data_hora == data_consulta:
                print("Já temos consulta marcada no mesmo horário, tente outro horário.")
                return

        if data_consulta > datetime.datetime.now():
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

def listar_consultas():
    for indice, consulta in enumerate(consultas):
        print(f"{indice}: {consulta["paciente"], consulta["data"], consulta["hora"],consulta["especialidade"]}")

def cancelar_consulta():
    listar_consultas()
    consulta_cancelar = int(input(f"Qual consulta deseja cancelar?: "))
    confirmacao = int(input(f"A consulta {consulta_cancelar} é a que deseja cancelar?: 1-Sim 2-Não"))
    if confirmacao == 1:
        consultas.pop(consulta_cancelar)
        print("Consulta cancelada com sucesso.")


    elif confirmacao == 2:
        print("Não foi possível cancelar a consulta, tente novamente...")

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

    if menu == 1:
        cadastro_paciente()

    elif menu == 2:
        marcar_consulta()

    elif menu == 3:
        cancelar_consulta()

    elif menu == 4:
        print("Obrigado por utilizar nossos serviços")
        break
