import sys

class Usuario:
	def __init__(self,nome,carteira):
		self.__nome = nome
		self.__carteira = carteira
	
	@property
	def nome(self):
		return self.__nome
	
	@property
	def carteira(self):
		return self.__carteira

	def propoe_lance(self,leilao,valor):
    		lance = Lance(self,valor)
    		leilao.propoe(lance)
			#self.__carteira -= valor
			#self.carteira -= valor

class Lance:
	def __init__(self,usuario,valor):
		self.usuario = usuario
		self.valor = valor

class Leilao:
	def __init__(self, descricao):
		self.descricao = descricao
		self.__lances = []
		self.maior_lance = sys.float_info.min
		self.menor_lance = sys.float_info.max
		
	def propoe(self,lance):
		if not self.__lances or self.__lances[-1].usuario != lance.usuario and self.__lances[-1].valor<lance.valor:
			self.__lances.append(lance)
			for lance in self.__lances:
				if lance.valor > self.maior_lance:
					self.maior_lance = lance.valor
				if lance.valor < self.menor_lance:
					self.menor_lance = lance.valor
		else:
			raise ValueError("Erro ao propor lance!")

	@property
	def lances(self):
		return self.__lances[:]
