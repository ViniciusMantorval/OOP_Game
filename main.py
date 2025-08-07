import pygame ,random

pygame.init()


telaWidth=800
telaHeight=600

screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()
running = True
dt = 0

cooldown=1

class Mario:
    quantidade=0
    def __init__(self,speed,size,color):
        Mario.quantidade+=1
        self.speed = speed
        self.size = size
        self.color = color
        self.position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.velocity= pygame.Vector2(0,0)
        self.create()
    def information(self):
        print(f"My speed as Mario is {self.speed}, my size is {self.size}, my x is {self.position[0]} and my y is {self.position[1]}")
    def move(self):
        mario.position.x += mario.velocity.x 
        mario.position.y += mario.velocity.y 
        self.create()
    def create(self):
        pygame.draw.circle(screen, self.color, self.position, self.size)
    def collision(self):
        for enemy in Enemy.enemies:
            global running
            closest_x = max(enemy.rect.left ,min(self.position.x, enemy.rect.right))
            closest_y = max(enemy.rect.top ,min(self.position.y, enemy.rect.bottom))
            dist_x = self.position.x - closest_x
            dist_y = self.position.y - closest_y
            distance_squared = dist_x**2 + dist_y**2

            if distance_squared <= self.size**2:
                running=False
                print("touching")
class Enemy:
    enemies=[]
    def __init__(self,speed,size):
        self.speed = speed
        self.size= size
        self.position= pygame.Vector2(random.randint(0, screen.get_width())-self.size-1,random.randint(0, screen.get_height()-self.size-1))

        self.rect = pygame.Rect(
            int(self.position.x), int(self.position.y), int(self.size), int(self.size)
        )
        Enemy.enemies.append(self)
    def create(self):
        pygame.draw.rect(screen,"pink",self.rect)
class Horizontal_enemy(Enemy):
    def __init__(self, speed, size):
        super().__init__(speed, size)
        self.move_i = 0
        self.move_time=random.randint(60,180)
        self.create()
    def create(self):
        pygame.draw.rect(screen,"Blue",self.rect)
        self.move()
    def move(self):
        if(self.move_i<=self.move_time):
            if(self.rect.right>screen.get_width()):
                self.move_time= self.move_i
            self.position.x+=self.speed
            self.rect = pygame.Rect(
            int(self.position.x), int(self.position.y), int(self.size), int(self.size)
        )
        if(self.move_i>self.move_time):
            if(self.rect.left<0):
                self.move_i=0
            self.position.x-=self.speed
            self.rect = pygame.Rect(
            int(self.position.x), int(self.position.y), int(self.size), int(self.size)
        )
        if(self.move_i>=2*self.move_time):
            self.move_i =0
        self.move_i+=1
class Vertical_enemy(Enemy):
    def __init__(self, speed, size):
        super().__init__(speed, size)
        self.move_i = 0
        self.move_time=random.randint(60,240)
        self.create()
    def create(self):
        pygame.draw.rect(screen,"red",self.rect)
        self.move()
    def move(self):
        if(self.move_i<=self.move_time):
            if(self.rect.top<0):
                self.move_time= self.move_i
            self.position.y+=self.speed
            self.rect = pygame.Rect(
            int(self.position.x), int(self.position.y), int(self.size), int(self.size)
        )
        if(self.move_i>self.move_time):
            if(self.rect.bottom>=screen.get_height()):
                self.move_i=0
            self.position.y-=self.speed
            self.rect = pygame.Rect(
            int(self.position.x), int(self.position.y), int(self.size), int(self.size)
        )
        if(self.move_i>=2*self.move_time):
            self.move_i =0
        self.move_i+=1
mario= Mario(17,30,"yellow")
for i in range(10):
    enemy= f"horizontal_enemy{i}"
    enemy=Horizontal_enemy(2,30)
    enemy= f"vertical_enemy{i}"
    enemy=Vertical_enemy(2,30)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    
    for enemy in Enemy.enemies:
        enemy.create()
    mario.move()
    mario.collision()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        mario.velocity.y -= mario.speed * dt
    if keys[pygame.K_s]:
        mario.velocity.y += mario.speed * dt
    if keys[pygame.K_a]:
        mario.velocity.x -= mario.speed * dt
    if keys[pygame.K_d]:
        mario.velocity.x += mario.speed * dt

    if(pygame.mouse.get_pressed()[0]):
        [x,y] = pygame.mouse.get_pos()
        if(cooldown %7==0 and cooldown !=0):
            print(f"{x,y} tangente: {y/x}")
        else:
            print("Em recarga")
        cooldown+=1
        
    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000


pygame.quit()
