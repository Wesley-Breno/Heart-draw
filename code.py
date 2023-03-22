import turtle  # Biblioteca que sera responsavel por fazer o desenho do coracao

while True:  # Fazendo um loop infinito para o programa continuar desenhando o coracao infinitamente
    
    # Configurando a tela
    tela = turtle.Screen()
    tela.bgcolor('black')
    tela.setup(width=600, height=400)
    tela.delay(1)
    
    # Configurando a caneta
    tartaruga = turtle.Turtle()
    tartaruga.color('red')
    tartaruga.pensize(5)

    # Comando numericos que serao usados para fazer a caneta girar para a direita e seguir em frente
    comandos = [50, 100, 50, 50, 80, 50, 50, 21,
                270, 25, 400, 35, 60, 50, 70, 125]

    for c in range(len(comandos)):  # Desenhando coracao
        if c == 0:  # Se for o primeiro comando
            tartaruga.left(comandos[c])
        else:
            if c % 2 == 0:  # Se for para virar a direcao da caneta
                tartaruga.left(comandos[c])
            else:  # Se for para seguir em frente
                tartaruga.forward(comandos[c])

    tela.clear()  # Limpando tela
