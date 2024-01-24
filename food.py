import pygame
import random

class Food:
    def __init__(self, largura, altura, snake):
        self.largura = largura
        self.altura = altura
        self.tamanho = 20
        self.snake = snake
        self.atualizar_posicao()
        
    def atualizar_posicao(self):
        while True:
            # Gerar coordenadas divisíveis por 40
            self.x_comida = round(random.randrange(80, self.largura - self.tamanho, 40))
            self.y_comida = round(random.randrange(80, self.altura - self.tamanho, 40))
            
            # Verificar se acomida não está posição da cobra
            if not any((self.x_comida, self.y_comida) == (x, y) for x, y in self.snake.lista_cobra):
                break
        
    def desenhar(self, tela):
        pygame.draw.rect(tela, (255, 0, 0), [self.x_comida, self.y_comida, self.tamanho, self.tamanho])
        pygame.draw.rect(tela, (0, 0, 0), [self.x_comida, self.y_comida, self.tamanho, self.tamanho], 1)
