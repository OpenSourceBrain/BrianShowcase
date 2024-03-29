'''
Brian simulator compliant Python export for:

Components:
    fn1 (Type: fitzHughNagumoCell:  I=0.8 (dimensionless) SEC=1.0 (SI time))
    net1 (Type: network)
    sim1 (Type: Simulation:  length=200.0 (SI time) step=0.01 (SI time))

'''
'''
    This Brian file has been generated by org.neuroml.export (see https://github.com/NeuroML/org.neuroml.export)
         org.neuroml.export  v1.9.0
         org.neuroml.model   v1.9.0
         jLEMS               v0.10.7
'''
from brian import *

from math import *
import sys

import numpy as np


if len(sys.argv) > 1 and sys.argv[1] == '-nogui':
    show_gui = False
else:
    show_gui = True

# Adding simulation Component(id=sim1 type=Simulation) of network: net1 (Type: network)

defaultclock.dt = 10.0*msecond
duration = 200000.0*msecond
steps = int(duration/defaultclock.dt)+1

#    Population fnPop1 contains components of: Component(id=fn1 type=fitzHughNagumoCell) 

fn1_eqs=Equations('''
    dV/dt = ((((V - ((V ** 3.0) / 3.0)) - W) + I) / SEC) :  1
    dW/dt = ((0.08 * (V + (0.7 - (0.8 * W)))) / SEC) :  1
    SEC = 1.0 * second : second 
    I = 0.8: 1 
''')

fnPop1 = NeuronGroup(1, model=fn1_eqs)
# Initialise a second time...


# Inputs

if show_gui:

    # Display: Component(id=d1 type=Display)
    trace_d1__V = StateMonitor(fnPop1,'V',record=[0]) # V (Type: Line:  scale=1.0 (dimensionless) timeScale=1.0 (dimensionless))
    trace_d1__W = StateMonitor(fnPop1,'W',record=[0]) # W (Type: Line:  scale=1.0 (dimensionless) timeScale=1.0 (dimensionless))

# Saving to file: ex9.dat, reference: of1
record_of1__V = StateMonitor(fnPop1,'V',record=[0]) # V (Type: OutputColumn)
record_of1__W = StateMonitor(fnPop1,'W',record=[0]) # W (Type: OutputColumn)

print("Running simulation for %s (dt = %s, #steps = %s)"%(duration,defaultclock.dt, steps))
run(duration) # Run a simulation from t=0 to just before t=duration 
run(defaultclock.dt) # Run one more time step to allow saving the point at t=duration

# Saving to file: ex9.dat, reference: of1
all_of1 = np.array( [ record_of1__V.times, record_of1__V[0] , record_of1__W[0]  ] )
all_of1 = all_of1.transpose()
file_of1 = open("ex9.dat", 'w')
for l in all_of1:
    line = ''
    for c in l: 
        line = line + ('\t%s'%c if len(line)>0 else '%s'%c)
    file_of1.write(line+'\n')
file_of1.close()

if show_gui:

    import matplotlib.pyplot as plt

    # Display: Component(id=d1 type=Display)
    display_d1 = plt.figure("Ex9: FitzHugh-Nagumo cell model in LEMS")
    plot_V = display_d1.add_subplot(111, autoscale_on=True)
    plot_V.plot(trace_d1__V.times/second,trace_d1__V[0], color="#ee40FF", label="V")
    plot_V.legend()
    plot_W = display_d1.add_subplot(111, autoscale_on=True)
    plot_W.plot(trace_d1__W.times/second,trace_d1__W[0], color="#BBA0AA", label="W")
    plot_W.legend()
    plt.show()
