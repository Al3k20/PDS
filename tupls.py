# Solicita ao usuário que insira as coordenadas
coordenadas = input("Digite a latitude e longitude separadas por vírgula: ")

# Divide os valores e converte para float
latitude, longitude = map(float, coordenadas.split(","))

# Exibe os valores desempacotados
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
