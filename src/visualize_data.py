import json
import matplotlib.pyplot as plt

def visualize_data():
    with open("data/movies.json") as f:
        data = json.load(f)
    movies = data['results']
    titles = [movie['title'] for movie in movies[:10]]
    ratings = [movie['vote_average'] for movie in movies[:10]]

    plt.barh(titles, ratings)
    plt.xlabel("Ratings")
    plt.ylabel("Movies")
    plt.title("Top 10 Movies by Rating")
    plt.show()

if __name__ == "__main__":
    visualize_data()
