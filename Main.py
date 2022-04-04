from make_noise import remove_random_accent, remove_random_space, replace_accent_chars
import numpy as np
import pandas as pd
import re

df = pd.read_csv("data_full.csv", encoding="utf-8", index_col=0)
df_wrong1 = remove_random_accent(df['data'][:10000])
df_wrong2 = remove_random_space(df['data'][10000:20000])
df_wrong3 = replace_accent_chars(df['data'][30000:])
print(df_wrong3[:3])