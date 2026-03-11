## ENUNCIADO EJERCICIO
se te ha encargado el desarrollo de una aplicacion de softwater para una vetrinaria que necesita calcula el precio de una operacion segun el numero de horas que toma y el salario por hora acordado por el doctor que la perfoma. La aplicacion debe registral el codigo y el nombre de la operacion, las horas que toma cada operacion y el salario por hora de cada doctor

> - el numero de horas puede variar entre operaciones y el salrio puede variar entre doctores.
> - el calculo corresponde unicamente al valor bruto.
> - la aplicacion debe calcular el costo de una unica operacion.
> - para simplificar el ejercicio no se requiere persistencia de los datos,

## HISTORIA DE USUARIO:
> - calculo y visualizacion costo operacion.
> - como: el dueño de una veterinaria.
> - quiero:ingresar los datos de una operacion.
> - para:calcular automaticamente el costo de cadas operacion y obtener el total consolidado por todas las operaciones.

## DESCIPCION:
> - el sistema debe permitir registrar multiples empleados,calcular el precio de cada operacion y mostrar el total acomulado de todas las operaciones.

## REQUISITOS:
la herramienta debe permitirte ingresar los siguiented datos de cada operacion:
> - codigo operacion.
> - nombre operacion.
> - nombre del doctor.
> - duracion operacion.
> - el salario por hora del doctor.
calcular la nomina mensual individual de cada empleado mediante la formula:

### costo operacion = duracion operacion * salario por hora del doctor.

la herramienta debe ser facil de usar y no requiera conocimientos tecnicos avanzados.

## CRITERIOS DE ACCEPTACION:
> - el sistema permite ingresar una o mas operaciones.
> - para cada operacion valida: se calcula el costo individual correctamente y se muestra el valor calculado.
> - el sistema muestra el total consolidado de todas las operaciones.  

--diagrama de casos.png

## DIAGRAMA CASOS DE USO EXTENDIDO:
> - nombre: Calculador costo operaciones.
> - actores: Dueño veterinaria.
> - proposito:Registrar datos y Calcular el costo de una operacion.

## CURSO DE EVENTOS:

1. el dueño ingresa la cantidad de operaciones a procesar.

2. para cada operacion:
> -   el dueño ingresa el codigo de la operacion.
> - el dueño ingresa el nombre de la operacion.
> - el dueño ingresa el nombre del doctor.
> - el dueño ingresa la duracion de la operacion.
> - el dueño ingresa el salario por hora del doctor.

3.Una vez capturados todos los empleados, el sistema recorre nuevamente la informacion almacenada y calcula el costo individual de cada operacion mediante la operacion:
	-duracion * salario por hora del doctor.

4.acomula cada resultado en una variable que representa el total de todas las operaciones.

5.la alpicacion miestra el total consolidado de todas las operacion.

Postcondicion: el total nomina mensual a sido calculado y mostrado al usuario.
                                                                                                     
