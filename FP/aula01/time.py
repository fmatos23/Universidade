
def secToClock():
    segundos = int(input("tempo em segundos: "))
    h = segundos // 60 // 60
    m = (segundos // 60) % 60
    s = segundos % 60

    print("{:02d}:{:02d}:{:02d}".format(h, m, s))

def minToClock():
    minutos = int(input("tempo em minutos: "))

    h = minutos // 60
    m = minutos % 60
    s = (minutos % 60) * 60

    print("{:02d}:{:02d}:{:02d}".format(h, m, s))


def hourToClock():
    hours = float(input("horas: "))

    h = int(hours)  # The whole hours part
    m = int((hours % 1) * 60)  # Extract the decimal part as minutes and convert to int
    s = int(((hours % 1) * 60 % 1) * 60)  # Extract the decimal part as seconds and convert to int

    print("{:02d}:{:02d}:{:02d}".format(h, m, s))


# Example usage:
hourToClock()



