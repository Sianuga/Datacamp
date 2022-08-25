import pandas as pd
import matplotlib.pyplot as plt

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

movie_dict = {"years": years, "durations": durations}
durations_df = pd.DataFrame.from_dict(movie_dict)

fig = plt.figure()
plt.plot(durations_df["years"], durations_df["durations"])
plt.title("Netflix Movie Durations 2011-2020")
plt.show()

netflix_df = pd.read_csv("netflix_data.csv")
netflix_df_movies_only = netflix_df[netflix_df['type'] == "Movie"]
netflix_movies_col_subset = netflix_df_movies_only[["title", "country", "genre", "release_year", "duration"]]

fig = plt.figure(figsize=(12, 8))
plt.scatter(x=netflix_movies_col_subset["release_year"], y=netflix_movies_col_subset["duration"])
plt.title("Movie Duration by Year of Release")
plt.show()

short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"] < 60]
colors = []

for ind, rows in netflix_movies_col_subset.iterrows():
    if rows['genre'] == "Children":
        colors.append("red")
    elif rows['genre'] == "Documentaries":
        colors.append("blue")
    elif rows['genre'] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12, 8))
plt.scatter(x=netflix_movies_col_subset["release_year"], y=netflix_movies_col_subset["duration"], c=colors)
plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.show()
