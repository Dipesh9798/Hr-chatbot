#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 05:06:28 2021

@author: mps
"""

class_dict = {1:'Holiday',2:'Leave Policy',3:'Attendance',4:'Exit Process',5:'Refferal Bonus', 6:'other', 7:'quit'}
context ={'holiday','leave policy','attendance','exit process','refferal bonus','business travel policy'}
other_context = {}

intent ={'holiday':[],'leave policy':[],'attendance':[],'exit process':[],'refferal bonus':[]}

exit_criteria = {'exit':{'got what you were looking':{'yes':{'would you like to continue or quit':{'yes','quit'}},'no':{'continue'}}}}

key_to_context ={'floating':'holiday', 'holiday':'holiday', 'holiday calendar':'holiday','floating holiday':'holiday',
                 'indian holiday':'holiday','leave':'leave policy','eligible':'leave policy','continuous':'leave policy',
                 'privilege leave':'leave policy',' pl ':'leave policy','casual leave':'leave policy',' cl ':'leave policy',
                 'sick leave':'leave policy',' sl ':'leave policy','leave balance':'leave policy','advance leave':'leave policy',
                 'leave calendar':'leave policy','timesheets':'attendance','timesheet':'attendance','client timesheet':'attendance',
                 'floating holiday':'attendance','wrong hours':'attendance','standard working hours':'attendance',
                 
                 'exit': 'exit process', 'post exit': 'exit process', 'resigned': 'exit process', 'resigned associate': 'exit process',
                  'notice period': 'exit process', 'formal notification': 'exit process', 'LWD': 'exit process',
                  'hand over': 'exit process', 'project hand over': 'exit process', 'knowledge transfer': 'exit process',
                  'clearance checklist': 'exit process', 'alumni network': 'exit process', 'resignation': 'exit process',
                  'resignation acceptance letter': 'exit process', 'relieving': 'exit process', 'relieving letter': 'exit process',
                  'experience letter': 'exit process', 'settlement': 'exit process', 'encashment': 'exit process',
                  'leave encashment': 'exit process', 'insurance post exit': 'exit process', 'withdrawal': 'exit process',
                  'pf withdrawal': 'exit process', 'gratuity payment': 'exit process',

                  'referral': 'referral bonus', 'referral bonus': 'referral bonus', 'referred': 'referral bonus',
                  'hired': 'referral bonus', 'referral joins': 'referral bonus',
                  'business travel request':'business travel policy', 'travel request':'business travel policy',
                  'accommodation during travel':'business travel policy',
                  'medical insurance':'mediclaim policy','mid year inclusion':'mediclaim policy','mid-year inclusion':'mediclaim plolicy',
                  'change the nominations':'mediclaim policy'}

sub_context = {'leave policy':{'casual,sick,floating,covid,privilege','other leaves'}, 'holiday':{'client','floating','other questions'},
               'attendance':{'continue'},'exit process':{'continue'},'other':{}}



important_keyword_to_identify_context = ['india','client','us','usa','u.s.a','united state']

            
digression = {"digression":['are you sure it is related to HR','HAHA thats funny']}

## Digression, context if not able to find one, sub_context, Reinforcement, 

# Two parrlel systems one is  recommendation based and other is qna based

qna = {'holiday':{'floating':{'Associates are eligible for 2 Floating Holidays designated for respective locations. ',
                            'To avail, associates should apply on the HRMS system with prior approval from the Project Manager and Mentor marking RMG.',},
                  
                  'client':{'Associate at client site needs to work on the day when client do not have a holiday. If the associate is an Abzooba employee, he/she can work with their Abzooba manager to get a comp day off.'}
                  ,'other questions':'','others':'','other':''},
       'leave policy':{'pl':{"15, for new joiners' leaves are allotted on pro rata basis considering date of joining.  7 of such leaves are carried forward to the next year, or on prorate basis considering date of joining."},
                       'privilege leave':{"15, for new joiners' leaves are allotted on pro rata basis considering date of joining.  7 of such leaves are carried forward to the next year, or on prorate basis considering date of joining."},
                       'casual':{"10, for new joiners' leaves are allotted on pro rata basis considering date of joining. Such leaves are not carried forward to the next year."},
                       "cl":{"10, for new joiners' leaves are allotted on pro rata basis considering date of joining. Such leaves are not carried forward to the next year."},
                       'sick':{"3, such leaves are carried forward and maximum accumulation is 56"},
                       'sl':{"3, such leaves are carried forward and maximum accumulation is 56"},
                       'floating':"",
                       "covid":"",
                       'other leaves':{},
                       'others':"",
                       'other':""
                       }
       
       }











## Priyal








class_dict = {1:'Holiday',2:'Leave Policy',3:'Attendance',4:'Exit Process',5:'Refferal Bonus', 6:'Got my answer no more questions'}
context ={'holiday','leave policy','attendance','exit process','refferal bonus'}

intent ={'holiday':[],'leave policy':[],'attendance':[],'exit process':[],'refferal bonus':[]}


key_to_context ={'floating':'holiday', 'holiday':'holiday', 'holiday calendar':'holiday','floating holiday':'holiday',
                 'indian holiday':'holiday','leave':'leave policy','eligible':'leave policy','continuous':'leave policy',
                 'privilege leave':'leave policy',' pl ':'leave policy','casual leave':'leave policy',' cl ':'leave policy',
                 'sick leave':'leave policy',' sl ':'leave policy','leave balance':'leave policy','advance leave':'leave policy',
                 'leave calendar':'leave policy','timesheets':'attendance','timesheet':'attendance','client timesheet':'attendance',
                 'floating holiday':'attendance','wrong hours':'attendance','standard working hours':'attendance',
                 
                 'exit': 'exit process', 'post exit': 'exit process', 'resigned': 'exit process', 'resigned associate': 'exit process',
                  'notice period': 'exit process', 'formal notification': 'exit process', 'LWD': 'exit process',
                  'hand over': 'exit process', 'project hand over': 'exit process', 'knowledge transfer': 'exit process',
                  'clearance checklist': 'exit process', 'alumni network': 'exit process', 'resignation': 'exit process',
                  'resignation acceptance letter': 'exit process', 'relieving': 'exit process', 'relieving letter': 'exit process',
                  'experience letter': 'exit process', 'settlement': 'exit process', 'encashment': 'exit process',
                  'leave encashment': 'exit process', 'insurance post exit': 'exit process', 'withdrawal': 'exit process',
                  'pf withdrawal': 'exit process', 'gratuity payment': 'exit process',

                  'referral': 'referral bonus', 'referral bonus': 'referral bonus', 'referred': 'referral bonus',
                  'hired': 'referral bonus', 'referral joins': 'referral bonus'}

sub_context = {'leave policy':{'casual,sick,floating,covid,privilege','other leaves'}, 'holiday':{'client','floating','other questions'},
               'attendance':{'Abzooba timesheet','client timesheet','wrong hours','standard working hours'},'exit process':{'Regisned','notice period','LWD','project                                        handover''knowledge transfer','clearance','Alumni network','relieving letter','experience letter','Final settlement','leave enchasment',                                        insurance''PFwithdrawal'},
               'refferal bonus':{'contractor','bonus','policy','eligible'}}



important_keyword_to_identify_context = ['india','client','us','usa','u.s.a','united state']

            
digression = {"digression":['are you sure it is related to HR','HAHA thats funny']}

## Digression, context if not able to find one, sub_context, Reinforcement, 

# Two parrlel systems one is  recommendation based and other is qna based

qna = {'holiday':{'floating':{'Associates are eligible for 2 Floating Holidays designated for respective locations. ',
                            'To avail, associates should apply on the HRMS system with prior approval from the Project Manager and Mentor marking RMG.',},
                  
                  'client':{'Which holiday calendar is applicable for associates working at client site?','Associate at client site needs to work on the day when client do not have a holiday. If the associate is an Abzooba employee, he/she can work with their Abzooba manager to get a comp day off.'}
                  ,'other questions':'','others':'','other':''},
       'leave policy':{'pl':{"15, for new joiners' leaves are allotted on pro rata basis considering date of joining.  7 of such leaves are carried forward to the next year, or on prorate basis considering date of joining."},
                       'privilege leave':{"15, for new joiners' leaves are allotted on pro rata basis considering date of joining.  7 of such leaves are carried forward to the next year, or on prorate basis considering date of joining."},
                       'casual':{"10, for new joiners' leaves are allotted on pro rata basis considering date of joining. Such leaves are not carried forward to the next year."},
                       "cl":{"10, for new joiners' leaves are allotted on pro rata basis considering date of joining. Such leaves are not carried forward to the next year."},
                       'sick':{"3, such leaves are carried forward and maximum accumulation is 56"},
                       'sl':{"3, such leaves are carried forward and maximum accumulation is 56"},
                       'floating':"",
                       "covid":"",
                       'other leaves':{},
                       'others':"",
                       'other':""
                       },
        'attendance':{'Abzooba timesheet':{'The person needs to be referred to the appropriate RMG coordinator who will generate the needed access to our internal timesheets'},
					 'timesheet':{'The person needs to be referred to the appropriate RMG coordinator who will generate the needed access to our internal timesheets'},
					 'client timesheet':{'The person needs to be referred to the appropriate RMG coordinator who will generate the needed access to our internal timesheets'}
					 'wrong hours':{'Please email the following teams to correct this error:Human_resources@abzooba.com ,Joanita.Sontakke@abzooba.com'},
					 'standard working hours':{'It is 9.30 A.M. to 6.00 P.M. From Monday to Friday. It may change basis business / project need.'},
					 'Regular working hours':{'It is 9.30 A.M. to 6.00 P.M. From Monday to Friday. It may change basis business / project need.'}},
		'exit process':{'notice period':{'Leave is not encouraged on notice period and Abzooba reserves the right to deduct salary or extend notice for absence from office in lieu of the leaves taken during the notice period.'},
						'LWD':{'In case the resignation decision stands confirmed, Leadership conveys the relieving date or Last Working Day to RMG and HR at the earliest. On the receipt of formal approval from Leadership HR Ops communicate LWD to resigned associate. (preferably within 30 days from the date of resignation)'},
						'project handover':{'Ideally, associate is expected to complete his / her project hand over / knowledge transfer at least one day prior to actual LWD.'},
						'knowledge transfer':{'Ideally, associate is expected to complete his / her project hand over / knowledge transfer at least one day prior to actual LWD.},
						'clearance':{'Associate needs to get clearance from following departments (Considering the pandemic situation HR Ops will get the following clearance from the respective stakeholder)MentorProject ManagerITAdminRMGFinanceComplianceSocial Media Undertaking (Mandatory)'},
						'Alumni Network':{'Please notify HR Ops representative during exit interview or write to us at alumni@abzooba.com so that we can add you to our Alumni Network.'}
						'experience letter':{'On successful handover of Abzooba / client assets relieving letter and experience letter will be issued to resigned associate.'},
						'relieving letter':{'On successful handover of Abzooba / client assets relieving letter and experience letter will be issued to resigned associate.'},
						'Final Settelment':{'Your final pay dues will be held back by Abzooba until you submit all the assets. On successful completion of asset handover, your Full and Final Settlement will be disbursed along with the upcoming pay cycle (On the first day of the month)'},
						'Leave enchasment':{'Only Privileged Leave balance will be encashed based on current basic salary. This is not applicable to those who are resigning on probation.'},
						'PF':{'Employees Provident Fund - You can find the UAN no in Payslip. The provident fund amount can be withdrawn after 2 months from date of release if you are not continuing the account further. The date of exit will be updated from Abzooba within this period of time.'},
					    'insurance':{"Abzooba's group health insurance coverage will be applicable until LWD. The prorated premium will be refunded, those who have added parents/in-laws & does not have any claim for the current year for any of the family members."},
						'gratuity':{'Gratuity - This is only applicable to those who have worked 5 years or more in the organisation (without any break-in service)'},
						'post exit queries':{'"Please write to Finance Team at finance@abzooba.com For any query related to full and final settlement, Form-16, Payslip, SodexoFor query related to Leave, Medical Insurance, statutory compliance like EPF, Gratuity etc. and any other concern, please connect with Employee Success Team at human_resources@abzooba.com'}}
		'refferal bonus':{'contractor':{'Temporary contractual associates and former associates are not eligible for the referral program.'},
						 'long after':{'(Please check with HR policy in India). In US it is 1 month'},
						 'policy':{'Please get this information from HR'},
						 'send refferal':{'All referral requests should be made through the incident management platform -JIRA by raising tickets, as a response to the job postings available on Abzooba website, or mailers sent by the Recruitment team. While making requests for referral, it is necessary to attach the resume of the candidate being referred.'},
						 'eligiblity':{'Temporary contractual associates and former associates are not eligible for the referral program. Spouses or Children of existing associates are exempted from the referral program.Fresher profiles and profile of Interns are welcome, but they are exempted from the referral program.The Reporting Managers, Project Managers, COE and Delivery Heads will not be a part of the referral policy when their referees join their team.This policy is also not applicable in cases where the reporting of a candidate is pre-decided and the reporting manager/project manager refers the candidate being aware of the situation, or in a scenario where the referee on joining the organization, is made to report the associate or project manager, who had referred him/her.'}}
						 