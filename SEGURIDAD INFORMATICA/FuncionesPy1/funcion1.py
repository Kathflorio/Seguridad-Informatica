def suma_recursiva(n):
    """Esta función calcula la suma de todos los números enteros hasta n de manera recursiva."""
    if n == 0:
        return 0
    else:
        return n + suma_recursiva(n-1)
resultado = suma_recursiva(5)
print(resultado)  # Output: 15