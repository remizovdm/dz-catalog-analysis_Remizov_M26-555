import math


def main():
    print("Hello from dz1!")

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, 
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
  total_rating = 0
  for movie in movies:
    total_rating += movie["rating"]
  avg = total_rating / len(movies)
  return round(avg, 1)

def catalog_age_stats(movies, current_year=2026):
  age = list(map(lambda movie: current_year - movie["year"], movies))
  the_oldest = age[0]
  for i in age:
    if i > the_oldest:
      the_oldest = i
  the_newest = age[0]
  for i in age:
    if i < the_newest:
      the_newest = i
  total_age = 0
  for i in age:
    total_age += i
    avg_age = total_age / len(age)
  avg_age_round = math.ceil(avg_age)
  return (the_oldest, the_newest, avg_age_round)

def duration_in_hours(minutes):
  h = minutes // 60
  min = minutes % 60
  return f'{h}ч {min}м'

def rating_tier(rating):
  if rating >= 9:
    return "шедевр"
  elif rating >= 7 and rating <= 8.9:
    return "хорошо"
  elif rating >= 5 and rating <= 6.9:
    return "средне"
  else:
    return "слабо"

def decade_label(year):
  match year:
    case _ if year > 2020:
        return "новые"
    case _ if year >= 2015 and year <= 2020:
        return "недавние"
    case _ if year < 2015:
        return "старые"


# for movie in movies:
#   if "comedy" in movie["genres"] :
#     continue
#   else:
#     print(movie["title"])

# i = 0
# while i < len(movies):
#   if movies[i]["rating"] > 9.3:
#       print(movies[i]["title"])
#       break 
#   i += 1
# else:
#   print("Шедевров не найдено")

def count_long_movies(movies, threshold=120):
  counter = 0
  for movie in movies:
    if movie["duration_min"] > threshold:
      counter += 1 
  return counter


def normalize_title(title):
  title_list = title.split()

  for i in range(len(title_list)):
    title_list[i] = title_list[i][0].upper() + title_list[i][1:]
  
  title_updated = " ".join(title_list) 
  return title_updated

def make_slug(title):
  slug = title.lower()
  slug = slug.replace(" ","-")
  return slug

def format_report_line(movie):
  return (
      f'"{normalize_title(movie["title"])}" '      
      f'({movie["year"]}) — '
      f'{movie["rating"]}/10, ' 
      f'{duration_in_hours(movie["duration_min"])}, '
      f'жанры: {", ".join(sorted(movie["genres"]))}'
  )

def titles_sorted_by_rating(movies):
  sorted_titles = []
  sorted_by_rating = sorted(movies, key = lambda movie: movie['rating'])
  for movie in sorted_by_rating:
    sorted_titles.append(normalize_title(movie['title']))
  return sorted_titles

def top_n_by_rating(movies, n=3):
  top_by_rating = []
  sorted_by_rating = sorted(movies, key = lambda movie: movie['rating'], reverse=True)
  for i in range(n):
    title_and_rating = (normalize_title(sorted_by_rating[i]['title']), 
                        sorted_by_rating[i]['rating'])
    top_by_rating.append(title_and_rating)
  return top_by_rating

def count_by_genre(movies):
  genres_count = {}
  for movie in movies:
    for genre in movie['genres']:
      genres_count[genre] = genres_count.get(genre, 0) + 1
  return genres_count

def actor_filmography(movies):
  filmography = {}
  for movie in movies:
    for actor in movie['actors']:
      if actor not in filmography:
        filmography[actor] = []
      filmography[actor].append(normalize_title(movie["title"]))
  return filmography

movies_with_rating_higher_than_average = {
    movie['title']: movie['rating'] 
    for movie in movies 
    if movie['rating'] > average_rating(movies)
    }

def all_genres(movies):
  genres = set()
  for movie in movies:
    genres.update(movie['genres'])
  return genres

def common_actors(movie1, movie2):
  actors1 = set(movie1['actors'])
  actors2 = set(movie2['actors'])
  return actors1 & actors2

def genres_only_in_one(movies_a, movies_b):
  genres_a = set()
  genres_b = set()
  for movie in movies_a:
    genres_a.update(movie['genres'])
  for movie in movies_b:
    genres_b.update(movie['genres'])
  return genres_a - genres_b

def iter_high_rated(movies, min_rating=8.0):
  for movie in movies:
    if movie['rating'] >= min_rating:
      yield movie

# for movie in iter_high_rated(movies):
#     print(format_report_line(movie))

# sum(m["duration_min"] for m in movies if m["rating"] > 7)

def build_report(movies):
  print('ОТЧЕТ ПО КАТАЛОГУ')
  print(f'Средний рейтинг: {average_rating(movies)}')
  print(
    f"Средний возраст фильмов: "
    f"{catalog_age_stats(movies, current_year=2026)[2]} лет"
)
  print('\n')
  print('Топ-3 фильма:')
  for title, rating in top_n_by_rating(movies, n=3):
    for movie in movies:
      if normalize_title(movie["title"]) == title:
        print('  '  + format_report_line(movie))
  print('\n')
  print('Фильмов по жанрам:')
  movies_by_genre = count_by_genre(movies)
  for key, value in movies_by_genre.items():
    print(f'  {key} - {value}')
  print('\n')
  genres_all = [genre for genre in all_genres(movies)]
  genres_all.sort()
  genres_in_a_line = ", ".join(genres_all)
  print(f'Все жанры каталога: {genres_in_a_line}')

if __name__ == "__main__":
  build_report(movies)