# Import spacy and load the 'en_core_web_md'
import spacy
nlp = spacy.load('en_core_web_md')

description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch\
    him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

#----------------------------------#
# Following a good practice in programming, I split this task in two functions, where each one does only one relevant task.
#----------------------------------#

# This function reads the file 'movies.txt' and find similarities with the text inside the variable 'description' right above.
# Results are appended to an empty list where we are going to find the highest result and return its index in the list.
def movie_suggestion(description):
    
    desc = nlp(description)

    ranking = []

    with open("movies.txt", "r+") as list_of_movies:
        for movies in list_of_movies:
            similarity = nlp(movies).similarity(desc)
            ranking.append(similarity)

        for idx, val in enumerate(ranking):
                if val == max(ranking):
                  return idx


# Next function goes back to the file 'movies.txt' and get only the movie where the index is equal to the index returned by the previous function.
# And then prints the name of the movie.
def get_movie():
    with open("movies.txt", "r+") as list_of_movies:
        recommendations = list(list_of_movies)
        print(recommendations[movie_suggestion(description)])


# Now we call the function that returns the name of the movie.
get_movie()
