#!/bin/bash
# environment Initialization
module load apps/python/conda 
module load libs/cudnn/8.0.5.39/binary-cuda-11.1.1
source activate pytorch
# Shell Script Excute
cd /home/elp21aau/SACCT/SACCT/Benchmarks/sacw/
python3 sacw_20210405.py --cuda true 1>>sacw_20210405.py.log 2>>sacw_20210405.py.log

cd /home/elp21aau/SACCT/SACCT/Benchmarks/sacwo
python3 sacwo_20210404.py --cuda true 1>>sacwo_20210404.log 2>>sacwo_20210404_error.log

cd /home/elp21aau/SACCT/SACCT/Benchmarks/twitch_small
python3 twitch_small.py 1>>twitch_small.log 2>>twitch_small.log

cd /home/elp21aau/SACCT/SACCT/Benchmarks/twitch_star
python3 twitch_star.py 1>>twitch_star.log 2>>twitch_star.log

cd /home/elp21aau/SACCT/SACCT/SACCT/
python3 main.py --cuda true 1>>main.py.log 2>>main.py.log