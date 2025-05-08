menu = { "Pizza" : 9, "Pasta" : 10.50, "Zuppa" : 7, "Hamburger" : 15.50,"Cotoletta" : 10, "Salmone" : 20.20, "Patatine fritte" : 5.50,
    "Patate al forno" : 5.50, "Verdura del giorno" : 7, "Cheesecake" : 6, "Tiramisu'" : 6, "Focaccia con Nutella" : 6, "Coca Cola" : 3.50, 
    "Acqua" : 1.50, "Vino" : 5 } # Menu' del giorno

ordine = { "Pizza" : 9, "Cotoletta": 10, "Verdura del giorno" : 7, "Tiramisu'" : 6, "Vino" : 5 } #ordine del cliente

print(ordine)
print(ordine["Pizza"])
print(ordine["Cotoletta"])
print(ordine["Verdura del giorno"])
print(ordine["Tiramisu'"])
print(ordine["Vino"])

somma = (ordine["Pizza"] + ordine["Cotoletta"] + ordine["Verdura del giorno"] + ordine["Tiramisu'"] + ordine["Vino"]) 
print(somma) #Conto da pagare