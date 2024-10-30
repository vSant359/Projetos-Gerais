from PIL import Image

# Carrega a imagem
imagem = Image.open(r'C:\\Users\\despachatur\\Documents\\Projetos-Gerais\\Projetos-Gerais\\Front-end\\assets\\dom-quixote.png')

# Define a nova largura
nova_largura = 850  # Altere para a largura desejada

# Calcula a nova altura mantendo a proporção
proporcao = imagem.height / imagem.width
nova_altura = int(nova_largura * proporcao)

# Redimensiona a imagem
nova_imagem = imagem.resize((nova_largura, nova_altura))

# Salva a nova imagem
nova_imagem.save(r'C:\\Users\\despachatur\\Documents\\Projetos-Gerais\\Projetos-Gerais\\Front-end\\assets\\dom-quixote.png')
