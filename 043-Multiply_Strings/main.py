#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Filename: main.py
#
# Description: 
#
# Copyright (c) 2017, Yusheng Yi <yiyusheng.hust@gmail.com>
#
# Version 1.0
#
# Initial created: 2017-07-07 19:06:37
#
# Last   modified: 2017-07-07 19:58:04
#
#
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num_map = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9} 
        
        num1_sum = 0
        for i in range(1,len(num1)+1):
                num1_sum += num_map[num1[-i]]*pow(10,i-1) 
        
        num2_sum = 0
        for i in range(1,len(num2)+1):
                num2_sum += num_map[num2[-i]]*pow(10,i-1)
                
        return(str(num1_sum*num2_sum))
