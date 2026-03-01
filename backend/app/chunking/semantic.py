import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt")

def semantic_chunk(text,max_chunk_size=500):
    sentences=sent_tokenize(text)
    chunks=[]
    current_chunk=""

    for sentence in sentences:
        if len(current_chunk)+len(sentence)<=max_chunk_size:
            current_chunk+=sentence+" "
        else:
            chunks.append(current_chunk.strip())
            current_chunk=sentence+" "

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks