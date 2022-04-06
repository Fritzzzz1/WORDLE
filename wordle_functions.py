from Constants import *
from Wordle import Wordle
import pygame


def load_word_set(path: str):
    word_set = []
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.append(word)
    return word_set


def determine_unused_letters(attempts):
    guessed_letters = "".join(attempts)
    unused_letters = ""

    for letter in ALPHABET:
        if letter not in guessed_letters:
            unused_letters += letter

    return unused_letters


def draw_guess(attempts, result, window, font):
    render_list = ["", "", "", "", ""]
    spacing = 0

    for x in range(0, 5):
        render_list[x] = font.render(result[x].character, True, BLACK)

        pygame.draw.rect(window, result[x].color,
                         pygame.Rect(60 + spacing, SQUARE_SIZE + (attempts * BLOCK_SIZE),
                                     SQUARE_SIZE, SQUARE_SIZE))

        window.blit(render_list[x], (75 + spacing, 60 + (attempts * BLOCK_SIZE)))
        spacing += BLOCK_SIZE


def draw_board(window):

    for x in range(Wordle.WORD_LENGTH):
        for y in range(Wordle.MAX_ATTEMPTS):
            pygame.draw.rect(window, GREY,
                             pygame.Rect(X_MARGIN + (x * BLOCK_SIZE),
                                         Y_MARGIN + (y * BLOCK_SIZE),
                                         SQUARE_SIZE, SQUARE_SIZE), LINE_THICKNESS)


def apply_color_to_result(result):

    for letter in result:
        if letter.is_in_position:
            letter.color = GREEN

        elif letter.is_in_word:
            letter.color = YELLOW

        else:
            letter.color = GREY


def display_results(wordle: Wordle, window, font):

    for word in wordle.attempts:
        result = wordle.guess(word)
        apply_color_to_result(result)
        draw_guess(len(wordle.attempts) - 1, result, window, font)


def get_fonts():
    normal = pygame.font.SysFont("Halvetica neue", 40)
    big = pygame.font.SysFont("Halvetica neue", 80)
    small = pygame.font.SysFont("free sans bold", 30)

    font_dic = {
        "normal": normal,
        "big": big,
        "small": small
    }
    return font_dic


def get_prompts(fonts, secret):
    you_win = fonts.get("big").render("You Win!", True, GREEN)
    you_lose = fonts.get("big").render("You Lose...", True, RED)
    play_again = fonts.get("big").render("Play Again?", True, ORANGE)
    illegal_word = fonts.get("small").render("Illegal word!", True, RED)
    secret_word = fonts.get("normal").render(secret + "...", True, LIGHT_GREEN)
    all_letters_font = fonts.get("small").render(ALPHABET, False, LIGHT_GREEN)

    prompt_dic = {
        "win": you_win,
        "lose": you_lose,
        "again": play_again,
        "invalid": illegal_word,
        "secret": secret_word,
        "abc": all_letters_font
    }
    return prompt_dic


def get_surface(prompt, string=None, font=None):
    if prompt is None:
        prompt = font.render(string, False, GREY)

    surface = prompt.get_rect(center=(WIDTH / 2, 25))

    return surface
