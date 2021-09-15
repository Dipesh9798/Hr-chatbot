

# ---------------------------------

from art import *
import return_answer
import chat_bot_functions as cbf
import ast
from config import *
#import return_answers_extractive_ai
import time
timeout = time.time() + 600
import json 

# context = None
old_context = None
number = 0
session_status = False  ## Make it True when user communicate and make it False after giving answer and wait
old_inp =''
inp = ''
decision1 = 0
decision2 = 0

#----------------------------------------

    
# print(session_values)
    




import os
from flask import Flask, json, jsonify, make_response, request, session
from flask_session import Session
from flask_cors import CORS



app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

CORS(app)

service_name = 'CARD_SERVICE'
file_name = 'app.py'

dic = {"Hi":"Hello","How are you":"I am fine"}

def return_basics():
    return "Hi, I am Manav, Your HR Buddy         \nI can help you with below given topics, Please pick a number                        \n\n 1.Holiday   2. Leave Policy  3. Attendance  4. Exit Process  5. Refferal Bonus 6. other 7. quit"
                        
@app.route('/home/<msg>',methods=['POST','GET'])
def home(msg):
    
    session_values = {}
    with open("session_values",'r') as f:
        session_values = ast.literal_eval(f.read())
    
    print("This is data - ",msg)
    # global context
    
    
    print(type(msg))
    if(msg =='hi' or msg == "Hi"):
        return {"message":str(return_basics())}
    
    print("====",session_values['context'] == None , session_values['old_context'] ==None , session_values['decision1'] ==0 , session_values['decision2'] ==0 ,  session_values['decision3'] ==0 , session_values['decision4'] ==0)
    
    if(session_values['context'] == None  and session_values['decision1'] ==0 and session_values['decision2'] ==0 and  session_values['decision3'] ==0 and session_values['decision4'] ==0):
        print(session_values['context'] )
        
        session_values['context'] = class_dict[msg].lower()
        session_values['decision1'] = 1
        session_values['decision2'] = 0
        session_values['decision3'] = 0
        session_values['decision4'] = 0
        with open("session_values",'w') as f:
            f.write(str(session_values))
    
        return {"message":session_values['context']+"are you interested in :"+ str(sub_context[session_values['context']])}
    
    elif(session_values['context'] != None  and session_values['decision1'] ==1 and session_values['decision2'] ==0 and  session_values['decision3'] ==0 and session_values['decision4'] ==0):
    	
        print("------",session_values)
        
        session_values['decision1'] = 1
        session_values['decision2'] = 1
        session_values['decision3'] = 0
        session_values['decision4'] = 0
        
        with open("session_values",'w') as f:
            f.write(str(session_values))
    
        return {"message":str(qna[session_values['context']][msg])+"\n\n Got what you were looking? \n\n 1. yes or 2. no"}
    
    

    elif(session_values['context'] !=None and session_values['decision1'] ==1 and session_values['decision2'] ==1 and session_values['decision3'] ==0 and session_values['decision4'] ==0 and session_values['trigger'] == 0):
    	
        
        
        if(msg == '1'):
            session_values['decision1'] = 1
            session_values['decision2'] = 1
            session_values['decision3'] = 1
            session_values['decision4'] = 0
            
            with open("session_values",'w') as f:
                f.write(str(session_values))
            return {"message": "want to 1. continue or 2. quit"}
        
        elif(msg == '2'):
            session_values['trigger'] = 1
            with open("session_values",'w') as f:
                f.write(str(session_values))
            return {"message":"cool ! keep asking\n\nGive it a shot by asking more contextual questions"}
        
    elif(session_values['context'] !=None and session_values['decision1'] ==1 and session_values['decision2'] ==1 and session_values['decision3'] ==1 and session_values['decision4'] ==0):
        if(msg == '1'):
            
            session_values['decision1'] = 1
            session_values['decision2'] = 1
            session_values['decision3'] = 1
            session_values['decision4'] = 1
            
            with open("session_values",'w') as f:
                f.write(str(session_values))
            
            return {"message":"Still interested in "+session_values['context']+' \n\n1. yes or 2. no'}
        
        elif(msg == '2' and session_values['decision1'] ==1 and session_values['decision2'] ==1 and session_values['decision3'] ==1):
            return {"message":"press 7 to exit"}
        
        elif(msg == '7'):
            session_values['context'] = None
            session_values['old_context'] = None
            session_values['decision1'] = 0
            session_values['decision2'] = 0
            session_values['decision3'] = 0
            session_values['decision4'] = 0
            
            with open("session_values",'w') as f:
                f.write(str(session_values))
            
            return {"message":'Thanks for chatting with me have a nice day!'}
    elif(session_values['context'] !=None and session_values['decision1'] ==1 and session_values['decision2'] ==1 and session_values['decision3'] ==1 and session_values['decision4'] ==1):
        if(msg == '1'):
            session_values['decision1'] = 1
            session_values['decision2'] = 0
            session_values['decision3'] = 0
            session_values['decision4'] = 0
            
            with open("session_values",'w') as f:
                f.write(str(session_values))
        
            return {"message":session_values['context']+"are you interested in :"+ str(sub_context[session_values['context']])}
        
        elif(msg == '2'):
            session_values['old_context'] = session_values['context']
            session_values['context'] = None 
            session_values['decision1'] = 0
            session_values['decision2'] = 0
            session_values['decision3'] = 0
            session_values['decision4'] = 0
            with open("session_values",'w') as f:
                f.write(str(session_values))
            return {"message":"\nI can help you with below given topics, Please pick a number                        \n\n 1.Holiday   2. Leave Policy  3. Attendance  4. Exit Process  5. Refferal Bonus 6. other 7. quit"}

    elif(session_values['trigger'] == 1):
        session_values['old_context'] = session_values['context']
        session_values['context'] = cbf.get_context(msg)
        if(session_values['old_context'] == session_values['context']):
            session_values['trigger'] = 0
            session_values['decision1'] = 1
            session_values['decision2'] = 1
            session_values['decision3'] = 0
            session_values['decision4'] = 0
            with open("session_values",'w') as f:
                f.write(str(session_values))
            
            return {"message":str(return_answer.return_top_one_result(msg,session_values['context']))+"\n\n Got what you were looking? \n\n 1. yes or 2. no"}
            
        else:
            session_values['trigger'] = 0
            session_values['decision1'] = 1
            session_values['decision2'] = 1
            session_values['decision3'] = 0
            session_values['decision4'] = 0
            with open("session_values",'w') as f:
                f.write(str(session_values))
            return {"message":"context changed to : "+session_values['context']+"\n\n"+str(return_answer.return_top_one_result(msg,session_values['context']))+"\n\n Got what you were looking? \n\n 1. yes or 2. no"}
        
        


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=5001)
