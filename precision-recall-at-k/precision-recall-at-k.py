def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    top_k = recommended[:k]
    hits = len(set(top_k) & set(relevant))
    
    precision = hits / k
    recall = hits / len(relevant)
    
    return [precision, recall]