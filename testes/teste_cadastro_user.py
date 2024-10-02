import unittest
from src.cadastro_user import cadastro_usuario, usuarios

class TestCadastroUsuario(unittest.TestCase):

    def setUp(self):
        usuarios.clear()

    def teste_cadastro_novo_usuario(self):
        resultado = cadastro_usuario("Pedro Henrique", "pedrohenrique@gmail.com")
        self.assertEqual(resultado, "Usuário cadastrado com sucesso")
        self.assertEqual(usuarios, [0]['nome'],'Pedro Henrique')
    
    def teste_cadastro_email_invalido(self):
        resultado = cadastro_usuario("Pedro Henrique", "")
        self.assertEqual(resultado, "Email invalido")
