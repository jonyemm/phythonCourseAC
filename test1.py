
total = input("Costo total: ")
totalPersonas = input("Total de Personas: ")
porcentajePropina = input("Porcentaje de Propina: ")

propina = ((float(porcentajePropina)/100) * float(total)) 
totalConPropina = round(float(total) + propina, 2)
pagoPorPersona = round(totalConPropina / float(totalPersonas), 2)


print("\n\nGran Total: " + str(totalConPropina) + "\nPago por Persona: " + str(pagoPorPersona) )