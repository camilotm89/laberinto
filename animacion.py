import pygame
import ConfigParser

from leerfondo import *




ANCHO=600
ALTO=600

def mapa():
    archivo='mapa.map'
    mapa=ConfigParser.ConfigParser()
    mapa.read(archivo)
    archivo= mapa.get('nivel1','origen')
    Plano=mapa.get('nivel1','mapa').split('\n')
    #print Plano
    #print 'secciones',mapa.sections()
    tabla=Traer_fondo(archivo,32,32)
    posx=0
    posy=0
    #####diccionario######
    d={}
    for sec in mapa.sections():
        if len(sec)==1:
            #print sec,mapa.get(sec,'nombre')
            x=int(mapa.get(sec, 'ux'))
            y=int(mapa.get(sec, 'uy'))
            d[sec]=[x,y]


    
    var_y=0
    for f in Plano:
        var_x=0
        for e in f:
            pos=d[e]
            x=pos[0]
            y=pos[1]
            lin_x=var_x*32
            lin_y=var_y*32
            pantalla.blit(tabla[x][y], (0+lin_x,0+lin_y))
            var_x+=1
        var_y+=1

class muro(pygame.sprite.Sprite):
    def __init__(self, obj_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=obj_img
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]


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
        self.muros=[]
        self.vida=100

    def update(self):
        #movimientos
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
        

        #colisiones
        lcol=pygame.sprite.spritecollide(self,muros,False)
        for e in lcol:
            self.vida-=1

            if self.dir==3:
                self.rect.right=e.rect.left
            if self.dir==1:
                self.rect.left=e.rect.right
            if self.dir==2:
                self.rect.top=e.rect.bottom
            if self.dir==0:
                self.rect.bottom=e.rect.top




class nivel(pygame.sprite.Sprite):
    def __init__(self, ar_mapa, an_re,al_re):
        pygame.sprite.Sprite.__init__(self)
        self.mapa=Ret_mapa(ar_mapa)
        self.fondo=Traer_fondo(archivo, an_re, al_re)
"""
    def Ret_mapa(self):
        mapa=ConfigParser.ConfigParser()
        mapa.read(archivo)
        archivo= mapa.get('nivel1','origen')
        plano=mapa.get('nivel1','mapa').split('\n')
        #print plano
        #print 'secciones',mapa.sections()
        posx=0
        posy=0
        d={}
        for sec in mapa.sections():
            if len(sec)==1:
                #print sec,mapa.get(sec,'nombre')
                x=int(mapa.get(sec, 'ux'))
                y=int(mapa.get(sec, 'uy'))
                muro=int(mapa.get(sec,'muro'))
                d[sec]=[x,y]

    def Traer_fondo(archivo,an_re, al_re):
        imagen=pygame.image.load('fondo.png')
        ancho, alto=imagen.get_size()
        print alto,ancho
        #an_re=32
        #al_re=32
        tabla=[]

        for var_x in range (0,(ancho/an_re)):
            fila=[]
            for var_y in range (0, (alto/al_re)):
                cuadro=(0+(var_x*32),0,an_re,al_re)
                img_cuadro=imagen.subsurface(cuadro)
                fila.append(img_cuadro)
            tabla.append(fila)
        return tabla"""

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
    ########



    ###########


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
        mapa()
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)