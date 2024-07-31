#不想再更新，再加连原来的FPS都要不保
#以下不可修改！！！
loading = 1
state = 'welcome'
loading += 1
loading_width = 0
loading += 1
circle_width = 0
loading += 1
circle_y = 500
loading += 1
#以上不可修改！！！
#可修改区域（以下）
w_fps = 25  #危险FPS,15-40为宜
loading += 1
g_fps = 50  #优秀FPS,50-55为宜
loading += 1
title = 'get fps'  #标题
loading += 1
#以下为不可修改(我的代码不能改)=======================================================================================================
import time

loading += 1
import pgzrun

loading += 1

WIDTH = 800
loading += 1
HEIGHT = 600
loading += 1
TITLE = title
loading += 1
old_time = time.time()
loading += 1
fps = 0
loading += 1
fps_list = []
loading += 1
long_line = 0
loading += 1
fps_draw = 0
loading += 1
fps_OK = True

try:
    loading += 1
    long = Actor('long', [15, 300])
    loading += 1
    long.height = 600
    loading += 1
    long.width = 20
    loading += 1
    long.top = 0
    loading += 1
    long.left = 5
    loading += 1
except:
    pass


def update_fps():
    global old_time, fps, fps_draw, fps_list
    now_time = time.time()
    fps += 1
    if now_time - old_time >= 1:
        fps_draw = fps
        fps = 0
        old_time = now_time
        fps_list.append(fps_draw)


def draw_fps_text():
    if fps_draw <= w_fps:
        screen.draw.text('FPS:' + str(fps_draw), [725, 550], color='red')
    elif fps_draw >= g_fps:
        screen.draw.text('FPS:' + str(fps_draw), [725, 550], color='green')
    else:
        screen.draw.text('FPS:' + str(fps_draw), [725, 550], color='#FFFFFF')


def get_long():
    global long_line
    long_line = (70 - fps_draw) * 8.571428571428571


def draw_long():
    try:
        long.draw()
        screen.draw.line([long.left - 5, long_line], [long.right + 5, long_line], color='#FFFFFF')
    except:
        pass


def draw_fps_p():
    for i in range(0, len(fps_list) - 1):
        if fps_list[i] < fps_list[i + 1]:
            screen.draw.line([100 + (i * 700) / len(fps_list), 500 - 7.142857142857 * fps_list[i]],
                             [100 + ((i + 1) * 700) / len(fps_list), 500 - 7.142857142857 * fps_list[i + 1]],
                             color='green')
        elif fps_list[i] == fps_list[i + 1]:
            screen.draw.line([100 + (i * 700) / len(fps_list), 500 - 7.142857142857 * fps_list[i]],
                             [100 + ((i + 1) * 700) / len(fps_list), 500 - 7.142857142857 * fps_list[i + 1]],
                             color='blue')
        else:
            screen.draw.line([100 + (i * 700) / len(fps_list), 500 - 7.142857142857 * fps_list[i]],
                             [100 + ((i + 1) * 700) / len(fps_list), 500 - 7.142857142857 * fps_list[i + 1]],
                             color='red')

def welcome_update():
    global loading , loading_width , state , circle_width , circle_y
    if state == 'welcome':
        loading += 1
        if loading == 100:
            state = 'on'
        loading_width = 4*loading
        circle_width = 5*loading
        #print('welcome')
    elif state == 'on':
        if loading != 0:
            loading -= 4
            loading_width = 4 * loading
            circle_width = 5 * loading
            #print(loading)
        else:
            circle_y += 10
def welcome_draw():
    global loading , loading_width , state , circle_width , circle_y
    if state == 'welcome' or loading != 0:
        screen.draw.color = 'red'
        screen.draw.filled_circle((400,300),circle_width,(79,117,255))
        if state == 'welcome':
            screen.draw.text('Produced by Ao Lanxiang\nFPS go', midtop = (400, 100), color='white', fontsize=40, width=800, align='center')
            screen.draw.text('loading ' + str(loading) + '%',midtop = (400,300),color = 'white',fontsize = 20)
    screen.draw.color = 'blue'
    if loading != 0:
        screen.draw.filled_rect(Rect((200,circle_y - 10),(loading_width,20)),'blue')
        screen.draw.filled_circle((200 + loading_width,circle_y),10,'blue')
    if circle_y < HEIGHT + 10:
        screen.draw.filled_circle((200,circle_y),10,'blue')

def fps_list_setting():
    global fps_list
    if len(fps_list) == 60:
        new_list = []
        for i in range(30):
            new_num = (fps_list[i] + fps_list[i + 1]) / 2
            new_list.append(new_num)
        fps_list = new_list

def fps_not_ok():
    global fps_draw , fps_OK , w_fps
    if fps_draw <= w_fps:
        fps_OK = False
    else:
        fps_OK = True#不想做了

def fps_not_ok_draw():
    global fps_OK
    pass

def update():
    welcome_update()
    update_fps()
    get_long()
    fps_list_setting()


def draw_anything_else():
    pass


def draw():
    screen.clear()
    draw_fps_text()
    draw_long()
    draw_fps_p()
    welcome_draw()
    draw_anything_else()

pgzrun.go()