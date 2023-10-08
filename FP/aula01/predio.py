def distanciaTempo(A, M):
    altura = 3
    velocidade = 1
    dias = 365

    distancia_total = 2 * (A * M * dias * altura) / 1000

    tempo = (distancia_total / velocidade) / 3600

    return distancia_total, tempo


print(distanciaTempo(3, 2))
