def precision_at_k(results,relevant_keywords):
    hits=0
    for r in results:
        if any(keyword.lower() in r["text"].lower() for keyword in relevant_keywords):
            hits+=1
    return hits/len(results)