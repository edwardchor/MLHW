import numpy as np
import pandas as pd
import os
import pprint

os.chdir('/Users/edwardchor/Base/Laboratory/MLCourse/HWML1/')
train_df=pd.DataFrame(pd.read_csv('./spambasetrain.csv'),columns=['x'+str(i) for i in range(9)]+['label']).astype(pd.Int32Dtype)
print(train_df.head())


# print(train_df.))
