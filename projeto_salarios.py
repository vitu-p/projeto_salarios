## Aluno: Vitor Pinheiro Alves
## Projeto Salários
lista_salbruto = []
crescente_salbruto = []
def entrada_salario():
    salario_bruto = 1
    while(True):
        try:
            while(salario_bruto != 0.00):
                salario_bruto = float(input("Salário Bruto: "))
                if salario_bruto < 0.00: continue
                elif salario_bruto == 0.00: break
                else:
                    lista_salbruto.append(salario_bruto)
            if salario_bruto == 0.00:
                break
        except ValueError: continue
    return lista_salbruto

def aliquota_inss(salario: float):
    if salario <= 1518.00:
        return 0.075
    if salario <= 2793.88:
        return 0.09
    if salario <= 4190.84:
        return 0.12
    if salario <= 8157.41:
        return 0.14
    else:
        return 0
    
def deducao_inss(salario: float):
    if salario <= 1518.00:
        return 0.00
    if salario <= 2793.88:
        return 22.77
    if salario <= 4190.84:
        return 106.59
    if salario <= 8157.41:
        return 190.40
    else:
        return 951.62

def aliquota_ir(salario: float):
    if salario <= 2259.20:
        return 0.00
    if salario <= 2826.65:
        return 0.075
    if salario <= 3751.05:
        return 0.15
    if salario <= 4664.68:
        return 0.225
    else:
        return 0.275 

def deducao_ir(salario: float):
    if salario <= 2259.20:
        return 0.00
    if salario <= 2826.65:
        return 169.44
    if salario <= 3751.05:
        return 381.44
    if salario <= 4664.68:
        return 662.77
    else:
        return 896.00
    
def bubblesort(elementos: list):
    n = len(elementos)
    for j in range (n-1):
        for i in range (n-1-j):
            if elementos[i] > elementos[i +1]:
                elementos[i], elementos[i + 1] = elementos[i + 1], elementos[i]

    return elementos

def calculos(lista_salario: list):
    with open('CALCULOS.txt', 'w', encoding="utf-8") as f:
        f.write(f"\n{'Bruto':>12}{'AliqInss':>12}{'Val.Inss':>12}{'Base I.R.':>12}{'AliqIR':>12}{'Val.IR':>12}{'Liquido':>12}")
    n = len(lista_salario)
    i = 0
    for i in range(n):
        salbruto = lista_salario[i]
        aliqinss = aliquota_inss(salbruto)
        deducaoinss = deducao_inss(salbruto)
        valinss = (salbruto * aliqinss) - deducaoinss
        if valinss<0:
            valinss *= -1
        aliqir = aliquota_ir(salbruto-valinss)
        deducaoir = deducao_ir(salbruto-valinss)
        valir = ((salbruto - valinss)*aliqir) - deducaoir
        if valir < 10.0:
            valir = 0.0
        salliquido = salbruto - valinss - valir
        if deducaoinss == 951.62:
            with open('CALCULOS.txt', 'a', encoding="utf-8") as f:
                f.write(f"\n{salbruto:>12.2f}{"'Teto'":>12}{valinss:>12.2f}{(salbruto-valinss):>12.2f}{aliqir*100:>12.2f}{valir:>12.2f}{salliquido:>12.2f}")
        else:
            with open('CALCULOS.txt', 'a', encoding="utf-8") as f:
                f.write(f"\n{salbruto:>12.2f}{aliqinss*100:>12.2f}{valinss:>12.2f}{(salbruto-valinss):>12.2f}{aliqir*100:>12.2f}{valir:>12.2f}{salliquido:>12.2f}")
    with open('CALCULOS.txt', 'a', encoding="utf-8") as f:
        f.write(f"\nFim dos dados")
    return 'CALCULOS.txt'

lista_salbruto = entrada_salario()
crescente_salbruto = bubblesort(lista_salbruto)
calculos(crescente_salbruto)
with open('CALCULOS.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
