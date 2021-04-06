import pygame
# import math

from fonts import all_fonts
from Button import Button
from InputBox2 import InputBox

# setup display
pygame.init()
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
window = pygame.display.set_mode((WIDTH, HEIGHT - 64))
pygame.display.set_caption("Quiz format")

# fonts
LETTER_FONT = pygame.font.SysFont('', 40)
WORD_FONT = pygame.font.SysFont(all_fonts[6], 60)
TITLE_FONT = pygame.font.SysFont(all_fonts[5], 80)
TINY_FONT = pygame.font.SysFont(all_fonts[6], 20)

# load questions
questions = []

# while loop variables
play = True
state = 1

# Some helpful constants
FPS = 60
SEC = 1000

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
LIGHT_BLUE = (176, 217, 235)

# buttons
MARGIN = 12
MARGIN_double = 2 * MARGIN
buttons = []

# design quiz
quiz_button = WORD_FONT.render("Design Quiz", True, BLACK)
quiz_button_w = quiz_button.get_width()
quiz_button_h = quiz_button.get_height()
x_quiz_rect = (WIDTH - quiz_button_w) / 2 - MARGIN
y_quiz_rect = (HEIGHT - 4 * quiz_button_h) / 2 - MARGIN
w_quiz_rect = (quiz_button_w+MARGIN_double)
h_quiz_rect = (quiz_button_h+MARGIN_double)
design_button = Button(BLACK, False, 0, x_quiz_rect, y_quiz_rect, w_quiz_rect, h_quiz_rect, 'Design Quiz', 'design')

# online quiz
online_button = Button(BLACK, False, 0,
                       x_quiz_rect, y_quiz_rect+quiz_button_h+2*MARGIN_double,
                       w_quiz_rect, h_quiz_rect, 'Online Quiz', 'online')
buttons.append(design_button)
buttons.append(online_button)

# login button
login_text = WORD_FONT.render("Login", True, BLACK)
login_w = login_text.get_width()
login_h = login_text.get_height()
login_button = Button(BLACK, False, 0,
                      WIDTH-login_w-2*MARGIN_double, login_h+MARGIN, login_w, login_h, 'Login', 'login')
buttons.append(login_button)

# go back button
back_button = Button(BLACK, True, 30, MARGIN_double, MARGIN_double, 40, 40, '<')
buttons.append(back_button)

# login inputs
inputs_login = []
name = InputBox(2*WIDTH/5+MARGIN_double, HEIGHT/4, WIDTH/2, MARGIN, True, '', 'First Name   ')
inputs_login.append(name)
last_name = InputBox(2*WIDTH/5+MARGIN_double, HEIGHT/4+3*MARGIN_double, WIDTH/2, MARGIN, True, '', 'Last Name   ')
inputs_login.append(last_name)
email = InputBox(2*WIDTH/5+MARGIN_double, HEIGHT/4+6*MARGIN_double, WIDTH/2, MARGIN, True, '', 'E-mail   ')
inputs_login.append(email)


def draw_title(text):
    text = TITLE_FONT.render(text, True, BLACK)
    text_w = text.get_width()
    window.blit(text, (WIDTH / 2 - text_w / 2, 60))


def delay(time):
    pygame.time.delay(time)
    pygame.display.update()


def display_message(message, message2, second):
    # blur the menu
    blur = pygame.Surface((WIDTH, HEIGHT))
    blur.set_alpha(10)
    blur.fill(WHITE)
    window.blit(blur, (0, 0))
    # create message
    text = WORD_FONT.render(message, True, BLACK)
    text_w = text.get_width()
    text_h = text.get_height()
    new_margin = 3*MARGIN_double
    pygame.draw.rect(window, LIGHT_BLUE, ((WIDTH-text_w-new_margin)/2,
                                          (HEIGHT-text_h-new_margin)/2, text_w+new_margin, text_h+new_margin), 0)
    pygame.draw.rect(window, BLACK, ((WIDTH-text_w-new_margin)/2,
                                     (HEIGHT-text_h-new_margin)/2, text_w+new_margin, text_h+new_margin), 3)
    window.blit(text, ((WIDTH-text_w)/2, (HEIGHT-text_h)/2))

    # exit button
    if message == "Do you want to exit?":
        make_exit = True
        for button in buttons:
            if button.get_name() == 'exit':
                make_exit = False
        if make_exit:
            exit_button = Button(BLACK, False, 0,
                                 (WIDTH-text_w-new_margin)/2,
                                 (HEIGHT-text_h-new_margin)/2, text_w+new_margin, text_h+new_margin, message, 'exit')
            buttons.append(exit_button)
    # optional extra message
    if second:
        text2 = TINY_FONT.render(message2, True, BLACK)
        text2_w = text2.get_width()
        # text2_h = text2.get_height()
        window.blit(text2, ((WIDTH-text2_w)/2, (HEIGHT+text_h)/2))
    # update display
    pygame.display.update()


def draw_menu():
    # background
    window.fill(WHITE)

    # title
    draw_title("Quiz Maker")

    # buttons
    # - design quiz
    for button in buttons:
        if button.get_name() != 'exit':
            if button.is_over(pygame.mouse.get_pos()):
                button.draw(window, True)
            else:
                button.draw(window, False)

    # - online quiz

    # update the display!
    pygame.display.update()


def draw_design():
    window.fill(WHITE)
    draw_title("Design Quiz")
    if back_button.is_over(pygame.mouse.get_pos()):
        back_button.draw(window, True)
    else:
        back_button.draw(window, False)
    pygame.display.update()


def draw_quiz():
    window.fill(WHITE)
    draw_title("Quiz by Liam")
    if back_button.is_over(pygame.mouse.get_pos()):
        back_button.draw(window, True)
    else:
        back_button.draw(window, False)
    pygame.display.update()


def draw_login():
    window.fill(WHITE)
    draw_title("Login")
    if back_button.is_over(pygame.mouse.get_pos()):
        back_button.draw(window, True)
    else:
        back_button.draw(window, False)
    for box in inputs_login:
        box.draw(window)
    pygame.display.update()


def save_data():
    with open('Login.txt', 'w') as f:
        f.write("1")
        f.write("\n")
        for box in inputs_login:
            f.write(box.get_text())
            f.write('\n')
    f.close()

# 1 = menu
# 2 = design quiz
# 3 = online quiz
# 4 = login
# 5 = quit


def main():
    global state
    global play
    while play:
        main_clock = pygame.time.Clock()
        while state == 1 and play:
            main_clock.tick(FPS)
            draw_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()
                    if design_button.is_over((m_x, m_y)):
                        state = 2
                    elif online_button.is_over((m_x, m_y)):
                        state = 3
                    elif login_button.is_over((m_x, m_y)):
                        state = 4
                    elif back_button.is_over((m_x, m_y)):
                        state = 5
        while state == 2 and play:
            main_clock.tick(FPS)
            draw_design()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()
                    if back_button.is_over((m_x, m_y)):
                        state = 1

        while state == 3 and play:
            main_clock.tick(FPS)
            draw_quiz()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()
                    if back_button.is_over((m_x, m_y)):
                        state = 1

        while state == 4 and play:
            main_clock.tick(FPS)

            for event in pygame.event.get():
                for box in inputs_login:
                    box.handle_event(event)
                if event.type == pygame.QUIT:
                    play = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()
                    if back_button.is_over((m_x, m_y)):
                        state = 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_TAB:
                        count = 0
                        for box in inputs_login:
                            if box.get_active():
                                box.toggle_active()
                                index_box = inputs_login.index(box)
                                inputs_login[(index_box+1)%(len(inputs_login))].toggle_active()
                                break
                            else:
                                count += 1
                        if count >= len(inputs_login):
                            inputs_login[0].toggle_active()
                draw_login()
            for box in inputs_login:
                box.update()

        while state == 5 and play:
            main_clock.tick(FPS)
            display_message("Do you want to exit?", "Click inside to exit, outside to stay.", True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()
                    for button in buttons:
                        if button.get_name() == 'exit':
                            if button.is_over((m_x, m_y)):
                                play = False
                            else:
                                state = 1
    save_data()


if __name__ == '__main__':
    main()

pygame.quit()
