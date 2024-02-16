# Função para processar um nome e atualizar o dicionário
def process_name(name, name_dict):
    # Divida o nome em partes usando o espaço como delimitador
    parts = name.split()

    # O último nome é a última parte
    last_name = parts[-1]

    # imprime apenas o primeiro nome
    first_name = parts[:1]

    # Atualize o dicionário
    if last_name in name_dict:
        name_dict[last_name].update(first_name)
    else:
        name_dict[last_name] = set(first_name)

# Ler nomes do arquivo
with open('names.txt', 'r') as file:
    names = file.read().splitlines()

# Criar um dicionário vazio para armazenar os resultados
name_dict = {}

# Processar cada nome na lista
for name in names:
    process_name(name, name_dict)

# Imprimir resultados
for last_name, first_names in name_dict.items():
    print(f"{last_name}: {', '.join(first_names)}")
