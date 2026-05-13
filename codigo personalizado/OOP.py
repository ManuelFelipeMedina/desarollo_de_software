class Operacion:
    def __init__(self,identificacion_operacion,nombre_operacion,nombre_docotor,duracion_operacion,salario_hora):
        self.identificacion_operacion = identificacion_operacion
        self.nombre_operacion = nombre_operacion
        self.nombre_docotor = nombre_docotor
        self.duracion_operacion = horas_trabajadas
        self.salario_hora = salario_hora
        
    def calcular_salario_total(self):
            return int(self.horas_trabajadas) * int(self.sueldo_hora)

def main():
     Empleados = []
     
     nomina_total = 0
     
     cantidad_empleados = int(input("digite la cantidad de empleados: "))
     
     for i in range(cantidad_empleados):
     
          print(f"\n Empleado {i + 1}: ")
          identificacion_operacion = input("Digite la identificacion de la operacion: ")
          nombre_operacion = input("digite el nombre del empleado: ")
          nombre_docotor = input("digite el nombre del empleado: ")
          duracion_operacion = input("digite las horas trabajadas del empleado: ")
          salario_hora = input("digite el sueldo por hora del empleado: ")


          Operaciones = Operacion(identificacion,nombre_operacion,nombre_docotor,duracion_operacion,salario_hora)
          Operaciones.append(Operacion)

     costo_total = sum(emp.calcular_salario_total() for op in Operaciones)
     
     print(f"\n El costo total de las operaciones es: {costo_total}")
if __name__ == "__main__":
     main()