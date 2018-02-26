import pygame
import ConfigParser

from leerfondo import *

ANCHO=768+32
ALTO=640

play=False

level1=True



"""
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
"""

class puerta(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]

class espada(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('espada2.gif')
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]

class llave(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('llave.gif')
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]

class Muro(pygame.sprite.Sprite):
    def __init__(self, obj_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=obj_img
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]

class enemigo(pygame.sprite.Sprite):
    def __init__(self, mati, pos):
        pygame.sprite.Sprite.__init__(self)
        self.mati=mati
        self.dir=3
        self.con=0
        self.vel=3

        self.image=self.mati[2][0]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.muros=[]
        self.vida=1
        self.protagonista=[]
    def update(self):
###########movimientos
        if self.dir==3:
            self.rect.x+=self.vel
        if self.dir==1:
            self.rect.x-=self.vel
############Colisiones enemigo
        lcol=pygame.sprite.spritecollide(self,self.muros,False)

        for e in lcol:
            #self.vida-=1

            if self.dir==3:
                if not (self.rect.left==e.rect.right):
                    self.rect.right=e.rect.left
                    self.dir=1

            if self.dir==1:
                if not (self.rect.right==e.rect.left):
                    self.rect.left=e.rect.right
                    self.dir=3

        if self.dir==3:
            self.image=self.mati[3][self.con]

        if self.dir==1:
            self.image=self.mati[1][self.con]


        if self.con<4:
            self.con+=1
        else:
            self.con=0
        
        pcol=pygame.sprite.spritecollide(self,protagonista,False)
        for e in pcol:            
            if self.dir==3:
                if not (self.rect.left==e.rect.right-7):
                    self.rect.right=e.rect.left+7
                    self.image=self.mati[7][self.con]
                    jp.vida-=1
                    punch.play()
                    zombie.play()
                
                    

            if self.dir==1:
                if not (self.rect.right==e.rect.left+7):
                    self.rect.left=e.rect.right-7
                    self.image=self.mati[5][self.con]
                    jp.vida-=1
                    punch.play()
                    zombie.play()
                    
"""

            if self.dir==0:
                self.rect.top=e.rect.bottom
            if self.dir==2:
                self.rect.bottom=e.rect.top"""

class jugador(pygame.sprite.Sprite):
    def __init__(self, mati, pos):
        pygame.sprite.Sprite.__init__(self)
        self.mati=mati
        self.dir=5
        self.accion="stand"
        self.con=0

        self.image=self.mati[2][0]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.muros=[]
        self.enemigos=[]
        self.vida=100
        self.armado=False
        self.tiene_llave=False
        self.level=1


    def update(self):
###########movimientos
        if self.accion=="move":
            if self.dir==3:
                self.rect.x+=4
            if self.dir==1:
                self.rect.x-=4
            if self.dir==2:
                self.rect.y+=4
            if self.dir==0:
                self.rect.y-=4
###########direcciones sin movimiento
        if self.dir==5:
            self.image=self.mati[3][0]

        if self.dir==6:
            self.image=self.mati[1][0]
        if self.dir==7:
            self.image=self.mati[0][0]
        if self.dir==8:
            self.image=self.mati[2][0]

#################ataques
        if self.armado:
            if self.accion=="atk":
                #if self.dir==9:
                   

                if self.dir==3 or self.dir==5:
                    self.dir=9
                if self.dir==1 or self.dir==6:
                    self.dir=10
                if self.dir==0 or self.dir==7:
                    self.dir=11
                if self.dir==2 or self.dir==8:
                    self.dir=12

                if self.dir==9:
                    self.image=self.mati[7][self.con]
                if self.dir==10:
                    self.image=self.mati[5][self.con]
                if self.dir==11:
                    self.image=self.mati[4][self.con]
                if self.dir==12:
                    self.image=self.mati[6][self.con]

                if self.con<4:
                    self.con+=1
                else:
                    self.dir=self.dir-4
                    self.accion="stand"

####################
        direccion=self.dir
        if direccion>4:
            direccion= direccion -4

        else:
            self.image=self.mati[direccion][self.con]
            if self.con<5:
                self.con+=1
            else:
                self.con=0
##########colision con enemigos ######################
        atkmode=False
        if self.armado:
            if self.accion=="atk":
                atkmode=True
                
                
        ecol=pygame.sprite.spritecollide(self,enemigos,atkmode)

        for e in ecol:
            #self.vida-=1

            #if self.dir==3:
            if self.rect.right==e.rect.left:
                e.rect.left=self.rect.right


            #if self.dir==1:
            if self.rect.left==e.rect.right:
                #if not (self.rect.right==e.rect.left):
                e.rect.right=self.rect.left


###############colisiones con muros##############
        lcol=pygame.sprite.spritecollide(self,self.muros,False)
        for e in lcol:            
            if self.dir==3:
                self.rect.right=e.rect.left
            if self.dir==1:
                self.rect.left=e.rect.right
            if self.dir==0:
                self.rect.top=e.rect.bottom
            if self.dir==2:
                self.rect.bottom=e.rect.top

################colisiones con objetos###############

        if pygame.sprite.spritecollide(self,espadas,True):
            print "tiene espada"
            self.armado=True


        if pygame.sprite.spritecollide(self,llaves,True):
            print "haz conseguido la llave"
            self.tiene_llave=True
            minillave=pygame.image.load('minillave.gif')
            pantalla.blit(minillave,[600,600])

        if jp.tiene_llave:
            if pygame.sprite.spritecollide(self,puertas,True):
                print "haz superado este nivel"
                puertas.remove(puerta1)
                if puertas.has(puerta2):
                    puertas.remove(puerta2)
                

            


class nivel(pygame.sprite.Sprite):
    def __init__(self, ar_mapa, an_re,al_re):
        pygame.sprite.Sprite.__init__(self)
        self.mapa=self.Ret_mapa(ar_mapa)
        self.fondo=self.Traer_fondo(self.ar_fondo, an_re, al_re)


    def Ret_mapa(self,archivo):
        mapa=ConfigParser.ConfigParser()
        mapa.read(archivo)
        self.ar_fondo= mapa.get('nivel1','origen')
        plano=mapa.get('nivel1','mapa').split('\n')
        posx=0
        posy=0
        d={}


        for sec in mapa.sections():
            if len(sec)==1:
                x=int(mapa.get(sec, 'ux'))
                y=int(mapa.get(sec, 'uy'))
                muro=int(mapa.get(sec, 'muro'))
                d[sec]=[[x,y], muro]

        info_muros=[]
        nf=0


        for fila in plano:
            nc=0
            for e in fila:
                lista=d[e]
                if lista[1]==1:
                    pos=[nf,nc]
                    info=[pos,lista[0]]
                    info_muros.append(info)
                nc+=1
            nf+=1
        return info_muros


    def Traer_fondo(self, archivo,an_re, al_re):
        imagen=pygame.image.load('fondo.png')
        ancho, alto=imagen.get_size()
        #print alto,ancho
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
        return tabla

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    soundtrack=pygame.mixer.Sound('OST.ogg')
    #soundtrack.play() 

    swip = pygame.mixer.Sound("sword_air.ogg")
    dieskull = pygame.mixer.Sound("dieskull.ogg")
    punch = pygame.mixer.Sound("punch.wav")
    punch.set_volume(.2)
    zombie = pygame.mixer.Sound("zombie.ogg")
    zombie.set_volume(.2)
    sounds=[swip,dieskull]


####  matriz de Sprite caminando  #################

    imagen=pygame.image.load('sprt.png').convert_alpha()
    m=[]
    for fila in range(8):
        lista=[]
        for i in range(9):
            cuadro=imagen.subsurface(47+(i*47),((8+fila)*47),47,47)
            lista.append(cuadro)
        m.append(lista)

#### sprites enemigo
    imagen_enm=pygame.image.load('skull.png').convert_alpha()
    n=[]
    for fila in range(8):
        lista=[]
        for i in range(9):
            cuadro=imagen_enm.subsurface(47+(i*47),((8+fila)*47),47,47)
            lista.append(cuadro)
        n.append(lista)


    
    

    espada1=espada([450,525])
    espada2=espada([130,160])
    espadas=pygame.sprite.Group()
    espadas.add(espada1)
    

    llave1=llave([690,178])
    llave2=llave([50,520])
    llaves=pygame.sprite.Group()
    llaves.add(llave1)


    puerta1=puerta('close.gif',[22*32,32])
    puertas=pygame.sprite.Group()
    puertas.add(puerta1)

    puerta2=puerta('close.gif',[22*32 , 32*11])


    jp=jugador(m,[48,520])
    enm1=enemigo(n,[470,420])
    enm2=enemigo(n,[100,40])
    enm3=enemigo(n,[300,140])
    enm4=enemigo(n,[100,240])
    todos=pygame.sprite.Group()
    todos.add(espada1)
    todos.add(puerta1)
    todos.add(llave1)
    todos.add(jp)
    todos.add(enm1)
    todos.add(enm2)

#######################

    enemigos=pygame.sprite.Group()
    jp.enemigos=enemigos
    enemigos.add(enm1)
    enemigos.add(enm2)
    #todos.add(enemigos)
######
    protagonista=pygame.sprite.Group()
    protagonista.add(jp)

################

    #todos=pygame.sprite.Group()
    #creamos nivel1

    muros=pygame.sprite.Group()
    mapa=nivel('mapa.map',32,32)

    for ls in mapa.mapa:
        pos_p=ls[0]
        x=pos_p[1]*32
        y=pos_p[0]*32
        pos_i=ls[1]
        xi=pos_i[0]
        yi=pos_i[1]
        #print ls[0], x, y, 'imagen ', xi, yi
        m=Muro(mapa.fondo[xi][yi],[x,y])
        muros.add(m)
        todos.add(m)

    jp.muros=muros
    enm1.muros=muros
    enm2.muros=muros
    todos.add(jp)


    #####creamos nivel2########
    muros2=pygame.sprite.Group()
    mapa2=nivel('mapa2.map',32,32)
    mm2=pygame.sprite.Group()
    for ls in mapa2.mapa:
        pos_p=ls[0]
        x=pos_p[1]*32
        y=pos_p[0]*32
        pos_i=ls[1]
        xi=pos_i[0]
        yi=pos_i[1]
        #print ls[0], x, y, 'imagen ', xi, yi
        m2=Muro(mapa2.fondo[xi][yi],[x,y])
        muros2.add(m2)
        mm2.add(m2)

    

    fuente =pygame.font.Font(None,30)


    
    

    pygame.display.flip()
    reloj=pygame.time.Clock()
    fin=False
    pant_ini=True
    i=0
    paso=True

    
    #pygame.time.wait(4000)

########### INICIO ###################

    while pant_ini and not fin:
        for event in pygame.event.get():
            keys=pygame.key.get_pressed()
            if event.type==pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                pant_ini=False
            inicio=pygame.image.load('inicio.jpg')
            pantalla.blit(inicio,[50,0])
            
            text_ini=fuente.render('presiona una tecla para continuar...', True, [255,255,255])
            pantalla.blit(text_ini,[200,300])
            nivel1=True
            pygame.display.flip()
            reloj.tick(50)

    soundtrack.play()

############ NIVEL 1 ###################

    while not fin and puertas.has(puerta1):
        for event in pygame.event.get():
            keys=pygame.key.get_pressed()
            if level1==False:
                fin=True
            if event.type==pygame.QUIT:
                fin=True
            if keys[pygame.K_RIGHT]:
                jp.dir=3
                jp.accion="move"
            if keys[pygame.K_LEFT]:
                jp.dir=1
                jp.accion="move"
            if keys[pygame.K_UP]:
                jp.dir=0
                jp.accion="move"
            if keys[pygame.K_DOWN]:
                jp.dir=2
                jp.accion="move"
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

            #condicionales para el ataque
            if keys[pygame.K_SPACE]:                
                jp.accion="atk"
                if jp.armado:
                    sounds[0].play()
                """if jp.dir==3 or jp.dir==5:
                    jp.dir=9
                if jp.dir==1 or jp.dir==6:
                    jp.dir=9
                if jp.dir==0 or jp.dir==7:
                    jp.dir=9
                if jp.dir==2 or jp.dir==8:
                    jp.dir=9"""

            if event.type==pygame.KEYUP:
                if jp.accion=="atk":
                    print 'solto'

              
        vida=str(jp.vida)
        pantalla.fill([15,15,15])
        texto=fuente.render('vida: '+ vida + '     inventario:  ', True, [255,255,255])
        if jp.armado:
            pantalla.blit(pygame.image.load('espada2.gif'),[240,610])
        if jp.tiene_llave:
            pantalla.blit(pygame.image.load('llave.gif'),[270,610])
        pantalla.blit(texto, [20,612])
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(50)

############  NIVEL 2   ###############
    todos.remove(espada1)
    espadas.remove(espada1)
    todos.remove(puerta1)
    todos.remove(llave1)
    todos.remove(enm1)
    todos.remove(enm2)
    todos.remove(jp)
    todos.remove(muros)

    llaves.add(llave2)
    puertas.add(puerta2)
    todos.add(puerta2)


    jp.muros=muros2
    enm3.muros=muros2
    enm4.muros=muros2
    enemigos.add(enm3)
    enemigos.add(enm4)
    todos.add(mm2)
    
    espadas.add(espada2)
    todos.add(espada2)
    #todos.add(puerta1)
    todos.add(llave2)
    
    todos.add(enm3)
    todos.add(enm4)
    todos.update()

    pantalla.fill([15,15,15])
    
    #jp.muros=muros2
    todos.add(jp)
    print "termino un ciclo"
    jp.vida=100
    jp.armado=False
    jp.tiene_llave=False
    
    pygame.display.flip()

    while not fin and puertas.has(puerta2):
        print "segundo ciclo"
        for event in pygame.event.get():
            keys=pygame.key.get_pressed()
            if event.type==pygame.QUIT:
                fin=True
            if keys[pygame.K_RIGHT]:
                jp.dir=3
                jp.accion="move"
            if keys[pygame.K_LEFT]:
                jp.dir=1
                jp.accion="move"
            if keys[pygame.K_UP]:
                jp.dir=0
                jp.accion="move"
            if keys[pygame.K_DOWN]:
                jp.dir=2
                jp.accion="move"
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

            #condicionales para el ataque
            if keys[pygame.K_SPACE]:                
                jp.accion="atk"
                if jp.armado:
                    sounds[0].play()
                """if jp.dir==3 or jp.dir==5:
                    jp.dir=9
                if jp.dir==1 or jp.dir==6:
                    jp.dir=9
                if jp.dir==0 or jp.dir==7:
                    jp.dir=9
                if jp.dir==2 or jp.dir==8:
                    jp.dir=9"""

            if event.type==pygame.KEYUP:
                if jp.accion=="atk":
                    print 'solto'


                  
        vida=str(jp.vida)
        pantalla.fill([15,15,15])
        texto=fuente.render('vida: '+ vida + '     inventario:  ', True, [255,255,255])
        if jp.armado:
            pantalla.blit(pygame.image.load('espada2.gif'),[240,610])
        if jp.tiene_llave:
            pantalla.blit(pygame.image.load('llave.gif'),[270,610])
        pantalla.blit(texto, [20,612])
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(50)
    pantalla.fill([0,0,0])
    while not fin:
        for event in pygame.event.get():
            keys=pygame.key.get_pressed()
            if event.type==pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                pant_ini=False
            inicio=pygame.image.load('inicio.jpg')
            pantalla.blit(inicio,[50,0])
            
            text_ini=fuente.render('HAS GANADO', True, [0,0,0])
            pantalla.blit(text_ini,[200,300])
            nivel1=True
            pygame.display.flip()



