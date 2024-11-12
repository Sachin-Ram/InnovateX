import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import os

class Location_Recommender:

    def __init__(self, data_file, vectorizer_file='/home/sachin/Innovate_X_/Model/vectorizer.pkl', model_matrix_file='/home/sachin/Innovate_X_/Model/model_matrix.pkl'):
        self.data_file = data_file
        self.vectorizer_file = vectorizer_file
        self.model_matrix_file = model_matrix_file
        self.df = None
        self.vectorizer = None
        self.model_matrix = None

        # Load the dataset and the model (if saved), otherwise train a new model
        self.load_data()
        self.load_or_train_model()

    def load_data(self):
        """Load the dataset from the given file path."""
        self.df = pd.read_csv(self.data_file)



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
        self.model_matrix = self.vectorizer.fit_transform(self.df['Attraction'])

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
        self.df['Similarity_Score'] = cos_similarities.flatten()

        # Sort the cities by similarity score (highest first) and return top recommendations
        recommendations = self.df.sort_values(by='Similarity_Score', ascending=False)
        return recommendations[['City']].head(top_n)

