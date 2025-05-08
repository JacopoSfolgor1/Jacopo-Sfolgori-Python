'''8-17. Styling Functions: Choose any three programs you wrote for this chapter, 
and make sure they follow the styling guidelines described in this section.'''

def city_country(name: str, country: str):
    return f"{name} , {country}"

print(city_country(input("inserisci name: "),input("inserisci country: ")))



def show_messages(messages: list):
    for message in messages: 
        print(message)
    
print(show_messages(["Ciao","funziona","per","favore"]))




def build_profile(**key_value):
    built_profile: str = ""
    for key, value in key_value.items():
        built_profile += f" {key}: {value}."
    return built_profile
    
  

print(build_profile(name = "Jacopo", last_name = "Sfolgori", età = 26, altezza = 180, capelli = "castano"))


