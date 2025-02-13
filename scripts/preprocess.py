import pandas as pd

def preprocess(data):
    # Load the messages
    df = pd.read_json(data)

    # Basic preprocessing
    df['content'] = df['content'].astype(str)  # Ensure content is string
    df['tokens'] = df['content'].apply(lambda x: x.split())  # Simple tokenization

    # Save the preprocessed data with UTF-8 encoding to preserve Amharic characters
    df.to_csv('preprocessed.csv', index=False, encoding='utf-8-sig')

    print("Preprocessed data saved to preprocessed.csv")