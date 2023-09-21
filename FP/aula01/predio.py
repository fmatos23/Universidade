def distanciaTempo(A, M):
    altura = 3
    velocidade = 1
    dias = 365


    distancia_total = 2 * A * M * 2 * dias * altura

    # Calcular o tempo total em horas
    tempo = (distancia_total / velocidade) / 3600

    return distancia_total, tempo

