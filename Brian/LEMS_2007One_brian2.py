'''
Brian simulator compliant Python export for:

Components:
    RS (Type: izhikevich2007Cell:  v0=-0.06 (SI voltage) k=7.0E-7 (SI conductance_per_voltage) vr=-0.06 (SI voltage) vt=-0.04 (SI voltage) vpeak=0.035 (SI voltage) a=30.0 (SI per_time) b=-2.0E-9 (SI conductance) c=-0.05 (SI voltage) d=1.0E-10 (SI current) C=1.0E-10 (SI capacitance))
    RS_Iext (Type: pulseGenerator:  delay=0.1 (SI time) duration=0.32 (SI time) amplitude=1.0E-10 (SI current))
    net1 (Type: network)
    sim1 (Type: Simulation:  length=0.52 (SI time) step=2.5E-6 (SI time))

'''
'''
    This Brian file has been generated by org.neuroml.export (see https://github.com/NeuroML/org.neuroml.export)
         org.neuroml.export  v1.9.0
         org.neuroml.model   v1.9.0
         jLEMS               v0.10.7
'''
from brian2 import *

from math import *
import sys

import numpy as np


if len(sys.argv) > 1 and sys.argv[1] == '-nogui':
    show_gui = False
else:
    show_gui = True

# Adding simulation Component(id=sim1 type=Simulation) of network: net1 (Type: network)

defaultclock.dt = 0.0025*msecond
duration = 520.0*msecond
steps = int(duration/defaultclock.dt)+1

#    Population RS_pop contains components of: Component(id=RS type=izhikevich2007Cell) 

RS_eqs=Equations('''
    dv/dt = (iMemb / C) :  volt
    du/dt = (a * ((b * (v - vr)) - u)) :  amp
    v0 = -0.06 * volt : volt 
    k = 7.0E-7 * kilogram**-2 * meter**-4 * second**6 * amp**3 : kilogram**-2 * meter**-4 * second**6 * amp**3 
    vr = -0.06 * volt : volt 
    vt = -0.04 * volt : volt 
    vpeak = 0.035 * volt : volt 
    a = 30.0 * second**-1 : second**-1 
    b = -2.0E-9 * siemens : siemens 
    c = -0.05 * volt : volt 
    d = 1.0E-10 * amp : amp 
    C = 1.0E-10 * farad : farad 
    iSyn = RS_pop_iSyn(t) :  amp
    iMemb = (((k * (v - vr)) * (v - vt)) + (iSyn - u)) :  amp
''')

RS_pop = NeuronGroup(1, model=RS_eqs, threshold = 'v > vpeak', reset = """v = c
u = u + d""")
RS_pop.v = RS_pop.v0
RS_pop.u = 0.0
# Initialise a second time...
RS_pop.v = RS_pop.v0
RS_pop.u = 0.0


# Inputs
#    Input RS_Iext on: synapses of RS_pop[0]: RS_Iext (Type: pulseGenerator:  delay=0.1 (SI time) duration=0.32 (SI time) amplitude=1.0E-10 (SI current))
RS_pop_iSyn = TimedArray( np.concatenate( ( 
         np.repeat(0, int(0.1/defaultclock.dt)) , 
         np.repeat(1.0E-10, int(0.32/defaultclock.dt)) , 
         np.repeat(0, (steps - int(0.42/defaultclock.dt))) ) ) * amp , 
         dt=defaultclock.dt)


if show_gui:

    # Display: Component(id=d1 type=Display)
    trace_d1__RS_v = StateMonitor(RS_pop,'v',record=[0]) # RS v (Type: Line:  scale=0.001 (dimensionless) timeScale=0.001 (dimensionless))

    # Display: Component(id=d2 type=Display)
    trace_d2__RS_u = StateMonitor(RS_pop,'u',record=[0]) # RS u (Type: Line:  scale=1.0E-12 (dimensionless) timeScale=0.001 (dimensionless))

# Saving to file: RS_One.dat, reference: of0
record_of0__v = StateMonitor(RS_pop,'v',record=[0]) # v (Type: OutputColumn)
record_of0__u = StateMonitor(RS_pop,'u',record=[0]) # u (Type: OutputColumn)

print("Running simulation for %s (dt = %s, #steps = %s, code generation target = %s)"%(duration,defaultclock.dt, steps, prefs.codegen.target))
run(duration) # Run a simulation from t=0 to just before t=duration 
run(defaultclock.dt) # Run one more time step to allow saving the point at t=duration

# Saving to file: RS_One.dat, reference: of0
all_of0 = np.array( [ record_of0__v.t, record_of0__v.v[0] , record_of0__u.u[0]  ] )
all_of0 = all_of0.transpose()
file_of0 = open("RS_One.dat", 'w')
for l in all_of0:
    line = ''
    for c in l: 
        line = line + ('\t%s'%c if len(line)>0 else '%s'%c)
    file_of0.write(line+'\n')
file_of0.close()

if show_gui:

    import matplotlib.pyplot as plt

    # Display: Component(id=d1 type=Display)
    display_d1 = plt.figure("RS v")
    plot_RS_v = display_d1.add_subplot(111, autoscale_on=True)
    plot_RS_v.plot(trace_d1__RS_v.t/second,trace_d1__RS_v.v[0], color="#0000ff", label="RS v")
    plot_RS_v.legend()

    # Display: Component(id=d2 type=Display)
    display_d2 = plt.figure("RS u")
    plot_RS_u = display_d2.add_subplot(111, autoscale_on=True)
    plot_RS_u.plot(trace_d2__RS_u.t/second,trace_d2__RS_u.u[0], color="#ff0000", label="RS u")
    plot_RS_u.legend()
    plt.show()
