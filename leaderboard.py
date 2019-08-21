import pygame as pg
from text import *


# modified insertion sort to sort data of the format of the leaderboard data
def insertion_sort(list):
    for index in range(1, len(list)):
        value = list[index]
        i = index - 1
        while i >= 0:
            if int(value[1]) > int(list[i][1]):
                list[i+1] = list[i]
                list[i] = value
                i -= 1
            else:
                break
    return list


# function that sorts and ranks data to make it suitable for the leaderboard
def sorting_and_ranking(leaderboard_unranked):
    for counter in range(len(leaderboard_unranked) - 1):
        leaderboard_unranked[counter][1] = int(leaderboard_unranked[counter][1])
    sorted_leaderboard = insertion_sort(leaderboard_unranked)


    names_sorted = []
    scores_sorted = []

    for i in range(0, len(sorted_leaderboard)):
        names_sorted.append(sorted_leaderboard[i][0])
    for i in range(0, len(sorted_leaderboard)):
        scores_sorted.append(sorted_leaderboard[i][1])

    ranks = []

    for i in range(1, len(names_sorted) + 1):
        ranks.append(i)

    ranked_leaderboard = [ranks, names_sorted, scores_sorted]

    return ranked_leaderboard


# writing the leaderboard data to the 'leaderboard.txt' file
def write_leaderboard_to_file(ranked_leaderboard):
    with open('leaderboard.txt', 'w') as file:
        for counter in range(len(ranked_leaderboard[0])):
            file.write(str(ranked_leaderboard[0][counter]) + ", ")
            file.write(str(ranked_leaderboard[1][counter]) + ", ")
            file.write(str(ranked_leaderboard[2][counter]) + "\n")


# displaying the leaderboard on the screen
def display_leaderboard(ranked_leaderboard, display, high_score_text):
    pg.draw.rect(display, black, (250, 230, 760, 420))
    display.blit(rank_text, [280, 230])
    display.blit(name_text, [540, 230])
    display.blit(score_text, [850, 230])
    display.blit(high_score_text, [500, 175])

    if len(ranked_leaderboard[0]) == 1:
        rank = leaderboard_text.render(str(ranked_leaderboard[0][0]), True, white)
        name = leaderboard_text.render(str(ranked_leaderboard[1][0]), True, white)
        score = leaderboard_text.render(str(ranked_leaderboard[2][0]), True, white)
        display.blit(rank, [display_width * 0.25, 280])
        display.blit(name, [display_width * 0.41, 280])
        display.blit(score, [display_width * 0.68, 280])

        pg.display.update()

    elif len(ranked_leaderboard[0]) < 10:
        for counter in range(len(ranked_leaderboard[0])):
            rank = leaderboard_text.render(str(ranked_leaderboard[0][counter]), True, white)
            name = leaderboard_text.render(str(ranked_leaderboard[1][counter]), True, white)
            score = leaderboard_text.render(str(ranked_leaderboard[2][counter]), True, white)
            display.blit(rank, [display_width * 0.25, 280 + (counter * 35)])
            display.blit(name, [display_width * 0.41, 280 + (counter * 35)])
            display.blit(score, [display_width * 0.68, 280 + (counter * 35)])
            pg.display.update()

    else:
        for counter in range(10):
            rank = leaderboard_text.render(str(ranked_leaderboard[0][counter]), True, white)
            name = leaderboard_text.render(str(ranked_leaderboard[1][counter]), True, white)
            score = leaderboard_text.render(str(ranked_leaderboard[2][counter]), True, white)
            display.blit(rank, [display_width * 0.25, 280 + (counter * 35)])
            display.blit(name, [display_width * 0.41, 280 + (counter * 35)])
            display.blit(score, [display_width * 0.68, 280 + (counter * 35)])
            pg.display.update()

# array of the scores for one player
scores = []

# saving the scores of the current play session
def save_score(score):
    global scores
    scores.append(score)

# finding the high score from a play session
def find_high_score(scores):
    high_score = 0
    for i in range(len(scores)):
        if scores[i] > high_score:
            high_score = scores[i]
    return high_score


