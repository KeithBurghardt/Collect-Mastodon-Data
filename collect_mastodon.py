import pandas as pd
import os, time
from glob import glob
import psutil
from collections import Counter

min_inst = 0
max_inst = 100
timeout =60
file = 'top_instances.txt'
instances = pd.read_csv(file,sep='\t')['Instance'].values





def get_process_count(pname):
    process_ctr = Counter()
    for process in psutil.process_iter():
        try:
            process_cmd_list = process.cmdline()
            for p in process_cmd_list:
                process_ctr[p] += 1
        except Exception:
            continue
    for p, cnt in process_ctr.items():
        if pname in p:
            return cnt
    return 0

for instance in instances[min_inst:max_inst]:    
    try:
        os.system('Rscript collect_mastodon.r '+instance+' &')
    except: continue
time.sleep(timeout)
while True:
    time.sleep(int(timeout/10))
    for instance in instances[min_inst:max_inst]:
        try:            
            all_files = glob('mastodon_data/'+instance.replace('.','-')+'_stream_*.txt')
            if len(all_files) > 0:
                latest_file = max(all_files, key=os.path.getctime)
                diff_time = time.time()-os.path.getctime(latest_file)
                cnt = get_process_count('R')+get_process_count('Rscript')
                # we run if: 
                # file is stale
                # but we avoid creating 100+ instances of R if a file updates rarely
                # and if the latest file is 0 size then collect_mastodon.r fails, so we should not attempt it
                condition = diff_time > timeout and cnt < max_inst-min_inst and os.path.getsize(latest_file) > 0
                if condition:
                    os.system('Rscript collect_mastodon.r '+instance +' &')
        except:
            continue
    



