from random import *

import pygame

#para mostrar un random de enteros randint(1,100)
#para mostrar un random de float uniform(1,100)

ANCHO = 800
ALTO = 750
MIDDLE = [int(ANCHO/2),int(ALTO/2)]
#MIDDLE = [400,700]

def Cart_Pant(pc): #pasa de cartesiano a pantalla
    ''' Transformación lineal de puntos cartecianos
    a puntos en pantalla
    p = punto'''
    xp = pc[0] + MIDDLE[0]
    yp = -pc[1] + MIDDLE[1]

    return [int(xp),int(yp)]



def decision(particulas,cant_parametros):
    posicion=0
    resultado=0
    while posicion < (cant_parametros-1):
        resultado = resultado + 100*pow(particulas[posicion+1]-particulas[posicion],2) + pow(1-particulas[posicion],2)
        posicion+=1
    return resultado


def cambios(particulas,cant_particulas,cant_parametros,w,c1,c2,gbest,mejores,velocidades):
    wf=uniform(0,w)
    c1f=uniform(0,c1)
    c2f=uniform(0,c2)
    #wf=0.3219
    #c1f=0.3935
    #c2f=0.9837
    print("El valor de w es: "+str(wf))
    print("El valor de c1 es: "+str(c1f))
    print("El valor de c2 es: "+str(c2f))
    i=0
    while i < cant_particulas:
        temp_particula=particulas[i]
        temp_mejor=particulas[i]
        temp_velocidad=velocidades[i]
        vec1=[]
        vec2=[]
        vec3=[]
        j=0
        while j<cant_parametros:
            a=wf*temp_velocidad[j]
            vec1.append(a)
            b=c1f*temp_mejor[j]-c1f*temp_particula[j]
            vec2.append(b)
            c=c2f*gbest[j]-c2f*temp_particula[j]
            vec3.append(c)
            j+=1
        j=0
        while j < cant_parametros:
            velocidades[i][j] = vec1[j] + vec2[j] + vec3[j]
            particulas[i][j] = particulas[i][j] + velocidades[i][j]
            j+=1
        i+=1

    return [particulas,velocidades]


if __name__ == '__main__':
    print("Esta optimizacion se aplica sobre la Funcion de Rosenbrock")

    cant_particulas = int(input("Ingrese la cantidad de particulas del sistema: "))
    cant_parametros = int(input("Ingrese la cantidad de parametros de las particulas "))
    iteraciones = int(input("Ingrese la cantidad de iteraciones "))
    c1 = float(input("Ingrese el valor de maximo de c1: "))
    c2 = float(input("Ingrese el valor maximo de c2: "))
    w = float(input("Ingrese el valor maximo de la inercia(W): "))

    i = 0

    particulas = [] #Se guardan las particulas del sistema en este vector (vector de vectores)
    velocidades = [] #Se guardan las velocidades de las particulas
    mejores = []

    while i < cant_particulas:
        j=0
        a=[]
        b=[]
        while j < cant_parametros:
            valor=int(input("Ingrese el parametro "))
            valor2=0
            b.append(valor2)
            a.append(valor)
            j+=1
        particulas.append(a)
        velocidades.append(b)
        i+=1
        print()

    mejores = particulas
    i=0
    gbest=[]
    maximo=0
    while i<cant_particulas:
        evaluacion = decision(particulas[i],cant_parametros)
        if evaluacion > maximo:
            gbest=particulas[i]
            maximo = evaluacion
        i+=1

    print(maximo)
    print(gbest)
    #print(particulas)
    #print(velocidades)
    #print(mejores)
    print()
    print()
    print()
    if cant_parametros == 2:
        i=0
        pygame.init()
        ventana = pygame.display.set_mode([ANCHO,ALTO])
        reloj = pygame.time.Clock()
        while i < iteraciones:
            print("GBEST de la iteracion en vector")
            print(gbest)
            print("GBEST de la iteracion en valor numerico")
            print(maximo)
            soluciones = cambios(particulas,cant_particulas,cant_parametros,w,c1,c2,gbest,mejores,velocidades)
            particulas = soluciones[0]
            velocidades = soluciones[1]
            ventana.fill([0,0,0])
            l=0
            while l < cant_particulas:
                pygame.draw.circle(ventana,[255,255,255],Cart_Pant(100*particulas[l]),2)
                l+=1
            pygame.display.flip()
            print("Vector de la posicion de las particulas")
            print(particulas)
            print("Vector las las velocidades de las particulas")
            print(velocidades)
            print()
            j=0
            while j < cant_particulas:
                evaluacion1 = decision(particulas[j],cant_parametros)
                evaluacion2 = decision(mejores[j],cant_parametros)
                if evaluacion1 > evaluacion2:
                    mejores[j] = particulas[j]
                if evaluacion1 > maximo:
                    maximo = evaluacion1
                    gbest = particulas[j]
                j+=1
            i+=1
            reloj.tick(1)
        fin = False
        while not fin:
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    fin=True
