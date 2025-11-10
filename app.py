# app.py

# Importación desde el módulo 'src'
from src.procesador import Analizador

def main():
    # 1. Definición de la ruta del archivo (puede ser la causa del FileNotFoundError si está mal)
    # **REVISA ESTA RUTA:** Debe coincidir exactamente con la ubicación de tu CSV.
    archivo = "datos/sri_ventas_2024.csv" 
    
    # 2. Creación del Analizador (CORRECTAMENTE INDENTADO Y CON LA RUTA)
    analizador = Analizador(archivo)
    
    # Verificación de datos cargados para evitar fallos
    if not analizador.datos:
        # El error ya se imprimió en procesador.py, aquí solo salimos.
        print(f"ERROR: No se pudo continuar el análisis. Verifique el archivo y la ruta: {archivo}")
        return
    
    # 3. Lógica principal del programa
    print("Ventas totales por provincia:")
    resumen = analizador.ventas_totales_por_provincia()
    for prov, total in resumen.items():
        print(f"\t{prov}: ${total:,.2f}") # Uso de , para miles
        
    print("\nCompras para una provincia")
    provincia = input("\tIngrese el nombre de una provincia: ")
    
    ventas = analizador.ventas_por_provincia(provincia)
    
    # 4. Manejo del resultado
    if ventas > 0.0:
        print(f"\tVentas de {provincia}: ${ventas:,.2f}")
    else:
        # Se muestra este mensaje si ventas_por_provincia retorna 0.0
        print(f"\tERROR: No se encontraron ventas para la provincia '{provincia}'.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()