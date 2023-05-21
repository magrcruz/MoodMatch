from .modelsRecomendation import Content
import random

def generate_recommendation(num_words, type, emotion):
    words = ["apple", "banana", "orange", "grape", "pear", "melon", "pineapple"]
    random_words = random.choices(words, k=num_words)
    random_recommendations = []
    for i in random_words:
        content = Content(
            title=i,
            author='Random Author',
            link='https://example.com',
            type=type
        )
        random_recommendations.append(content)
    return random_recommendations
