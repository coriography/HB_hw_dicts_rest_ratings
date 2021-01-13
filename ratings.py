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



# # sort dictionary by key
# dict_ratings = sorted(scores)
# # loop through keys again to print?
# for rating in scores:
#     # print variables in f-string
#         # output example: Big Bean Shack is rated at 3.
#     print(f"{rating} is rated at {rating}")
