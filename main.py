# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 17:09
# @Author  : Eric Shen
# @Email   : Eric_Shenarrzine@outlook.com
# @File    : main.py.py
# @Software: PyCharm

"""

# 从角色简介中获取角色简介信息
# 通过选择需要编辑的角色相关文件，编辑对应文件
# GUI 界面展示角色相关信息， 包括图片，简介，描述，主线故事，通过点击关联人物可以跳转

1. 学习tkinter创建自定义图形的方法
2. 设计UI
3. 绘制UI
4. 添加

"""
import re

EACH_CHARACTER_PATTERN = re.compile('姓名-.+?(?=姓名-)', re.DOTALL)
EACH_CHARACTER_NAME_PATTERN = re.compile('(?<=姓名-).+(?=[：:])')


def load_all_characters_info(which_file: str) -> dict:
    char_dict = {}
    raw_content = open(which_file, 'r', encoding='utf-8').read()
    _all = re.findall(EACH_CHARACTER_PATTERN, raw_content)
    index = 0
    for i in _all:
        char_dict[re.findall(EACH_CHARACTER_NAME_PATTERN, i)[0]] = [index, i]
        index += 1
    return char_dict


class Character:

    def __init__(self, name, brief, species, age, *relations):
        self.name = name
        self.brief = brief
        self.species = species
        self.age = age
        self.relations = relations
        pass

    def showinfo(self):
        print('名字:\t' + self.name)
        print('简介:\t' + self.brief)
        print('种族:\t' + self.species)
        print('年龄:\t' + self.age)
        print('关系:\t', end='')
        print(self.relations)

    def addinfo(self, info_type, content, **args):
        pass

    def load_info(self, who: str):
        char_dict = load_all_characters_info('角色')
        self.brief = char_dict[who][1]
        print(char_dict[who][1])

    def save_character(self):
        pass

    def delete_character(self):
        pass


taran = Character('taran', 'assassin', 'greeling', '21', {'lover': 'tuna', 'parents': 'Tarlonarr, ?'})
taran.load_info('塔伦')
