#!/usr/bin/python3
import pandas as pd
import os

directory = 'open-round1'
keyword_spam_filepath = os.path.join(directory, 'Keyword_spam_question.csv')
keyword_list_filepath = os.path.join(directory, 'Extra Material 2 - keyword list_with substring.csv')

keyword_spam_df = pd.read_csv(keyword_spam_filepath)[:10]
keyword_list_df = pd.read_csv(keyword_list_filepath)[:10]

print(keyword_spam_df.head())
print(keyword_list_df.head())



def get_reverse_index(list_df):
	keyword_index_dict = {}
	for index, row in list_df.iterrows():
		group = row['Group']
		keywords = row['Keywords'].split(", ")
		for word in keywords:
			keyword_index_dict[word] = group
	return keyword_index_dict

print(get_reverse_index(keyword_list_df))
