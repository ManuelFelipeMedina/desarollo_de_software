identificaciones_operaciones = []
nombres_operaciones = []
nombres_doctores = []
duraciones_operaciones = []
salario_por_hora = []
nomina_total = 0

cantidad_empleados  = int(input("Digite la cantidad de operaciones: "))

for i in range (cantidad_empleados):

    identificacion_operacion = input("Digite la identificacion de la operacion: ")
    nombre_operacion = input("Digite el nombre de la operacion: ")
    duracion = float(input("Digite la duracion de la operacion: "))
    salario = float(input("Digite el salario por hora del doctor: "))
    nombre_doctor = input("Digite el nombre del doctor: ")
    
    identificaciones.append(identificacion)
    nombres_operaciones.append(nombre_operacion)
    nombres_doctores.append(nombre_doctor)
    duraciones_operaciones.append(duracion)
    salario_por_hora.append(salario)
    
for i in range (cantidad_empleados) :
    nomina_total = nomina_total+horas_trabajadas[i]*sueldo_hora[i]
    
print("El valor total de la nomina es: ",nomina_total)