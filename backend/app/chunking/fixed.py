def fixed_chunk(text,chunk_size=500,overlap=100):
    chunks=[]
    start=0
    step=chunk_size-overlap

    while start<len(text):
        end=start+chunk_size
        chunk=text[start:end]
        chunks.append(chunk)
        start+=step

    return chunks