import pandas as pd
from progressbar import *


trump_df = pd.read_csv('Data/test.csv', lineterminator='\n')
print("Read Data Complete!")
# biden_df = pd.read_csv('pycode\hashtag_joebiden.csv',lineterminator='\n')

# print(trump_df.index)
# print(trump_df)
has = dict()
cnt = 0

widgets = ['Progress: ', Percentage(), ' ', Bar('#'), ' ', Timer(),
           ' ', ETA(), ' ', FileTransferSpeed()]

pbar = ProgressBar(widgets=widgets, maxval=len(trump_df)).start()

for i in trump_df.index:
    cur = trump_df[i:i+1]["tweet_id"].values[0]
    if cur in has:
        print("Find Duplicate at {}!".format(i))
        print("Old: {}".format(trump_df[has[cur]:has[cur]+1]))
        print("New: {}".format(trump_df[i:i+1]))
        print()
        cnt += 1
    else:
        has[cur] = i
    pbar.update(i+1)
pbar.finish()
print("Done, find {} duplicate.".format(cnt))
