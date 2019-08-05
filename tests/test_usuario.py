from dominio import Usuario, Leilao, Lance

def test_deve_subtrair_o_valor_do_lance_na_carteira_do_usuario_quando_for_proposto():
    aislan = Usuario('Aislan')

    leilao = Leilao("bolo")

    aislan.propoe_lance(leilao,50.00)

    assert aislan.carteira == 50.00