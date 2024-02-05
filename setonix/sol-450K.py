## Template for running solvation analysis to save coordination numbers.
import MDAnalysis as mda
import solvation_analysis
from solvation_analysis.solute import Solute
import pickle

temp = "450"
ClO_rad = 4.2
i1 = "LI"
i2 = "CL"
i3 = "O"

u = mda.Universe("1584atom-topology.gro", f"LiClH2O-{temp}K.lammpstrj", topology_format="GRO", format="LAMMPSDUMP")

i1s = u.atoms.select_atoms(f"type {i1}")
i2s = u.atoms.select_atoms(f"type {i2}")
i3s = u.atoms.select_atoms(f"type {i3}")

sol1 = Solute.from_atoms(i1s, {i2: i2s, i3: i3s}, solute_name=i1)
sol2 = Solute.from_atoms(i2s, {i1: i1s, i3: i3s}, solute_name=i2, radii={i3: ClO_rad})
sol1.run(0,100000)
sol2.run(0,100000)

print(sol1.coordination.coordination_numbers)
print(sol2.coordination.coordination_numbers)
data_dump = [sol1.coordination, sol2.coordination]
file_dump = open(f"co-nums-{temp}K.data", 'wb')
pickle.dump(data_dump, file_dump)
file_dump.close()
