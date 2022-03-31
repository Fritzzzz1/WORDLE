from Header import *


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
            unused_letters = unused_letters + letter
    return unused_letters


def convert_result_to_color(result: List[LetterState]):
    guess_color_code = [grey, grey, grey, grey, grey]
    i = 0

    for letter in result:
        if letter.is_in_position:
            guess_color_code[i] = green

        elif letter.is_in_word:
            guess_color_code[i] = yellow
        i += 1

    return guess_color_code


def draw_guess(attempts, word, guess_color_code, window, font):
    render_list = ["", "", "", "", ""]
    spacing = 0

    for x in range(0, 5):
        render_list[x] = font.render(word[x], True, black)
        pygame.draw.rect(window, guess_color_code[x], pygame.Rect(60 + spacing, 50 + (attempts * 80), 50, 50))
        window.blit(render_list[x], (75 + spacing, 60 + (attempts * 80)))
        spacing += 80


def display_results(wordle: Wordle, window, font):
    result = []
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        draw_guess(len(wordle.attempts) - 1, word, colored_result_str, window, font)



