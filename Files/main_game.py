from player import *
import sys
from level import *
from settings import *




class Game:
    def __init__(self):
        init()
        self.screen = display.set_mode((WIDTH, HEIGHT), RESIZABLE)
        display.set_caption("Warrior")
        self.clock = time.Clock()  

        self.level = Level()  
    def run(self):
        while True:
            for e in event.get():
                if e.type == QUIT:
                    quit()
                    sys.exit()
            
            self.screen.fill((0, 0 ,0))
            self.level.run()
            display.update()
            self.clock.tick(FPS)
if __name__ == '__main__':
    game = Game()
    game.run()