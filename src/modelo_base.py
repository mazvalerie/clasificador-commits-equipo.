# Script base para el procesamiento de datos y modelo de IA
import os

def inicializar_proyecto():
    print("Iniciando componentes del sistema de Inteligencia Artificial...")
    print(f"Directorio de trabajo actual: {os.getcwd()}")
    
    ruta_csv = "data/dataset_prueba.csv"
    if os.path.exists(ruta_csv):
        print(f"Dataset encontrado con éxito en: {ruta_csv}")
    else:
        print("Dataset no encontrado.")

if __name__ == "__main__":
    inicializar_proyecto()
