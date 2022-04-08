#!/bin/bash
# environment Initialization
module load apps/python/conda 
module load libs/cudnn/8.0.5.39/binary-cuda-11.1.1
# Shell Script Excute
python main.py --num_steps 402 >> mainPyLog
# Function Defin
function errorExist(){
    previousCondition = $?
    if previousCondition -ne 0
    then 
        echo 'errorExist' >errorExistLog
        exit
    fi
}
