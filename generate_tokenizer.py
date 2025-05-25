import json

# Create a small vocabulary with common words and hate speech-related terms
sample_words = [
    '<oov>', 'i', 'you', 'love', 'hate', 'kill', 'die', 'what', 'a', 'dog',
    'whore', 'stupid', 'good', 'bad', 'nice', 'really', 'wanna', 'just', 'the', 'is'
]
word_index = {word: idx + 1 for idx, word in enumerate(sample_words)}

# Save to hate_comment_detection.json
with open('hate_comment_detection.json', 'w') as f:
    json.dump(word_index, f)
print("hate_comment_detection.json generated successfully!")