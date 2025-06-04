'''Progettare un sistema di videonoleggio con i seguenti requisiti:
1. Classe Movie:
Attributi:
● movie_id: str - Identificatore di un film.
● title: str - Titolo del film.
● director: str - Regista del film.
● is_rented: boolean - Booleano che indica se il film è noleggiato o meno.
Metodi:
● rent(): Contrassegna il film come noleggiato se non è già noleggiato. Se il film
non è già noleggiato imposta is_rented a True, altrimenti stampa il messaggio "Il
film '{self.title}' è già noleggiato."
● return_movie(): Contrassegna il film come restituito. Se il film è già noleggiato
imposta is_rented a False, altrimenti stampa il messaggio "Il film '{self.title}' non è
stato noleggiato da questo cliente."
2. Classe Customer:
Attributi:
● customer_id: str - Identificativo del cliente.
● name: str - Nome del cliente.
● rented_movies: list[Movie] - Lista dei film noleggiati.
Metodi:
● rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies se non è già
stato noleggiato, altrimenti stampa il messaggio "Il film '{movie.title}' è già
noleggiato."
● return_movie(movie: Movie): Rimuove il film dalla lista rented_movies se già
presente, altrimenti stampa il messaggio "Il film '{movie.title}' non è stato
noleggiato da questo cliente."
3. Classe VideoRentalStore:
Attributi:
● movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore
l'oggetto Movie.
● customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per
valore l'oggetto Customer.
Metodi:
● add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel
videonoleggio se non è già presente, altrimenti stampa il messaggio "Il film con
ID '{movie_id}' esiste già."
● register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel
videonoleggio se non è già presente, altrimenti stampa il messaggio "Il cliente
con ID '{customer_id}' è già registrato."
● rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un
film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
"Cliente o film non trovato."
● return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un
film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
"Cliente o film non trovato."
● get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film
noleggiati dal client (customer.rented_movies) se il cliente esiste nel
videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una
lista vuota.'''

class Movie:
    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented

    def rent(self): 
        if self.is_rented == False:
           self.is_rented = True 
           return self.is_rented
        return "il film {self.title} è già noleggiato."
   
    def return_movie(self):
        if self.is_rented == True:
            self.is_rented = False
            return self.is_rented
        return "Il film {self.title} non è stato noleggiato da questo cliente."
    
class Customer:
    def __init__(self, customer_id: str, name: str, rented_movies: list[Movie]):
        self.customer_id = customer_id
        self.name = name
        self.rented_movies = rented_movies

    def rent_movie(self, movie: Movie):
        if movie.is_rented == True:
            return "Il film {movie.title} è già noleggiato"        
        return self.rented_movies.append(movie)
    
    def return_movie(self, movie: Movie):
        if movie in self.rented_movies:
            return self.rented_movies.remove(movie)
        return "Il film {movie.title} non è stato noleggiato da questo cliente."

class VideoRentalStore:
    def __init__(self, movies: dict[str, Movie], customers: dict[str, Customer]):
        self.movies = movies
        self.customers = customers

    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id in self.movies:
            return "Il film con ID {movie_id} esiste già."
        
        return self.movies.append(Movie(movie_id, title, director))
        
    def register_customer(self, customer_id: str, name: str):
        if customer_id in self.customers:
            return "il cliente con ID {customer_id} è già registrato"
        
        return self.customers.append(Customer(customer_id, name))
    '''● rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un
film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
"Cliente o film non trovato."
● return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un
film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
"Cliente o film non trovato."
● get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film
noleggiati dal client (customer.rented_movies) se il cliente esiste nel
videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una
lista vuota.'''
    def rent_movie(self, customer_id: str, movie_id: str):
        for m in self.movies: 
            if customer_id in self.customers and movie_id in self.movies:
                return self.movies[m].is_rented == True
            return "Cliente o film non trovato"
        
    def return_movie(self, customer_id: str, movie_id: str):
        for m in self.movies:
            if customer_id in self.customers and movie_id in self.movies:
                self.return_movie(movie_id)
            return "Cliente o film non trovato."
        
    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        for m in self.customers:
            if customer_id in self.customers:
                return self.customers[m].rented_movies()
            return "Cliente non trovato" 