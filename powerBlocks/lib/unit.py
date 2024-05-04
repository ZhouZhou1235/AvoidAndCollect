import pygame,random,sys

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,walls,gameStatus,groups) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((25,25))
        self.image.fill("green")
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = 0.7
        self.walls = walls
        self.life = 10
        self.score = 0
        self.canAddSpeed = False
        self.gameStatus = gameStatus
        print("PINKCANDY 载入玩家")
    def input(self):
        keyboard = pygame.key.get_pressed()
        if keyboard[pygame.K_w]:
            self.direction.y = -1
        elif keyboard[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keyboard[pygame.K_a]:
            self.direction.x = -1
        elif keyboard[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        if keyboard[pygame.K_SPACE]:
            if self.canAddSpeed==False:
                if self.speed < 2:
                    self.speed += 0.3
                    self.canAddSpeed = True
    def move(self):
        if self.direction.magnitude()>0:
            self.direction = self.direction.normalize()
        self.position.x += self.direction.x * self.speed
        self.rect.centerx = self.position.x
        self.prevent_x()
        self.position.y += self.direction.y * self.speed
        self.rect.centery = self.position.y
        self.prevent_y()
    def prevent_x(self):
        collide = pygame.sprite.spritecollide(self,self.walls,False)
        for wall in collide:
            if self.direction.x > 0:
                self.rect.right = wall.rect.left
            elif self.direction.x < 0:
                self.rect.left = wall.rect.right
            self.position.x = self.rect.centerx
    def prevent_y(self):
        collide = pygame.sprite.spritecollide(self,self.walls,False)
        for wall in collide:
            if self.direction.y > 0:
                self.rect.bottom = wall.rect.top
            elif self.direction.y < 0:
                self.rect.top = wall.rect.bottom
            self.position.y = self.rect.centery
    def update(self):
        self.input()
        self.move()

class Block(pygame.sprite.Sprite):
    def __init__(self,pos,walls,player,groups) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((25,25))
        self.image.fill("red")
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = random.randint(3,7)/10
        self.walls = walls
        self.player = player
        self.following = False
    def move(self):
        if self.direction.magnitude()>0:
            self.direction = self.direction.normalize()
        self.position.x += self.direction.x * self.speed
        self.rect.centerx = self.position.x
        self.prevent_x()
        self.position.y += self.direction.y * self.speed
        self.rect.centery = self.position.y
        self.prevent_y()
    def prevent_x(self):
        collide = pygame.sprite.spritecollide(self,self.walls,False)
        for wall in collide:
            if self.direction.x > 0:
                self.rect.right = wall.rect.left
            elif self.direction.x < 0:
                self.rect.left = wall.rect.right
            self.position.x = self.rect.centerx
    def prevent_y(self):
        collide = pygame.sprite.spritecollide(self,self.walls,False)
        for wall in collide:
            if self.direction.y > 0:
                self.rect.bottom = wall.rect.top
            elif self.direction.y < 0:
                self.rect.top = wall.rect.bottom
            self.position.y = self.rect.centery
    def follow(self):
        self.seeRange = 200
        moveX = self.player.position.x-self.position.x
        moveY = self.player.position.y-self.position.y
        see = (abs(moveX)<self.seeRange and abs(moveY)<self.seeRange)
        if see:
            if moveY<0:
                self.direction.y = -1
            elif moveY>0:
                self.direction.y = 1
            else:
                self.direction.y = 0
            if moveX<0:
                self.direction.x = -1
            elif moveX>0:
                self.direction.x = 1
            else:
                self.direction.x = 0
            self.following = True
        else:
            num = random.randint(1,1000)
            if num<5:
                self.direction.x = 0
                self.direction.y = 0
                self.following = False
            else:
                self.autoMove()
                self.following = True
    def autoMove(self):
        if self.following==False:
            thisX = random.randint(-1,1)
            thisY = random.randint(-1,1)
            self.direction.x = thisX
            self.direction.y = thisY
    def crash(self):
        if self.rect.colliderect(self.player):
            pygame.sprite.Sprite.kill(self)
            if self.player.speed>0.2:
                self.player.speed -= 0.1
            self.player.life -= 1
            if self.player.life<=0:
                print(f"游戏结束，本次吃到{self.player.score}颗星星。")
                self.player.gameStatus = 2
    def endGame(self):
        pass
    def update(self):
        self.follow()
        self.move()
        self.crash()

class Star(pygame.sprite.Sprite):
    def __init__(self,pos,walls,player,groups) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((25,25))
        self.image.fill("yellow")
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = 0.2
        self.walls = walls
        self.player = player
        self.following = False
    def move(self):
        if self.direction.magnitude()>0:
            self.direction = self.direction.normalize()
        self.position.x += self.direction.x * self.speed
        self.rect.centerx = self.position.x
        self.prevent_x()
        self.position.y += self.direction.y * self.speed
        self.rect.centery = self.position.y
        self.prevent_y()
    def prevent_x(self):
        collide = pygame.sprite.spritecollide(self,self.walls,False)
        for wall in collide:
            if self.direction.x > 0:
                self.rect.right = wall.rect.left
            elif self.direction.x < 0:
                self.rect.left = wall.rect.right
            self.position.x = self.rect.centerx
    def prevent_y(self):
        collide = pygame.sprite.spritecollide(self,self.walls,False)
        for wall in collide:
            if self.direction.y > 0:
                self.rect.bottom = wall.rect.top
            elif self.direction.y < 0:
                self.rect.top = wall.rect.bottom
            self.position.y = self.rect.centery
    def follow(self):
        self.seeRange = 300
        moveX = self.player.position.x-self.position.x
        moveY = self.player.position.y-self.position.y
        see = (abs(moveX)<self.seeRange and abs(moveY)<self.seeRange)
        if see:
            if moveY<0:
                self.direction.y = -1
            elif moveY>0:
                self.direction.y = 1
            else:
                self.direction.y = 0
            if moveX<0:
                self.direction.x = -1
            elif moveX>0:
                self.direction.x = 1
            else:
                self.direction.x = 0
            self.following = True
        else:
            num = random.randint(1,2000)
            if num<5:
                self.direction.x = 0
                self.direction.y = 0
                self.following = False
            else:
                self.autoMove()
                self.following = True
    def autoMove(self):
        if self.following==False:
            thisX = random.randint(-1,1)
            thisY = random.randint(-1,1)
            self.direction.x = thisX
            self.direction.y = thisY
    def crash(self):
        if self.rect.colliderect(self.player):
            if self.player.speed<0.3:
                self.player.speed += 0.1
            self.player.score += 1
            pygame.sprite.Sprite.kill(self)
            if self.player.score >=45:
                print(f"剩余生命{self.player.life} 游戏通关！")
                self.player.gameStatus = 1
            print("吃到星星")
    def update(self):
        self.follow()
        self.move()
        self.crash()

class SpeedStar(pygame.sprite.Sprite):
    def __init__(self,pos,walls,player,groups) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((25,25))
        self.image.fill("skyblue")
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = 0.2
        self.walls = walls
        self.player = player
        self.following = False
    def move(self):
        if self.direction.magnitude()>0:
            self.direction = self.direction.normalize()
        self.position.x += self.direction.x * self.speed
        self.rect.centerx = self.position.x
        self.prevent_x()
        self.position.y += self.direction.y * self.speed
        self.rect.centery = self.position.y
        self.prevent_y()
    def prevent_x(self):
        collide = pygame.sprite.spritecollide(self,self.walls,False)
        for wall in collide:
            if self.direction.x > 0:
                self.rect.right = wall.rect.left
            elif self.direction.x < 0:
                self.rect.left = wall.rect.right
            self.position.x = self.rect.centerx
    def prevent_y(self):
        collide = pygame.sprite.spritecollide(self,self.walls,False)
        for wall in collide:
            if self.direction.y > 0:
                self.rect.bottom = wall.rect.top
            elif self.direction.y < 0:
                self.rect.top = wall.rect.bottom
            self.position.y = self.rect.centery
    def follow(self):
        self.seeRange = 300
        moveX = self.player.position.x-self.position.x
        moveY = self.player.position.y-self.position.y
        see = (abs(moveX)<self.seeRange and abs(moveY)<self.seeRange)
        if see:
            if moveY<0:
                self.direction.y = -1
            elif moveY>0:
                self.direction.y = 1
            else:
                self.direction.y = 0
            if moveX<0:
                self.direction.x = -1
            elif moveX>0:
                self.direction.x = 1
            else:
                self.direction.x = 0
            self.following = True
        else:
            num = random.randint(1,3000)
            if num<5:
                self.direction.x = 0
                self.direction.y = 0
                self.following = False
            else:
                self.autoMove()
                self.following = True
    def autoMove(self):
        if self.following==False:
            thisX = random.randint(-1,1)
            thisY = random.randint(-1,1)
            self.direction.x = thisX
            self.direction.y = thisY
    def crash(self):
        if self.rect.colliderect(self.player):
            self.player.canAddSpeed = False
            pygame.sprite.Sprite.kill(self)
            print("吃到加速星星")
    def update(self):
        self.follow()
        self.move()
        self.crash()

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,groups):
        super().__init__(groups)
        self.image = pygame.Surface((w,h))
        self.image.fill(pygame.Color('blue'))
        self.rect = self.image.get_rect(topleft=(x,y))