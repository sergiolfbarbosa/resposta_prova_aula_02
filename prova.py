#[LP-A02] Escreva um programa em python que pergunte ao usuário a velocidade de um carro.
#Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
#Nesse caso, exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.

velocidade = int(input("Digite sua velocidade: "))
multa_valor = 165
aplicacao_multa = 0

if velocidade <= 80:
    print("Usuário, o senhor(a) não foi multado!")
elif velocidade > 80:
    aplicacao_multa = multa_valor + (20 * (velocidade - 80))
    print(f"Usuário, o senhor(a) foi multado em R${aplicacao_multa:,.2f}!")