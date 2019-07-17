import pandas as pd
import numpy as np

class data_pre:
    def __init__(self, df_data):
        self.df_data = df_data
        self.colum = ['5 Minutes', 'Lane 1 Flow (Veh/5 Minutes)', '% Observed']
        self.time_pre()
    def time_pre(self):
        drop_index = list(self.df_data[self.df_data['% Observed'] == 0].index)
        self.df_data.drop(drop_index, inplace=True)

        data_date_train = self.df_data['5 Minutes']
        date_value_train = data_date_train.values
        y_m_d = []
        h_m_s = []
        for index in date_value_train:
            str1 = index.split()
            y_m_d.append(str1[0])
            h_m_s.append(str1[1])
        NSM = []
        # 计算NSM 这是这一天的第多少分钟24 * 60 =1440

        for index in h_m_s:
            str1 = index.split(':')
            NSM.append((int(str1[0]) * 60 + int(str1[1])) / 5)
        self.df_data['NSM'] = NSM

        # 将日期化为星期表示
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # 日月年
        # 规定01/01/2015为周五用4表示，
        flag = 4
        week_index = []

        for index in y_m_d:
            str1 = index.split('/')
            count_day = int(str1[1])

            for i in range(int(str1[0]) - 1):
                count_day += month[i]
            temp_point = (count_day % 7) + flag - 1

            if temp_point <= 7:
                week_flag = temp_point
            else:
                week_flag = temp_point - 7
            week_index.append(week_flag)

        self.df_data['day_of_week'] = week_index





df_0 = pd.read_csv('../dataset/data_merge/object_point.csv')
data_pre(df_0)
comu = ['NSM', 'day_of_week', 'Lane 1 Flow (Veh/5 Minutes)']
df_0[comu].to_csv('../ending_dataset/data_760643.csv', index=False)


df_1 = pd.read_csv('../dataset/data_merge/object_point.csv')
data_pre(df_1)
comu = ['NSM', 'day_of_week', 'Lane 1 Flow (Veh/5 Minutes)']
df_1[comu].to_csv('../ending_dataset/data_774671.csv', index=False)

df_2 = pd.read_csv('../dataset/data_merge/object_point.csv')
data_pre(df_2)
comu = ['NSM', 'day_of_week', 'Lane 1 Flow (Veh/5 Minutes)']
df_2[comu].to_csv('../ending_dataset/data_718173.csv', index=False)