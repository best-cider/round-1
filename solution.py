#!/usr/bin/python3
import pandas as pd
import os

directory = 'open-round1'
keyword_spam_filepath = os.path.join(directory, 'Keyword_spam_question.csv')
keyword_list_filepath = os.path.join(directory, 'Extra Material 2 - keyword list_with substring.csv')

keyword_spam_df = pd.read_csv(keyword_spam_filepath)
keyword_list_df = pd.read_csv(keyword_list_filepath)

print(keyword_spam_df.head())
print(keyword_list_df.head())