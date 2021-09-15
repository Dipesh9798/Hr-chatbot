#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 05:03:45 2021

@author: mps
"""
from art import *
import return_answer
import chat_bot_functions as cbf

from config import *
#import return_answers_extractive_ai
import time
timeout = time.time() + 600


context = None
old_context = None
number = 0
session_status = False  ## Make it True when user communicate and make it False after giving answer and wait
old_inp =''
inp = ''
decision1 = 0
decision2 = 0

qna_pairs =['question','answer','context','rating']

    

def anything_else():
    
   #1 print('\nGot what you were looking? yes or no')
    inp = input()
    
    if(len(inp)>5):
        chat()
    if(inp == 'yes' or inp == 'Yes'):
        print('please rate your expirience with Manav between 1 to 5')
        inp = int(input())
        
        
        return inp
    else:
        return 0
    
def chat():
    global context
    
    
    inp = int(input())
    number = inp
    context = class_dict[number]
    if(number):
        print('\nPlease ask about '+class_dict[number])
        
    inp = input()
    
    
    answer = return_answer.return_top_one_result(inp)
    return answer

tprint("manav")

print("Hi, I am Manav, Your HR Buddy")
print("\nI can help you with below given topics, Please pick a number")
print("\n\n\n 1.Holiday   2. Leave Policy  3. Attendance  4. Exit Process  5. Refferal Bonus 6. other 7. quit")


while number!=7:
    tempp = []
    print('context',context)
    number = cbf.take_number_input()
    if(number == 7):
        print(cbf.thank_you())
        continue
    question = ''
    if(number):
        context = class_dict[number].lower()
        print('\nPlease ask about '+class_dict[number])
        #question = take_   text_input()
        #print(question) 
    #print(return_answer.return_top_one_result(question))
    while number!=7:
        if(decision1):
            decision1 = 0
            pass
        else:
            
            print('context',context)
            if(sub_context[context]=={'continue'}):
                print('.......')
                pass
            else:
                
                print("are you interested in :"+ str(sub_context[context]))
                sub_cont_user = cbf.take_text_input()
                if(len(qna[context][sub_cont_user])>0):
                    if(sub_cont_user == 'continue'):
                        print('\nPlease ask queries about '+context)
                        
                    print(qna[context][sub_cont_user])
                    
                    inp = cbf.yes_no()
                    if(inp == 1):
                        print("want to 1. continue or 2. quit")
                        inp1 = int(input())
                        if(inp1 == 2):
                            print("press 7 to quit")
                            inp2 = int(input())
                            number = inp2
                            continue
                        else:
                            print("Still interested in "+context+' 1. yes or 2. no')
                            inp3 = int(input())
                            if(inp3 == 1):
                                continue
                            else:
                                print("cool ! keep asking")
                                break
                    else:
                        print("Please provide us more information about your query so that we can answer your query!")
                    
                else:
                    print("Please provide us more information about your query so that we can answer your query!")
                
        # if(context in list(sub_context)):
        #     sub_ = cbf.sub_context(context)
        question = cbf.take_text_input()
        tempp.append(question)
        old_context = context
        context = cbf.get_context(question)
        if(old_context == context):
            pass
        else:
            print("Ask about "+context)
        print(question)
        tempp.append(return_answer.return_top_one_result(question,context))
        tempp.append(context)
        print(return_answer.return_top_one_result(question,context))
        
        
        inp = cbf.yes_no()
        if(inp == 1):
            print("want to 1. continue or 2. quit")
            inp1 = int(input())
            if(inp1 == 2):
                print("press 7 to quit")
                inp2 = int(input())
                number = inp2
            else:
                print("Still interested in "+context+' 1. yes or 2. no')
                inp3 = int(input())
                if(inp3 == 1):
                    continue
                else:
                    print("cool ! keep asking")
                    break
        else:
            decision1 =1
            print("Please provide us more information about your query so that we can answer your query!")
        # confirmation = cbf.yes_no()
        # if(confirmation==1):
        #     print("\n Cool keep asking")
        #     pass
        # else:
        #     print(return_answer.return_top_three_result(question, context))
            # print("please look at below answers and suggest us the correct option as 1,2,3")
    
    # if(is_satisfied() =='yes'):
    #     ask_for_rating()
    #     thank_you()
    # else:
    #     question = what_else()
    #     print(return_answer.return_top_one_result(question))
        
    if(number ==7):
        print(cbf.thank_you())
        pass
    else:
        
        old_context = context
        context = cbf.get_context(question)
        print("\n\n\n 1.Holiday   2. Leave Policy  3. Attendance  4. Exit Process  5. Refferal Bonus 6. other 7. quit")
        if(context == class_dict[number].lower()):
            pass
        else:
            # print("/Are you sure to move to " + class_dict[number])
            print("\n\n\n 1.Holiday   2. Leave Policy  3. Attendance  4. Exit Process  5. Refferal Bonus 6. other 7. quit")
    
           
    
            
    

'''
while number!=6:
    if(time.time() > timeout):
        print("You were out for 1 min logging you out from your session")
        break
    
   # if(old_inp == inp):
        #time.sleep(60)
        #session_status = True
        
    answer = chat()
    
    print(answer)
    rating = anything_else()
    if(rating<1):
        print("\n\n\n 1.Holiday   2. Leave Policy  3. Attendance  4. Exit Process  5. Refferal Bonus  6. Got my answer no more questions")
        
    else: 
        number = 6
        print("Store data to to database question, answer, rating")
    
    old_inp = inp

        
    #break
'''


