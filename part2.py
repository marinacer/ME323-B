#TROCA A ESCOLHA
#A PORTA CERTA É A SEGUNDA-2ª
import random
from pylab import plot,xlabel,ylabel,show

n_teste = 0 #nº de vezes testadas
sucesso = 0 #nº de sucessos

x = [] #informação p/ o gráfico
y = []

for a in range(1,10000):
    escolha = random.choice([1,2,3]) #escolhe aletoriamente entre 1, 2 ou 3
    x.append(a)
    n_teste = n_teste + 1
    if escolha == 2:
        sucesso = sucesso + 1
        y.append(sucesso/n_teste)
    else:
        if escolha == 1:
            escolha = random.choice([2,3])
            if escolha == 2:
                sucesso = sucesso + 1
                y.append(sucesso/n_teste)
            else:
                y.append(sucesso/n_teste)
        else:
            escolha = random.choice([1,2])
            if escolha == 2:
                sucesso = sucesso + 1
                y.append(sucesso/n_teste)
            else:
                y.append(sucesso/n_teste)


plot(x,y)                               #plot do gráfico de y no tempo
xlabel("nº tentativas")
ylabel("acertos")
show()
