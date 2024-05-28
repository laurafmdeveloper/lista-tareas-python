
class User:

    # Con el constructor, declaramos e inicializamos las variables de estado. 
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname 
        self.task_list = []             # Por defecto, task_list se crea como una lista vacía


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


 
    # Elimina una tarea existente dado su índice en la lista
    # Utilizamos la estructura 'try except' para manejar el error que lanzaría un index fuera de rango
    # Devuelve un booleano
    def remove_task(self, task_index):
        try:
            if 0 <= task_index < len(self.task_list):
                self.task_list.pop(task_index)
                return True # Informa de que la tarea se ha eliminado correctamente
            else:
                raise IndexError("Índice fuera de rango.")
        except IndexError as e:
            print(f"Error: {e}")
            return False # Informa de que la tarea no se ha podido eliminar
  

    # Métodos de la lista de tareas:
    # Getter
    def get_task_list(self):
        return self.task_list

    # Función que devuelve un String formateado de las tareas enumeradas según el orden de inserción
    def get_task_list_to_string(self):

        if len(self.task_list) == 0:
            return f"El usuario {self.name} no tiene ninguna tarea en su lista"

        list_to_string = f"Lista de {self.name}:\n"
        for index, task in enumerate(self.task_list):
            list_to_string  += "\t{0}) {1}\n".format((index + 1), str(task)) 
        
        return list_to_string


    # Sobreescribimos el método str para obtener información del User
    def __str__(self):
        return f"\nNombre completo: {self.name} {self.surname}\n{self.get_task_list_to_string()}\n"
