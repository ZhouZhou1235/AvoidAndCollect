import pygame,sys,time
from lib.setting import *
from lib.running import *

class Game:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.FULLSCREEN).convert_alpha()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(GAME_TITLE)
        self.clock.tick(FPS)
        pygame.key.stop_text_input()
        print("PINKCANDY 窗口初始化完成")
    def sign(self):
        self.display_surface = pygame.display.get_surface()
        self.display_surface.fill("gray")
        font1 = pygame.font.Font("./resource/font/zpix.ttf",75)
        theStr = "PINKCANDYZHOU作品"
        self.display_surface.blit(font1.render(theStr,True,(50,50,50),None),(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        pygame.display.update()
        time.sleep(3)
    def welcome(self):
        self.display_surface = pygame.display.get_surface()
        self.display_surface.fill((244,241,222))
        font1 = pygame.font.Font("./resource/font/zpix.ttf",100)
        font3 = pygame.font.Font("./resource/font/zpix.ttf",36)
        self.display_surface.blit(font1.render("躲避与收集",True,(50,50,50),None),(SCREEN_WIDTH/4,SCREEN_HEIGHT/4))
        tipList = ['PINKCANDYZHOU作品','按1/2/3键选择难度并开始','按ESC退出游戏','',
                   'WASD或方向键控制移动 按空格键加速','',
                   '游戏难度 1','需要收集50个方块 较少障碍 加速方块充足',
                   '游戏难度 2','需要收集75个方块 一定障碍 一些加速方块',
                   '游戏难度 3','需要收集100个方块 很多障碍 加速方块很少']
        for i in range(len(tipList)):
            lineHeight = 36
            self.display_surface.blit(font3.render(tipList[i],True,(50,50,50)),(SCREEN_WIDTH/3,SCREEN_HEIGHT/2+i*lineHeight))
        isWelcome = True
        while isWelcome:
            keyboard = pygame.key.get_pressed()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keyboard[pygame.K_ESCAPE]:
                    print("PINKCANDY 结束运行")
                    pygame.quit()
                    sys.exit()
                if keyboard[pygame.K_1] or keyboard[pygame.K_KP_1]:
                    self.running = Running(1)
                    print("PINKCANDY 游戏开始")
                    isWelcome = False
                elif keyboard[pygame.K_2] or keyboard[pygame.K_KP_2]:
                    self.running = Running(2)
                    print("PINKCANDY 游戏开始")
                    isWelcome = False
                elif keyboard[pygame.K_3] or keyboard[pygame.K_KP_3]:
                    print("PINKCANDY 游戏开始")
                    self.running = Running(3)
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
                        self.welcome()
                        print("PINKCANDY 游戏重载")
                        break

if __name__ == "__main__":
    start = Game()
    start.run()