'''8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs 
that describe you. All the values must be passed to the function as parameters. 
The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"'''
def build_profile(**key_value):
    built_profile: str = ""
    for key, value in key_value.items():
        built_profile += f" {key}: {value}."
    return built_profile
    
  

print(build_profile(name = "Jacopo", last_name = "Sfolgori", età = 26, altezza = 180, capelli = "castano"))


