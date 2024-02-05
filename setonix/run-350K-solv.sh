#!/bin/bash -l
#SBATCH -A interns202319
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --partition=work
#SBATCH --mem-per-cpu=150G
#SBATCH --time=24:00:00

module load python/3.10.10

srun -n 1 -N 1 python3 sol-350K.py
