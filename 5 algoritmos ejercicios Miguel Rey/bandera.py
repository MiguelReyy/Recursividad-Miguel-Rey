def organizar_fichas_rvb(num_rojo, num_verde, num_azul):
    # Crear una lista de fichas con la cantidad especificada de fichas de cada color
    fichas = ['rojo'] * num_rojo + ['verde'] * num_verde + ['azul'] * num_azul
    
    # Inicializar índices para insertar la próxima ficha de cada color
    rojo_idx = 0  # Índice para insertar la próxima ficha roja
    verde_idx = num_rojo  # Índice para insertar la próxima ficha verde
    azul_idx = num_rojo + num_verde  # Índice para insertar la próxima ficha azul
    
    # Iterar sobre las fichas y mover las fichas verdes y azules a sus posiciones correctas
    for i in range(len(fichas)):
        if fichas[i] == 'verde':
            fichas[verde_idx] = 'verde'  # Mover la ficha verde a su posición correcta
            verde_idx += 1
        elif fichas[i] == 'azul':
            fichas[azul_idx] = 'azul'  # Mover la ficha azul a su posición correcta
            azul_idx += 1
    
    return fichas

# Pedir al usuario que ingrese el número de fichas de cada color
num_rojo = int(input("Ingrese el número de fichas rojas: "))
num_verde = int(input("Ingrese el número de fichas verdes: "))
num_azul = int(input("Ingrese el número de fichas azules: "))

# Organizar las fichas en el orden RVB
fichas_ordenadas = organizar_fichas_rvb(num_rojo, num_verde, num_azul)

# Mostrar el resultado
print("Fichas ordenadas:", fichas_ordenadas)
