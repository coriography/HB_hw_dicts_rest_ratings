"""Restaurant rating lister."""

def process_scores():
    """Read scores file and return dictionary of {restaurant-name: score}."""

    scores_txt = open('scores.txt')

    scores = {}

    for line in scores_txt:
        line = line.rstrip()
        restaurant, score = line.split(":")
        scores[restaurant] = int(score)
    return scores


def print_sorted_scores(scores):
    """Prints sorted restaurant scores."""
    # sort dictionary
    # use .items and unpack to variables
    for restaurant, score in scores.items():
        print(f"{restaurant} is rated at {score}")
    

scores = process_scores()

print_sorted_scores(scores)