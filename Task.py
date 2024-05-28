 
"""
# try except finally:
 Manejan errores en tiempo de ejecución del programa, y así, evitan que el programa se pare
 
Estos errores los encontramos cuando sintaxis del código es correcta pero 
algún valor (introducido por el usuario) que recibe una función u objeto no lo es,

debido a varias causas, 
p. ej:
- Introducir una distancia negativa para calcular el perímetro de un cuadrado
- Dividir para cero, que es una indeterminación matemática
"""

class Task:
    
    name="no name"
    description="no description"
    is_completed= False
    

    # Constructor: Establece el estado inicial de una instancia
    def __init__(self, name, description) -> None: 
        self.name = name
        self.description = description


    def get_name(self):
        return self.name 
    def set_name(self, new_name):
        self.name = new_name

    
    def get_description(self):
        return self.description
    def set_description(self, new_description):
        self.description = new_description


    def get_is_completed(self):
        return self.is_completed
    
    #Función que marca la tarea como completada
    def set_as_completed(self):
        self.is_completed = True


    # Reescribimos el método str para poder imprimir la información de cada objeto en un string
    def __str__(self):
        return f"Título: {self.name}: \tCompletada: {self.is_completed} \n\tDescripción: {self.description}\n"
