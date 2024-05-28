
class User:

    # Declaración de variables de estado con valores por defecto
    # La variable task_list, además de ser declarada, se inicializa como una lista vacía
    name = ""
    surname = ""
    task_list = []
    
    # Con el constructor, inicializamos el resto de variables de estado. 
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname


    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name

    
    def get_surname(self):
        return self.surname 
    def set_surname(self, new_surname):
            self.surname = new_surname
        

    # Métodos que operan sobre una tarea:
    # Permiten agregar una nueva
    def add_new_task(self, new_task):
        self.task_list.append(new_task)
    # Elimina una tarea existente por su índice en la lista
    def remove_task(self, task_index):
        self.task_list.pop(task_index)


    # Métodos de la lista de tareas:
    # Getter
    def get_task_list(self):
        return self.task_list

    # Función que devuelve un String formateado de las tareas enumeradas según el orden de inserción
    def get_task_list_to_string(self):

        if len(self.task_list) == 0:
            return f"El usuario {self.name} no tiene ningún elemento en su lista"

        list_to_string = f"Lista de {self.name}:\n"
        
        for index, task in enumerate(self.task_list):
            list_to_string  += "\t{0}) {1}\n".format((index+1), str(task)) 
        
        return list_to_string


    # Sobreescribimos el método str para obtener información del User
    def __str__(self):
        return f"\nNombre completo: {self.name} {self.surname}\n{self.get_task_list_to_string()}\n"
