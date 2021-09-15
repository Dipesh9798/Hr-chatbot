#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 07:57:27 2021

@author: mps
"""

from config import *

def get_context(question):
    global context
    question = question.lower()
    context_keys = list(key_to_context)
    context_keys.sort(key = len, reverse = True)
    for key in context_keys:
        if key in question:
            context = key_to_context[key]
            
    return context

