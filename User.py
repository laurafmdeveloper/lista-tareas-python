
class User:
    name="no name"
    surname="no surname"
    
    task_list= []

    #DEUDA TECNICA: en el constructor permitir crear la lista directamente o vacia
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
        

    # Funciones que permiten agregar y eliminar una tarea
    def add_new_task(self, new_task):
        self.task_list.append(new_task)

    def remove_task(self, task_index):
        self.task_list.pop(task_index)


    # Lista de tareas
    # Getter
    def get_task_list(self):
        return self.task_list

    # Función que devulve un String formateado en que las tareas se presentan enumeradas según el orden de inserción
    def get_task_list_to_string(self):

        if len(self.task_list) == 0:
            return f"El usuario {self.name} no tiene ningún elemento en su lista"

        list_to_string = f"Lista de {self.name}:\n"
        
        for index, task in enumerate(self.task_list):
            list_to_string  += "\t{0}) {1}\n".format((index+1), str(task)) 
        
        return list_to_string



    # def __str__(self) -> str:
    #     str_con_el_resultado = 'Objeto de deportes: '
    #     for deporte in self.listado_deportes:
    #         str_con_el_resultado += "\n  * {}".format(deporte)
    #     return str_con_el_resultado

    def __str__(self):
        return f"\nNombre completo: {self.name} {self.surname}\n{self.get_task_list_to_string()}\n"
