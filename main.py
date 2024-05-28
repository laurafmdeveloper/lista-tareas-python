from Task import *
from User import *


# Instanciamos varios objetos de la clase Task
t1 = Task('T1 título', 'T1 descripción')
t2 = Task('Nota mental', 'Lisa necesita aparato')
t3 = Task('Lista de la compra', 'Leche, pan y huevos')

# Instanciamos varios objetos de la clase User
homer = User('Homer J.', 'Simpson')
lisa = User('Lisa', 'Simpson')
 
 
 
print("- Homer no tiene tareas -") 
print(homer.get_task_list_to_string())

print("- Añadimos 3 tareas a la lista de Homer -")
homer.add_new_task(t3) 
homer.add_new_task(t2) 
homer.add_new_task(t1)
print(homer.get_task_list_to_string())

print("\n- Nº de tareas de Homer: ", (len(homer.get_task_list())), "-" )

homer.remove_task(2)
print("- Tarea borrada -")
print("- Nº de tareas de Homer: ", (len(homer.get_task_list())), "-" ) 


print( '\n\n******** BORRAR pero mantener como test de formatos( ojo task y user que queden los 2 bien ******'  )

print( '\n\nstr(homer)'  )
print(str(homer))
print( 'str(t2)'  )
print(str(t2))