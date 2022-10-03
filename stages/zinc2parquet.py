import pandas as pd
import sys
from os import listdir, path

def process_zinc(pf_zinc, df_out):
    #check empty file
    if path.getsize(pf_zinc) == 0:
        return df_out
    
    df = pd.read_csv(pf_zinc, sep='\t', low_memory=False)

    # here recreate out in case of empty
    if df_out.shape == (0,0):
        return df
    else:
        df_out = pd.concat([df_out, df], axis=0, ignore_index=True)
    return df_out


## MAIN ##
##########

InDirPath = sys.argv[1]
OutFileName = sys.argv[2]


# test on the first file
l_dir = listdir(InDirPath)

df_out = pd.DataFrame()

for dir_zinc in l_dir:
    l_f_zinc = listdir(InDirPath + dir_zinc)
    for f_zinc in l_f_zinc:
        pf_zinc = "%s%s/%s"%(InDirPath, dir_zinc, f_zinc)
        df_out = process_zinc(pf_zinc, df_out)

df_out.to_parquet(OutFileName)