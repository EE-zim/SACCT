#!/bin/bash
#$ -l rmem=12G
#$ -l gpu=1
#$ -M zliu73@sheffield.ac.uk
#$ -m abe
module load apps/python/conda
module load libs/cudnn/8.0.5.39/binary-cuda-11.1.1
source activate pytorch
cd /home/elp21aau/SACCT/SACCT
python3 main.py --num_steps 402 >> mainPyLog
