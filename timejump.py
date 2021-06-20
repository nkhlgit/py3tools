#!/usr/bin/python3

import argparse
from datetime import datetime

ap= argparse.ArgumentParser(
        usage="%(prog)s -d time_diff_in_Sec -f file_name",
        description = "find time jump in log file"
        )
ap.add_argument( '-d', required=True, type=int )
ap.add_argument( '-f',required=True )
args = ap.parse_args()
file1=args.f
max_dif_sec=args.d
i = 0
j = 0
k = 0
dtl=datetime.now()
ll = ' '
with open(file1 , 'r') as f1:
        for l in f1:
            i += 1
            la = l.strip().split(' ')
            l0 = la[0]
            if l0.startswith('2021'):
                j += 1
                dts = l0.strip()[0:19]
                dt = datetime.fromisoformat(dts)
                time_dif_sec = abs(int((dt-dtl).total_seconds()))
                if time_dif_sec > max_dif_sec:
                    k += 1
                    print('\n>>>Jumped  {} sec #{}  line: {} from: {} to: {} '.format(time_dif_sec,k,i,dtl, dt))
                    print(ll)
                    print(l)
                dtl=dt
                ll=l
