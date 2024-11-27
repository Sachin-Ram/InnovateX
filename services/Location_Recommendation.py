import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import os

class Location_Recommender:

    def __init__(self, city_data_file, place_data_file, vectorizer_file='/home/sachin/Innovate_X_/Model/vectorizer.pkl', model_matrix_file='/home/sachin/Innovate_X_/Model/model_matrix.pkl'):
        self.city_data_file = city_data_file
        self.place_data_file = place_data_file
        self.vectorizer_file = vectorizer_file
        self.model_matrix_file = model_matrix_file
        self.city_df = None
        self.place_df = None
        self.vectorizer = None
        self.model_matrix = None

        # Load the datasets and the model (if saved), otherwise train a new model
        self.load_city_data()
        self.load_place_data()
        self.load_or_train_model()

    def load_city_data(self):
        """Load the city dataset from the given file path."""
        self.city_df = pd.read_csv(self.city_data_file)

    def load_place_data(self):
        """Load the place dataset from the given file path."""
        self.place_df = pd.read_csv(self.place_data_file)

    def load_or_train_model(self):
        """Load a saved model or train a new model if none exists."""
        if os.path.exists(self.vectorizer_file) and os.path.exists(self.model_matrix_file):
            try:
                # Try loading the pre-saved vectorizer and model matrix
                self.vectorizer = joblib.load(self.vectorizer_file)
                self.model_matrix = joblib.load(self.model_matrix_file)
                print("Loaded pre-trained model.")
            except Exception as e:
                print(f"Error loading pre-trained model: {e}. Training a new model.")
                self.train_and_save_model()
        else:
            print("No pre-trained model found. Training a new model.")
            self.train_and_save_model()

    def train_and_save_model(self):
        """Train a new model and save the vectorizer and model matrix."""
        # Initialize the TfidfVectorizer
        self.vectorizer = TfidfVectorizer(stop_words='english')

        # Fit and transform the 'Attraction' column into TF-IDF features
        self.model_matrix = self.vectorizer.fit_transform(self.city_df['Attraction'])

        # Ensure the directory exists before saving
        os.makedirs(os.path.dirname(self.vectorizer_file), exist_ok=True)

        # Save the vectorizer and model matrix for future use
        joblib.dump(self.vectorizer, self.vectorizer_file)
        joblib.dump(self.model_matrix, self.model_matrix_file)

    def recommend_city(self, user_preferences, top_n=5):
        """Recommend cities based on user preferences."""
        # Convert user preferences into the same TF-IDF vector space
        user_vector = self.vectorizer.transform([user_preferences])

        # Calculate cosine similarity between the user's preferences and each city's attractions
        cos_similarities = cosine_similarity(user_vector, self.model_matrix)

        # Add similarity score to the DataFrame
        self.city_df['Similarity_Score'] = cos_similarities.flatten()

        # Sort the cities by similarity score (highest first) and return top recommendations
        recommendations = self.city_df.sort_values(by='Similarity_Score', ascending=False)
        return recommendations[['City']].head(top_n)

    def recommend_places(self, city, user_preferences, top_n=5):
        """Recommend places in a given city based on user preferences."""
        # Filter places belonging to the selected city
        city_places = self.place_df[self.place_df['City'] == city]

        if city_places.empty:
            return f"No places found for the city {city}."

        # Initialize a TfidfVectorizer for places if not already initialized
        place_vectorizer = TfidfVectorizer(stop_words='english')
        place_matrix = place_vectorizer.fit_transform(city_places['Description'])

        # Transform the user preferences into the place vector space
        user_vector = place_vectorizer.transform([user_preferences])

        # Calculate cosine similarity
        cos_similarities = cosine_similarity(user_vector, place_matrix)

        # Add similarity scores to the places DataFrame
        city_places = city_places.copy()
        city_places['Similarity_Score'] = cos_similarities.flatten()

        # Sort and return the top places
        recommendations = city_places.sort_values(by='Similarity_Score', ascending=False)
        return recommendations[['Place']].head(top_n)
