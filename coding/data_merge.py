import pandas as pd
import numpy as np

def data_Merge(path, name):

    name_list = 'pems_'


    df_1 = pd.read_excel(path + name_list + '1.xlsx')
    # print(np.shape(df_1))
    for i in range(2, 10):
        df_2 = pd.read_excel(path + name_list + str(i)+'.xlsx')
        # print(np.shape(df_2))
        df_1 = pd.concat([df_1, df_2])

    # print(np.shape(df_1))
    column = ['5 Minutes', 'Lane 1 Flow (Veh/5 Minutes)', '% Observed']
    df_1[column].to_csv('../dataset/data_merge/'+name + '.csv', index=False)

data_Merge('../dataset/object_point/', 'object_point')
print('object_point:ending')

data_Merge('../dataset/object_point_1/', 'object_point_1')
print('object_point_1:ending')

data_Merge('../dataset/object_point_2/', 'object_point_2')
print('object_point_2:ending')