## Python file to run MDAnalysis RDF on LiCl-out-440K.lammpstrj, also uses a full topology.

import MDAnalysis as mda
import pickle
from MDAnalysis.analysis import rdf

print("Building Universe")
u = mda.Universe("full-out-topol.lammpstrj", "LiClH2O-375K.lammpstrj", topology_format="LAMMPSDUMP", format="LAMMPSDUMP")
print("Selecting Lis")
Lis = u.select_atoms("type Li")
print("Selecting Cls")
Cls = u.select_atoms("type Cl")
print("Selecting Os")
Os = u.select_atoms("type O")

print("Setting up rdfs")
print("Setting LiLi")
rdfLiLi = rdf.InterRDF(Lis, Lis, nbins=10000)
print("Setting LiCl")
rdfLiCl = rdf.InterRDF(Lis, Cls, nbins=10000)
print("Setting ClCl")
rdfClCl = rdf.InterRDF(Cls, Cls, nbins=10000)
print("Setting LiO")
rdfLiO = rdf.InterRDF(Lis, Os, nbins=10000)
print("Setting ClO")
rdfClO = rdf.InterRDF(Cls, Os, nbins=10000)

print("Running LiLi")
rdfLiLi.run()
print("Running LiCl")
rdfLiCl.run()
print("Running ClCl")
rdfClCl.run()
print("Running LiO")
rdfLiO.run()
print("Running ClO")
rdfClO.run()

print("Saving data")
LiLi = [rdfLiLi.results.bins, rdfLiLi.results.rdf]
LiCl = [rdfLiCl.results.bins, rdfLiCl.results.rdf]
ClCl = [rdfClCl.results.bins, rdfClCl.results.rdf]
LiO = [rdfLiO.results.bins, rdfLiO.results.rdf]
ClO = [rdfClO.results.bins, rdfClO.results.rdf]
data_list = [LiLi, LiCl, ClCl, LiO, ClO]

file_dump = open("data-375K-rdf.data", 'wb')
pickle.dump(data_list, file_dump)
file_dump.close()
print("Process complete")
