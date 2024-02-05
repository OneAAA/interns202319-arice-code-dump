## Template for running solvation analysis to save coordination numbers.
import MDAnalysis as mda
import solvation_analysis
from solvation_analysis.solute import Solute
import pickle

i1 = "LI"
i2 = "CL"
i3 = "O"
start = 0
stop = 100

u = mda.Universe("1584atom-topology.gro", "LiClH2O-temp.lammpstrj", topology_format="GRO", format="LAMMPSDUMP")

i1s = u.atoms.select_atoms(f"type {i1}")
i2s = u.atoms.select_atoms(f"type {i2}")
i3s = u.atoms.select_atoms(f"type {i3}")

sol1 = Solute.from_atoms(i1s, {i2: i2s, i3: i3s}, solute_name=i1)
sol2 = Solute.from_atoms(i2s, {i1: i1s, i3: i3s}, solute_name=i2)
sol1.run(start, stop)
sol2.run(start, stop)

data_dump = [sol1.coordination, sol2.coordination, sol1.residence, sol2.residence)
file_dump = open("co-nums-temp.data", 'wb')
pickle.dump(data_dump, file_dump)
file_dump.close()
