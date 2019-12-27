#Adaline.py
import sys, numpy, math
import matplotlib.pyplot as plt

#Animation.py
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

"""Classe Adaline, a qual eh uma rede neural basica"""
class Adaline:
    """Construtor da classe"""
    def __init__(self, entrada):
        self.gain = 100.0 #Serve para deixar a funcao mais continua
        self.w = [0.0, 0.0] #Vetor de tamanho 2 para o peso
        self.x = entrada #Matriz 4x2 Sao as entradas possiveis para 2 bits, ao inves de 0 e 1 tem-se -1 e 1
        self.t = [] #Vetor de tamanho 4 para a saida esperada
        self.b = 0.0
        self.y = 0.0
        self.soma = 0.0
        self.eta = 0.01 #Taxa de aprendizado
        self.iteraPesos = []

    """"""        
    def f(self, arg):
        return math.tanh(arg * self.gain)
        
    """"""
    def treinamento(self, maxiterates):
        y_interm = 0.0 #O y_interm é igual a "y in term" (Termo y de entrada)
        n_epocas = 0
        for i in range(1, maxiterates):
            hits = 0 #Numero de acertos no treinamento
            n_epocas += 1
            for j in range(0, 4): #Percorre o numero de valores da porta Logica (2 bits = 2^2 = 4 possibilidades)
                y_interm = self.propaga(j)
                y = self.f(y_interm)
                self.atualiza_pesos(j, y_interm)
                if y == self.t[j]:
                    hits += 1
                else:
                    self.atualiza_bias(j)
            v = [self.b, self.w[0], self.w[1]]
            self.iteraPesos.append(v)
            if hits == 4:
                break
        print("Numero de iteracoes: " + str(n_epocas))
        print("Vetor de Pesos Final: " + str([self.b, self.w[0], self.w[1]]))
        for i in range(len(self.iteraPesos)):
            print("Vetor de Pesos: It " + str(i) + " " + str(self.iteraPesos[i]))
 
    """"""
    def propaga(self, i):
        soma = 0.0
        for j in range(0, 2):
            soma += self.x[i][j]*self.w[j]
        return soma + self.b
    
    """"""
    def propaga2(self, x1, x2):
        soma = 0.0
        soma = x1*self.w[0] + x2*self.w[1]
        return soma + self.b
    
    """"""
    def atualiza_pesos(self, i, y_in):
        for j in range(0,2):
            self.w[j] += self.eta * (self.t[i] - y_in) * self.x[i][j];
    
    """"""
    def atualiza_bias(self, i):
        self.b += self.t[i] * self.eta;
    
    """"""
    def apresenta_resultados(self):
        for i in range(0,4):
            propaga = self.propaga(i)
            saida = self.f(propaga)
            print("Entrada " + str(self.x[i]) + ", Classe: " + str(saida))
    
    """Apenas inicializa o vetor t do objeto com o dado da Porta Logica a ser treinada"""
    def cria_treinamento(self, A):
        for i in range(0,4):
            self.t.append(A[i])
            
    """"""
    """def plota_grafico(self):
        arq = open("lalala.ppm", 'w')
        arq.write("P3\n3000 3000\n255\n")
        count = 0
        for x11 in range(-1500,1500):
            count += 1
            for x22 in range(-1500,1500):
                x1 = float(x11)/1000.0
                x2 = float(x22)/1000.0
                if (abs(abs(x1)-1.0)<0.2 and abs(abs(x2)-1.0)<0.2):
                    arq.write("255 0 0 ")
                elif(self.propaga2(x1,x2)<0):
                    arq.write("255 255 0 ")
                else:
                    arq.write("0 255 255 ")
            arq.write("\n")
        arq.close()
    """
        
"""Gera o grafico de saida"""
def plota_grafico(entradas, saidas):
    for i in range(len(entradas)):
        if saidas[i] == 1:
            ax.plot(entradas[i][0], entradas[i][1], "k+")
        else:
            ax.plot(entradas[i][0], entradas[i][1], "ro")
    anim = animation.FuncAnimation(fig, animate, init_func=initialize)
    plt.show()

# initialization function: plot the background of each frame
def initialize():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    val = i % len(rede.iteraPesos)
    x = [0, -rede.iteraPesos[val][0]/rede.iteraPesos[val][2]]
    y = [-rede.iteraPesos[val][0]/rede.iteraPesos[val][1], 0]
    line.set_data(x, y)
    return line,

if len(sys.argv) < 2:
    print("Digite python3 " + str(sys.argv[0]) + " <testeDesejado>")
    exit(0) #Se os parametros nao forem passados adequadamente, sai do programa
    
fig = plt.figure()
ax = plt.axes(xlim=(-5, 5), ylim=(-5, 5))
line, = ax.plot([], [], lw=2)

maxiterates = 1000 #Numero maximo de iteracoes para encontrar o resultado
amostras = [[-1, -1],[-1, 1],[1, -1],[1, 1]] #Entradas
use = int(sys.argv[1]) #Pega o teste por parametro
if use == 1: #Porta Logica OR
    print("TESTANDO PORTA LOGICA OR...")
    saidas = [-1, 1, 1, 1] #Porta logica OR (Os valores sao as saidas das entradas self.x que esta harded coded no objeto)
elif use == 2: #Porta Logica AND
    print("TESTANDO PORTA LOGICA AND...")
    saidas = [-1, -1, -1, 1] #Porta logica AND (Os valores sao as saidas das entradas self.x que esta harded coded no objeto)
elif use == 3: #Porta Logica XOR
    print("TESTANDO PORTA LOGICA XOR...")
    saidas = [-1, 1, 1, -1] #Porta logica XOR (Os valores sao as saidas das entradas self.x que esta harded coded no objeto)
else:
    print("1-OR, 2-AND, 3-XOR")
if use in [1,2,3]:
    rede = Adaline(amostras) #Instancia um objeto da classe Adaline()
    rede.cria_treinamento(saidas) #Chama a funcao para copiar os dados para o vetor do Objeto
    rede.treinamento(maxiterates) #Chama a funcao para treinar a Rede neural ate o numero maximo de iteracoes definido, ou ate ela aprender
    rede.apresenta_resultados() #
    plota_grafico(amostras,saidas) #


