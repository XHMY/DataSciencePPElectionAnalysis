import pandas as pd
from progressbar import *
import numpy as np


def remove_duplicate(df, has):
    cnt = 0
    widgets = ['Progress: ', Percentage(), ' ', Bar('#'), ' ', Timer(),
               ' ', ETA()]
    pbar = ProgressBar(widgets=widgets, maxval=len(df)).start()
    res_df = df[0:1]
    has.add(df[0:1]["created_at"].values[0])
    for i in df.index:
        cur = df[i:i+1]
        if cur["created_at"].values[0] in has:
            cnt += 1
        else:
            has.add(cur["created_at"].values[0])
            res_df = res_df.append(cur)
        pbar.update(i+1)
    pbar.finish()
    print("Done! drop {} duplicate.".format(cnt))
    return res_df


has = set()
trump_df = pd.read_csv('Data/hashtag_donaldtrump.csv', lineterminator='\n')
print("Read Trump Data Complete!")
print("Start Processing Trump Data...")
trump_df["tag_biden"] = np.zeros(len(trump_df), dtype=np.int)
trump_df["tag_trump"] = np.ones(len(trump_df), dtype=np.int)
trump_df = trump_df.drop(['tweet', 'user_description'], axis=1)
res_df = remove_duplicate(trump_df, has)
del trump_df

biden_df = pd.read_csv('Data/hashtag_joebiden.csv', lineterminator='\n')
print("Read Trump Data Complete!")
print("Start Processing Biden Data...")
biden_df["tag_biden"] = np.ones(len(biden_df), dtype=np.int)
biden_df["tag_trump"] = np.zeros(len(biden_df), dtype=np.int)
biden_df = biden_df.drop(['tweet', 'user_description'], axis=1)
res_df.append(remove_duplicate(biden_df, has))

res_df.to_csv("election_twitter_data.csv", index=False)
# biden_df = pd.read_csv('pycode\hashtag_joebiden.csv',lineterminator='\n')
