#!/bin/bash -l
#SBATCH -A interns202319-gpu
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --time=20:00:00

/scratch/interns202319/shared/lammps/build/lmp -i in-275K.lammps -sc out-275K.lammps
