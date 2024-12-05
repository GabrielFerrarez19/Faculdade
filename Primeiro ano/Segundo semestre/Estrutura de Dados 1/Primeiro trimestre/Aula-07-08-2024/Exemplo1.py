def calcula_tempo(velocidade, distancia):
    tempo = distancia/velocidade 
    return tempo

def calcula_distancia(velocidade, tempo):
    distancia = velocidade * tempo
    return distancia

v = 10 
t = calcula_tempo(v, 5 )
print("------Tempo------")
print(t)
d = calcula_distancia(v,t)
print("------Distancia------")
print(d)
