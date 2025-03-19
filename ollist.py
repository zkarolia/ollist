import pandas as pd

# Load the dataset
df = pd.read_csv('c:/archive/olist_order_reviews_dataset.csv')  

# Handle missing values 
df['review_score'] = df['review_score'].fillna(0).astype(int)

# Define a function to map scores to sentiment
def map_sentiment(score):
    if score >= 4:
        return 'Positive'
    elif score == 3:
        return 'Neutral'
    elif score <= 2:
        return 'Negative'

# Apply the function to the review_score column
df['sentiment'] = df['review_score'].apply(map_sentiment)

# Check the results
print(df[['review_score', 'sentiment']].head())

import matplotlib.pyplot as plt

# Count the occurrences of each sentiment
sentiment_counts = df['sentiment'].value_counts()

# Plot the distribution
sentiment_counts.plot(kind='bar', color=['green', 'orange', 'red'], figsize=(8, 5))
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=0)
plt.show()

# Combine reviews into text grouped by sentiment
positive_reviews = ' '.join(df[df['sentiment'] == 'Positive']['review_comment_title'].fillna(''))
neutral_reviews = ' '.join(df[df['sentiment'] == 'Neutral']['review_comment_title'].fillna(''))
negative_reviews = ' '.join(df[df['sentiment'] == 'Negative']['review_comment_title'].fillna(''))

from wordcloud import WordCloud

# Define a function to generate word clouds
def generate_wordcloud(text, title, color):
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap=color).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()

# Positive reviews (green shades)
generate_wordcloud(positive_reviews, 'Positive Reviews Word Cloud', 'Greens')

# Neutral reviews (orange shades)
generate_wordcloud(neutral_reviews, 'Neutral Reviews Word Cloud', 'Oranges')

# Negative reviews (red shades)
generate_wordcloud(negative_reviews, 'Negative Reviews Word Cloud', 'Reds')
