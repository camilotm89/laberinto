import pygame
import ConfigParser

ANCHO=600
ALTO=400

def Traer_fondo(archivo,an_re, al_re):
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

    pantalla.blit(tabla[0][5], [200,200])


    pygame.display.flip()


    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
