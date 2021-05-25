#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import tools


# 获取视频目录
video_list, dir_video = tools.get_directory(tools.VIDEO)
video_list.sort()
# print(video_list)

# 获取字幕目录
subtitle_list, dir_subtitle = tools.get_directory(tools.SUBTITLE)
subtitle_list.sort()
# print(subtitle_list)

# 打印视频文件列表 & 获取用户选择(序号)
while True:
    tools.print_info(video_list, tools.VIDEO)
    video_choice_list = tools.get_choice()
    opt = tools.print_choice(video_list, video_choice_list)
    if not opt:
        break

# 生成用户选择视频文件名列表
user_video_list = tools.generate_list(video_list, video_choice_list)

# 打印字幕文件列表 & 获取用户选择(序号)
while True:
    tools.print_info(subtitle_list, tools.SUBTITLE)
    subtitle_choice_list = tools.get_choice()
    opt = tools.print_choice(subtitle_list, subtitle_choice_list)
    if not opt:
        break

# 生成用户选择字幕文件名列表
user_subtitle_list = tools.generate_list(subtitle_list, subtitle_choice_list)

# 重命名字幕文件
tools.rename(user_video_list, user_subtitle_list, dir_video, dir_subtitle)
print('重命名成功！')

# 是否要清空 Sub 文件夹
if dir_subtitle == './Sub':
    opt = input('是否要清空 Sub 文件夹？Y/n: ')
    if opt == 'Y' or opt == 'y':
        tools.clear_Sub_folder()
        print('清理完毕！')
