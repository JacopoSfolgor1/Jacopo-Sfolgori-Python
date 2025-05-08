from persona import Persona
from alieno import Alieno

#creare oggetto p della classe persona

p: Persona = Persona("Jacopo", "Sfolgori", 26)

#visualizza info

print(p)

#creare oggetto et della classe alieno

et: Alieno = Alieno("Andromeda")

#visualizza info

print(et)

#fare in modo che oggetto p invochi metodo speak

p.speak()

#fare in modo che oggetto et invochi metodo speak

et.speak()