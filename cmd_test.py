# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 15:14:00 2022

@author: admin
"""


import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--square',help='please enter a number:',type=int,default=100)#当给了默认值是可以不传参直接运行不报错
#parser.add_argument('input_str',help='please enter a character:',type=str)
args=parser.parse_args()
print(args.square**2)