from formagenerica import FormaGenerica

class Rettangolo(FormaGenerica):

    # iniziallizza oggetto classe rettangolo

    def __init__(self):
        super().__init__()
        
        self.setShape("rettangolo")

    def draw(self) -> None:
        print(f"\n{self.getShape()}\n")

        #outer for ciclo for esterno
        for i in range(5):
            
            #inner for
            for j in range(5 * 2):
                
                #lato a e b rettangolo
                if i == 0 or i == 5-1:
                    print("*", end = " ")
                
                #lato c e d rettangolo
                elif j == 0 or j == (5 * 2) - 1:
                    print("*", end = " ")

                #stampa spazi bianchi
                else:
                    print(" ", end = " ")
            
            print("\n", end="")