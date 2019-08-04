from dominio import Usuario, Lance, Leilao

aislan = Usuario('Aislan')
aline = Usuario('Aline')

lance_do_aislan = Lance(aislan,100.00)
lance_da_aline = Lance(aline,150.00)

leilao = Leilao('bolo')

leilao.propoe(lance_do_aislan)
leilao.propoe(lance_da_aline)


for lance in leilao.lances:
	print(f'O {lance.usuario.nome} deu lance de {lance.valor}')


print(f'Maior lance: {leilao.maior_lance}')
print(f'Menor lance: {leilao.menor_lance}')

