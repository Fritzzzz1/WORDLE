from wordle_functions import *

pygame.init()

font = pygame.font.SysFont("Halvetica neue", 40)
font_big = pygame.font.SysFont("Halvetica neue", 80)
font_small = pygame.font.SysFont("free sans bold", 30)
word_set = load_word_set("Data/full_wordlist.txt")
secret = random.choice(word_set)

you_win = font_big.render("You Win!", True, light_green)
you_lose = font_big.render("You Lose...", True, red)
play_again = font_big.render("Play Again?", True, blue)
right_answer = font_big.render(secret + "...", True, light_green)

height = 600
width = 500
fps = 30

all_letters_font = font_small.render(ALPHABET, False, light_green)
surface_of_all_letters = all_letters_font.get_rect(center=(width / 2, 25))


def run_game():
    #edit out
    print(secret)

    wordle = Wordle(secret)
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((width, height))

    window.fill(black)

    for x in range(Wordle.WORD_LENGTH):
        for y in range(Wordle.MAX_ATTEMPTS):
            pygame.draw.rect(window, grey, pygame.Rect(60 + (x * 80), 50 + (y * 80), 50, 50), 2)

    pygame.display.set_caption("Wordle!")

    unused_letters = ALPHABET
    guess = ""

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                guess += event.unicode.upper()
                if event.key == pygame.K_BACKSPACE:
                    guess = guess[:-2]

                if len(guess) > 5:
                    guess = guess[:-1]

                if event.key == K_RETURN and wordle.is_solved:
                    run_game()

                if event.key == K_RETURN and len(wordle.attempts) == 6:
                    run_game()

                if event.key == K_RETURN and len(guess) > 4:
                    if guess.upper() not in word_set:
                        print("Word is not in list of valid words.")
                        continue

                    wordle.attempt(guess)
                    unused_letters = determine_unused_letters(wordle.attempts)
                    display_results(wordle, window, font)
                    guess = ""

        window.fill(black, (0, 500, 500, 200))
        window.fill(black, surface_of_all_letters)

        unused_letters_font = font_small.render(unused_letters, False, light_green)
        surface_of_unused_letters = unused_letters_font.get_rect(center=(width / 2, 25))
        render_guess = font.render(guess, True, grey)

        window.blit(unused_letters_font, surface_of_unused_letters)
        window.blit(render_guess, (180, 530))

        if wordle.is_solved:
            window.blit(you_win, (108, 168))
            window.blit(play_again, (75, 328))

        if len(wordle.attempts) == 6 and not wordle.is_solved:
            window.blit(you_lose, (108, 168))
            window.blit(play_again, (75, 328))
            window.blit(right_answer, (135, 520))

        pygame.display.update()
        clock.tick(fps)








