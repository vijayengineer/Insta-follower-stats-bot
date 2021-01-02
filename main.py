from InstaChannel import InstaChannel
import pandas as pd
import os
import time
from datetime import datetime


to_csv_timestamp = datetime.today().strftime('%Y%m%d_%H%M%S')
path = os.getcwd()
filename = path + '/data/' + to_csv_timestamp + '_instaChannel.csv'
headings = ['Follower_Name','Number of followers','Following','Posts']
df= pd.DataFrame([headings])
df.to_csv(filename,mode = 'a', header = None, index=False)

insta_follower = InstaChannel()
insta_follower.login()
insta_follower.find_followers()
data = insta_follower.gather_stats()
df= pd.DataFrame([data])
df.to_csv(filename,mode = 'a', header = None, index=False)