import asyncio
from websockets.sync.client import connect
import pygame
pygame.font.init()
class player:
    def __init__(self,x,y,app):
        self.rect = pygame.Rect(x,y,50,50)
        self.name = input()
        self.positions = {}
        self.names = []
        self.app = app
    def update(self):
        
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.rect.y -= 5
        if key[pygame.K_s]:
            self.rect.y += 5
        if key[pygame.K_a]:
            self.rect.x -= 5
        if key[pygame.K_d]:
            self.rect.x += 5
        self.hello()
        for i in self.names:
            pygame.draw.rect(self.app.screen,"red",pygame.Rect(int(self.positions[i][0]),int(self.positions[i][1]),50,50))
        #print(self.names)
    def hello(self):

        with connect("ws://localhost:8765") as websocket:
            websocket.send(f"{self.rect.x} {self.rect.y} {self.name}")    
            message = websocket.recv()
            for i in message.split("k"):
                if i != "":
                    d = i.split(" ")
                    self.positions[d[2]] = [int(d[0]),int(d[1])]
                    if not d[2] in self.names:
                        self.names.append(d[2])
            #print(f"Received: {message}")

class App:
    def __init__(self,width=800,height=800):
        self.screen = pygame.display.set_mode((width,height))
        self.run = True
        self.clock = pygame.time.Clock()
        self.player = player(0,0,app=self)
    def update(self):
        while self.run:
            self.clock.tick(60)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.screen.fill("cyan")
            self.player.update()
            pygame.display.flip()
if __name__ == "__main__":
    r = App()
    r.update()