import random
def elementos(nivel,num):
    if nivel ==1:
        elementos=["Aluminio" , "Argon" , "Bario" , "Berilio" , "Boro" , "Bromo" , "Calcio" , "Carbono" , "Cesio" , "Cloro" , "Cobre" , "Flúor" , "Fosforo" , "Francio" , "Galio" , "Helio" , "Hidrogeno" , "Litio" , "Magnesio" , "Mercurio" , "Neon" , "Nitrogeno" , "Oro" , "Oxigeno" , "Plata" , "Potasio" , "Radio" , "Silicio" , "Sodio "]
    else:
        elementos=["Actinio","Americio","Berkelio","Bohrio","Californio","Circonio","Copernicio","Curio","Darmstadtio","Dubnio","Einstenio","Escandio","Estroncio","Fermio","Flerovio","Hafnio","Hassio","Itrio","Kriptón","Lantano","Laurencio","Livermorio","Meitnerio","Mendelevio","Moscovio","Neptunio","Nihonio","Niobio","Nobelio","Oganesón","Plutonio","Prometio","Radón","Roentgenio","Rubidio","Rutherfordio","Seaborgio","Tantalio","Tecnecio","Teneso","Titanio","Vanadio","Xenón"]
    return elementos[num]

def simbolos(nivel,num):
    if nivel==1:
        simbolos=["Al","Ar","Ba","Be","B","Br","Ca","C","Cs","Cl","Cu","F","P","Fr","Ga","He","H","Li","Mg","Hg","Ne","N","Au","O","Ag","K","Ra","Si","Na"]
    else:
         simbolos=["Ac","Am","Bk","Bh","Cf","Zr","Cn","Cm","Ds","Db","Es","Sc","Sr","Fm","Fl","Hf","Hs","Y","Kr","La","Lr","Lv","Mt","Md","Mc","Np","Nh","Nb","No","Og","Pu","Pm","Rn","Rg","Rb","Rf","Sg","Ta","Tc","Ts","Ti","V","Xe"]   
    return simbolos[num]
    
    
def quimica1():
    puntaje=0  
    elementos_incorrectos=[]
    vistos=[]
    print("Nivel 1")
    print()
    num=random.randint(0,28)
    for i in range(0,10):        
        while num in vistos:
            num = random.randint(0,28)
        vistos.append(num)    
        print("¿Cual es el simbolo quimico del siguiente elemento?")
        elemento=elementos(1,num)
        simbolo=simbolos(1,num)
        print(elemento)
        print()
        respuesta=input("Simbolo: ").lower()
        if respuesta == simbolo.lower():
            puntaje+=1
            print("Correcto")
            print()
            print("______________________________________________________")
        else:
            print("Incorrecto")
            elementos_incorrectos.append(elemento)
            print(f"La respuesta era {simbolo}")
            print()
            print("______________________________________________________")
    if puntaje>=7:
        print("Pasaste al nivel 2")
        print()
        for i in range(0,10):            
            while num in vistos:
                num = random.randint(0,28)
            elemento=elementos(2,num)
            simbolo=simbolos(2,num)    
            vistos.append(num)    
            print("¿Cual es el simbolo quimico del siguiente elemento?")
            print(elemento)
            print()
            respuesta=input("Simbolo: ").lower()
            if respuesta == (simbolo).lower():
                puntaje+=1
                print("Correcto")
                print()
                print("______________________________________________________")
            else:
                print("Incorrecto")
                print()
                elementos_incorrectos.append(elemento)
                print(f"La respuesta era {simbolo}")
                print()
                print("______________________________________________________")
        if puntaje>15:
            print("Felicidades ganaste")
            print(f"Tu puntaje es {puntaje}")
        else:
            print("Fin del juego")
            print(f"Tu puntaje es {puntaje}")
            print("Recuerda practicar los siguientes elementos")   
            n=0
            for i in range(4):
                for j in range(3):
                    n+=1
                    if n<=len(elementos_incorrectos):
                        print(elementos_incorrectos[n-1], end="  ")                 
                print()          
            
    else:
        print("Fin del juego")
        print(f"Tu puntaje es {puntaje}")
        print("Recuerda practicar los siguientes elementos")   
        n=0
        for i in range(4):
            for j in range(3):
                n+=1
                if n<=len(elementos_incorrectos):
                    print(elementos_incorrectos[n-1], end="  ")
                                    
            print()
        

def quimica2():
    puntaje=0  
    elementos_incorrectos=[]
    vistos=[]
    print("Nivel 1")
    print()
    num=random.randint(0,28)
    for i in range(0,10):        
        while num in vistos:
            num = random.randint(0,28)
        vistos.append(num)    
       
        elemento=elementos(1,num)
        simbolo=simbolos(1,num)
        print(simbolo)
        print()
        respuesta=input("Elemento: ").lower()
        if respuesta == elemento.lower():
            puntaje+=1
            print("Correcto")
            print()
            print("______________________________________________________")
        else:
            print("Incorrecto")
            elementos_incorrectos.append(simbolo)
            print(f"La respuesta era {elemento}")
            print()
            print("______________________________________________________")
    if puntaje>=7:
        print("Pasaste al nivel 2")
        print()
        for i in range(0,10):            
            while num in vistos:
                num = random.randint(0,28)
            elemento=elementos(2,num)
            simbolo=simbolos(2,num)    
            vistos.append(num)    
            print("¿A que elemento pertenece este simbolo?")
            print(simbolo)
            print()
            respuesta=input("Elemento: ").lower()
            if respuesta == (elemento).lower():
                puntaje+=1
                print("Correcto")
                print()
                print("______________________________________________________")
            else:
                print("Incorrecto")
                print()
                elementos_incorrectos.append(simbolo)
                print(f"La respuesta era {elemento}")
                print()
                print("______________________________________________________")
        if puntaje>15:
            print("Felicidades ganaste")
            print(f"Tu puntaje es {puntaje}")
        else:
            print("Fin del juego")
            print(f"Tu puntaje es {puntaje}")
            print("Recuerda practicar los siguientes elementos")   
            n=0
            for i in range(4):
                for j in range(5):
                    n+=1
                    if n<=len(elementos_incorrectos):
                        print(elementos_incorrectos[n-1], end="  ")                 
                print()          
            
    else:
        print("Fin del juego")
        print(f"Tu puntaje es {puntaje}")
        print("Recuerda practicar los siguientes elementos")   
        n=0
        for i in range(4):
            for j in range(5):
                n+=1
                if n<=len(elementos_incorrectos):
                    print(elementos_incorrectos[n-1], end="  ")
                                    
            print()

def quimica3():
    puntaje=0  
    elementos_incorrectos=[]
    vistos=[]
    print("Nivel 1")
    print()
    num=random.randint(0,28)    
    for i in range(0,10):
        while num in vistos:
            num = random.randint(0,28)
        vistos.append(num)
        op=random.randint(0,28)
        if op%2==0:     
            print("¿A que elemento pertenece este simbolo?")
            elemento=elementos(1,num)
            simbolo=simbolos(1,num)
            print(simbolo)
            print()
            respuesta=input("Elemento: ").lower()
            if respuesta == elemento.lower():
                puntaje+=1
                print("Correcto")
                print()
                print("______________________________________________________")
            else:
                print("Incorrecto")
                elementos_incorrectos.append(simbolo)
                print(f"La respuesta era {elemento}")
                print()
                print("______________________________________________________")
        else:
            print("¿Cual es el simbolo quimico del siguiente elemento?")
            elemento=elementos(1,num)
            simbolo=simbolos(1,num)
            print(elemento)
            print()
            respuesta=input("Simbolo: ").lower()
            if respuesta == simbolo.lower():
                puntaje+=1
                print("Correcto")
                print()
                print("______________________________________________________")
            else:
                print("Incorrecto")
                elementos_incorrectos.append(elemento)
                print(f"La respuesta era {simbolo}")
                print()
                print("______________________________________________________")
            
    if puntaje>=7:
        print("Pasaste al nivel 2")
        print()
        for i in range(0,10):
            while num in vistos:
                num = random.randint(0,28)
            vistos.append(num)
            op=random.randint(0,28)
            if op%2==0:
                elemento=elementos(2,num)
                simbolo=simbolos(2,num)     
                print("¿A que elemento pertenece este simbolo?")
                print(simbolo)
                print()
                respuesta=input("Elemento: ").lower()
                if respuesta == (elemento).lower():
                    puntaje+=1
                    print("Correcto")
                    print()
                    print("______________________________________________________")
                else:
                    print("Incorrecto")
                    print()
                    elementos_incorrectos.append(simbolo)
                    print(f"La respuesta era {elemento}")
                    print()
                    print("______________________________________________________")
        else:
            elemento=elementos(2,num)
            simbolo=simbolos(2,num)       
            print("¿Cual es el simbolo quimico del siguiente elemento?")
            print(elemento)
            print()
            respuesta=input("Simbolo: ").lower()
            if respuesta == (simbolo).lower():
                puntaje+=1
                print("Correcto")
                print()
                print("______________________________________________________")
            else:
                print("Incorrecto")
                print()
                elementos_incorrectos.append(elemento)
                print(f"La respuesta era {simbolo}")
                print()
                print("______________________________________________________")
            
        if puntaje>15:
            print("Felicidades ganaste")
            print(f"Tu puntaje es {puntaje}")
        else:
            print("Fin del juego")
            print(f"Tu puntaje es {puntaje}")
            print("Recuerda practicar los siguientes elementos")   
            n=0
            for i in range(4):
                for j in range(5):
                    n+=1
                    if n<=len(elementos_incorrectos):
                        print(elementos_incorrectos[n-1], end="  ")                 
                print()          
            
    else:
        print("Fin del juego")
        print(f"Tu puntaje es {puntaje}")
        print("Recuerda practicar los siguientes elementos")   
        n=0
        for i in range(4):
            for j in range(5):
                n+=1
                if n<=len(elementos_incorrectos):
                    print(elementos_incorrectos[n-1], end="  ")
                                    
            print()
   

print("""Opcion 1:Aidvinar el simbolo
Opcion 2:Adivinar el elemento
Opcion 3: Modo Random""")
print("Selecciona el tipo de juego: 1,2 o 3")
juego = int(input())        

if juego == 1:
    quimica1()
elif juego ==2:
    quimica2()
else:
    quimica3()
    
    