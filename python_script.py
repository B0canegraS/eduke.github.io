import time

def procesar_donacion(monto):
    print(f"Procesando donación de ${monto}...")
    time.sleep(2)
    print("¡Donación procesada exitosamente!")

# Simulación de procesamiento de una donación
donacion = float(input("Introduce el monto de tu donación: "))
procesar_donacion(donacion)
