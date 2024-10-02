usuarios = []

def cadastro_usuario(nome, email):
    for usuario in usuarios:
        if usuario['email'] == email:
            return "Esse email já existe"

    if not email.strip():
        return "Email invalido"

    novo_usuario = {
        'nome' : nome,
        'email': email


    }   

    usuarios.append(novo_usuario)
    return "Usuário cadastrado com sucesso" 