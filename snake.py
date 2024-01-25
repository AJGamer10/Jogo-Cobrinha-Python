import pygame
import time

class Snake:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.tamanho = 20
        self.velocidade = 20
        self.comprimento = 2
        self.delta_x = self.tamanho
        self.delta_y = 0
        self.x_cobra = 40 * 7
        self.y_cobra = 40 * 7
        self.lista_cobra = [(self.x_cobra, self.y_cobra)]
        self.game_over = False
        self.ultimo_movimento = time.time()
        
    def mover(self):
        self.x_cobra += self.delta_x
        self.y_cobra += self.delta_y
        
        if self.x_cobra >= self.largura:
            self.x_cobra = 80
        elif self.x_cobra < 80:
            self.x_cobra = self.largura - self.tamanho

        if self.y_cobra >= self.altura:
            self.y_cobra = 80
        elif self.y_cobra < 80:
            self.y_cobra = self.altura - self.tamanho

        cabeca_cobra = (self.x_cobra, self.y_cobra)
        self.lista_cobra.append(cabeca_cobra)

        if len(self.lista_cobra) > self.comprimento:
            del self.lista_cobra[0]
                
    def mudar_direcao(self, event):
        # Verifica se a cobra já se moveu pelo menos um quadrado
        if len(self.lista_cobra) > 1:
            # Adiciona um intervalo mínimo entre as mudanças de direção
            if time.time() - self.ultimo_movimento < 0.1:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.delta_x == 0:
                    self.delta_x = -self.tamanho
                    self.delta_y = 0
                elif event.key == pygame.K_RIGHT and self.delta_x == 0:
                    self.delta_x = self.tamanho
                    self.delta_y = 0
                elif event.key == pygame.K_UP and self.delta_y == 0:
                    self.delta_y = -self.tamanho
                    self.delta_x = 0
                elif event.key == pygame.K_DOWN and self.delta_y == 0:
                    self.delta_y = self.tamanho
                    self.delta_x = 0
                    
            # Atualiza o tempo da última mudança de direção
            self.ultimo_movimento = time.time()
            
    def verificar_colisao_comida(self, food):
        cabeca_cobra = pygame.Rect(self.x_cobra, self.y_cobra, self.tamanho, self.tamanho)
        comida = pygame.Rect(food.x_comida, food.y_comida, food.tamanho, food.tamanho)

        if cabeca_cobra.colliderect(comida):
            food.atualizar_posicao()
            self.comprimento += 1
    
    def verificar_colisao(self):
        cabeca_cobra = pygame.Rect(self.x_cobra, self.y_cobra, self.tamanho, self.tamanho)
        
        # Verificar colisão com as bordas
        if (
            self.x_cobra <= 80 or self.x_cobra >= self.largura - self.tamanho or
            self.y_cobra <= 80 or self.y_cobra >= self.altura - self.tamanho
        ):
            self.game_over = True
        
        # Verificar colisão com a própria cobra
        for segmento in self.lista_cobra[:-1]:
            if cabeca_cobra.colliderect(pygame.Rect(segmento[0], segmento[1], self.tamanho, self.tamanho)):
                self.game_over = True
            
    def desenhar(self, tela):
        for i, segmento in enumerate(self.lista_cobra):
            # Calcular a posição relativa do segmento da cobra
            rel_pos = i / len(self.lista_cobra) # Varia de 0 a 1
            
            # Calcular a cor com base no degradê de verde para azul
            cor_verde = (0, 255, 0)
            cor_azul = (0, 0, 255)
            cor_segmento = (
                int((1 - rel_pos) * cor_verde[0] + rel_pos * cor_azul[0]),
                int((1 - rel_pos) * cor_verde[1] + rel_pos * cor_azul[1]),
                int((1 - rel_pos) * cor_verde[2] + rel_pos * cor_azul[2])
            )
            
            pygame.draw.rect(tela, cor_segmento, [segmento[0], segmento[1], self.tamanho, self.tamanho])
            pygame.draw.rect(tela, (0, 0, 0), [segmento[0], segmento[1], self.tamanho, self.tamanho], 1)
        