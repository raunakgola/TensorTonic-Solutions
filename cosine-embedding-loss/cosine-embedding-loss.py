def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    dot_product = sum(a*b for a, b in zip(x1, x2))
    norm_x1 = math.sqrt(sum(a*a for a in x1))
    norm_x2 = math.sqrt(sum(a*a for a in x2))
    
    cos_sim = dot_product / (norm_x1 * norm_x2)
    
    if label == 1:
        return 1 - cos_sim
    else:
        return max(0, cos_sim - margin)