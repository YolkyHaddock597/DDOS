
import os
import time
from joblib import Parallel, delayed

# Define here
MY_CONST="JASON"
IP_TO_CHECK=('23.92.18.130')

def main(i):
    #tic = time.perf_counter()
    os.system('ping -n 4 {}'.format(IP_TO_CHECK))
    #toc = time.perf_counter()
    #print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")

def my_ping_logic():
    i = 1
    while i <= 100:
        print(i)
        os.system('ping -n 4 {}'.format(IP_TO_CHECK))
        i += 1    



if __name__ == "__main__":
    num = 8
    Parallel(n_jobs= 30)(delayed(main)(i) for i in range(num)) #change number under n_jobs
    
    # Define here