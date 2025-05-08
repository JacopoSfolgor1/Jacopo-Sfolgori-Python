class Alieno:
    '''
    di un alieno interessa sapere galssia provenienza self.galaxi: str
    '''

    #inizializza oggetto classe alieno
    def __init__(self, galaxy: str):
        
        self.setGalaxy(galaxy)

    def setGalaxy(self, galaxy: str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else:
            print("Errore! La galassia di provenienza non può essere una stringa vuota")

    def getGalaxy(self) -> str:
        return self.galaxy

    def speak(self) -> None:
        print("\nsufhasujgh\n")    

    def __str__(self) -> str:
        return f"\nAlieno provieniente dalla galassia {self.galaxy}\n"
    
        
