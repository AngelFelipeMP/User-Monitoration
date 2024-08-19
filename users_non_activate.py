import pandas as pd
from icecream import ic
import os

# path = '/Volumes/THUD_ResearchHub/Feedback and SMART Trial/automated-code-driving-feedback/data/user_details/users_created.csv'
Path_users_created =  os.getcwd() + '/data/user_details' + '/users_created.csv'

# df = pd.read_csv(Path_users_created, usecols=['Policy Number','User Enrollment Date','Email Address', 'Trial'], index_col='Policy Number' )
df = pd.read_csv(Path_users_created, index_col='Policy Number' )
df = df.loc[((df['Trial']=='feedback') | (df['Trial']=='smart')),:]
df['activated_date'] = df['User Enrollment Date'].apply(lambda x: pd.to_datetime(x))
df['today'] = pd.to_datetime('today')
df['send_tracking_email'] = df.apply(lambda row: 'Yes' if pd.Timedelta(weeks=3) <= (row['today'] - row['activated_date']) < pd.Timedelta(weeks=4) else 'No', axis=1)

#COMMENT: We will need this line once we have the email passwords
# df_email = df.loc[df['send_tracking_email']=='Yes',['Email Address']]

df.to_csv(os.getcwd() + '/data/tracking_users/users_created_no_activated_' + str(pd.to_datetime('today').strftime('%Y-%m-%d %H:%M:%S')) + '.csv', index=False)
