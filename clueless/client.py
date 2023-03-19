# #Client Module
import pygame
from network import Network
import pickle
pygame.font.init()

WIDTH = 500
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player")


# def redraw_window(window, player1, player2):
#      window.fill((255,255,255))
#      player1.draw(window)
#      player2.draw(window)
#      pygame.display.update()

# def run():
#     run = True
#     network = Network()
#     player1 = network.get_player()
#     clock = pygame.time.Clock()

#     while run:
#         clock.tick(60)
#         player2 = network.send(player1)

#         for event in pygame.event.get():
#              if event.type == pygame.QUIT:
#                   run = False
#                   pygame.quit()

#         player1.move()
#         redraw_window(window, player1, player2)

# run()




class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("arial", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


def redraw_window(win, game, p):
    win.fill((128,128,128))

    if not(game.connected()):
        font = pygame.font.SysFont("arial", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("arial", 60)
        text = font.render("Your Move", 1, (0, 255,255))
        win.blit(text, (80, 200))

        text = font.render("Opponent", 1, (0, 255, 255))
        win.blit(text, (380, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.both_went():
            text1 = font.render(move1, 1, (0,0,0))
            text2 = font.render(move2, 1, (0, 0, 0))
        else:
            if game.p1_went and p == 0:
                text1 = font.render(move1, 1, (0,0,0))
            elif game.p1_went:
                text1 = font.render("Turn Complete", 1, (0, 0, 0))
            else:
                text1 = font.render("Waiting...", 1, (0, 0, 0))

            if game.p2_went and p == 1:
                text2 = font.render(move2, 1, (0,0,0))
            elif game.p2_went:
                text2 = font.render("Turn Complete", 1, (0, 0, 0))
            else:
                text2 = font.render("Waiting...", 1, (0, 0, 0))

        if p == 1:
            win.blit(text2, (100, 350))
            win.blit(text1, (400, 350))
        else:
            win.blit(text1, (100, 350))
            win.blit(text2, (400, 350))

        turn_button.draw(window)

    pygame.display.update()


#btns = [Button("Rock", 50, 500, (0,0,0)), Button("Scissors", 250, 500, (255,0,0)), Button("Paper", 450, 500, (0,255,0))]

turn_button = Button("Take Turn", 250, 500, (0,0,0))

def main():
    run = True
    clock = pygame.time.Clock()
    network = Network()
    player = int(network.get_player())
    print("You are player", player)

    while run:
        clock.tick(60)
        try:
            game = network.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.both_went():
            redraw_window(window, game, player)
            pygame.time.delay(500)
            try:
                game = network.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("arial", 90)
            text = font.render("currently playing", 1, (255,0,0))
            window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if turn_button.click(pos) and game.connected():
                    if player == 0:
                        if not game.p1_went:
                            network.send(turn_button.text)
                    else:
                        if not game.p2_went:
                            network.send(turn_button.text)

        redraw_window(window, game, player)

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        window.fill((128, 128, 128))
        font = pygame.font.SysFont("arial", 60)
        text = font.render("Click to Play!", 1, (255,0,0))
        window.blit(text, (100,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu_screen()