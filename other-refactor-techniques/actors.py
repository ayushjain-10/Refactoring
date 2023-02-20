# by Kami Bigdely
# Extract class
first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

class Actor:
    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
    def display_movies(self):
        print("Movies Played: ", end='')
        for m in self.movies:
            print(m, end=', ')
        print()

def send_hiring_email(email):
    print("email sent to: ", email)
    
actors = [Actor(first_names[i], last_names[i], birth_year[i], movies[i], emails[i]) for i in range(len(emails))]

for actor in actors:
    if actor.birth_year > 1985:
        print(actor)
        actor.display_movies()
        send_hiring_email(actor.email)

