class Estudiante:
        identificacion:int
        nombre: str
        semestre: str
        calificaciones: list[float]

        def __init__(self, identificacion, nombre, semestre, calificaciones):
            self.identificacion = identificacion
            self.nombre = nombre
            self.semestre = semestre
            self.calificaciones = calificaciones

        def obtener_promedio(self):
            if not self.calificaciones:
                return 0.0
            return sum(self.calificaciones) / len(self.calificaciones)

        def ver_informacion(self):
            promedio = self.obtener_promedio()
            return (
            f"ID: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Semestre: {self.semestre}\n"
            f"Promedio: {promedio:.2f}"
        )

estudiantes: list[Estudiante] = []
while True:
    print("\n1. Agregar estudiante")
    print("2. Ver promedio estudiante")
    print("3. Ver información de un estudiante")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        identificacion = int(input("Ingrese la identificación del estudiante: "))
        nombre = input("Ingrese el nombre del estudiante: ")
        semestre = input("Ingrese el semestre del estudiante: ")
        print("Ingrese las calificaciones del estudiante")
        notas = []
        for i in range(3):
            nota = float(input(f"Calificación {i + 1}: "))
            notas.append(nota)
        estudiante = Estudiante(identificacion, nombre, semestre, notas)
        estudiantes.append(estudiante)

    elif opcion == "2" or opcion == "3":
        id_buscar = int(input("Ingrese la identificación del estudiante: "))
        encontrado = False
        for est in estudiantes:
            if est.identificacion == id_buscar:
                if opcion == "2":
                    print(f"Promedio: {est.obtener_promedio():.2f}")
                else:
                    print("\n--- Información del Estudiante ---")
                    print(est.ver_informacion())
                encontrado = True
                break
            if not encontrado:
                print("Estudiante no encontrado.")

            elif opcion == "4":
                break
        else:
            print("Opción no válida. Intente nuevamente.")