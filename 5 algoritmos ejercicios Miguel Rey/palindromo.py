def is_palindrome(text):
    # Paso 1: Filtrar el texto para conservar solo caracteres alfanuméricos y convertir a minúsculas
    filtered_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Paso 2: Sustituir los caracteres acentuados por su equivalente sin acento
    accented_chars = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for accented, unaccented in accented_chars.items():
        filtered_text = filtered_text.replace(accented, unaccented)
    
    # Paso 3: Verificar si el texto filtrado es igual a su imagen reflejada
    return filtered_text == filtered_text[::-1]

# Pedir al usuario que ingrese la frase
phrase = input("Ingresa una frase para verificar si es un palíndromo: ")

# Verificar si es un palíndromo
if is_palindrome(phrase):
    print(f'"{phrase}" es un palíndromo.')
else:
    print(f'"{phrase}" no es un palíndromo.')
