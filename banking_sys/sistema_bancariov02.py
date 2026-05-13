def menu(saldo):
    
    menu=f"""
    Saldo:{saldo:.2f}
    ======MENU======
    [d]Depositar
    [s]Sacar
    [e]Extrato
    [nu]Novo usuário
    [nc]Nova conta
    [q]Sair
    ================
    """
    return input(menu)

def depositar(saldo,extrato,valor,/):
    if valor>0:
        saldo += valor
        extrato += f"Depósito={valor:.2f}\n"
        
    else: 
        print("Falha de operação!O valor informado é inválido,tente novamente.")

    return saldo,extrato

def sacar(*,saque,numero_saques,saldo,extrato):
    if saque>SAQUE_MAXIMO:
        print("Falha na operação!O valor é inválido, insira um valor até,no máximo, R$500,00.")
        
    elif numero_saques==SAQUE_LIMITE:
        print("Falha na operação!Número diário de saques atingido")
        
    elif saque>saldo:
        print("Falha na operação!Você não tem saldo suficiente")
        
    elif saque>0:
        saldo -= saque
        extrato += f"Saque:{saque:.2f}\n"
        numero_saques += 1
        
    else:
        print("Falha na operação!O valor é igual ou menor que zero,insira um valor válido.")

    return saldo,extrato,numero_saques

def exibir_extrato(saldo,/,*,extrato):
    if not extrato:
            print("Não houveram alterações.")
        
    else:
            print("Extrato".center(30,"=")+"\n"+f"{extrato}\n "+"".center(30,"="))
            print("Saldo".center(30,"=")+"\n"+f"{saldo:.2f}\n "+"".center(30,"="))

def criar_usuario():
    nome=input("insira seu nome:")
    data_nascimento=input("insira sua data de nascimento(ex:20/10/2010):")
    local=input("Insira seu endereço(ex:logradouro-número-bairro-cidade/sigla do Estado)")
    while True:
        cpf = input("Insira seu CPF (apenas números): ").strip()
        cpf_existe = any(usuario["cpf"] == cpf for usuario in usuarios)
        if cpf_existe:
            print("Erro: Este CPF já está cadastrado! Tente outro.")
        
        elif (not (cpf.isdigit()) or (len(cpf) != 11)):
            print("Erro: O CPF deve conter exatamente 11 números.")
    
        else:
            break
    print("Usuário cadastrado com sucesso!")    
    return {"nome":nome,"data_nascimento":data_nascimento,"endereco":local,"cpf":cpf}
    


def criar_conta():
    while True:
        cpf=input("Insira o CPF de seu usuário(apenas números):")
        usuario_encontrado = next((u for u in usuarios if u["cpf"] == cpf), None)
        if not usuario_encontrado:
            print("Erro: Usuário não encontrado!")
            continue
        break
        
        
    numero_conta = len(contas) + 1
    NUMERO_AGENCIA="0001"
    return{
        "agencia":NUMERO_AGENCIA,
        "numero_conta":numero_conta,
        "usuário":usuario_encontrado["nome"],
        "cpf":cpf
}



usuarios = []

contas = []

saldo=0

SAQUE_MAXIMO=500

SAQUE_LIMITE=3

numero_saques=0

extrato=""

while True:
    opcao=menu(saldo)

    if opcao=="d":

        valor=float(input("Insira o quanto deseja depositar:").replace(",","."))
        saldo,extrato=depositar(saldo,extrato,valor)    
            

    elif opcao=="s":
            
            saque=float(input(f"Insira o valor de saque:\n\tValor máximo:{(SAQUE_MAXIMO)}\n\tSaques realizados:{numero_saques}\n").replace(",","."))
            saldo,extrato,numero_saques=sacar(
            saque=saque, 
            numero_saques=numero_saques, 
            saldo=saldo, 
            extrato=extrato
            )
            
            
    elif opcao=="e":
        exibir_extrato(saldo,extrato=extrato)
            
    elif opcao=="q":
        break
        
    elif opcao=="nu":
       usuarios.append(criar_usuario())
        
    elif opcao=="nc":
        contas.append(criar_conta())
        
    else:
        print("Falha na operação!Insira um valor válido.")
        