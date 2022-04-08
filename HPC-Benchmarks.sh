#!/bin/bash
# environment Initialization
module load apps/python/conda 
module load libs/cudnn/8.0.5.39/binary-cuda-11.1.1
source activate pytorch
# Shell Script Excute
cd /home/elp21aau/SACCT/SACCT/Benchmarks/sacwo
python3 sacwo_20210404.python 

