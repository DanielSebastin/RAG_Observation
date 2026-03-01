def noise_ratio(results,relevant_keywords):
    irrelevant=0
    for r in results:
        if not any(keyword.lower() in r["text"].lower() for keyword in relevant_keywords):
            irrelevant+=1
    return irrelevant/len(results)