#como funciona el bot
import random
bot_pts=0
bot_ronda=0
si= "si"
no= "no"
verdadero = True
while verdadero == True:
    bot_ronda = bot_ronda+random.randint(1,7)
    cant=100
    if bot_ronda >= 0 or bot_ronda <=1:
        prob=0.9
        lista = [si] * int(prob * cant) + [no] * int((1 - prob) * cant)
        resultados={si:0,no:0}
        for i in range(100):
            resultados[random.choice(lista)]+=1
            prob_si= (100*resultados[si])/(resultados[no] + resultados[si])
            print("paso por aqui")
        if prob_si == si:
            break
        if prob_si == no:
            print("break 1")
            verdadero= False
            break

    elif bot_ronda >=1.5 or bot_ronda <=5:
        prob = 0.7
        lista = [si] * int(prob * cant) + [no] * int((1 - prob) * cant)
        resultados = {si: 0, no: 0}
        for i in range(100):
            resultados[random.choice(lista)] += 1
            prob_si = (100 * resultados[si]) / (resultados[no] + resultados[si])
            print("paso por aqui 2")
        if prob_si == si:
            break
        if prob_si == no:
            print("break 1")
            verdadero = False
            break
        break
    elif bot_ronda>= 3.5 or bot_ronda <=5:
        prob = 0.55
        lista = [si] * int(prob * cant) + [no] * int((1 - prob) * cant)
        resultados = {si: 0, no: 0}
        for i in range(100):
            resultados[random.choice(lista)] += 1
            prob_si = (100 * resultados[si]) / (resultados[no] + resultados[si])
            print("paso por aqui 3 ")
        if prob_si == si:
            break
        if prob_si == no:
            print("break 1")
            verdadero = False
            break
    elif bot_ronda>=5.5 or bot_ronda<=7:
        prob = 0.3
        lista = [si] * int(prob * cant) + [no] * int((1 - prob) * cant)
        resultados = {si: 0, no: 0}
        for i in range(100):
            resultados[random.choice(lista)] += 1
            prob_si = (100 * resultados[si]) / (resultados[no] + resultados[si])
            print("paso por aqui 4")
        if prob_si == si:
            break
        if prob_si == no:
            print("break 1")
            verdadero = False
            break

print(bot_ronda)