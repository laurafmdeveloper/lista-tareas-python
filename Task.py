class Task:
    
    # Constructor: Establece el estado inicial del objeto (Creando e inicializando las variables)
    def __init__(self, name, description) -> None: 
        self.name = name
        self.description = description
        self.is_completed= False               # Por defecto, las tareas se crean como no completadas 


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


    # Reescribimos el método str para poder imprimir la información que nos interesa de cada objeto
    # Devuelve un String formateado
    def __str__(self):
        return f"Título: {self.name} \tCompletada: {self.is_completed} \n\tDescripción: {self.description}\n"
