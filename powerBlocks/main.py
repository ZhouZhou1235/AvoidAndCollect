import pygame,sys,time
from lib.setting import *
from lib.running import *

class Game:
    def __init__(self) -> None:
        # self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.FULLSCREEN).convert_alpha()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(GAME_TITLE)
        self.clock.tick(FPS)
        self.running = Running()
        print("PINKCANDY 窗口初始化完成")
    def sign(self):
        self.display_surface = pygame.display.get_surface()
        self.display_surface.fill("gray")
        font1 = pygame.font.Font("./resource/font/zpix.ttf",50)
        font2 = pygame.font.Font("./resource/font/zpix.ttf",75)
        self.display_surface.blit(font1.render("游戏引擎",True,(50,50,50),None),(SCREEN_WIDTH/10,SCREEN_HEIGHT/2))
        self.display_surface.blit(font2.render("https://pinkcandy.top",True,(50,50,50),None),(SCREEN_WIDTH/10,SCREEN_HEIGHT/1.5))
        pygameLogo = pygame.image.load("./resource/graph/pygame_logo.gif").convert_alpha()
        self.display_surface.blit(pygameLogo,(SCREEN_WIDTH/10,SCREEN_HEIGHT/4))
        pygame.display.update()
        time.sleep(3)
    def welcome(self):
        self.display_surface = pygame.display.get_surface()
        self.display_surface.fill("white")
        font1 = pygame.font.Font("./resource/font/zpix.ttf",100)
        font2 = pygame.font.Font("./resource/font/zpix.ttf",50)
        self.display_surface.blit(font1.render("能量方块（测试版）",True,(50,50,50),None),(SCREEN_WIDTH/4,SCREEN_HEIGHT/4))
        self.display_surface.blit(font2.render("PINKCANDYZHOU",True,(50,50,50),None),(SCREEN_WIDTH/3,SCREEN_HEIGHT/2.5))
        self.display_surface.blit(font2.render("按SPACE键开始游戏",True,(50,50,50),None),(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        isWelcome = True
        while isWelcome:
            keyboard = pygame.key.get_pressed()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keyboard[pygame.K_ESCAPE]:
                    print("PINKCANDY 结束运行")
                    pygame.quit()
                    sys.exit()
                if keyboard[pygame.K_SPACE]:
                    print("PINKCANDY 游戏开始")
                    isWelcome = False
    def run(self):
        print("PINKCANDY 开始运行")
        pygame.init()
        self.sign()
        self.welcome()
        while True:
            while True:
                self.running.run()
                keyboard = pygame.key.get_pressed()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or keyboard[pygame.K_ESCAPE]:
                        print("PINKCANDY 结束运行")
                        pygame.quit()
                        sys.exit()
                    if keyboard[pygame.K_r]:
                        self.running = Running()
                        print("PINKCANDY 游戏重载")
                        break

if __name__ == "__main__":
    start = Game()
    start.run()