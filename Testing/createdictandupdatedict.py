def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    # cancella pass e scrivi il tuo codice
    created: dict = {"profile" : name, "email": email, "telefono": telefono}
    return created

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    # cancella pass e scrivi il tuo codice
    dictionary["profile"] = name
    if email is not None:
        dictionary["email"] = email
    if telefono is not None:
        dictionary["telefono"] = telefono
    return dictionary
        


contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))

	

#{'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 788787}
#{'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 123456789}