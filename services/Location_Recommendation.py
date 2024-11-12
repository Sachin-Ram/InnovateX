import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib  # For saving the model

class Location_Recommender:

    def __init__(self, data_file, vectorizer_file='vectorizer.pkl', model_matrix_file='model_matrix.pkl'):
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
        try:
            # Try loading the pre-saved vectorizer and model matrix
            self.vectorizer = joblib.load(self.vectorizer_file)
            self.model_matrix = joblib.load(self.model_matrix_file)
            print("Loaded pre-trained model.")
        except:
            print("No pre-trained model found. Training a new model.")
            # Initialize the TfidfVectorizer
            self.vectorizer = TfidfVectorizer(stop_words='english')
            # Fit and transform the 'Attraction' column into TF-IDF features
            self.model_matrix = self.vectorizer.fit_transform(self.df['Attraction'])
            # Save the vectorizer and model matrix for future use
            self.save_model()

    def save_model(self):
        """Save the vectorizer and model matrix to files."""
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
        return recommendations[['City', 'Attraction', 'Similarity_Score']].head(top_n)

# Main execution
if __name__ == "__main__":
    # Replace with the path to your CSV file
    recommender = Location_Recommender(data_file="/content/updated_travel_recommendations.csv")

    # Get user preferences at runtime
    user_preferences = input("Enter your preferences (e.g., 'adventure, trekking, beach'): ")

    # Recommend cities based on the input
    recommendations = recommender.recommend_city(user_preferences)

    # Display top 5 recommended cities along with their attractions and similarity scores
    print("Top 5 recommended cities based on your preferences:")
    print(recommendations)
