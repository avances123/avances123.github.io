+++

title = "El problema de las tres puertas"
date =  "2014-11-09"

+++

Vamos a hacer una simulacion para averiguar un problema famoso de probabilidad, el **problema de las tres puertas**, o de **monty hall**. Este problema siempre resulta controvertido, o al menos divertido, ya que esconde una serie de eventos con cierta probabilidad que **no son independientes** pero lo parecen.

El enunciado es el siguiente:

> Supón que estás en un concurso, y se te ofrece escoger entre tres puertas: detrás de una de ellas hay un coche, y detrás de las otras, cabras. Escoges una puerta, digamos la nº1, y el presentador, que sabe lo que hay detrás de las puertas, abre otra, digamos la nº3, que contiene una cabra. Entonces te pregunta: "¿No prefieres escoger la nº2?". ¿Es mejor para ti cambiar tu elección?

Puedes ver el [resultado teorico][1] desde ya, pero aqui vamos a simularlo muchas veces a ver si es mejor quedarme con la puerta que elegí, o gano mas veces cambiando la puerta. Es un buen ejemplo como en unas pocas lineas de codigo, podemos simular un problema complejo para inferir la probabilidad de un evento. Solo basta con modelar el problema, hacerlo muchas veces y ver que pasa para hacerte una idea.

Esta funcion repite un numero ```numTrials``` de veces el concurso, almacena los 3 posibles resultados:

* ```stickWins``` Numero de veces que ganamos quedandonos con la puerta que elegimos la primera vez
* ```switchWins``` Numero de veces que ganamos cambiando a la otra puerta que queda disponible
* ```noWin``` Numero de veces que no ganamos

Despues en cada experimento, colocaremos el premio en una de las tres puertas aleatoriamente, y elegiremos una puerta tambien aleatoriamente,

Usaremos una funcion para decidir que puerta abre monty, la hemos llamado ```chooseFcn``` y se la pasaremos por parametro, asi podemos hacer un monty mas flexible.

Contabilizamos el resultado del experimento:

* Si monty abre la puerta con el premio has perdido (esto no pasa nunca en el problema original, puesto que en el concurso monty **sabia** donde estaba el premio y abria la otra puerta sin el)
* Si la puerta que elegimos es la del premio, hemos ganado sin cambiarnos
* Si monty no ha abierto la del premio, y no es la que elegimos previamente, significa que hemos cambiado y ganado.

Aqui esta el experimento entero:

```python
def simMontyHall(numTrials,chooseFcn):
    stickWins, switchWins, noWin = (0, 0, 0)
    prizeDoorChoices = [1,2,3]
    guessChoices = [1,2,3]
    for t in range(numTrials):
        prizeDoor = random.choice([1, 2, 3])
        guess = random.choice([1, 2, 3])
        toOpen = chooseFcn(guess, prizeDoor)
        if toOpen == prizeDoor:
            noWin += 1
        elif guess == prizeDoor:
            stickWins += 1
        else:
            switchWins += 1
    return (stickWins, switchWins)
```

La funcion que determina el comportamiento de monty es la siguiente:

* Si no he elegido la 1 ni tiene el premio, me da la 1
* Lo mismo para la 2
* Lo mismo para la 3

En general devuelve *la puerta que no tiene premio y no es la mia*
```python
def montyChoose(guessDoor, prizeDoor):
    if 1 != guessDoor and 1 != prizeDoor:
        return 1
    if 2 != guessDoor and 2 != prizeDoor:
        return 2
    return 3
```

Ya solo nos falta ejecutar el experimento muchas veces y ver los resultados, ganare mas veces plantandome, ganare mas veces aceptando la opcion de monty de cambiar de puerta? dara igual?

![Resultados cuando monty elige una puerta adrede](/images/montyhall1.png)

Queda claro que si te cambias tienes mas posibilidades de ganar. Pero que pasaria si monty abre una puerta **sin conocer** lo que hay detras, es decir aleatoriamente? En ese caso podria abrir la que tiene el premio y tu, perder automaticamente. Veamos la funcion que lo implementa, es muy sencilla:

```python
def randomChoose(guessDoor, prizeDoor):
    if guessDoor == 1:
        return random.choice([2,3])
    if guessDoor == 2:
        return random.choice([1,3])
    return random.choice([1,2])
```

Simplemente abre aleatoriamente una de las otras dos puertas que no elegi. Ganare mas veces plantandome, ganare mas veces aceptando la opcion de monty de cambiar de puerta? dara igual?

![Resultados cuando monty elige una puerta aleatoriamente](/images/montyhall2.png)



[1]: http://es.wikipedia.org/wiki/Problema_de_Monty_Hall
