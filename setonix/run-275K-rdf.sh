#!/bin/bash -l
#SBATCH -A interns202319
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --partition=work
#SBATCH --time=04:00:00

module load python/3.10.10

srun -n 1 -N 1 python3 rdf-275K.py
