# -*- coding: utf-8 -*-
#%%
import random
#para poder contar las cantidades de cursos
cont2=0
cont3=0
cont5=0
cont7=0
cont11=0
cont13=0
cont17=0
cont19=0
cont23=0
cont29=0
cont31=0
Fitnesvalor=[0]*10
#esta funcion lo que haces es crear un individuo
def CrearNúmeros():
    a=0
    Random=[]
    while(a<=5):
        A1 = str(random.randint(0,1))
        A2 = str(random.randint(0,1))
        A3 = str(random.randint(0,1))
        A4 = str(random.randint(0,1))
        B = A1+A2+A3+A4
        Random.append(B)
        if B=='1011' or B=='1100' or B=='1101' or B=='1110' or B=='0000':
            Random.pop(a)
            a=a-1
        a=a+1    

    return Random
#esta funcion lo que hace es llamar al individuo y 
def CrearPoblación_10():
    Población = []
    for i in range(10):
        Población_Aux = []
        Lunes = CrearNúmeros()
        Población_Aux.append(Lunes)
        Martes = CrearNúmeros()
        Población_Aux.append(Martes)
        Miércoles = CrearNúmeros()
        Población_Aux.append(Miércoles)
        Jueves = CrearNúmeros()
        Población_Aux.append(Jueves)
        Viernes = CrearNúmeros()
        Población_Aux.append(Viernes)
        Sábado = CrearNúmeros()
        Población_Aux.append(Sábado)
        Población.append(Población_Aux)
        
    return Población
#esta funcion es para poder calcular el fitnes y error:
def CuentaError(P):
    Fitness = [0]*10
    Cont2 = 0
    Cont3 = 0
    Cont5 = 0
    Cont7 = 0
    Cont11 = 0
    Cont13 = 0
    Cont17 = 0
    Cont19 = 0
    Cont23 = 0
    Cont29 = 0
    Cont31 = 0
    global fit
    global cont
    global Fitnesvalor
    for j in range(len(P)):
        for i in range(6):
            priaux=P[j][i]
            Cont2=Cont2+priaux.count('0001')
            Cont3=Cont3+priaux.count('0010')
            Cont5=Cont5+priaux.count('0011')
            Cont7=Cont7+priaux.count('0100')
            Cont11=Cont11+priaux.count('0101')
            Cont13=Cont13+priaux.count('0110')
            Cont17=Cont17+priaux.count('0111')
            Cont19=Cont19+priaux.count('1000')
            Cont23=Cont23+priaux.count('1001')
            Cont29=Cont29+priaux.count('1010')
            Cont31=Cont31+priaux.count('1111')

        cont=Cont2+Cont3+Cont5+Cont7+Cont11+Cont13+Cont17+Cont19+Cont23+Cont29+Cont31
        Fit = 2*(Cont2)+ 3*(Cont3) + 5*(Cont5) +7*(Cont7)+ 11*(Cont11)+ 13*(Cont13) + 17*(Cont17)+19*(Cont19)+23*(Cont23)+29*(Cont29)+31*(Cont31)                                                                             
        print("mi fitness: ", end='')
        print(Fit)
        #Fit = 3*(Cont2)+ 5*(Cont3) + 7*(Cont5) +11*(Cont7)+ 13*(Cont11)+ 17*(Cont13) + 19*(Cont17)+23*(Cont19)+29*(Cont23)+31*(Cont29)+37*(Cont31)                                                                             
        
        #Fit = 2**(Cont2)+ 3**(Cont3) + 5**(Cont5) +7**(Cont7)+ 11**(Cont11)+ 13**(Cont13) + 17**(Cont17)+19**(Cont19)+23**(Cont23)+29**(Cont29)+31**(Cont31)                                                                             
        
        
        Fitness[j] = 573 - Fit
        for i in range(len(Fitness)):
            aux=Fitness[i]
            Fitness[i]=abs(aux)

        Cont2 = 0
        Cont3 = 0
        Cont5 = 0
        Cont7 = 0
        Cont11 = 0
        Cont13 = 0
        Cont17 = 0
        Cont19 = 0
        Cont23 = 0
        Cont29 = 0
        Cont31 = 0
    return Fitness
def Compara(FitN,poblacion):
    global BucleFin
    if 0 in FitN:
        PoblaciónFinal = poblacion[FitN.index(0)]
        print("si")
        BucleFin=1
        return PoblaciónFinal
        
    else:
        BucleFin=0
    
def Hijos(Pobla1):
    Pareja = [1,2,3,4,5,6,7,8,9,10]
    #randon pareja
    random.shuffle(Pareja)
    # juntar las parejas
    PuntoCrossover=[]
    Poblares=[]
    total1=[]
    rest1=[]
    rest2=[]
    #
    for i in range(5):
        PuntoCrossover.append(random.randint(0,5))
        PuntoCrossover.append('0')
        
    PoblaAux = Pobla1
    
    #juntan a los padres
    for i in range (len(Pobla1)):
        Poblares.append(PoblaAux[Pareja[i]-1])
        
    #hijos
    #Realizo la permutación del Punto Crossover
    for i in range (0,10,2):
        PtoCross = PuntoCrossover[i]
        #parte 1 del crossover del padre 1 se va para el hijo 1 
        CrossoverAux1A=Poblares[i][0:PtoCross+1]
        #parte 2 del crossover del padre 2 se va para el hijo 1
        CrossoverAux1=Poblares[i+1][PtoCross+1:]
        #sacar los valores del primer hijo
        rest1=CrossoverAux1A+CrossoverAux1
        total1.append(rest1)
        #parte 1 de crossover del padre 2 se va para el hijo 2 
        CrossoverAux2A=Poblares[i+1][0:PtoCross+1]
        #parte 2 del cossover del padre 1 se va para el hijo 2
        CrossoverAux2=Poblares[i][PtoCross+1:]
        rest2=CrossoverAux2A+CrossoverAux2
        total1.append(rest2)
    return total1

for y in range(1000):
    Pobla=CrearPoblación_10()
    Fitnessaux=CuentaError(Pobla)
    print("el error de la poblacion es: ", end='')
    print(Fitnessaux)
    IdxMax = Fitnessaux.index(max(Fitnessaux))
    IdxMin = Fitnessaux.index(min(Fitnessaux))
    Reemplazo = Pobla[IdxMin]
    Pobla[IdxMax] = Reemplazo
    #emparejar e hijos 
    valorfinal=Hijos(Pobla)
    pob=Compara(Fitnessaux, valorfinal)
    if BucleFin==1:
        break
    else: 
        pass

# pob me arrolará un lista como como se ve en el comentario 

# pob=[['0100', '0111', '1010', '1000', '0001', '0111'],
#      ['0011', '0100', '1001', '0010', '1010', '1010'],
#      ['1001', '1111', '0100', '0011', '0001', '0001'],
#      ['0111', '0100', '0010', '0111', '1111', '0001'],
#      ['1010', '0001', '1001', '1000', '0011', '0111'],
#      ['0110', '0010', '0101', '1000', '0110', '0111']]


variablepo=[[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]] 
PoblaciónFinal=pob
contando=[0]*11

# cantidad de ataques que realizará 

for a in range (1000):
    random.shuffle(pob)
    for i in range(6):
        auxiliar=[]
        auxiliar1=[]
        auxiliar=PoblaciónFinal[i][0:3]     
        auxiliar=list(set(auxiliar))
        
        if cont2>=3 and ('0001' in auxiliar):
            auxiliar.remove('0001')
        if cont3>=3 and ('0010' in auxiliar):
            auxiliar.remove('0010')
        if cont5>=3 and ('0011' in auxiliar):
            auxiliar.remove('0011')
        if cont7>=3 and ('0100' in auxiliar):
            auxiliar.remove('0100') 
        if cont11>=3 and ('0101' in auxiliar):
            auxiliar.remove('0101')
        if cont13>=3 and ('0110' in auxiliar):
            auxiliar.remove('0110')
        if cont17>=3 and ('0111' in auxiliar):
            auxiliar.remove('0111')
        if cont19>=3 and ('1000' in auxiliar):
            auxiliar.remove('1000')
        if cont23>=3 and ('1001' in auxiliar):
            auxiliar.remove('1001')
        if cont29>=3 and ('1010' in auxiliar):
            auxiliar.remove('1010')
        if cont31>=6 and ('1111' in auxiliar):
            auxiliar.remove('1111') 
        VALOR=3-len(auxiliar)
    
        if VALOR!=0:
            for j in range(VALOR):
                
            
                if '0001' not in auxiliar and cont2<3:
                    auxiliar.append('0001')
                
                elif '0011' not in auxiliar and cont5<3:
                    auxiliar.append('0011')
                    
                elif '0010' not in auxiliar and cont3<3:
                    auxiliar.append('0010')
                
                elif '0101' not in auxiliar and cont11<3:
                    auxiliar.append('0101')
                
                elif '0100' not in auxiliar and cont7<3:
                    auxiliar.append('0100')
                
                elif '0110' not in auxiliar and cont13<3:
                    auxiliar.append('0110')
                    
                elif '1000' not in auxiliar and cont19<3:
                    auxiliar.append('1000')    
                
                elif '0111' not in auxiliar and cont17<3:
                    auxiliar.append('0111')
            
                elif cont31<6:
                    auxiliar.append('1111')
                
                elif '1010' not in auxiliar and cont29<3:
                    auxiliar.append('1010')
                
                elif '1001' not in auxiliar and cont23<3:
                    auxiliar.append('1001')
                
                
        else:
            pass
        
        variablepo[i][0:3]=auxiliar
        cont2=cont2+auxiliar.count('0001')
        cont3=cont3+auxiliar.count('0010')
        cont5=cont5+auxiliar.count('0011')
        cont7=cont7+auxiliar.count('0100')
        cont11=cont11+auxiliar.count('0101')
        cont13=cont13+auxiliar.count('0110')
        cont17=cont17+auxiliar.count('0111')
        cont19=cont19+auxiliar.count('1000')
        cont23=cont23+auxiliar.count('1001')
        cont29=cont29+auxiliar.count('1010')
        cont31=cont31+auxiliar.count('1111')
        contando[0]=cont2
        contando[1]=cont3
        contando[2]=cont5
        contando[3]=cont7
        contando[4]=cont11
        contando[5]=cont13
        contando[6]=cont17
        contando[7]=cont19
        contando[8]=cont23
        contando[9]=cont29
        contando[10]=cont31  
            
        auxiliar1=PoblaciónFinal[5][3:6]
        auxiliar1=list(set(auxiliar1))
        if cont2>=3 and ('0001' in auxiliar1):
            auxiliar1.remove('0001')
        if cont3>=3 and ('0010' in auxiliar1):
            auxiliar1.remove('0010')
        if cont5>=3 and ('0011' in auxiliar1):
            auxiliar1.remove('0011')
        if cont7>=3 and ('0100' in auxiliar1):
            auxiliar1.remove('0100') 
        if cont11>=3 and ('0101' in auxiliar1):
            auxiliar1.remove('0101')
        if cont13>=3 and ('0110' in auxiliar1):
            auxiliar1.remove('0110')
        if cont17>=3 and ('0111' in auxiliar1):
            auxiliar1.remove('0111')
        if cont19>=3 and ('1000' in auxiliar1):
            auxiliar1.remove('1000')
        if cont23>=3 and ('1001' in auxiliar1):
            auxiliar1.remove('1001')
        if cont29>=3 and ('1010' in auxiliar1):
            auxiliar1.remove('1010')
        if cont31>=6 and ('1111' in auxiliar1):
            auxiliar1.remove('1111')   
        VALOR1=3-len(auxiliar1)
        if VALOR1!=0: 
            for k in range(VALOR1):
            
                if ('0001' not in auxiliar1) and cont2<3:
                    auxiliar1.append('0001')
                
                
                
                elif ('0011' not in auxiliar1) and cont5<3:
                    auxiliar1.append('0011')
               
                elif ('0010' not in auxiliar1) and cont3<3:
                    auxiliar1.append('0010')
                    
                    
                elif ('0100' not in auxiliar1) and cont7<3:
                    auxiliar1.append('0100')
                
                
                elif ('0110' not in auxiliar1) and cont13<3:
                    auxiliar1.append('0110')
                
                elif ('0101' not in auxiliar1) and cont11<3:
                    auxiliar1.append('0101') 
                    
                elif ('0111' not in auxiliar1) and cont17<3:
                    auxiliar1.append('0111')


                elif ('1001' not in auxiliar1) and cont23<3:
                    auxiliar1.append('1001')
                
                elif ('1000' not in auxiliar1) and cont19<3:
                    auxiliar1.append('1000')
                    
                elif cont31<6:
                    auxiliar1.append('1111')
                
                elif ('1010' not in auxiliar1) and cont29<3:
                    auxiliar1.append('1010') 
        
        else: 
            pass
        variablepo[i][3:]=auxiliar1
        cont2=cont2+auxiliar1.count('0001')
        cont3=cont3+auxiliar1.count('0010')
        cont5=cont5+auxiliar1.count('0011')
        cont7=cont7+auxiliar1.count('0100')
        cont11=cont11+auxiliar1.count('0101')
        cont13=cont13+auxiliar1.count('0110')
        cont17=cont17+auxiliar1.count('0111')
        cont19=cont19+auxiliar1.count('1000')
        cont23=cont23+auxiliar1.count('1001')
        cont29=cont29+auxiliar1.count('1010')
        cont31=cont31+auxiliar1.count('1111')
    
        contando[0]=cont2
        contando[1]=cont3
        contando[2]=cont5
        contando[3]=cont7
        contando[4]=cont11
        contando[5]=cont13
        contando[6]=cont17
        contando[7]=cont19
        contando[8]=cont23
        contando[9]=cont29
        contando[10]=cont31
    print("Ataques relizados: ", end='')
    print(a+1)
    if cont2==3 and cont3==3 and cont5==3 and cont7==3 and cont11==3 and cont13==3 and cont17==3 and cont19==3 and cont23==3 and cont29==3 and cont31==6:
        
        break
    else:
        pass  
resultado=[[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]

if cont2==3 and cont3==3 and cont5==3 and cont7==3 and cont11==3 and cont13==3 and cont17==3 and cont19==3 and cont23==3 and cont29==3 and cont31==6:
    for i in range(6):
        for j in range(6):
            if (variablepo[i][j] == '0001'):
                resultado[i][j] = 'Inglés'
            elif (variablepo[i][j] == '0010'):
                resultado[i][j] = 'Alemán'
            elif (variablepo[i][j] == '0011'):
                resultado[i][j] = 'Frances'
            elif (variablepo[i][j] == '0100'):
                resultado[i][j] = 'Italiano'
            elif (variablepo[i][j] == '0101'):
                resultado[i][j] = 'Portugues'
            elif (variablepo[i][j] == '0110'):
                resultado[i][j] = 'Chino m.'
            elif (variablepo[i][j] == '0111'):
                resultado[i][j] = 'Ruso'
            elif (variablepo[i][j] == '1000'):
                resultado[i][j] = 'Japones'
            elif (variablepo[i][j] == '1001'):
                resultado[i][j] = 'Arabe'
            elif (variablepo[i][j] == '1010'):
                resultado[i][j] = 'Español'
            elif (variablepo[i][j] == '1111'):
                resultado[i][j] = 'Libre'
    Po = resultado  #Cambiamos de Nombre por comodidad para el fString
    print("ENCONTRÓ!!!!")
    print("En el intento N°: ", end='') 
    print(a+1) 
    print("Contador de cursos: ",end='')
    print(contando)
    print("#####################################################################################")
    print("horario perfecto(en BITS)")
    print(variablepo)
    print("#####################################################################################")
    print("HORARIO | LUNES  | MARTES  | MIÉRCOLES | JUEVES  | VIERNES | SÁBADO")
    print(f"------  |{Po[0][0]:11}|{Po[1][0]:11}|{Po[2][0]:11}|{Po[3][0]:11}",end='')
    print(f"|{Po[4][0]:11}|{Po[5][0]:11}")
    print(f"15-17   |{Po[0][1]:11}|{Po[1][1]:11}|{Po[2][1]:11}|{Po[3][1]:11}",end='')
    print(f"|{Po[4][1]:11}  |{Po[5][1]:11}")
    print(f"------  |{Po[0][2]:11}|{Po[1][2]:11}|{Po[2][2]:11}|{Po[3][2]:11}",end='')
    print(f"|{Po[4][2]:11}|{Po[5][2]:11}") 
    print("-----------------------------------------------------------------------------")
    print(f"------  |{Po[0][3]:11} |{Po[1][3]:11}|{Po[2][3]:11}|{Po[3][3]:11}",end='')
    print(f"|{Po[4][3]:11}|{Po[5][3]:11}")
    print(f"17-19   |{Po[0][4]:11}|{Po[1][4]:11}|{Po[2][4]:11}|{Po[3][4]:11}",end='')
    print(f"|{Po[4][4]:11}|{Po[5][4]:11}")
    print(f"------  |{Po[0][5]:11} |{Po[1][5]:11}|{Po[2][5]:11}|{Po[3][5]:11}",end='')
    print(f"|{Po[4][5]:11}|{Po[5][5]:11}")
    print("#####################################################################################")
    print("SE PUDO ENCONTRAR SOLUCION!!!!!!") 
else:
    print("No se pudo encontrar una solución")
