
import pgzrun
from pygame import color
from random import randint
WIDTH=564
HEIGHT=564
diem=0
gameover=False
mario= Actor('mario')
mario.pos=100,200
coin= Actor('coin')
coin.pos=300,300
music.play('nhac')
def draw():
    screen.blit('background',(0,0))
    mario.draw()
    coin.draw()
    screen.draw.text("score "+str(diem),color="black",topleft=(10,10))
    if gameover:    
        screen.blit('background',(0,0))
        screen.draw.text("Height Score "+str(diem),color="black",center=(564/2,564/2))
def place_coin():
    coin.x=randint(20,(WIDTH-20))
    coin.y=randint(20,(HEIGHT-20))
place_coin()
def update():
    global diem
    if keyboard.left :
        mario.x=mario.x-6
    elif  keyboard.up:
        mario.y=mario.y-6
    elif  keyboard.down:
        mario.y=mario.y+6
    elif  keyboard.right:
        mario.x=mario.x+6
    chamcoin =mario.colliderect(coin)
    if chamcoin:
        diem+=10
        place_coin()
    elif mario.x >= 560:
        mario.x=0
    elif mario.y >=560:
        mario.y=0
    elif mario.x <= 0:
        mario.x=560
    elif mario.y <=0:
        mario.y=560     
          
def hetgio():
    global gameover
    gameover= True

clock.schedule(hetgio,40.0)
place_coin
        
pgzrun.go()
hellllo
