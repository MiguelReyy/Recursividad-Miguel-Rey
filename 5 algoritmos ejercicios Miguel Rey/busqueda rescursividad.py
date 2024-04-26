def binary_search_recursive(arr, target, start=0, end=None):
    # Si 'end' no se especifica, se establece como el índice del último elemento en la lista
    if end is None:
        end = len(arr) - 1
    
    # Si el índice de inicio supera al de fin, el elemento no está presente en la lista
    if start > end:
        return -1  # Elemento no encontrado
    
    mid = (start + end) // 2  # Encontrar el índice medio
    
    # Si el elemento en el índice medio es igual al objetivo, retornar el índice medio
    if arr[mid] == target:
        return mid
    # Si el elemento en el índice medio es menor que el objetivo, realizar búsqueda en la mitad derecha del arreglo
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, end)
    # Si el elemento en el índice medio es mayor que el objetivo, realizar búsqueda en la mitad izquierda del arreglo
    else:
        return binary_search_recursive(arr, target, start, mid - 1)
    
# Solicitar al usuario que ingrese la lista y el elemento a buscar
try:
    arr_input = input("Ingrese la lista ordenada de números separados por espacios: ").split()
    arr = [int(x) for x in arr_input]  # Convertir los elementos de la lista a enteros
except ValueError:
    print("Error: La lista contiene caracteres no numéricos.")
    exit()

target_element = input("Ingrese el elemento que desea buscar en la lista: ")

# Verificar si la lista está ordenada
if arr != sorted(arr):
    print("Error: La lista ingresada no está ordenada.")
else:
    try:
        target_element = int(target_element)
        # Realizar la búsqueda binaria recursiva
        index = binary_search_recursive(arr, target_element)
        if index != -1:
            print(f"El elemento {target_element} se encuentra en el índice {index}.")
        else:
            print(f"El elemento {target_element} no se encuentra en la lista.")
    except ValueError:
        print("Error: El elemento a buscar no es un número válido.")
