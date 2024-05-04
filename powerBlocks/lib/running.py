import pygame,random
from lib.setting import *
from lib.unit import *

class Running:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.blockNum = 50
        self.starNum = 45
        self.speedStarNum = 5
        self.gameStatus = 0
        self.loadUnit()
        print("PINKCANDY 游戏载入完成")
    def loadUnit(self):
        print("PINKCANDY 正在载入")
        self.player = Player((SCREEN_WIDTH/2,SCREEN_HEIGHT/2),self.walls,self.gameStatus,self.all_sprites)
        self.loadUnit_wall(EDGE)
        self.loadUnit_block(self.random_blockPos(self.blockNum))
        self.loadUnit_star(self.random_blockPos(self.starNum))
        self.loadUnit_speedStar(self.random_blockPos(self.speedStarNum))
    def loadUnit_wall(self,walls):
        for wall in walls:
            x = Wall(wall[0],wall[1],wall[2],wall[3],self.all_sprites)
            self.walls.add(x)
        print("PINKCANDY 载入空气墙")
    def loadUnit_block(self,blocks):
        for block in blocks:
            x = Block((block[0],block[1]),self.walls,self.player,self.all_sprites)
            self.blocks.add(x)
        print("PINKCANDY 载入方块")
    def loadUnit_star(self,stars):
        for star in stars:
            x = Star((star[0],star[1]),self.walls,self.player,self.all_sprites)
            self.stars.add(x)
    def loadUnit_speedStar(self,speedStars):
        for star in speedStars:
            x = SpeedStar((star[0],star[1]),self.walls,self.player,self.all_sprites)
            self.stars.add(x)
        print("PINKCANDY 载入星星")
    def random_blockPos(self,num):
        outList = []
        for i in range(num):
            x = random.randint(border*2,SCREEN_WIDTH-border*2)
            y = random.randint(border*2,SCREEN_HEIGHT-border*2)
            x_ok = x<SCREEN_WIDTH/2-border*2 or x>SCREEN_WIDTH/2+border*2
            y_ok = y<SCREEN_HEIGHT/2-border*2 or y>SCREEN_HEIGHT/2+border*2
            while x_ok==False or y_ok==False:
                x = random.randint(border*2,SCREEN_WIDTH-border*2)
                y = random.randint(border*2,SCREEN_HEIGHT-border*2)
                x_ok = x<SCREEN_WIDTH/2-border*2 or x>SCREEN_WIDTH/2+border*2
                y_ok = y<SCREEN_HEIGHT/2-border*2 or y>SCREEN_HEIGHT/2+border*2
            else:
                thisBlock = [x,y]
                outList.append(thisBlock)
        return outList
    def gameDone(self):
        font1 = pygame.font.Font("./resource/font/zpix.ttf",100)
        font2 = pygame.font.Font("./resource/font/zpix.ttf",25)
        if self.player.gameStatus != 0:
            self.display_surface.fill("white")
        if self.player.gameStatus == 1:
            self.all_sprites.empty()
            self.display_surface.blit(font1.render("采集完成了，真棒！按R键重新开始",True,(50,50,50),(225,225,225)),(SCREEN_WIDTH/4,SCREEN_HEIGHT/4))
        if self.player.gameStatus == 2:
            self.all_sprites.empty()
            self.display_surface.blit(font1.render("游戏失败！按R键重新开始",True,(50,50,50),(225,225,225)),(SCREEN_WIDTH/4,SCREEN_HEIGHT/4))
            self.display_surface.blit(font2.render("小技巧：吃到星星可以少量提升速度，而吃到速度星星后按空格可以大幅提升速度！",True,(50,50,50),(225,225,225)),(SCREEN_WIDTH/3,SCREEN_HEIGHT/2))
    def run(self):
        self.display_surface.fill((255,255,255))
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()
        self.gameDone()