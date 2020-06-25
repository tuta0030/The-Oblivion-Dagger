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
import os
import inspect

PATTERN_EACH_CHARACTER = re.compile('姓名-.+?(?=姓名-)', re.DOTALL)
PATTERN_EACH_CHARACTER_NAME = re.compile('(?<=姓名-).+(?=[：:])')
PATH_CHARACTERS_OBJ = os.curdir+'\\Characters\\'


def load_all_characters_info(which_file: str) -> dict:
    char_dict = {}
    raw_content = open(which_file, 'r', encoding='utf-8').read()
    _all = re.findall(PATTERN_EACH_CHARACTER, raw_content)
    index = 0
    for i in _all:
        char_dict[re.findall(PATTERN_EACH_CHARACTER_NAME, i)[0]] = [index, i]
        index += 1
    return char_dict


class Character:

    def __init__(self, name, brief, species, **kwargs):
        self.name = name
        self.brief = brief
        self.species = species
        self.relations = kwargs.get('relations', None)
        self.pet = kwargs.get('pet', None)
        self.age = kwargs.get('age', None)

    def load_info(self, who: str):
        char_dict = load_all_characters_info('角色')
        self.brief = char_dict[who][1]
        print(char_dict[who][1])

    def save_character(self):
        attributes = inspect.getmembers(self)
        with open(PATH_CHARACTERS_OBJ+self.name+'.py', 'w', encoding='utf-8') as f:
            for att in attributes:
                if not (att[0].startswith('__') and att[0].endswith('__')):
                    if not inspect.ismethod(self.__getattribute__(att[0])):
                        f.write(f'{att[0]} = "{att[1]}"')
                        f.write('\n')
                        print(att)

    def delete_character(self):
        os.remove(PATH_CHARACTERS_OBJ+self.name+'.py')


taran = Character('taran', 'None', 'greeling', relations={'lover': 'tuna'}, age='25')
taran.save_character()
