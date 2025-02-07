# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1)Write a function that takes a single movie and returns True if its IMDB score is above 5.5

print("1")

def is_high_score(movie):
    return movie['imdb'] > 5.5
 #example
movie = {
    "name": "Hitman",
    "imdb": 6.3,
    "category": "Action"
}

print(is_high_score(movie)) #True

#2)Write a function that returns a sublist of movies with an IMDB score above 5.5.

print("2")

def Score(movie_list): 
    return [movie for movie in movies if movie["imdb"] > 5.5]

scorem = Score(movies)
for movie in scorem:
    print(movie["name"])

#3)Write a function that takes a category name and returns just those movies under that category.

print("3")

def Categ(category): 
    category_movies = [movie["name"] for movie in movies if movie["category"] == category]
    return category_movies

cat=input()
result=Categ(cat)
print(result)

#4)Write a function that takes a list of movies and computes the average IMDB score.

print("4")

def average_imdb_score(movie_list):
    if not movie_list:
        return 0  # Возвращаем 0, если список пуст
    total_score = sum(movie["imdb"] for movie in movie_list)
    return total_score / len(movie_list)

average_score = average_imdb_score(movies)
print( average_score)

#5)Write a function that takes a category and computes the average IMDB score.

print("5")

def category_mm(category): 
    sum = 0  # суммы рейтингов
    c = 0    #  количества фильмов

    for movie in movies: 
        # Сравниваем категории (с учетом регистра)
        if movie["category"].lower() == category.lower(): 
            sum += movie["imdb"]  # Добавляем рейтинг фильма
            c += 1  # Увеличиваем счетчик фильмов
    
    if c > 0:
        full = sum / c  # средний рейтинг
        return full
    else:
        return None  #  если фильмы не найдены

cat = input().strip().lower()
result = category_mm(cat)

# Если найдена средняя оценка, выводим её
if result is not None:
    print(result)
else:
    print("wrong category")





