# Game Module
from sys import exit
from clueless import Board, Button, Network
from clueless.Network import Network
import pickle
import pygame


class Game:
    WIDTH = 875
    HEIGHT = 700
    FPS = 60

    def __init__(self):
        pygame.init()
        
        self.network = Network()
        self.id = int(self.network.get_id())
        self.playing = True
        player_caption = "Clue-Less Player " + str(self.id)
        pygame.display.set_caption(player_caption)
        self.state = "START"
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.gameLoop()

    def gameLoop(self):

        while self.playing:
            self.tick()
            self.render()

            try:
                #game = self.network.send_receive("get")
                game_data = self.network.build_package("get", "")
                #print(game_data)
                game = self.network.send_receive(game_data)
                #game = self.network.send_receive("get")
            except:
                run = False
                print("Couldn't get game")
                break

            events = pygame.event.get()
            self.checkEvents(events)
            self.addView()

            #receive updates
            #update = self.network.receive()
            
            #if (update != self.id):
            #    if(update[0] != self.id and update != prev_turn):
            #        print("update: ", update)
            #    prev_turn = update
            
        # when pygame.QUIT event happens, change self.playing to False 
        # the while loop will end and quit the game
        pygame.quit()

    def checkEvents(self, events) :
        for event in events:
            if event.type == pygame.QUIT:
                self.playing = False

    def addView(self):
        # Add board
        board = Board.Board()
        board.loadTiles(self.screen, board)

        # Initialize Buttons
        buttonYPos = 75
        buttonXPos = 650
        buttonDistance = 60
        isRoomSelectionActive = board.loadButton(self.screen, "Go To Room", buttonXPos, buttonYPos)
        isAccuseSelectionActive = board.loadButton(self.screen, "Accuse", buttonXPos, buttonYPos + buttonDistance)
        isSuggestSelectionActive = board.loadButton(self.screen, "Suggest", buttonXPos, buttonYPos + buttonDistance*2)
        isEndTurnSelectionActive = board.loadButton(self.screen, "End Turn", buttonXPos, buttonYPos + buttonDistance*3)

        mousePos = pygame.mouse.get_pos()
        if isRoomSelectionActive:
            self.state = "CHOOSING"
            board.loadRoomOptions(self.screen)
            turn_data = self.network.build_package(self.state, str(mousePos))
            #print(turn_data)
            self.network.send(turn_data)

        #Manually record the rectangle position of close button. Everytime this button is pressed, close the options box
        closeRect = pygame.Rect(820, 570, 55, 30)
        if (closeRect.collidepoint(mousePos) and pygame.mouse.get_pressed()[0] == 1 and self.state == 'CHOOSING'):
            board.closeRoomOptions(self.screen)
            self.state = "START"
            isRoomSelectionActive = False

    def render(self):
        pygame.display.update()

    def tick(self):
        self.clock.tick(self.FPS)

