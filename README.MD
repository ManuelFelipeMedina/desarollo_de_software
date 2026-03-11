| Contenidos  |
| ----------- |
| ENUNCIADO EJERCICIO    |
| HISTORIA DE USUARIO   |
| DESCIPCION   |
| REQUISITOS |
| CRITERIOS DE ACCEPTACION |
| DIAGRAMA CASOS DE USO |
| DIAGRAMA CASOS DE USO EXTENDIDO |
| CURSO DE EVENTOS |
| PSEUDOCODIGO |


## ENUNCIADO EJERCICIO
se te ha encargado el desarrollo de una aplicacion de softwater para una vetrinaria que necesita calcula el precio de una operacion segun el numero de horas que toma y el salario por hora acordado por el doctor que la perfoma. La aplicacion debe registral el codigo y el nombre de la operacion, las horas que toma cada operacion y el salario por hora de cada doctor

- el numero de horas puede variar entre operaciones y el salrio puede variar entre doctores.
- el calculo corresponde unicamente al valor bruto.
- la aplicacion debe calcular el costo de una unica operacion.
- para simplificar el ejercicio no se requiere persistencia de los datos,

## HISTORIA DE USUARIO:
- calculo y visualizacion costo operacion.
- como: el dueño de una veterinaria.
- quiero:ingresar los datos de una operacion.
- para:calcular automaticamente el costo de cadas operacion y obtener el total consolidado por todas las operaciones.

## DESCIPCION:
- el sistema debe permitir registrar multiples empleados,calcular el precio de cada operacion y mostrar el total acomulado de todas las operaciones.

## REQUISITOS:
la herramienta debe permitirte ingresar los siguiented datos de cada operacion:
- codigo operacion.
- nombre operacion.
- nombre del doctor.
- duracion operacion.
- el salario por hora del doctor.
- calcular la nomina mensual individual de cada empleado mediante la formula:

### costo operacion = duracion operacion * salario por hora del doctor.

la herramienta debe ser facil de usar y no requiera conocimientos tecnicos avanzados.

## CRITERIOS DE ACCEPTACION:
- el sistema permite ingresar una o mas operaciones.
- para cada operacion valida: se calcula el costo individual correctamente y se muestra el valor calculado.
- el sistema muestra el total consolidado de todas las operaciones.  

![alt text](https://github.com/ManuelFelipeMedina/desarollo_de_software/blob/main/DIAGRAMA%20CASOS%20DE%20USO.png)


## DIAGRAMA CASOS DE USO EXTENDIDO:
- nombre: Calculador costo operaciones.
- actores: Dueño veterinaria.
- proposito:Registrar datos y Calcular el costo de una operacion.

## CURSO DE EVENTOS:

1. el dueño ingresa la cantidad de operaciones a procesar.

2. para cada operacion

    1. el dueño ingresa el codigo de la operacion
    2. el dueño ingresa el nombre de la operacion
	3. el dueño ingresa el nombre del doctor 
	4. el dueño ingresa la duracion de la operacion
	5. el dueño ingresa el salario por hora del doctor

3. Una vez capturados todos los empleados, el sistema recorre nuevamente la informacion almacenada y calcula el costo individual de cada operacion mediante la operacion:
	### duracion * salario por hora del doctor.

4. acomula cada resultado en una variable que representa el total de todas las operaciones.

5. la alpicacion miestra el total consolidado de todas las operacion.

- Postcondicion: el total nomina mensual a sido calculado y mostrado al usuario.

## PSEUDOCODIGO:
```
inicio
caractres:identificaciones[50],nombres_operaciones[50],nombres_doctores[50]
Real:duraciones_operaciones[50],salario_por_hora[50]
caracteres: identificacion, nombre_operaciones, nombre_doctore.
Entero: numero_operaciones, i
real: duracion_operacion,salario_por_hora, totaloperacionees <- 0
imprimir: "digite el numero de operaciones: "
asignar: numero_operaciones
para i = 0 hasta numero_operaciones - 1, 1

imprimir: "digite la identificacion de la operacion"
	asignar: identificacion
	imprimir:"digite el nombre de la operacion"
	asignar:nombre_operaciones
	imprimir:"digite las duracion de la operacion"
	asignar:duracion_operacion
	imprimir:"digite el nombre del doctor"
	asignar:nombre_doctor
	imprimir:"digite el salario por hora del doctor"
	asignar:salario_por_hora
	identificaciones[i] <- identificacion
	nombres_operaciones[i] <- nombre_operaciones
	duraciones_operaciones[i] <- duracion_operacion
	nombres_doctores[i] <- nombre_doctores
	salario_por_hora[i] <- salario_por_hora
finPara

para i = 0 hasta numero_operaciones - 1, 1
	totaloperacionees <- totaloperacionees + (duraciones_operaciones[i] * salario_por_hora[i])
finPara

imprimir: "el total de las operaciones es: " + totaloperacionees

fin
```

                                                                                                     
