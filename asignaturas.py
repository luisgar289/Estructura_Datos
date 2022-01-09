asignaturas = "Matematicas", "Expresion oral", "Estructura de datos", "Base de datos", "Idiomas"
print("Por favor ingresa la nota de cada uno de tus cursos ")
m = int(input("{0}: ".format(asignaturas[0])))
e_o = int(input("{0}: ".format(asignaturas[1])))
e_d = int(input("{0}: ".format(asignaturas[2])))
bd = int(input("{0}: ".format(asignaturas[3])))
i = int(input("{0}: ".format(asignaturas[4])))

tupla = m, e_o, e_d, bd, i

print("En {0} tu calificacion es {1}".format(asignaturas[0], tupla[0]))
print("En {0} tu calificacion es {0}".format(asignaturas[1]),tupla[1])
print("En {0} tu calificacion es {0}".format(asignaturas[2]),tupla[2])
print("En {0} tu calificacion es {0}".format(asignaturas[3]),tupla[3])
print("En {0} tu calificacion es {0}".format(asignaturas[4]),tupla[4])
