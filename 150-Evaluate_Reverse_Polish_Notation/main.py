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
# Initial created: 2017-07-07 20:11:34
#
# Last   modified: 2017-07-08 13:42:55
#
#
#
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
       """
        #tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        list_oprs = ['+','-','*','/']
        ind_opr = 2

        while(len(tokens) > 1):
            while(1):
                if not tokens[ind_opr] in list_oprs:
                    ind_opr += 1
                    continue
                else:
                    break
            x = int(tokens[ind_opr-2])
            y = int(tokens[ind_opr-1])
            if tokens[ind_opr] == "/" and x*y < 0:
                tokens[ind_opr] = abs(x)/abs(y)*-1
            else:
                tokens[ind_opr] = eval('x'+tokens[ind_opr]+'y')
            del tokens[ind_opr-1]
            del tokens[ind_opr-2]
            ind_opr = ind_opr-1
