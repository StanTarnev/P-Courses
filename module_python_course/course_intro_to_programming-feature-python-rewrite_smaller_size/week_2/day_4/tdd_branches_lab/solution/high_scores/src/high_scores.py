def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def highest_to_lowest(scores):
    scores.sort(reverse = True)
    return scores


def personal_top_three(scores):
    sorted_scores = highest_to_lowest(scores)
    count = 3
    
    if len(scores) < 3:
        count = len(scores)
    
    return sorted_scores[0:count]
