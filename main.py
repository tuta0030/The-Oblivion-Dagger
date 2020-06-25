# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 17:09
# @Author  : Eric Shen
# @Email   : Eric_Shenarrzine@outlook.com
# @File    : main.py.py
# @Software: PyCharm

"""

故事生成器

1. 平淡的开头
2. 遇到了问题
3. 寻找解决办法
4. 找到解决办法
5. 付出严重代价
6. 勉强击败敌人
7. 改变了自己
8. 回到了平淡的生活

"""

import re
import os
import inspect


class StoriesGenerator(object):

    def __init__(self, who, where, problem, how, boss, solution):
        self.who = who
        self.where = where
        self.problem = problem
        self.how = how
        self.boss = boss
        self.solution = solution

    def mundane_start(self):
        pass

    def encounter_problem(self):
        pass

    def finding_solution(self):
        pass

    def find_the_solution(self):
        pass

    def defeated_enemy(self):
        pass

    def pay_a_great_price(self):
        pass

    def change_self(self):
        pass

    def back_to_mundane(self):
        pass

    def main(self):
        pass
