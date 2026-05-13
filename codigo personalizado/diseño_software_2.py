def main():
    operaciones = []

    costo_total = 0

    cantidad_operaciones = int(input("digite la cantidad de operaciones: "))

    for i in range(cantidad_operaciones):

            print(f"operacion {i+1}:")
            identificacion_operacion = input("Digite la identificacion de la operacion: ")
            nombre_operacion = input("Digite el nombre de la operacion: ")
            nombre_docotor = input("Digite el nombre del doctor: ")
            duracion = float(input("Digite la duracion de la operacion: "))
            salario = float(input("Digite el salario por hora del doctor: "))

            operacion = {
                 "identificacion" : identificacion,
                 "nombre operacion" : nombre_operacion,
                 "nombre doctor" : nombre_doctor,
                 "duracion" : duracion,
                 "salario": salario
            }

            operaciones.append(operacion)

    for op in operaciones:
         costo_total += op["hora"] * op["sueldo"]

    print (f"el costo total de todas las operaciones es: {costo_total}")

















if __name__ == "__main__":
    main()