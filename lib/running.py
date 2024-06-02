import pygame,random,time
from lib.setting import *
from lib.unit import *

class Running:
    def __init__(self,mode) -> None:
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.mode = mode
        if mode==1:
            self.blockNum = 15
            self.starNum = 50
            self.speedStarNum = 15
            self.fullScore = self.starNum
        elif mode==2:
            self.blockNum = 25
            self.starNum = 75
            self.speedStarNum = 10
            self.fullScore = self.starNum
        elif mode==3:
            self.blockNum = 35
            self.starNum = 100
            self.speedStarNum = 5
            self.fullScore = self.starNum
        self.gameStatus = 0
        self.loadUnit(self.fullScore)
        print("PINKCANDY 游戏载入完成")
    def loadUnit(self,fullScore):
        print("PINKCANDY 正在载入")
        self.player = Player((SCREEN_WIDTH/2,SCREEN_HEIGHT/2),self.walls,self.gameStatus,self.all_sprites,fullScore)
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
            pass
        if self.player.gameStatus == 1:
            self.all_sprites.empty() 
            self.display_surface.blit(font1.render("采集完成，游戏胜利！",True,(50,50,50)),(SCREEN_WIDTH/4,SCREEN_HEIGHT/4))
            if self.mode==1:
                tipList = ['游戏难度 1','挑战更难的模式吧','','按下R键回到主界面']
                for i in range(len(tipList)):
                    lineHeight = 50
                    self.display_surface.blit(font2.render(tipList[i],True,(50,50,50)),(SCREEN_WIDTH/3,SCREEN_HEIGHT/2+i*lineHeight))
            elif self.mode==2:
                tipList = ['游戏难度 2','挑战更难的模式吧','','按下R键回到主界面']
                for i in range(len(tipList)):
                    lineHeight = 50
                    self.display_surface.blit(font2.render(tipList[i],True,(50,50,50)),(SCREEN_WIDTH/3,SCREEN_HEIGHT/2+i*lineHeight))
            elif self.mode==3:
                tipList = ['游戏难度 3','躲避大师！','','按下R键回到主界面','联系作者 QQ1479499289']
                for i in range(len(tipList)):
                    lineHeight = 50
                    self.display_surface.blit(font2.render(tipList[i],True,(50,50,50)),(SCREEN_WIDTH/3,SCREEN_HEIGHT/2+i*lineHeight))
        if self.player.gameStatus == 2:
            self.all_sprites.empty()
            self.display_surface.blit(font1.render("游戏失败！",True,(50,50,50)),(SCREEN_WIDTH/4,SCREEN_HEIGHT/4))
            tipList = ['只有十条命','碰到障碍方块减速并掉血','吃到星星少量提升速度','吃到速度星星完成','充能后按空格大幅提升速度','','按下R键回到主界面']
            for i in range(len(tipList)):
                lineHeight = 50
                self.display_surface.blit(font2.render(tipList[i],True,(50,50,50)),(SCREEN_WIDTH/3,SCREEN_HEIGHT/2+i*lineHeight))
    def run(self):
        self.display_surface.fill((244,241,222))
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()
        self.gameDone()