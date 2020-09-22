####################################################################
# Diego Sevilla 17238
####################################################################
# Curso: Redes
# Programa: functions.py
# Propósito: modulo de funciones utiles para el proyecto
# Fecha: 08/2020
####################################################################

# ----------------
# def function(params):
#    return null


def Wellcome():
    print("______________________________________________________________________________________")
    print("                   ¡   ¡   W   E   L   L   C   O   M   E   !   !                      ")
    print("                                                                                      ")
    print("                                       T   O                                          ")
    print("                                                                                      ")
    print("           X       X   M               M   P P P P P P     P P P P P P                ")
    print("            X     X    M M           M M   P           P   P           P              ")
    print("             X   X     M  M         M  M   P            P  P            P             ")
    print("              X X      M   M       M   M   P           P   P           P              ") 
    print("               X       M    M     M    M   P P P P P P     P P P P P P                ")
    print("              X X      M     M   M     M   P               P                          ")
    print("             X   X     M      M M      M   P               P                          ")
    print("            X     X    M       M       M   P               P                          ")
    print("           X       X   M               M   P               P                          ")
    print("______________________________________________________________________________________")
    print("--------------------------------------------------------------------------------------")
    print("                                                                                      ")
    print("                        #######################################                       ")
    print("                              ************************                                ")
    print("                                                                                      ")

def theEnd():
    print(" ")
    print("                                 ¡¡Bye Bye!!       ")
    print("                              ¡¡See you soon!! :D  ")
    print("                                                   ")
    print("                                   (o^^)o          ")
    print("                                    o(^^o)         ")
    print("                                   o(^^)o          ")
    print("                                                   ")
    print("                                 ¡ The End !       ")
    print("                                                   ")

def read_integer():
    """ Asks for an integer value and return that value.
        If the input value is not an integer, the function asks for it again """
    while True:
        valor = input("Choose an option: ")
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print("")
            print("¡Haa haaaa! ¡¿Didn't explode right?! ¡Try again! xp")
            print("")

