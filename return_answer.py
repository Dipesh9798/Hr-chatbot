#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 05:24:55 2021

@author: mps
"""

import pandas as pd
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
import numpy as np
import form_clusters


inp_csv  = pd.read_csv('hackathon-2021 data.csv')
questions = list(inp_csv.Questions)
contexts = list(inp_csv.Answer)

questions = list(inp_csv.Questions)
contexts = list(inp_csv.Answer)

embedded_qna_pair = {'question':[],'question_embedding':[],'answer':[], 'cluster_name' :[]}

for ind,quest in enumerate(questions):
    embedded_qna_pair['question'].append(quest)
    embedded_qna_pair['question_embedding'].append(model.encode(quest))
    embedded_qna_pair['answer'].append(contexts[ind])
    embedded_qna_pair['cluster_name'].append(form_clusters.get_context(quest).lower())
    
#print('embedded_qna_pair', embedded_qna_pair)
    


def return_top_one_result(question, context_cluster):
    embed_df = pd.DataFrame(embedded_qna_pair)
    
    # print(question, context_cluster, embed_df[['cluster_name','answer']])
    # print(list(embed_df[embed_df['cluster_name'] == context_cluster.lower()].question))
    embed_df = embed_df[embed_df['cluster_name'] == context_cluster.lower()]
    embeddings = np.array(list(embed_df.question_embedding)) 
    # embeddings = np.array(list(embed_df[embed_df['cluster_name'] == context_cluster.lower()].question_embedding))
    question_embedding = model.encode(question)
    cos_sim = util.pytorch_cos_sim(embeddings, question_embedding)
    # print(max(cos_sim))
    all_sentence_combinations = []
    for i in range(len(cos_sim)):
        all_sentence_combinations.append([ embed_df.iloc[i].question, cos_sim[i]])
    
    # print(all_sentence_combinations)
    all_sentence_combinations = sorted(all_sentence_combinations, key=lambda x: x[1], reverse=True)
        
    
    
    answer = embed_df[embed_df['question'] == all_sentence_combinations[0][0]]['answer'].values[0]
    score = float(all_sentence_combinations[0][1][0])
    
    return answer, score

def return_top_three_result(question, context_cluster):
    embed_df = pd.DataFrame(embedded_qna_pair)
    # print(question, context_cluster)
    embed_df = embed_df[embed_df['cluster_name'] == context_cluster.lower()]
    # embeddings = np.array(list(embed_df[embed_df['cluster_name'] == context_cluster.lower()].question_embedding))
    embeddings = np.array(list(embed_df.question_embedding)) 
    question_embedding = model.encode(question)
    cos_sim = util.pytorch_cos_sim(embeddings, question_embedding)
    # print(max(cos_sim))
    all_sentence_combinations = []
    counter = 0
    
    for i in range(len(cos_sim)):
        all_sentence_combinations.append([ embed_df.iloc[i].question, cos_sim[i]])
    
    all_sentence_combinations = sorted(all_sentence_combinations, key=lambda x: x[1], reverse=True)
    
    
    answer_list ={}
    
    for  i , score in all_sentence_combinations[0:3]:
        answer = embed_df[embed_df['question'] == i]['answer'].values[0] 
        counter+=1
        answer_list[counter] = {answer:float(score)}
        
        
    
    return answer_list