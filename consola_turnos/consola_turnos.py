import turnos_asignados


def preguntar():

    print("Bienvenido a farmacia Python")

    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmeticos")
        try:
            mi_rubro = input("Elija una opcion: ").upper()
            ["P", "F", "C"].index(mi_rubro)
        except ValueError:
            print("No es una opcion valida")
        else:
            break
    turnos_asignados.decorador(mi_rubro)


def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quieres otro turno?: [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Ingresa una opcion valida")
        else:
            if otro_turno == "N":
                print("gracias por su vista")
                break


inicio()
