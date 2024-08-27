menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def main():
    while True:
        opcao = input(menu).lower().strip()
        match opcao:
            case "d":
                depositar()
            case "s":
                sacar()
            case "e":
                print_extrato()
            case "q":
                break
            case _:
                print("Operacao invalida")
    
    return 0
                

def sacar():
    global numero_saques, LIMITE_SAQUES, limite, saldo, extrato
    if(numero_saques >= LIMITE_SAQUES):
        print("Operacao falhou. Numero de saques excedido")
        return
    valor = float(input("Informe o valor do saque: "))
    if(valor > limite):
        print("Operacao falhou. Valor do saque excedeu o limte")
        return
    if(valor > saldo):
        print("Operacao falhou. Saldo insuficiente")
        return
    if(valor > 0):
        saldo -= valor
        extrato += f'Saque: R${valor:.2f}\n'
        numero_saques += 1
        return

def depositar():
    global saldo, extrato
    valor = float(input("Informe o valor do deposito: "))
    if(valor <= 0):
        print("Operacao falhou. Valor invalido")
        return
    saldo += valor
    extrato += f'Deposito: R${valor:.2f}\n'

def print_extrato():
    global extrato
    print("\n" + "Extrato".center(32, "="))
    print(extrato)   
    print("=" * 32)
main()
