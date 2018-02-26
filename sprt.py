import pygame
import ConfigParser
import json
from leerfondo import *

with open('mapaj.json') as file:
    data=json.load(file)


ANCHO=600
ALTO=600
class jugador(pygame.sprite.Sprite):
    def __init__(self, mati, pos):
        pygame.sprite.Sprite.__init__(self)
        self.mati=mati
        self.dir=5
        self.con=0

        self.image=self.mati[2][0]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]

    def update(self):
        if self.dir==3:
            self.rect.x+=4
        if self.dir==1:
            self.rect.x-=4
        if self.dir==2:
            self.rect.y+=4
        if self.dir==0:
            self.rect.y-=4
        #direcciones sin movimiento
        if self.dir==5:
            self.image=self.mati[3][0]

        if self.dir==6:
            self.image=self.mati[1][0]
        if self.dir==7:
            self.image=self.mati[2][0]
        if self.dir==8:
            self.image=self.mati[0][0]
        
        direccion=self.dir
        if direccion>4:
            direccion= direccion -4

        else:
            self.image=self.mati[direccion][self.con]
            if self.con<2:
                self.con+=1
            else:
                self.con=0



if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    imagen=pygame.image.load('sprt.png').convert_alpha()
    m=[]
    for fila in range(4):
        lista=[]
        for i in range(9):
            cuadro=imagen.subsurface(47+(i*47),((8+fila)*47),47,47)
            lista.append(cuadro)
        m.append(lista)
    jp=jugador(m,[100,100])
    todos=pygame.sprite.Group()
    todos.add(jp)

    pygame.display.flip()
    reloj=pygame.time.Clock()
    fin=False
    i=0
    while not fin:
        for event in pygame.event.get():
            keys=pygame.key.get_pressed()
            if event.type==pygame.QUIT:
                fin=True
            if keys[pygame.K_RIGHT]:
                jp.dir=3
            if keys[pygame.K_LEFT]:
                jp.dir=1
            if keys[pygame.K_UP]:
                jp.dir=0
            if keys[pygame.K_DOWN]:
                jp.dir=2
            #condicional para cuando suelte la tecla almacenar direccion
            if jp.dir==3:
                if keys[pygame.K_RIGHT]:
                    pass
                else:
                    jp.dir=5
            if jp.dir==1:
                if keys[pygame.K_LEFT]:
                    pass
                else:
                    jp.dir=6
            if jp.dir==0:
                if keys[pygame.K_UP]:
                    pass
                else:
                    jp.dir=7
            if jp.dir==2:
                if keys[pygame.K_DOWN]:
                    pass
                else:
                    jp.dir=8

                

        #pantalla.fill([0,0,0])
        #pantalla.blit(lista[i],[100,100])
        pantalla.fill([0,0,0])
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)