import pandas as pd

df = pd.read_csv("netflix_data.csv")

# Filter only movies from the 1990s
movies_90s = df[(df["type"] == "Movie") &
                (df["release_year"] >= 1990) &
                (df["release_year"] <= 1999)]

# Drop rows where duration is missing
movies_90s = movies_90s.dropna(subset=["duration"])

# Find the most frequent duration 
most_common_duration = movies_90s["duration"].mode()[0]
print("Most frequent movie duration in the 1990s:", most_common_duration)

# Count short action movies
short_action_movies = movies_90s[(movies_90s["duration"] < 90) &
                                 (movies_90s["genre"].str.contains("Action", na=False))]

# Save the count in a variable
short_movie_count = len(short_action_movies)
print("Number of short action movies in the 1990s:", short_movie_count)

# Count how many are Dramas
romance_count = df["genre"].str.contains("Dramas", na=False).sum()
print("\nNumber of Dramas titles:", romance_count)

# Count all Brazilian titles 
brazil_total = df["country"].str.contains("Brazil", na=False).sum()
print("Total Brazilian titles:", brazil_total)

# Most common genres
print("\nTop 5 genres:")
print(df["genre"].value_counts().head(5))