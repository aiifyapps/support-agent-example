from typing import List
import ollama

def getEmbedding(words: str) -> List:
    embedding = ollama.embed(
        model='all-minilm',
        input=words
    )
    
    return embedding.embeddings[0]