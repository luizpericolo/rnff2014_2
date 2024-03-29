# coding: utf-8

import pandas as pd
import numpy
import matplotlib.pyplot as plt

spambase_headers = [
	'word_freq_make', 'word_freq_address', 'word_freq_all', 'word_freq_3d',
	'word_freq_our', 'word_freq_over', 'word_freq_remove', 'word_freq_internet',
	'word_freq_order', 'word_freq_mail', 'word_freq_receive', 'word_freq_will',
	'word_freq_people', 'word_freq_report', 'word_freq_addresses', 'word_freq_free',
	'word_freq_business', 'word_freq_email', 'word_freq_you', 'word_freq_credit',
	'word_freq_your', 'word_freq_font', 'word_freq_000', 'word_freq_money', 'word_freq_hp',
	'word_freq_hpl', 'word_freq_george', 'word_freq_650', 'word_freq_lab', 'word_freq_labs',
	'word_freq_telnet', 'word_freq_857', 'word_freq_data', 'word_freq_415', 'word_freq_85',
	'word_freq_technology', 'word_freq_1999', 'word_freq_parts', 'word_freq_pm', 'word_freq_direct',
	'word_freq_cs', 'word_freq_meeting', 'word_freq_original', 'word_freq_project', 'word_freq_re',
	'word_freq_edu', 'word_freq_table', 'word_freq_conference',
	'char_freq_semicolon', 'char_freq_left_paren', 'char_freq_left_bracket', 'char_freq_bang', 'char_freq_dollar',
	'char_freq_sharp', 'capital_run_length_average', 'capital_run_length_longest', 'capital_run_length_total',
	'classification'
]

df = pd.read_csv('spambase/spambase.data')

df_inputs_only = df.copy()
del df_inputs_only['classification']

df_inputs_only.to_csv('spambase/inputs_only.csv')

df_mean = df_inputs_only.mean()
df_mean.to_csv("spambase/mean.csv")

df_std_dev = df_inputs_only.std()
df_std_dev.to_csv('spambase/std_dev.csv')

# Daqui pra frente temos desvio padrao = 1 e media = 0 para todas as variáveis
df_normalized = (df_inputs_only - df_mean)/df_std_dev

df_normalized.to_csv('spambase/normalized.csv')

df_corr = df_normalized.corr()

df_corr.to_csv('spambase/corr.csv')

html = df_corr.to_html()

f_h = file("spambase/corr.html", 'w')

f_h.write(html)

f_h.close()


from pandas.tools.plotting import scatter_matrix

scatter_matrix(df, alpha=0.2)

plt.show()