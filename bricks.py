# 0 = free_space
# 1 = brick_unstable
# 2 = brick_stable
# 3 = dead_space
# 4 = ball
#images-----------------------------------------------------------------
b = b'\x00' * 3                                                         #black color
w = b'\xc0' * 3                                                         #white color
re = b'\xff' + b'\x33' * 2                                              #red color
bl = b'\x33' * 2 + b'\xff'                                              #blue color
gr = b'\x33' + b'\xff' + b'\x33'                                        #green color

b0 = (                                                                  #brick unstable
b + b + b + b + b + b + b + b + b + b + b + b + b + b + b +
b + b + b + b + b + b + b + b + b + b + b + b + b + b + b +
b + b + w + b + b + b + b + b + b + b + b + b + b + b + b +
b + b + w + w + b + b + b + b + b + b + b + b + b + b + b +
b + b + w + w + b + b + b + b + b + b + b + b + b + b + b +
b + b + w + w + b + b + b + b + b + b + b + b + b + b + b +
b + b + w + w + b + b + b + b + b + b + b + b + b + b + b +
b + b + w + w + b + b + b + b + b + b + b + b + b + b + b +
b + b + w + w + b + b + b + b + b + b + b + b + b + b + b +
b + b + w + w + b + b + b + b + b + b + b + b + b + b + b +
b + b + w + w + b + b + b + b + b + b + b + b + b + b + b +
b + b + w + w + w + w + w + w + w + w + w + w + b + b + b +
b + b + w + w + w + w + w + w + w + w + w + w + w + b + b +
b + b + b + b + b + b + b + b + b + b + b + b + b + b + b +
b + b + b + b + b + b + b + b + b + b + b + b + b + b + b)

b1 = (                                                                  #brick stable
b + b + b + b + b + b + b + b + b + b + b + b + b + b + b +
b + b + b + b + b + b + b + b + b + b + b + b + b + b + b +
b + b + w + w + w + w + w + w + w + w + w + w + w + b + b +
b + b + b + w + w + w + w + w + w + w + w + w + w + b + b +
b + b + b + b + w + w + w + w + w + w + w + w + w + b + b +
b + b + b + b + w + w + w + w + w + w + w + w + w + b + b +
b + b + b + b + w + w + w + w + w + w + w + w + w + b + b +
b + b + b + b + w + w + w + w + w + w + w + w + w + b + b +
b + b + b + b + w + w + w + w + w + w + w + w + w + b + b +
b + b + b + b + w + w + w + w + w + w + w + w + w + b + b +
b + b + b + b + w + w + w + w + w + w + w + w + w + b + b +
b + b + b + b + b + b + b + b + b + b + b + w + w + b + b +
b + b + b + b + b + b + b + b + b + b + b + b + w + b + b +
b + b + b + b + b + b + b + b + b + b + b + b + b + b + b +
b + b + b + b + b + b + b + b + b + b + b + b + b + b + b)

c0 = (                                                                  #cursor_0
w + w + w + w + w + w + w + w + w + w + w + w + w + w + w +
w + w + w + w + w + w + w + w + w + w + w + w + w + w + w +
w + w + b + b + b + b + b + b + b + b + b + b + b + w + w +
w + w + b + b + b + b + b + b + b + b + b + b + b + w + w +
w + w + b + b + w + w + w + w + w + w + w + b + b + w + w +
w + w + b + b + w + w + w + w + w + w + w + b + b + w + w +
w + w + b + b + w + w + w + w + w + w + w + b + b + w + w +
w + w + b + b + w + w + w + w + w + w + w + b + b + w + w +
w + w + b + b + w + w + w + w + w + w + w + b + b + w + w +
w + w + b + b + w + w + w + w + w + w + w + b + b + w + w +
w + w + b + b + w + w + w + w + w + w + w + b + b + w + w +
w + w + b + b + b + b + b + b + b + b + b + b + b + w + w +
w + w + b + b + b + b + b + b + b + b + b + b + b + w + w +
w + w + w + w + w + w + w + w + w + w + w + w + w + w + w +
w + w + w + w + w + w + w + w + w + w + w + w + w + w + w)

c1 = (                                                                  #cursor_1
w + w + w + w + w + w + w + w + w + w + w + w + w + w + w +
w + w + w + w + w + w + w + w + w + w + w + w + w + w + w +
w + w + b + b + b + b + b + b + b + b + b + b + b + w + w +
w + w + b + b + b + b + b + b + b + b + b + b + b + w + w +
w + w + b + b + b + b + b + b + b + b + b + b + b + w + w +
w + w + b + b + b + b + b + b + b + b + b + b + b + w + w +
w + w + b + b + b + b + b + b + b + b + b + b + b + w + w +
w + w + b + b + b + b + b + b + b + b + b + b + b + w + w +
w + w + b + b + b + b + b + b + b + b + b + b + b + w + w +
w + w + b + b + b + b + b + b + b + b + b + b + b + w + w +
w + w + b + b + b + b + b + b + b + b + b + b + b + w + w +
w + w + b + b + b + b + b + b + b + b + b + b + b + w + w +
w + w + b + b + b + b + b + b + b + b + b + b + b + w + w +
w + w + w + w + w + w + w + w + w + w + w + w + w + w + w +
w + w + w + w + w + w + w + w + w + w + w + w + w + w + w)

b_0 = (                                                                 #ball_0
b  + b  + re + re + re + re + b  + b  +
b  + re + re + re + re + re + re + b  +
re + re + re + re + re + re + re + re +
re + re + re + re + re + re + re + re +
re + re + re + re + re + re + re + re +
re + re + re + re + re + re + re + re +
b  + re + re + re + re + re + re + b  +
b  + b  + re + re + re + re + b  + b)

b_1 = (                                                                 #ball_1
b  + b  + bl + bl + bl + bl + b  + b  +
b  + bl + bl + bl + bl + bl + bl + b  +
bl + bl + bl + bl + bl + bl + bl + bl +
bl + bl + bl + bl + bl + bl + bl + bl +
bl + bl + bl + bl + bl + bl + bl + bl +
bl + bl + bl + bl + bl + bl + bl + bl +
b  + bl + bl + bl + bl + bl + bl + b  +
b  + b  + bl + bl + bl + bl + b  + b)

b_2 = (                                                                 #ball_2
b  + b  + gr + gr + gr + gr + b  + b  +
b  + gr + gr + gr + gr + gr + gr + b  +
gr + gr + gr + gr + gr + gr + gr + gr +
gr + gr + gr + gr + gr + gr + gr + gr +
gr + gr + gr + gr + gr + gr + gr + gr +
gr + gr + gr + gr + gr + gr + gr + gr +
b  + gr + gr + gr + gr + gr + gr + b  +
b  + b  + gr + gr + gr + gr + b  + b)
#-----------------------------------------------------------------------
import sys, random, pygame
from pygame.locals import *
from pygame.sprite import Sprite, Group
#-----------------------------------------------------------------------
# bricks
class Brick(Sprite):
    def __init__(self, step, position):
        super().__init__()
        self.surface = pygame.Surface([step, step])
        self.rect = self.surface.get_rect()
        self.rect.topleft = position
class BrickStable(Brick):
    def __init__(self, step, position):
        super().__init__(step, position)
        self.image = pygame.image.frombuffer(b1, (15, 15), 'RGB').convert()
class BrickUnstable(Brick):
    def __init__(self, step, position):
        super().__init__(step, position)
        self.image_0 = pygame.image.frombuffer(b1, (15, 15), 'RGB').convert()
        self.image_1 = pygame.image.frombuffer(b0, (15, 15), 'RGB').convert()

# balls
class Ball(Sprite):
    def __init__(self, ballpic, width, height, step):
        super().__init__()
        self.image = pygame.image.frombuffer(ballpic, (8, 8), 'RGB').convert()
        self.rect = self.image.get_rect()
        self.rect.center = get_ball_position(width, height, step)
        choice = [-1, 1]
        self.speed = [random.choice(choice), random.choice(choice)]
        #self.sound = pygame.mixer.Sound('Clink.ogg')
    def change_position(self, bricks_stable, bricks_unstable):
        self.rect = self.rect.move(self.speed)
        if pygame.sprite.spritecollide(self, bricks_stable, False, False):
            if self.speed == [1,1]:
                self.speed = [-1,1]
            elif self.speed == [-1,1]:
                self.speed = [-1,-1]
            elif self.speed == [-1,-1]:
                self.speed = [1,-1]
            elif self.speed == [1,-1]:
                self.speed = [1,1]
            #self.sound.play()
        elif pygame.sprite.spritecollide(self, bricks_unstable, False, False):
            self.speed = [0,0]
            result = 0
            return result

# scoreboard
class ScoreBoard():
    def __init__(self, step):
        self.level = level
        self.font = pygame.font.SysFont('Monospace', 18, bold=False)
    def update(self, step, level, colors, width, height, bricks_stable, curs_x, curs_y, curs_real_pos, balls):
        #level_00
        self.score_str_00 = "LEVEL: "
        self.score_image_00 = self.font.render(self.score_str_00, False, (192, 192, 192), (0,0,0))
        self.score_rect_00 = self.score_image_00.get_rect()
        self.score_rect_00.left = step
        self.score_rect_00.top = step
        screen.blit(self.score_image_00, self.score_rect_00)
        #level_01
        self.score_str_01 = "{}".format(level)
        self.score_image_01 = self.font.render(self.score_str_01, False, colors[level-1], (0,0,0))
        self.score_rect_01 = self.score_image_01.get_rect()
        self.score_rect_01.left = self.score_rect_00.right + 1
        self.score_rect_01.top = step
        screen.blit(self.score_image_01, self.score_rect_01)
        #len(bricks_stable)
        self.score_str_1 = "len(bricks_stable): {0} / 30".format(len(bricks_stable))
        self.score_image_1 = self.font.render(self.score_str_1, False, (192, 192, 192), (0,0,0))
        self.score_rect_1 = self.score_image_1.get_rect()
        self.score_rect_1.right = width - (step + width % step)
        self.score_rect_1.top = step
        screen.blit(self.score_image_1, self.score_rect_1)
        #cursor
        self.score_str_2 = 'cursor: (%02d,%02d)' % (curs_x, curs_y)
        self.score_image_2 = self.font.render(self.score_str_2, False, (192, 192, 192), (0,0,0))
        self.score_rect_2 = self.score_image_2.get_rect()
        self.score_rect_2.left = step
        self.score_rect_2.bottom = height - (step + height % step)
        screen.blit(self.score_image_2, self.score_rect_2)
        # balls
        self.semicolon_str = ';'
        self.semicolon_image = self.font.render(self.semicolon_str, False, (192, 192, 192), (0,0,0))
        self.semicolon_rect = self.semicolon_image.get_rect()
        self.semicolon_rect.bottom = height - (step + height % step)
        #
        balls_to_blit = []
        ball_ind = 0
        for ball in balls:
            position_0 = ball.rect.centerx // step - 1 
            position_1 = ball.rect.centery // step - 3
            self.score_str_3 = ' (%02d,%02d)' % (position_0, position_1)
            self.score_image_3 = self.font.render(self.score_str_3, False, colors[ball_ind], (0,0,0))
            self.score_rect_3 = self.score_image_3.get_rect()
            self.score_rect_3.bottom = height - (step + height % step)
            balls_to_blit.append((self.score_image_3, self.score_rect_3))
            if ball_ind < len(balls) - 1:
                balls_to_blit.append((self.semicolon_image, self.semicolon_rect))
            ball_ind += 1
        right_side = width - (step + width % step)
        for (i,r) in reversed(balls_to_blit):
            r.right = right_side
            right_side = r.left
            screen.blit(i,r)
        # ball_lable
        self.score_str_4 = "balls:"
        self.score_image_4 = self.font.render(self.score_str_4, False, (192, 192, 192), (0,0,0))
        self.score_rect_4 = self.score_image_4.get_rect()
        self.score_rect_4.right = right_side
        self.score_rect_4.bottom = height - (step + height % step)
        screen.blit(self.score_image_4, self.score_rect_4)
#=======================================================================
def get_matrix_0(width, height, step):
    lenx = (width - 2 * step) // step
    leny = (height - 6 * step) // step
    matrix = [['0' for x in range(lenx)] for y in range(leny)]
    return matrix, lenx, leny
    
def get_matrix_1(matrix, lenx, leny):
    matrix[0][0] = '3'
    matrix[0][-1] = '3'
    matrix[-1][0] = '3'
    matrix[-1][-1] = '3'
    for i in range(1, lenx-1):
        matrix[0][i] = '2'
        matrix[-1][i] = '2'
    for i in range(1, leny-1):
        matrix[i][0] = '2'
        matrix[i][-1] = '2'
    return matrix
    
def get_ball_position(width, height, step):
    ball_x = random.randint((step * 3), (width - step * 3))
    ball_y = random.randint((step * 5), (height - step * 5))
    ball_pos = (ball_x, ball_y)
    return ball_pos
        
def update_matrix(matrix, step):
    space_2, space_3 = [], []
    x, y = 15, 45
    for yy in matrix:
        for xx in yy:
            position = (x, y)
            if xx == '2':
                space_2.append(position)
            elif xx == '3':
                space_3.append(position)
            x += step
        x = 15
        y += step
    return space_2, space_3
    
def get_initial_bricks(step, space_2):
    for position in space_2:
        brick_stable = BrickStable(step, position)
        bricks_stable.add(brick_stable)
        
def delete_brick_unstable(position):
    for brick in bricks_unstable:
        if brick.rect.topleft == position:
            brick.kill()
            
# divide_space
def divide_space(balls, step, matrix, lenx, leny, new_chain, space_3):
    show_matrix(matrix)
    # 1) loop for matrix
    spaces = dict()
    symbols = []
    current_charge = 0
    current_symbol = 97
    for y in range(1, leny-1):
        for x in range(1, lenx-1):
            if matrix[y][x] == '0':
                if matrix[y][x-1] in symbols:
                    matrix[y][x] = matrix[y][x-1]
                    if matrix[y-1][x] == matrix[y][x]:
                        pass
                    elif matrix[y-1][x] in symbols:
                        key_0, key_1 = None, None
                        for key, value in spaces.items():
                            if matrix[y][x] in value:
                                key_1 = key
                            if matrix[y-1][x] in value:
                                key_0 = key
                        if key_0 != key_1:
                            spaces[key_1] += spaces[key_0]
                            spaces[key_0] = []
                else:
                    if matrix[y-1][x] in symbols:
                        matrix[y][x] = matrix[y-1][x]
                    else:
                        matrix[y][x] = chr(current_symbol)
                        symbols.append(matrix[y][x])
                        spaces[current_charge]=[]
                        spaces[current_charge].append(matrix[y][x])
                        current_symbol += 1                             
                        current_charge += 1
    print(spaces)
    show_matrix(matrix)
    # 2)find balls: to_0
    to_0 = []
    for ball in balls:
        ball_pos_x = ball.rect.center[0] // step - 1
        ball_pos_y = ball.rect.center[1] // step - 3
        ball_pos = matrix[ball_pos_y][ball_pos_x]
        for value in spaces.values():
            if ball_pos in value:
                to_0 += value
                value = []
    to_0 = set(to_0)
    print('to_0: ', to_0)
    # 3) when the balls are found: to_3
    to_3 = set()
    for symbol in symbols:
        if symbol not in to_0:
            to_3.add(symbol)
    print('to_3: ', to_3)
    # 4) deleting new_chain
    bricks_unstable.empty()
    # 5) update_0_matrix
    for y in range(1, leny-1):
        for x in range(1, lenx-1):
            if matrix[y][x] in to_0:
                matrix[y][x] = '0'
            elif matrix[y][x] in to_3:
                matrix[y][x] = '3'
            elif matrix[y][x] == '1':
                matrix[y][x] = '2'
                position = (((x+1) * step), ((y+3) * step))
                brick_stable = BrickStable(step, position)
                bricks_stable.add(brick_stable)
    # 6) update_1_matrix
    space_3 = []
    for y in range(0, leny):
        for x in range(0, lenx):
            if matrix[y][x] == '2':
                if (y != 0) and (matrix[y-1][x] == '0'):
                    pass
                elif (x != lenx-1) and (matrix[y][x+1] == '0'):
                    pass
                elif (y != leny-1) and (matrix[y+1][x] == '0'):
                    pass
                elif (x != 0) and (matrix[y][x-1] == '0'):
                    pass
                else:
                    matrix[y][x] = '3'
                    position = (((x+1) * step), ((y+3) * step))
                    for brick in bricks_stable:
                        if brick.rect.topleft == position:
                            brick.kill()
                    space_3.append(position)
            elif matrix[y][x] == '3':
                position = (((x+1) * step), ((y+3) * step))
                space_3.append(position)
    show_matrix(matrix)
    return matrix, space_3
    
# sound_play
def sound_play(sound):
    sound.play()

# temp------------------------------------------------------------------    
def show_matrix(matrix):
    for i in matrix:
        print(i)
    print()
    
#LEVEL==================================================================
def game(level):
    step = 15
    matrix, lenx, leny = get_matrix_0(width, height, step)
    matrix = get_matrix_1(matrix, lenx, leny)
    space_2, space_3 = update_matrix(matrix, step)

    #cursor
    curs_x, curs_y = 0, 0                                                   # initial positions (in matrix, not on screen)
    curs_offset_x, curs_offset_y = 0, 0                                     # initial offsets (by pressing the keys)
    curs_pos = (curs_x, curs_y)                                             # universal definition
    curs_pos_0 = (0, 0)
    curs_pos_1 = (0, 0)
    curs_move_up = False
    curs_move_down = False
    curs_move_left = False
    curs_move_right = False
    curs_image_0 = pygame.image.frombuffer(c0, (15, 15), 'RGB').convert()
    curs_image_1 = pygame.image.frombuffer(c1, (15, 15), 'RGB').convert()
    point_start = None
    point_finish = None

    #bricks
    new_chain = []
    get_initial_bricks(step, space_2)

    #space_3
    ds = pygame.image.fromstring(b1, (15, 15), 'RGB').convert()

    #balls
    ballpics = [b_0, b_1, b_2, 'b_3.bmp', 'b_4.bmp', 'b_5.bmp']
    for i in range(0, level):
        if level < 6:
            ballpic = ballpics[i]
        else:
            ballpic = random.choice(ballpics)
        ball = Ball(ballpic, width, height, step)
        balls.add(ball)
        
    #score
    colors = [(255, 51, 51), (51, 51, 255), (51, 255, 51)]                                               #for level numbers and for balls
    score = ScoreBoard(step)

    #temp
    iteration = 0
    reverse = False
    s = 0
    #while loop---------------------------------------------------------
    while True:
        if iteration == 100:
            reverse = not reverse
            iteration = 0
        
        matrix_0 = matrix

        # events
        #for event in pygame.event.get():
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                elif event.key == K_UP:
                    curs_move_up = True
                elif event.key == K_DOWN:
                    curs_move_down = True
                elif event.key == K_LEFT:
                    curs_move_left = True
                elif event.key == K_RIGHT:
                    curs_move_right = True
            elif event.type == KEYUP:
                if event.key == K_UP:
                    curs_move_up = False
                elif event.key == K_DOWN:
                    curs_move_down = False
                elif event.key == K_LEFT:
                    curs_move_left = False
                elif event.key == K_RIGHT:
                    curs_move_right = False
                    
        # cursor offsets
        if curs_move_up == True:
            if curs_y > 0:
                curs_offset_y -= 1
        elif curs_move_down == True:
            if curs_y < (leny-1):
                curs_offset_y += 1
        elif curs_move_left == True:
            if curs_x > 0:
                curs_offset_x -= 1
        elif curs_move_right == True:
            if curs_x < (lenx-1):
                curs_offset_x += 1
                
        # cursor update
        curs_pos_0 = (curs_x, curs_y)
        if curs_offset_y <= -step:
            curs_y -= 1
            curs_offset_y = 0
        elif curs_offset_y >= step:
            curs_y += 1
            curs_offset_y = 0
        elif curs_offset_x <= -step:
            curs_x -= 1
            curs_offset_x = 0
        elif curs_offset_x >= step:
            curs_x += 1
            curs_offset_x = 0
        curs_pos_1 = (curs_x, curs_y)
        #turn---------------------------------------------------------------
        if curs_pos_0 != curs_pos_1:
            i_0 = matrix[curs_pos_0[1]][curs_pos_0[0]]
            i_1 = matrix[curs_pos_1[1]][curs_pos_1[0]]
            print(curs_pos_0, ':', i_0, '___', curs_pos_1, ':', i_1)
            if i_0 == '3':
                pass
            elif i_0 == '2':
                if i_1 == '3':
                    pass
                elif i_1 == '2':
                    pass
                elif i_1 == '0':                                              # turn 2 -> 1 is impossible
                    point_start = curs_pos_0
                    matrix[curs_pos_1[1]][curs_pos_1[0]] = '1'
                    new_chain.append((((curs_x + 1) * step), ((curs_y + 3) * step)))
                    brick_unstable = BrickUnstable(step, new_chain[-1])
                    bricks_unstable.add(brick_unstable)
            elif i_0 == '1':
                if i_1 == '2':
                    point_finish = curs_pos_1
                    if point_finish == point_start:
                        if len(new_chain) == 1:
                            matrix[curs_pos_0[1]][curs_pos_0[0]] = '0'
                            delete_brick_unstable(new_chain[0])
                            new_chain = []
                        else:
                            new_chain = []
                            matrix, space_3 = divide_space(balls, step, matrix, lenx, leny, new_chain, space_3)
                    else:
                        new_chain = []
                        matrix, space_3 = divide_space(balls, step, matrix, lenx, leny, new_chain, space_3)
                elif i_1 == '1':
                    for i in new_chain[(new_chain.index((((curs_x + 1) * step), ((curs_y + 3) * step)))+1):]:
                        delete_brick_unstable(i)
                        matrix[int(i[1]/step - 3)][int(i[0]/step - 1)] = '0'
                    del new_chain[(new_chain.index((((curs_x + 1) * step), ((curs_y + 3) * step)))+1):]
                elif i_1 == '0':
                    matrix[curs_pos_1[1]][curs_pos_1[0]] = '1'
                    new_chain.append((((curs_x + 1) * step), ((curs_y + 3) * step)))
                    brick_unstable = BrickUnstable(step, new_chain[-1])
                    bricks_unstable.add(brick_unstable)
        #balls----------------------------------------------------------
        for ball in balls:
            result = ball.change_position(bricks_stable, bricks_unstable)
            if result == 0:
                break
        if result == 0:
            break
        #---------------------------------------------------------------
        if len(bricks_stable) <= 30:
            result = 1
            break
        #---------------------------------------------------------------
        screen.fill((0,0,0))
        
        # space_1
        for brick_unstable in bricks_unstable:
            if reverse == True:
                brick_unstable.image = brick_unstable.image_0
            else:
                brick_unstable.image = brick_unstable.image_1
        bricks_unstable.draw(screen)
        
        # space_2
        bricks_stable.draw(screen)
        
        # space_3
        for i in space_3:
            screen.blit(ds, i)
            
        # cursor
        curs_real_pos = (((curs_x + 1) * step), ((curs_y + 3) * step))
        if reverse == True:
            screen.blit(curs_image_0, curs_real_pos)
        else:
            screen.blit(curs_image_1, curs_real_pos)
        
        # balls
        balls.draw(screen)
        
        # score
        score.update(step, level, colors, width, height, bricks_stable, curs_x, curs_y, curs_real_pos, balls)
            
        # flip
        #pygame.display.flip()
        pygame.display.update() #optimized variant to flip parts of screen
        
        #temp---------------------------------------------------------------
        #print(iteration)
        iteration+=1
        #pygame.time.wait(0)
    return result
#GAME===================================================================
size = width, height = 1024, 600
pygame.init()
screen = pygame.display.set_mode(size, 0, 32) 
pygame.mouse.set_visible(False)
level = 1

#while
while True:
    bricks_stable = Group()
    bricks_unstable = Group()
    balls = Group()  
    result = game(level)
    if result == 0:
        level = 1
    elif result == 1:
        level += 1

        










    
