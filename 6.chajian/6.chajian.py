# coding=utf-8
#
#  
#
# Created by Jason Pan on 2021-01-14 23:04:58
# Copyright © 2021 Jason Pan. All rights reserved.
#
if __name__ == '__main__':
    print("")


import pandas as pd
data = pd.read_csv(filepath_or_buffer="stu.csv",
                   encoding="utf8",
                   sep=",")
data.info()