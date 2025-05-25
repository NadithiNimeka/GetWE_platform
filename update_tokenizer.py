import json

# Expanded vocabulary with more common and hate speech-related words
sample_words = [
    '<oov>', 'i', 'you', 'love', 'hate', 'kill', 'die', 'what', 'a', 'dog',
    'whore', 'stupid', 'good', 'bad', 'nice', 'really', 'wanna', 'just', 'the', 'is',
    'fuck', 'shit', 'bitch', 'asshole', 'damn', 'hell', 'idiot', 'faggot', 'nigger', 'slut',
    'cunt', 'bastard', 'dick', 'pussy', 'retard', 'trash', 'worthless', 'ugly', 'fat', 'loser',
    'happy', 'great', 'awesome', 'friend', 'beautiful', 'kind', 'amazing', 'wonderful', 'cool', 'best',
    'to', 'and', 'for', 'in', 'on', 'with', 'this', 'that', 'are', 'be',
    'app', 'like', 'share', 'thanks', 'today', 'new', 'project', 'work', 'team', 'support',
    'online', 'community', 'safe', 'safer', 'social', 'media', 'detection', 'speech', 'digital', 'ethics',
    'excited', 'looking', 'forward', 'conference', 'features', 'keep', 'up', 'insightful', 'important', 'awareness',
    'damn', 'fucking', 'ass', 'kys', 'moron', 'dumb', 'freak', 'pig', 'scum', 'homo',
    'we', 'all', 'have', 'so', 'it', 'my', 'me', 'your', 'they', 'will',
    'not', 'but', 'if', 'when', 'how', 'why', 'here', 'there', 'now', 'then'
]
word_index = {word: idx + 1 for idx, word in enumerate(sample_words)}

# Save to file
with open('hate_comment_detection.json', 'w') as f:
    json.dump(word_index, f)
print("hate_comment_detection.json updated successfully!")