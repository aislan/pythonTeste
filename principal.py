from dominio import Usuario, Lance, Leilao, Avaliador

aislan = Usuario('Aislan')
aline = Usuario('Aline')

lance_do_aislan = Lance(aislan,100.00)
lance_da_aline = Lance(aline,150.00)

leilao = Leilao('bolo')

leilao.lances.append(lance_do_aislan)
leilao.lances.append(lance_da_aline)


for lance in leilao.lances:
	print(f'{lance.usuario.nome} deu lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'Maior lance: {avaliador.maior_lance}')
print(f'Menor lance: {avaliador.menor_lance}')

print('teste')
print('teste')