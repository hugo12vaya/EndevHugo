#Hugo Vaya Simeon

#Importem les llibreries nececaries i inicialitzem contadors i variables.

import random
altraPartida = True
partides = 1
premi = 0
intents_totals = 0
intents_maxims = 0
intents_minims = 100

#Iniciem el bucle per a que començe la partida.

while altraPartida == True:

    major = 100

    menor = 1

    numero_secret = random.randint(menor,major)

    print (numero_secret)

    cantitat_maxima_intents = int(input("Dis-me la cantitat maxima d'intents: "))

    numero_demanat = int(input("Dis-me el numero secret: "))

    intents = 1

    #Mentres no encertem el numero secret haura de fer el seguent...

    while numero_demanat != numero_secret:

        if cantitat_maxima_intents == intents:

            break

        elif numero_demanat>major or numero_demanat<menor:
            
            print('El numero esta fora de rang.')

            numero_demanat = (int(input("El rang es " + str(menor) + " i " + str(major) + ": ")))

        elif numero_demanat>=menor and numero_demanat<numero_secret:

            menor = numero_demanat+1

            numero_demanat = (int(input("No. Es major. Esta entre " + str(menor) + " i " + str(major) + ": ")))
        
        elif numero_demanat<=major and numero_demanat>numero_secret:

            major = numero_demanat-1

            numero_demanat = (int(input("No. Es menor. Esta entre " + str(menor) + " i " + str(major) + ": ")))
        
        intents = intents + 1

    if numero_demanat == numero_secret:

        print("Molt bé! Ho has encertat en " ,intents, " intents.")

        premi = premi+1

        intents_totals = intents_totals+intents

    else: print("Has superat els intents i no ho has endevinat. El número era el " ,numero_secret, ".")

    if intents>intents_maxims and numero_demanat == numero_secret:

        intents_maxims = intents

    if intents<intents_minims and numero_demanat == numero_secret:

        intents_minims = intents

    resposta = input("Vols jugar altra partida? Si(s) o No(n): ")

    if resposta == 's' or resposta == 'S':

        altraPartida = True

        partides = partides +1

    elif resposta == 'n' or resposta == 'N':

        altraPartida = False

#Una vegada finalitzada la partida mostrarem els resultatas:

print('Has jugat',partides, 'partides')

print("PREMI " * premi)

if premi == 0:

    print('No et puc mostrar la mitjana')

else: print('La mitja de intents de les partides guanyades es ',intents_totals/premi)

if premi > 0:
    
    print('Has utilitzat un minim de',intents_minims, ' i un maxim de ',intents_maxims)

else: print('')