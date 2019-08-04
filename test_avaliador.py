from unittest import TestCase
from dominio import Usuario, Leilao, Lance, Avaliador

class TestAvaliador(TestCase):
    def setUp(self):
        self.aislan = Usuario('Aislan')
        self.lance_do_aislan = Lance(self.aislan,100.00)
        self.leilao = Leilao('bolo')
        

    def test_deve_retornar_o_menor_e_o_maior_valor_quando_adicionados_em_ordem_crescente(self):
        aline = Usuario('Aline')

        lance_da_aline = Lance(aline,150.00)

        self.leilao.propoe(self.lance_do_aislan)
        self.leilao.propoe(lance_da_aline)
        

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_menor_e_o_maior_valor_quando_adicionados_em_ordem_decrescente(self):
        
        aline = Usuario('Aline')

        
        lance_da_aline = Lance(aline,150.00)


        self.leilao.propoe(lance_da_aline)
        self.leilao.propoe(self.lance_do_aislan)
        
        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_marior_e_menor_lance_igual_quando_tiver_apenas_um_lance(self):
     
        self.leilao.propoe(self.lance_do_aislan)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 100.00

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
       

    def test_deve_retornar_marior_e_menor_lance_igual_quando_o_leilao_tiver_tres_lances(self):
        aline = Usuario('Aline')
        rafaela = Usuario('Rafaela')

 
        lance_da_aline = Lance(aline,110.00)
        lance_da_rafaela = Lance(rafaela,120.00)


        self.leilao.propoe(self.lance_do_aislan)
        self.leilao.propoe(lance_da_rafaela)
        self.leilao.propoe(lance_da_aline)
        
        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 120.00

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

