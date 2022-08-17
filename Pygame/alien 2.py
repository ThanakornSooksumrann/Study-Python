# Example 10-2
import pgzrun
from random import randint

def draw():
    screen.blit('backdrop800' ,(0, 0))
    ship.draw()
    alien.draw()
    for bullet in bullets:
        bullet.draw()
    screen.draw.text("Bullet : "+str(len(bullets)),topleft = (10, 10),fontsize = 28,color = 'white')

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor('bullet'))
        last = len(bullets)
        bullets[last-1].pos = ship.pos

def update():
    move()
    bullet_gun()
    alien_move()
    
    
def move():
    if keyboard.LEFT:
        ship.x -= 5
        if ship.left < 0:
            ship.left = 0
    elif keyboard.RIGHT:
        ship.x += 5
        if ship.right > WIDTH:
            ship.right = WIDTH
            
def bullet_gun():
    for bullet in bullets:
        bullet.y -= 8
        if bullet.top < 0:
            bullets.remove(bullet)
        if bullet.y < 100:
            if bullet.colliderect(alien):
                alien.pos = (60,30)
                bullets.remove(bullet)

def alien_move():
    alien.left += 3
    if alien.left > WIDTH:
        alien.right = 0

WIDTH = 800
HEIGHT = 600

ship = Actor('ship')
ship.pos = (WIDTH/2, HEIGHT-40)
bullets = []
alien = Actor("alien")
alien.pos = (400,25)
pgzrun.go()
