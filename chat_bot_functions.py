#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 11:35:08 2021

@author: mps
"""
from config import *
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
nlp = spacy.load('en')

def get_context(question):
    context = None
    question = question.lower()
    context_keys = list(key_to_context)
    context_keys.sort(key = len, reverse = True)
    for key in context_keys:
        if key in question:
            context = key_to_context[key]
            
    return context

def take_text_input():
    inp = input()
    return inp

def take_number_input():
    inp = int(input())
    return inp
            
def is_satisfied():
    print('\nGot what you were looking? 1. yes or 2. no')
    inp = int(input())
    return inp

def ask_for_rating():
    print('please rate your expirience with Manav between 1 to 5')
    inp = int(input())
    return inp

def thank_you():
    return 'Thanks for chatting with me have a nice day!'
    
    
    
def what_else():
    print("Please have one more round")
    inp = input()
    return inp

def answer_return_format():
    print(return_answer.return_top_one_result(question))
    
def yes_no():
    print('\nGot what you were looking? yes or no')
    print("\n 1. yes   2. no")
    inp = int(input())
    
    return inp

def another_round(context):
    inp = yes_no()
    if(inp == 1):
        print("want to 1. continue or 2. quit")
        inp1 = int(input())
        if(inp1 == 2):
            print("press 7 to quit")
            inp2 = int(input())
            return inp2
        else:
            print("Still interested in "+context+' 1. yes or 2. no')
            inp3 = int(input())
            return inp3
    else:
        inp1
                
def sub_context(context):
    # print('want to go with india or us?')
    inp = input()
    return inp.lower()

def remove_punctuation(txt):
    doc = nlp(txt)
    for ent in doc.ents:
        print(ent.text)
        if ent.text in STOP_WORDS:
            print(ent.text)
    