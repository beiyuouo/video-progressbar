from PIL import Image, ImageDraw, ImageFont
import os
import cv2
import numpy as np

width = 120
height = 1080
text_width = 90
size = (width, height)
bg_color = (0, 0, 0)
ft_color = (255, 255, 255)
pb_color = (255, 193, 37)
ft_size = 24
ft_num = text_width // ft_size
font = ImageFont.truetype(os.path.join('fonts', 'Muyao-Softbrush.ttf'), ft_size)
menu = ['第一阶段', '第二阶段', '第三阶段让我看看能写多长，他到底能不能自动换行，我就问你行不行']
end_point = ['0:05', '0:10', '0:20']
tmp_path = 'tmp'


def get_time(time: str) -> int:
    t = time.split(':')
    res = 0
    for i in range(len(t)):
        res += int(t[i]) * (60 ** (len(t) - i - 1))
    return res


def deal_text(items):
    new_menu = []
    for item in items:
        str = ""
        for idx, ch in enumerate(item):
            str += ch
            if (idx + 1) % ft_num == 0:
                str += '\n'
        new_menu.append(str)
    return new_menu


fps = 25

total_len = get_time(end_point[-1]) * fps

menu = deal_text(menu)

os.makedirs(tmp_path, exist_ok=True)


def generate_video(path):
    filelist = os.listdir(path)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter("VideoTest1.mp4", fourcc, fps, size, True)
    # 视频保存在当前目录下

    for item in filelist:
        if item.endswith('.jpg'):
            # 找到路径中所有后缀名为.jpg的文件，可以更换为.png或其它
            item = os.path.join(path, item)
            img = cv2.imread(item)
            # print(item, img)
            # cv2.imshow(f'{item}', img)
            video.write(img)

    video.release()


def add_text(draw, time_line):
    for t in range(len(menu)):
        xx = width // 2
        yy = height * (1 - (time_line[t] - (time_line[t] - (0 if t == 0 else time_line[t - 1])) / 2) / time_line[-1])
        draw.multiline_text(xy=(xx, yy), text=menu[t], font=font, fill=ft_color, align='center', anchor='mm')


def main():
    image = Image.new('RGB', (width, height), bg_color)

    time_line = []
    for i in range(len(end_point)):
        time_line.append(get_time(end_point[i]))
    print(time_line)
    print(menu)

    draw = ImageDraw.Draw(image)

    add_text(draw, time_line)

    image.save('base.jpg')

    for i in range(total_len):
        x0 = 0
        y0 = height * (1 - i / total_len)
        x1 = width
        y1 = height
        draw.rectangle(xy=(x0, y0, x1, y1), fill=pb_color)
        add_text(draw, time_line)
        image.save(os.path.join(tmp_path, '{:04d}.jpg'.format(i)))

    generate_video(tmp_path)
    pass


if __name__ == '__main__':
    main()
