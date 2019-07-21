from unittest import TestCase
from dominio import Usuario, Leilao, Lance, Avaliador

class TestAvaliador(TestCase):
    def test_avalia(self):
        aislan = Usuario('Aislan')
        aline = Usuario('Aline')

        lance_do_aislan = Lance(aislan,100.00)
        lance_da_aline = Lance(aline,150.00)

        leilao = Leilao('bolo')

        leilao.lances.append(lance_do_aislan)
        leilao.lances.append(lance_da_aline)
        

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

class TestAvaliador(TestCase):
    def test_avalia(self):
        aislan = Usuario('Aislan')
        aline = Usuario('Aline')

        lance_do_aislan = Lance(aislan,100.00)
        lance_da_aline = Lance(aline,150.00)

        leilao = Leilao('bolo')

        
        leilao.lances.append(lance_da_aline)
        leilao.lances.append(lance_do_aislan)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
