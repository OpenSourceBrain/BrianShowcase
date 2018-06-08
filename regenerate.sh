set -e

cd NeuroML2

jnml LEMS_Regular_HindmarshRose.xml -brian
jnml LEMS_Regular_HindmarshRose.xml -brian2

jnml LEMS_NML2_Ex9_FN.xml -brian 
jnml LEMS_NML2_Ex9_FN.xml -brian2

jnml LEMS_2007One.xml -brian2
jnml LEMS_FiveCells.xml -brian2

cp ../NeuroML2/LEMS_*_brian*py .

cd ..
