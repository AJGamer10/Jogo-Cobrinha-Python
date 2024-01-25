import pygame
from snake import Snake
from food import Food

pygame.init()

largura_tela = 800
altura_tela = 600
largura = 720
altura = 520
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo da Cobrinha")

relogio = pygame.time.Clock()
ticks = 7
fonte_small = pygame.font.SysFont(None, 20)
fonte = pygame.font.SysFont(None, 30)
fonte_titulo = pygame.font.SysFont(None, 50)

def mostrar_pontuacao(pontuacao):
    # Ajustar a largura do quadrado arredondado com base no número de dígitos na pontuação
    largura_quadrado = 150 + 10 * (len(str(pontuacao)) - 1)
    
    # Quadrado arredondado para exibir a pontuação
    rect = pygame.Rect(10, 10, largura_quadrado, 37)
    pygame.draw.rect(tela, (255, 255, 255), rect, border_radius=10)
    pygame.draw.rect(tela, (0, 0, 0), rect, 2, border_radius=10)
    
    texto = fonte.render("Pontuação: " + str(pontuacao), True, (0, 0, 0))
    tela.blit(texto, [20, 20])
    
def game_over(result, pontuacao):
    cor_clara = (251, 251, 251)  # Verde claro
    cor_escura = (205, 205, 205)   # Verde escuro
    borda = (150, 150, 150)
    tela.fill((0, 0, 0))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Retorna para a função que chamou game_over
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if largura_tela / 2 - 150 / 2 - 90 <= event.pos[0] <= largura_tela / 2 - 150 / 2 - 90 + 150 \
                        and altura_tela / 2 - 35 / 2 + 50 <= event.pos[1] <= altura_tela / 2 - 35 / 2 + 50 + 35:
                    # Clicou no botão "Recomeçar"
                    jogo()

                elif largura_tela / 2 - 150 / 2 + 90 <= event.pos[0] <= largura_tela / 2 - 150 / 2 + 90 + 150 \
                        and altura_tela / 2 - 35 / 2 + 50 <= event.pos[1] <= altura_tela / 2 - 35 / 2 + 50 + 35:
                    # Clicou no botão "Menu"
                    main()
        
        # Preencher a tela com um padrão xadrez de verde claro e escuro
        pygame.draw.rect(tela, borda, [70, 70, 660, 460])
        for i in range(80, largura, 20):
            for j in range(80, altura, 20):
                cor = cor_clara if (i + j) % 40 == 0 else cor_escura
                pygame.draw.rect(tela, cor, [i, j, 20, 20])
                
        # Desenha o quadro
        rect = pygame.Rect((largura_tela / 4), (altura_tela / 4), largura_tela / 2, altura_tela / 2)
        pygame.draw.rect(tela, (255, 255, 255), rect, border_radius=10)
        pygame.draw.rect(tela, (0, 0, 0), rect, 2, border_radius=10)
        
        # Desenha o Titulo
        titulo = fonte_titulo.render("Game Over", True, (0, 0, 0))
        titulo_rect = titulo.get_rect(center=(largura_tela / 2, altura_tela / 2 - 50))
        tela.blit(titulo, titulo_rect)
        
        # Desenha se ganhou ou perdeu
        
        result_text = fonte_small.render("Parabéns! Você venceu o jogo." if result == "venceu" else "Que pena, você perdeu! Mais sorte da próxima vez.", True, (0, 0, 0))
        result_rect = result_text.get_rect(center=(largura_tela / 2, altura_tela / 2))
        
        tela.blit(result_text, result_rect)
        
        # Desenha o botão de recomeçar
        restart = fonte.render("Recomeçar", True, (0, 0, 0))
        texto_rect = restart.get_rect(center=(largura_tela / 2 - 90, altura_tela / 2 + 50))
        
        rect = pygame.Rect(largura_tela / 2 - 150 / 2 - 90, altura_tela / 2 - 35 / 2 + 50, 150, 35)
        pygame.draw.rect(tela, (255, 255, 255), rect, border_radius=10)
        pygame.draw.rect(tela, (0, 0, 0), rect, 2, border_radius=10)
        
        tela.blit(restart, texto_rect)
        
        # Desenha o botão ir para o menu
        out = fonte.render("Menu", True, (0, 0, 0))
        texto_rect = out.get_rect(center=(largura_tela / 2 + 90, altura_tela / 2 + 50))
        
        rect = pygame.Rect(largura_tela / 2 - 150 / 2 + 90, altura_tela / 2 - 35 / 2 + 50, 150, 35)
        pygame.draw.rect(tela, (255, 255, 255), rect, border_radius=10)
        pygame.draw.rect(tela, (0, 0, 0), rect, 2, border_radius=10)
        
        tela.blit(out, texto_rect)
        
        pygame.display.update()
        relogio.tick(ticks)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if largura_tela / 2 - 150 / 2 <= event.pos[0] <= largura_tela / 2 - 150 / 2 + 150 \
                        and altura_tela / 2 - 35 / 2 + 50 <= event.pos[1] <= altura_tela / 2 - 35 / 2 + 50 + 35:
                    # Clicou no botão "Jogar"
                    jogo()

                elif largura_tela / 2 - 150 / 2 <= event.pos[0] <= largura_tela / 2 - 150 / 2 + 150 \
                        and altura_tela / 2 - 35 / 2 + 100 <= event.pos[1] <= altura_tela / 2 - 35 / 2 + 100 + 35:
                    # Clicou no botão "Sair"
                    pygame.quit()
                    quit()
        
        # Preencher a tela com um padrão xadrez de verde claro e escuro
        cor_clara = (251, 251, 251)  # Verde claro
        cor_escura = (205, 205, 205)   # Verde escuro
        borda = (150, 150, 150)
        pygame.draw.rect(tela, borda, [70, 70, 660, 460])
        for i in range(80, largura, 20):
            for j in range(80, altura, 20):
                cor = cor_clara if (i + j) % 40 == 0 else cor_escura
                pygame.draw.rect(tela, cor, [i, j, 20, 20])
        
        # Desenha o quadro
        rect = pygame.Rect((largura_tela / 4), (altura_tela / 4), largura_tela / 2, altura_tela / 2)
        pygame.draw.rect(tela, (255, 255, 255), rect, border_radius=10)
        pygame.draw.rect(tela, (0, 0, 0), rect, 2, border_radius=10)

        # Desenha o Título
        titulo = fonte_titulo.render("Jogo da Cobrinha", True, (0, 0, 0))
        titulo_rect = titulo.get_rect(center=(largura_tela / 2, altura_tela / 2 - 50))
        tela.blit(titulo, titulo_rect)

        # Desenha o botão de iniciar
        iniciar = fonte.render("Jogar", True, (0, 0, 0))
        texto_rect = iniciar.get_rect(center=(largura_tela / 2, altura_tela / 2 + 50))
        rect = pygame.Rect(largura_tela / 2 - 150 / 2, altura_tela / 2 - 35 / 2 + 50, 150, 35)
        pygame.draw.rect(tela, (255, 255, 255), rect, border_radius=10)
        pygame.draw.rect(tela, (0, 0, 0), rect, 2, border_radius=10)
        tela.blit(iniciar, texto_rect)

        # Desenha o botão de Sair
        sair = fonte.render("Sair", True, (0, 0, 0))
        texto_rect = sair.get_rect(center=(largura_tela / 2, altura_tela / 2 + 100))
        rect = pygame.Rect(largura_tela / 2 - 150 / 2, altura_tela / 2 - 35 / 2 + 100, 150, 35)
        pygame.draw.rect(tela, (255, 255, 255), rect, border_radius=10)
        pygame.draw.rect(tela, (0, 0, 0), rect, 2, border_radius=10)
        tela.blit(sair, texto_rect)

        pygame.display.update()
        relogio.tick(ticks)
    
def jogo():
    snake = Snake(largura, altura)
    food = Food(largura, altura, snake)
    
    cor_clara = (251, 251, 251)  # Verde claro
    cor_escura = (205, 205, 205)   # Verde escuro
    borda = (150, 150, 150)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            snake.mudar_direcao(event)
        
        if snake.game_over or largura * altura <= snake.comprimento:
            break
        
        snake.mover()
        snake.verificar_colisao_comida(food)
        snake.verificar_colisao()
        
        # Preencher a tela com um padrão xadrez de verde claro e escuro
        pygame.draw.rect(tela, borda, [70, 70, 660, 460])
        for i in range(80, largura, 20):
            for j in range(80, altura, 20):
                cor = cor_clara if (i + j) % 40 == 0 else cor_escura
                pygame.draw.rect(tela, cor, [i, j, 20, 20])
        
        food.desenhar(tela)
        snake.desenhar(tela)
        mostrar_pontuacao(snake.comprimento - 2)
        
        pygame.display.update()
        relogio.tick(ticks)
    game_over("venceu" if largura * altura <= snake.comprimento else "perdeu", snake.comprimento)
    
main()
