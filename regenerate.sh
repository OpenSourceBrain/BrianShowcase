set -e

cd NeuroML2

pynml Run_MorrisLecarSCell.xml -brian
pynml Run_MorrisLecarSCell.xml -brian2

pynml LEMS_Regular_HindmarshRose.xml -brian
pynml LEMS_Regular_HindmarshRose.xml -brian2

pynml LEMS_NML2_Ex9_FN.xml -brian
pynml LEMS_NML2_Ex9_FN.xml -brian2

pynml LEMS_2007One.xml -brian2
pynml LEMS_FiveCells.xml -brian2

pynml LEMS_NML2_Ex5_DetCell.xml -brian2

cp LEMS_*_brian*py ../Brian
cp Run_*_brian*py ../Brian

cd ..
