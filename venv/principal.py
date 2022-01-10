import pygame  # Importa biblioteca
import constantes  # Importa módulos de constatntes.py
import sprites  # Importa módulos de sprites.py

# Cria classe Game
class Game:
    def __init__(self):  # Inicializa o método construtor
        # Criando tela do jogo
        pygame.init()  # Inicializa a biblioteca pygame
        pygame.mixer.init()  # Inicializa mixer para audio
        # Atributo que cria tela
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_JOGO)  #Recebe nome do jogo
        self.relogio = pygame.time.Clock()  # Controla a taxa de frames do jogo
        self.esta_rodando = True  #Atributo que recebe se o jogo está rodando

    # Instancia as classes da sprites do jogo
    def novo_jogo(self):
        self.todas_as_sprites = pygame.sprite.Group()  #Armazena grupo de sprites
        self.rodar()
    
    #Loop do jogo
    def rodar(self):
        self.jogando = True  #Variável recebe verdade
        while self.jogando:  #Enquanto verdadeiro
            self.relogio.tick(constantes.FPS)  #Configura o FPS
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

