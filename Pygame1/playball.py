import pygame
import random

pygame.init()

width, height = 600, 700
screen = pygame.display.set_mode((width, height))

r = 10
panel_height = 15
panel_width = 150
panel_color = (75, 0, 130)
ball_color = (147, 112, 219)
panel_y_offset = 10
panel_x = (width - panel_width) // 2
panel_y = height - panel_height - panel_y_offset

block_width = 50  
block_height = 15  
block_rows = 8  
block_cols = 10  
block_margin = 5
block_color = panel_color
total_block_width = block_cols * block_width + (block_cols - 1) * block_margin
block_x_offset = (width - total_block_width) // 2
block_y_offset = 50

clock = pygame.time.Clock()

initial_ball_x, initial_ball_y = 300, 300
initial_ball_x_speed, initial_ball_y_speed = 6, 4
ball_x, ball_y = initial_ball_x, initial_ball_y
ball_x_speed, ball_y_speed = initial_ball_x_speed, initial_ball_y_speed

blocks = []
game_started = False
lives = 3

# Зеленый бонус - увеличение панели
green_bonus_active = False
green_bonus_width = 20
green_bonus_height = 20
green_bonus_x = random.randint(0, width - green_bonus_width)
green_bonus_y = 0
green_bonus_color = (0, 255, 0)
green_bonus_speed = 2

# синий бонус - уменьшение скорости шарика
blue_bonus_active = False
blue_bonus_x = random.randint(0, width - green_bonus_width)
blue_bonus_y = 0
blue_bonus_color = (0, 0, 255)
blue_bonus_speed = 2

panel_wide_mode = False
panel_wide_duration = 900
panel_wide_counter = 0

ball_slowed_down = False
ball_slow_duration = 900
ball_slow_counter = 0

red_bonus_active = False
red_bonus_x = random.randint(0, width - green_bonus_width)
red_bonus_y = 0
red_bonus_color = (255, 0, 0)
red_bonus_speed = 2

panel_narrow_mode = False
panel_narrow_duration = 1200 
panel_narrow_counter = 0

# бонус дополнительный шарик
ball_bonus_active = False
ball_bonus_x = random.randint(0, width - green_bonus_width)
ball_bonus_y = 0
ball_bonus_color = (255, 165, 0)  
ball_bonus_speed = 2

extra_ball_active = False
extra_ball_x = initial_ball_x
extra_ball_y = initial_ball_y
extra_ball_x_speed = initial_ball_x_speed
extra_ball_y_speed = initial_ball_y_speed

def create_blocks():
    for row in range(block_rows):
        for col in range(block_cols):
            block_x = block_x_offset + col * (block_width + block_margin)
            block_y = block_y_offset + row * (block_height + block_margin)
            block_rect = pygame.Rect(block_x, block_y, block_width, block_height)
            blocks.append(block_rect)

def update_ball(x, y, x_speed, y_speed):
    x += x_speed
    y += y_speed
    if x - r < 0 or x + r > width:
        x_speed = -x_speed
    if y - r < 0:
        y_speed = -y_speed
    if panel_x < x < panel_x + panel_width and y + r >= panel_y and y_speed > 0:
        y_speed = -y_speed
    for block in blocks[:]:
        if block.colliderect(pygame.Rect(x - r, y - r, r * 2, r * 2)):
            blocks.remove(block)
            global green_bonus_active, green_bonus_x, green_bonus_y, red_bonus_active, red_bonus_x, red_bonus_y, blue_bonus_active, blue_bonus_x, blue_bonus_y, ball_bonus_active, ball_bonus_x, ball_bonus_y
            if random.random() < 0.3 and (not green_bonus_active) and (not red_bonus_active) and (not blue_bonus_active) and (not ball_bonus_active):
                bonus_type = random.random()
                if bonus_type < 0.25:
                    green_bonus_active = True
                    green_bonus_x = random.randint(0, width - green_bonus_width)
                    green_bonus_y = 0
                elif bonus_type < 0.5:
                    blue_bonus_active = True  
                    blue_bonus_x = random.randint(0, width - green_bonus_width)
                    blue_bonus_y = 0
                elif bonus_type < 0.75:
                    red_bonus_active = True  
                    red_bonus_x = random.randint(0, width - green_bonus_width)
                    red_bonus_y = 0
                else:  
                    ball_bonus_active = True  
                    ball_bonus_x = random.randint(0, width - green_bonus_width)
                    ball_bonus_y = 0
            if abs(block.top - (y + r)) < 10 or abs(block.bottom - (y - r)) < 10:
                y_speed = -y_speed
            else:
                x_speed = -x_speed
            break
    return x, y, x_speed, y_speed

def draw_blocks():
    for block in blocks:
        pygame.draw.rect(screen, block_color, block)


done = True
create_blocks()

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            if lives == 0:
                lives = 3
            game_started = True
            ball_x, ball_y = initial_ball_x, initial_ball_y
            ball_x_speed, ball_y_speed = initial_ball_x_speed, initial_ball_y_speed
            blocks.clear()
            create_blocks()

    if game_started:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and panel_x > 0:
            panel_x -= 10
        if keys[pygame.K_RIGHT] and panel_x < width - panel_width:
            panel_x += 10

        ball_x, ball_y, ball_x_speed, ball_y_speed = update_ball(ball_x, ball_y, ball_x_speed, ball_y_speed)

        # зеленый бонус
        if green_bonus_active:
            green_bonus_y += green_bonus_speed
            if (panel_x < green_bonus_x + green_bonus_width and 
                panel_x + panel_width > green_bonus_x and 
                panel_y < green_bonus_y + green_bonus_height and 
                panel_y + panel_height > green_bonus_y):
                panel_width = int(panel_width * 1.2)
                panel_wide_mode = True
                panel_wide_counter = 0
                green_bonus_active = False
            if green_bonus_y > height:
                green_bonus_active = False

        # Синий бонус
        if blue_bonus_active:
            blue_bonus_y += blue_bonus_speed
            if (panel_x < blue_bonus_x + green_bonus_width and 
                panel_x + panel_width > blue_bonus_x and 
                panel_y < blue_bonus_y + green_bonus_height and 
                panel_y + panel_height > blue_bonus_y):
                ball_x_speed /= 1.5
                ball_y_speed /= 1.5
                ball_slowed_down = True
                ball_slow_counter = 0
                blue_bonus_active = False
            if blue_bonus_y > height:
                blue_bonus_active = False

        # Красный бонус
        if red_bonus_active:
            red_bonus_y += red_bonus_speed
            if (panel_x < red_bonus_x + green_bonus_width and 
                panel_x + panel_width > red_bonus_x and 
                panel_y < red_bonus_y + green_bonus_height and 
                panel_y + panel_height > red_bonus_y):
                panel_width /= 2
                panel_narrow_mode = True
                panel_narrow_counter = 0
                red_bonus_active = False
            if red_bonus_y > height:
                red_bonus_active = False

        if ball_bonus_active:
            ball_bonus_y += ball_bonus_speed
            if (panel_x < ball_bonus_x + green_bonus_width and 
                panel_x + panel_width > ball_bonus_x and 
                panel_y < ball_bonus_y + green_bonus_height and 
                panel_y + panel_height > ball_bonus_y):
                
                extra_ball_x = initial_ball_y  
                extra_ball_y = initial_ball_x
                extra_ball_x_speed = initial_ball_x_speed
                extra_ball_y_speed = initial_ball_y_speed
                extra_ball_active = True
                ball_bonus_active = False 

            if ball_bonus_y > height:
                ball_bonus_active = False

        if extra_ball_active:
            extra_ball_x, extra_ball_y, extra_ball_x_speed, extra_ball_y_speed = update_ball(extra_ball_x, extra_ball_y, extra_ball_x_speed, extra_ball_y_speed)
            if extra_ball_y - r > height:
                extra_ball_active = False  

        # Время
        if panel_wide_mode:
            panel_wide_counter += 1
            if panel_wide_counter >= panel_wide_duration:
                panel_width = int(panel_width / 1.2)
                panel_wide_mode = False

        if ball_slowed_down:
            ball_slow_counter += 1
            if ball_slow_counter >= ball_slow_duration:
                ball_x_speed *= 1.5
                ball_y_speed *= 1.5
                ball_slowed_down = False

        if panel_narrow_mode:
            panel_narrow_counter += 1
            if panel_narrow_counter >= panel_narrow_duration:
                panel_width *= 2
                panel_narrow_mode = False


        if ball_y + r > height:
            lives -= 1
            if lives > 0:
                ball_x, ball_y = initial_ball_x, initial_ball_y
                ball_x_speed, ball_y_speed = initial_ball_x_speed + 1, initial_ball_y_speed + 1
            else:
                game_started = False
                ball_x, ball_y = initial_ball_x, initial_ball_y
                ball_x_speed, ball_y_speed = initial_ball_x_speed, initial_ball_y_speed
                blocks.clear()
                create_blocks()

        if not blocks and game_started:
            
            font = pygame.font.Font(None, 36)  
            message_text = font.render("Красава!", True, (0, 0, 0))  
            text_rect = message_text.get_rect(center=(width // 2, height // 2))  
            screen.blit(message_text, text_rect)  
            pygame.display.flip()  
            pygame.time.wait(2000)  
            game_started = False  

    screen.fill((230, 230, 250))
    draw_blocks()
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), r)
    pygame.draw.rect(screen, panel_color, (panel_x, panel_y, panel_width, panel_height))

    if green_bonus_active:
        pygame.draw.rect(screen, green_bonus_color, (green_bonus_x, green_bonus_y, green_bonus_width, green_bonus_height))

    if blue_bonus_active:
        pygame.draw.rect(screen, blue_bonus_color, (blue_bonus_x, blue_bonus_y, green_bonus_width, green_bonus_height))

    if red_bonus_active:
        pygame.draw.rect(screen, red_bonus_color, (red_bonus_x, red_bonus_y, green_bonus_width, green_bonus_height))

    if ball_bonus_active:
        pygame.draw.rect(screen, ball_bonus_color, (ball_bonus_x, ball_bonus_y, green_bonus_width, green_bonus_height))

    if extra_ball_active:
        pygame.draw.circle(screen, ball_bonus_color, (extra_ball_x, extra_ball_y), r)


    font = pygame.font.Font(None, 36)
    lives_text = font.render(f'Жизни: {lives}', True, (0, 0, 0))
    screen.blit(lives_text, (10, 10))

    if lives == 0 and not game_started:  
        font = pygame.font.Font(None, 36)  
        message_text = font.render("Не повезло, не фортануло", True, (0, 0, 0))  
        text_rect = message_text.get_rect(center=(width // 2, height // 2))  
        screen.blit(message_text, text_rect)  
        pygame.display.flip()  
        pygame.time.wait(2000)  
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
