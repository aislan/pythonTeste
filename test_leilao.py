from unittest import TestCase
from dominio import Usuario, Leilao, Lance

class TestLeilao(TestCase):
    def setUp(self):
        self.aislan = Usuario('Aislan')
        self.lance_do_aislan = Lance(self.aislan,100.00)
        self.leilao = Leilao('bolo')
        

    def test_deve_retornar_o_menor_e_o_maior_valor_quando_adicionados_em_ordem_crescente(self):
        aline = Usuario('Aline')

        lance_da_aline = Lance(aline,150.00)

        self.leilao.propoe(self.lance_do_aislan)
        self.leilao.propoe(lance_da_aline)
        


        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_erro_quando_um_lance_menor_que_o_anterior_for_proposto(self):
        
        aline = Usuario('Aline')

        
        lance_da_aline = Lance(aline,150.00)

        with self.assertRaises(ValueError):
            self.leilao.propoe(lance_da_aline)
            self.leilao.propoe(self.lance_do_aislan)
            
    def test_deve_retornar_marior_e_menor_lance_igual_quando_tiver_apenas_um_lance(self):
     
        self.leilao.propoe(self.lance_do_aislan)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 100.00

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
       

    def test_deve_retornar_marior_e_menor_lance_igual_quando_o_leilao_tiver_tres_lances(self):
        aline = Usuario('Aline')
        rafaela = Usuario('Rafaela')

 
        lance_da_aline = Lance(aline,110.00)
        lance_da_rafaela = Lance(rafaela,120.00)


        self.leilao.propoe(self.lance_do_aislan)
        self.leilao.propoe(lance_da_aline)
        self.leilao.propoe(lance_da_rafaela)
       

        menor_valor_esperado = 100.00
        maior_valor_esperado = 120.00

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    
    #se não houver nenhum lance deve aceitar um novo lance
    def test_se_nao_houve_nenhum_lance_deve_aceitar_um_novo_lance(self):
        self.leilao.propoe(self.lance_do_aislan)
        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(1,quantidade_de_lances)

    #se já houver um lance deve aceitar um outro lance de outro usuário
    def test_se_ja_houve_um_lance_deve_aceitar_um_outro_lance_de_outro_usuario(self):
        aline = Usuario("Aline")
        lance_da_aline = Lance(aline,200)

        self.leilao.propoe(self.lance_do_aislan)
        self.leilao.propoe(lance_da_aline)

        quantidade_de_lances = len(self.leilao.lances)

        self.assertEqual(2,quantidade_de_lances)

    #se já houve um lande um usuário o próximo lance não deve ser do mesmo usuário
    def test_se_ja_houve_um_lance_de_um_usuario_o_proximo_lance_nao_deve_ser_do_mesmo_usuario(self):
        aislan = self.aislan
        lance_do_aislan = Lance(aislan,300)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_aislan)
            self.leilao.propoe(lance_do_aislan)
