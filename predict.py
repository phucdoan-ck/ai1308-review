THRESHOLD = 0.5


def predict(scores):
    if not scores:
        return "unknown"
    best_label = max(scores, key=scores.get)
    if scores[best_label] < THRESHOLD:
        return "unknown"
    return best_label
