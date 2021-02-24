# Add movie
# Remove movie
#list all movies in the library
# Find movie by movie title

# store films in a list of dictionary
# {title:, director:, year:}
films = []

def add_movie():
    title = input("Enter movie title: ")
    director = input("Enter movie director: ")
    year = int(input("Enter the year the film was released: "))
    film = {'Title':title, 'Director': director, 'Year':year}
    films.append(film)
    print(f"{title} added to the movie library")

def delete_movie():
    title = input("Enter the film you want to delete: ")
    for film in films:
        if film['Title'] == title:
            films.remove(film)
            print(f"{title} has been removed from the library ")
            return
    print(f"{title} is not in the movie registry!")


def list_movies():
    for film in films:
        print_film(film)

def search():
    title = input("Enter title of film you want to look up: ")
    for film in films:
        if film['Title'] == title:
            return True
        else:
            return False


def exit_library():
    print("Exiting Library...")

def print_film(film):
    print(f"Title: {film['Title']}\t Director: {film['Director']} \t Year: {film['Year']}")
action = {
    '1': add_movie,
    '2': list_movies,
    '3': delete_movie,
    '4': search,
    'q': exit_library
}

def main():
    print("Welcome to the film Library:")
    while True:
        print("1-> add movie to library")
        print("2-> list all the movies in the library")
        print("3-> remove movie form the library")
        print("4-> Check if a movie is in the library")
        print("q-> if you want to quit")
        choice = input("Choose what you want to do from the menu above: ")
        if choice in action:
            act = action[choice]
            if act==exit_library:
                act()
                break
            act()
        else:
            print("Incorrect option, please choose from the given menu!")
        


if __name__ == '__main__':
    main()
    