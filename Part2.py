import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("netflix_data.csv")

# Keep only movies
df_movies = df[df["type"] == "Movie"].copy()

# Make sure duration, year, and genre are valid
df_movies = df_movies.dropna(subset=["duration", "release_year", "genre"])

# Line chart: average movie length each year
avg_duration_per_year = df_movies.groupby("release_year")["duration"].mean()

plt.figure(figsize=(12,6))
avg_duration_per_year.plot()
plt.title("Average Movie Duration on Netflix Over Years")
plt.xlabel("Year")
plt.ylabel("Average Duration (minutes)")
plt.grid(True)
plt.show()

# Split genres into lists
df_movies["genre_list"] = df_movies["genre"].str.split(", ")

# One row for each genre
df_exploded = df_movies.explode("genre_list")

# Average length by year and genre
avg_duration_genre_year = (
    df_exploded.groupby(["release_year", "genre_list"])["duration"]
    .mean()
    .reset_index()
)

# Top 5 most common genres
top_genres = df_exploded["genre_list"].value_counts().head(5).index

# Line chart: average movie length by genre and year
plt.figure(figsize=(14,8))
sns.lineplot(
    data=avg_duration_genre_year[avg_duration_genre_year["genre_list"].isin(top_genres)],
    x="release_year", y="duration", hue="genre_list"
)
plt.title("Average Movie Duration by Genre Over the Years")
plt.xlabel("Release Year")
plt.ylabel("Average Duration (minutes)")
plt.grid(True)
plt.legend(title="Genre")
plt.show()

# Linear Regression
x = avg_duration_per_year.index.values
y = avg_duration_per_year.values

m, b = np.polyfit(x, y, 1)
y_pred = m * x + b    # Calculate predicted values

# Calculating R²
ss_res = np.sum((y - y_pred) ** 2)                  
ss_tot = np.sum((y - np.mean(y)) ** 2)              
r_squared = 1 - (ss_res / ss_tot)

# Show results
print(f"Slope coefficient: {m:.2f}")
print(f"Intercept coefficient: {b:.2f}")
print(f"R²: {r_squared:.4f}")

plt.figure(figsize=(12,6))
sns.scatterplot(x=x, y=y, label="Average Duration")
plt.plot(x, y_pred, color="red", label="Trend Line (Linear Regression)")
plt.title("Trend of Average Movie Duration on Netflix Over Time")
plt.xlabel("Release Year")
plt.ylabel("Average Duration (minutes)")
plt.legend()
plt.grid(True)
plt.show()
