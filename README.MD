| Contenidos  |
| ----------- |
| [ENUNCIADO EJERCICIO](https://github.com/ManuelFelipeMedina/desarollo_de_software/blob/main/README.MD#enunciado-ejercicio).   |
| [HISTORIA DE USUARIO](https://github.com/ManuelFelipeMedina/desarollo_de_software/blob/main/README.MD#historia-de-usuario).  |
| [DESCRIPCIÓN](https://github.com/ManuelFelipeMedina/desarollo_de_software/blob/main/README.MD#descipcion). |
| [REQUISITOS](https://github.com/ManuelFelipeMedina/desarollo_de_software/blob/main/README.MD#requisitos). |
| [CRITERIOS DE ACCEPTACION](https://github.com/ManuelFelipeMedina/desarollo_de_software/blob/main/README.MD#criterios-de-acceptacion). |
| [DIAGRAMA CASOS DE USO](https://github.com/ManuelFelipeMedina/desarollo_de_software/blob/main/README.MD#diagrama-casos-de-uso). |
| [DIAGRAMA CASOS DE USO EXTENDIDO](https://github.com/ManuelFelipeMedina/desarollo_de_software/blob/main/README.MD#diagrama-casos-de-uso-extendido). |
| [CURSO DE EVENTOS](https://github.com/ManuelFelipeMedina/desarollo_de_software/blob/main/README.MD#curso-de-eventos). |
| [DIAGRAMA FLUJO](https://github.com/ManuelFelipeMedina/desarollo_de_software?tab=readme-ov-file#diagrama-de-flujo). |
| [PSEUDOCODIGO](https://github.com/ManuelFelipeMedina/desarollo_de_software/blob/main/README.MD#pseudocodigo). |


## ENUNCIADO EJERCICIO
se te ha encargado el desarrollo de una aplicación de software para una veterinaria que necesita calcula el precio de una operación según el numero de horas que toma y el salario por hora acordado por el doctor que la preforma. La aplicación debe registral el Código y el nombre de la operación, las horas que toma cada operación y el salario por hora de cada doctor

- el numero de horas puede variar entre operaciones y el salario puede variar entre doctores.
- el calculo corresponde únicamente al valor bruto.
- la aplicación debe calcular el costo de una única operación.
- para simplificar el ejercicio no se requiere persistencia de los datos,

## HISTORIA DE USUARIO:
- calculo y visualización costo operación.
- como: el dueño de una veterinaria.
- quiero: ingresar los datos de una operación.
- para: calcular automáticamente el costo de cada operación y obtener el total consolidado por todas las operaciones.

## DESCRIPCIÓN:
- el sistema debe permitir registrar múltiples empleados, calcular el precio de cada operación y mostrar el total acumulado de todas las operaciones.

## REQUISITOS:
la herramienta debe permitirte ingresar los siguientes datos de cada operación:
- código operación.
- nombre operación.
- nombre del doctor.
- duración operación.
- el salario por hora del doctor.
- calcular la nomina mensual individual de cada empleado mediante la formula:

#### costo operación = duración operación * salario por hora del doctor.

la herramienta debe ser fácil de usar y no requiera conocimientos técnicos avanzados.

## CRITERIOS DE ACCEPTACION:
- el sistema permite ingresar una o mas operaciones.
- para cada operación valida: se calcula el costo individual correctamente y se muestra el valor calculado.
- el sistema muestra el total consolidado de todas las operaciones.  

## DIAGRAMA CASOS DE USO
![alt text](https://github.com/ManuelFelipeMedina/desarollo_de_software/blob/main/DIAGRAMA%20CASOS%20DE%20USO.png)


## DIAGRAMA CASOS DE USO EXTENDIDO:
- nombre: Calculador costo operaciones.
- actores: Dueño veterinaria.
- propósito: Registrar datos y Calcular el costo de una operación.

## CURSO DE EVENTOS:

1. el dueño ingresa la cantidad de operaciones a procesar.

2. para cada operación

    1. el dueño ingresa el Código de la operación
    2. el dueño ingresa el nombre de la operación
	3. el dueño ingresa el nombre del doctor 
	4. el dueño ingresa la duración de la operación
	5. el dueño ingresa el salario por hora del doctor

3. Una vez capturados todos los empleados, el sistema recorre nuevamente la información almacenada y calcula el costo individual de cada operación mediante la operación:
	#### duración * salario por hora del doctor.

4. acumula cada resultado en una variable que representa el total de todas las operaciones.

5. la aplicación muestra el total consolidado de todas las operaciones.

6. Postcondición: el total nomina mensual a sido calculado y mostrado al usuario.

## DIAGRAMA DE FLUJO
![alt text](https://github.com/ManuelFelipeMedina/desarollo_de_software/blob/main/diagrama%20dise%C3%B1o%20software.drawio.png)



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
