saldo=0

SAQUE_MAXIMO=500

SAQUE_LIMITE=3

numero_saques=0

extrato=""

while True:

    menu=f"""
Saldo:{saldo:.2f}
======MENU======
[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair
================
"""
        
    opcao=input(menu)
    if opcao=="d":

        valor=float(input("Insira o quanto deseja depositar:").replace(",","."))
        
        if valor>0:
            saldo += valor
            extrato += f"Depósito={valor:.2f}\n"
        
        else: 
            print("Falha de operação!O valor informado é inválido,tente novamente.")  

    elif opcao=="s":
        
        saque=float(input(f"Insira o valor de saque:\n\tValor máximo:{(SAQUE_MAXIMO)}\n\tSaques realizados:{numero_saques}\n").replace(",","."))
        
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

    elif opcao=="e":

        if not extrato:
            print("Não houveram alterações.")
        
        else:
            print("Extrato".center(11,"=")+"\n"+f"{extrato}\n"+"".center(11,"="))

    elif opcao=="q":
        break

    else:
        print("Falha na operação!Insira um valor válido.")
        