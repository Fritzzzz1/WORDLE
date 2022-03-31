import time

from wordle_functions import *


def run_game():
    pygame.init()

    word_set = load_word_set("Data/full_wordlist.txt")
    secret = random.choice(word_set)
    fonts = get_fonts()
    prompts = get_prompts(fonts, secret)

    wordle = Wordle(secret)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Wordle!")

    window = pygame.display.set_mode((width, height))
    window.fill(black)
    draw_board(window)

    guess = ""
    unused_letters = ALPHABET

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                guess += event.unicode.upper()

                if event.key == K_BACKSPACE:
                    guess = guess[:-2]

                if len(guess) > 5:
                    guess = guess[:-1]

                if event.key == K_RETURN and (wordle.is_solved or len(wordle.attempts) >= 6):
                    run_game()

                if event.key == K_RETURN and len(guess) > 4:
                    if guess.upper() not in word_set:
                        window.blit(prompts.get("invalid"), WINDOW_BOTTOM_RIGHT)
                        pygame.display.update()
                        time.sleep(1)
                        continue

                    wordle.attempt(guess)
                    unused_letters = determine_unused_letters(wordle.attempts)
                    display_results(wordle, window, fonts.get("normal"))
                    guess = ""

        prompts["unused"] = fonts.get("small").render(unused_letters, False, light_green)
        prompts["guess"] = fonts.get("normal").render(guess, True, grey)
        all_letters_surface = get_surface(prompts.get("abc"))
        unused_letters_surface = get_surface(prompts.get("unused"))

        window.fill(black, WINDOW_BOTTOM)
        window.fill(black, all_letters_surface)

        window.blit(prompts.get("unused"), unused_letters_surface)
        window.blit(prompts["guess"], WINDOW_TYPE_LOCATION)

        if wordle.is_solved:
            window.blit(prompts.get("win"), WINDOW_ENDGAME_PROMPT)
            window.blit(prompts.get("again"), WINDOW_AGAIN_PROMPT)

        if len(wordle.attempts) == 6 and not wordle.is_solved:
            window.blit(prompts.get("lose"), WINDOW_ENDGAME_PROMPT)
            window.blit(prompts.get("again"), WINDOW_AGAIN_PROMPT)
            window.blit(prompts.get("secret"), WINDOW_BOTTOM_RIGHT)

        pygame.display.update()
        clock.tick(fps)
