"""Restaurant rating lister."""

scores = {}

def process_scores():
    """Read scores file and return dictionary of {restaurant-name: score}."""

    scores_txt = open('scores.txt')

    for line in scores_txt:
        line = line.rstrip()
        restaurant, score = line.split(":")
        scores[restaurant] = int(score)
    return scores


def add_score():
    """Adds user entry to scores dictionary."""
    user_restaurant = input("Enter restaurant: ")
    user_score = input("Enter score: ")

    # add new input to dictionary
    return scores[user_restaurant] = user_score


def print_sorted_scores(scores):
    """Prints sorted restaurant scores."""
    # sort dictionary
    # use .items and unpack to variables
    for restaurant, score in sorted(scores.items()):
        print(f"{restaurant} is rated at {score}")



scores = process_scores()

print_sorted_scores(scores)