import requests

url = "https://api.geoapify.com/v2/places?categories=commercial.supermarket&filter=rect%3A10.716463143326969%2C48.755151258420966%2C10.835314015356737%2C48.680903341613316&limit=20&apiKey=b9d1895378094a11bc7c5526ae76f272"


def get_posts():
    response = requests.get(f"{url}/posts")
    if response.status_code == 200:
        return response.json()


def get_posts_by_user(userId):
    # cria um dicionário com pares de chave: valor para passar na string de consulta da url
    params = {'userId': userId}
    response = requests.get(f"{url}/posts", params=params)
    # o argumento params= é codificado na string de consulta da URL

    # print(response.request.url)  descomentar para ver a URL construida

    if response.status_code == 200:
        return response.json()  # descodifico JSON em um objeto python(lista)


def add_post(title, body, user_id):
    # criação do dicionário
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    response = requests.post(f"{url}/posts", json=data)
    # With json=... o conteudo pedido é enviado como JSON

    if response.status_code == 201:
        return response.json()


# Função que ao ler o ficheiro cria um dicionário
def read_file_to_dictionary(file_name):
    dictionary = {}
    with open(file_name, 'r') as file:
        current_key = None
        for line in file:
            elements = line.strip().split('.')
            key = elements[0]
            value = '.'.join(elements[1:])

            # verifica se a chave é a mesma que a da linha anterior
            if key == current_key:
                dictionary[key].append(value)
            else:
                # Se não é uma nova chave, cria uma nova lista com o valor atual
                dictionary[key] = [value]
                current_key = key

    return dictionary


# Função que valida tipos de atrações
def validate_attraction_types(attraction_types, categories):
    valid_types = []
    for attr_type in attraction_types:
        if attr_type in categories:
            valid_types.append(attr_type)
    return valid_types


file_name = 'categories.txt'

# cria o dicionário ao chamar a função
my_dictionary = read_file_to_dictionary(file_name)

# tirar as aspas para ver o dicionário criado
'''for key, values in my_dictionary.items():
    print(f"{key}: {', '.join(values)}")
'''
# inputs do utilizador
start_latitude = float(input("Enter your starting latitude: "))
start_longitude = float(input("Enter your starting longitude: "))
travel_distance = float(input("Enter the distance you want to travel in kilometers: "))
attraction_types = input("Enter the attraction types you want to visit (separated by commas): ").split(",")

# validação dos tipos de atrações
valid_attraction_types = validate_attraction_types(attraction_types, my_dictionary.keys())
for attraction_type in valid_attraction_types:
    if attraction_type in my_dictionary:
        print(f"{attraction_type}: {', '.join(my_dictionary[attraction_type])}")
print("Valid attraction types:", valid_attraction_types)



