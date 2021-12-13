set -e

cd NeuroML2

jnml Run_MorrisLecarSCell.xml -brian
jnml Run_MorrisLecarSCell.xml -brian2

jnml LEMS_Regular_HindmarshRose.xml -brian
jnml LEMS_Regular_HindmarshRose.xml -brian2

jnml LEMS_NML2_Ex9_FN.xml -brian
jnml LEMS_NML2_Ex9_FN.xml -brian2

jnml LEMS_2007One.xml -brian2
jnml LEMS_FiveCells.xml -brian2

jnml LEMS_NML2_Ex5_DetCell.xml -brian2

cp LEMS_*_brian*py ../Brian
cp Run_*_brian*py ../Brian

cd ..
