import os
import stat
from shutil import copy2, rmtree


SUBTITLE = 0
VIDEO = 1


# 获取字幕或视频路径

def get_directory(Tab):
    # 检查 Sub 目录是否存在
    isexist_sub()
    
    while True:
        try:
            if Tab == VIDEO:
                # 获取视频路径
                tmp_directory = input('请输入视频绝对路径（默认：..）：')
                # 处理路径末尾字符 '/'
                if tmp_directory:
                    if tmp_directory[-1] == '/':
                        tmp_directory = tmp_directory[:-1]
                else:
                    tmp_directory = '..'
            else:
                # 获取字幕路径
                tmp_directory = input('请输入字幕绝对路径（默认：./Sub）：')
                # 处理路径末尾字符 '/'
                if tmp_directory:
                    if tmp_directory[-1] == '/':
                        tmp_directory = tmp_directory[:-1]
                else:
                    tmp_directory = './Sub'
            # 获取文件名列表
            file_name_list = \
                [x for x in os.listdir(tmp_directory) if os.path.isfile(tmp_directory + '/' + x)]
        except FileNotFoundError:
            print('目录不存在，请重新输入！')
        except Exception as ex:
            raise ex
        else:
            break
    return file_name_list, tmp_directory


# 检测 Sub 目录是否存在 
def isexist_sub():
        if not os.path.exists('./Sub'):
            os.mkdir('./Sub')


# 打印列表信息
def print_info(info_list, flag):
    print('-' * 50)
    i = 1
    for x in info_list:
        print('[%d] %s' % (i, x))
        i += 1
    print('\n')
    if flag == SUBTITLE:
        print("请选择字幕文件 (1, 2, 3, or 1-4)：")
    elif flag == VIDEO:
        print("请选择视频文件 (1, 2, 3, or 1-4)：")


# 获取用户输入
def get_choice(in_list):
    in_list_len = len(in_list)
    input_list = input().split()
    if not input_list:  # 全选
        result_list = list(range(in_list_len))
    else:
        result_list = []
        for it in input_list:
            i = 0
            flag = False
            while i < len(it):
                if it[i] == '-':
                    flag = True
                    tmp = it.split('-')
                    start = int(tmp[0])
                    stop = int(tmp[1])
                    j = start
                    while j <= stop:
                        result_list.append(j - 1)
                        j += 1
                    break
                i += 1
            if not flag:
                result_list.append(int(it) - 1)
    result_list.sort()
    return result_list


# 打印用户选择列表
def print_choice(info_list, choice_list):
    print('=' * 50)
    print('你的选择是：')
    i = 1
    for x in choice_list:
        print("[%d] %s" % (i, info_list[x]))
        i += 1
    # 是否需要重选
    # flag = False
    while True:
        opt = input('是否需要修改(Y/n)：')
        if opt == 'Y' or opt == 'y':
            flag = True
            break
        elif opt == 'N' or opt == 'n':
            flag = False
            break
        else:
            print('输入参数有误，请重新输入！')

    return flag


# 生成用户选择文件列表
def generate_list(info_list, choice_list):
    result_list = []
    for x in choice_list:
        result_list.append(info_list[x])
    return result_list


# 字幕重命名
def rename(video_choice_list, subtitle_choice_list, dir_video, dir_subtitle):
    size = len(video_choice_list)
    i = 0
    while i < size:
        video_pos = video_choice_list[i].rfind('.')
        subtitle_pos = subtitle_choice_list[i].rfind('.')
        new_name = video_choice_list[i][:video_pos] + subtitle_choice_list[i][subtitle_pos:]
        # os.rename('./Sub/{}'.format(subtitle_choice_list[i]), '../{}'.format(new_name))
        # copy2('./Sub/{}'.format(subtitle_choice_list[i]), '../{}'.format(new_name))
        copy2((dir_subtitle + '/{}').format(subtitle_choice_list[i]), (dir_video + '/{}').format(new_name))
        i += 1


# 清空Sub文件夹
def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)


def clear_Sub_folder():
    rmtree('./Sub', onerror=remove_readonly)
    os.mkdir('./Sub')



