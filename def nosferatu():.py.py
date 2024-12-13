import pandas as pd
from rapidfuzz import fuzz, process

def find_similar_words(input,target,output):
    
    df = pd.read_excel(input)
    
    words = df['UNAIDED RECALL'].dropna().astype(str).tolist()
    flattened_words = []
    for word in words:
        flattened_words.extend(word.split())
    
    similar_words = [
        word for word, score, _ in process.extract(
            target_word, flattened_words, scorer=fuzz.ratio, limit=None
        ) if score > 50
    ]
    
    similar_words_df = pd.DataFrame(similar_words, columns=['Similar Words'])
    
    similar_words_df.to_excel(output, index=False)
