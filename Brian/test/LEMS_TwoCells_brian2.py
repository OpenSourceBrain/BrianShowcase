'''
Brian simulator compliant Python export for:

Components:
    weaklyAdapting (Type: izhikevichFergusonCell:  v0=-0.065 (SI voltage) vr=-0.0618 (SI voltage) vpeak=0.022600000000000002 (SI voltage) vt=-0.057 (SI voltage) c=-0.0658 (SI voltage) klow=5.0E-7 (SI conductance_per_voltage) khigh=3.2999999999999997E-6 (SI conductance_per_voltage) a=1.0 (SI per_time) b=3.0000000000000004E-9 (SI conductance) d=5.0E-12 (SI current) C=3.0E-10 (SI capacitance))
    stronglyAdapting (Type: izhikevichFergusonCell:  v0=-0.065 (SI voltage) vr=-0.0618 (SI voltage) vpeak=0.022600000000000002 (SI voltage) vt=-0.057 (SI voltage) c=-0.0658 (SI voltage) klow=1.0E-7 (SI conductance_per_voltage) khigh=3.2999999999999997E-6 (SI conductance_per_voltage) a=1.2 (SI per_time) b=3.0000000000000004E-9 (SI conductance) d=1.0E-11 (SI current) C=1.15E-10 (SI capacitance))
    weakIext (Type: pulseGenerator:  delay=0.0 (SI time) duration=1.0 (SI time) amplitude=1.0E-10 (SI current))
    weakIshift (Type: pulseGenerator:  delay=0.0 (SI time) duration=1.0 (SI time) amplitude=-4.5E-11 (SI current))
    strongIext (Type: pulseGenerator:  delay=0.0 (SI time) duration=1.0 (SI time) amplitude=1.0E-10 (SI current))
    strongIshift (Type: pulseGenerator:  delay=0.0 (SI time) duration=1.0 (SI time) amplitude=0.0 (SI current))
    net1 (Type: network)
    sim1 (Type: Simulation:  length=1.0 (SI time) step=2.0E-6 (SI time))

'''
'''
    This Brian file has been generated by org.neuroml.export (see https://github.com/NeuroML/org.neuroml.export)
         org.neuroml.export  v1.5.1
         org.neuroml.model   v1.5.1
         jLEMS               v0.9.8.8
'''
from brian2 import *

from math import *
import sys

import numpy as np
prefs.codegen.target = 'numpy'


if len(sys.argv) > 1 and sys.argv[1] == '-nogui':
    show_gui = False
else:
    show_gui = True

# Adding simulation Component(id=sim1 type=Simulation) of network: net1 (Type: network)

defaultclock.dt = 0.02*msecond
duration = 500*msecond
steps = int(duration/defaultclock.dt)

#    Population weakpop contains components of: Component(id=weaklyAdapting type=izhikevichFergusonCell) 

weaklyAdapting_eqs=Equations('''
    dv/dt = ((((k * (v - vr)) * (v - vt)) + (iSyn - u)) / C) :  volt
    du/dt = (a * ((b * (v - vr)) - u)) :  amp
    v0 = -0.065 * volt : volt 
    vr = -0.0618 * volt : volt 
    vpeak = 0.0226 * volt : volt 
    vt = -0.057 * volt : volt 
    c = -0.0658 * volt : volt 
    klow = 5.0E-7 * kilogram**-2 * meter**-4 * second**6 * amp**3 : kilogram**-2 * meter**-4 * second**6 * amp**3 
    khigh = 3.3E-6 * kilogram**-2 * meter**-4 * second**6 * amp**3 : kilogram**-2 * meter**-4 * second**6 * amp**3 
    a = 1.0 * second**-1 : second**-1 
    b = 3.0E-9 * siemens : siemens 
    d = 5.0E-12 * amp : amp 
    C = 3.0E-10 * farad : farad 
    iSyn = weakpop_iSyn(t) :  amp
    k = khigh :  kilogram**-2 * meter**-4 * second**6 * amp**3
''')



# Inputs
weakpop_iSyn = TimedArray([1e-10]*amp, dt=duration)

weakpop = NeuronGroup(1, model=weaklyAdapting_eqs, threshold = 'v > vpeak', reset = """v = c
u = u + d""")
weakpop.v = weakpop.v0
weakpop.u = 0.0
# Initialise a second time...
weakpop.v = weakpop.v0
weakpop.u = 0.0
#    Population strongpop contains components of: Component(id=stronglyAdapting type=izhikevichFergusonCell) 


def sint(t):
    return 1e-10*sin(t/(10*msecond))*amp

sint = Function(sint, arg_units=[msecond],
                    return_unit=amp)
 
stronglyAdapting_eqs=Equations('''
    dv/dt = ((((k * (v - vr)) * (v - vt)) + (iSyn - u)) / C) :  volt
    du/dt = (a * ((b * (v - vr)) - u)) :  amp
    v0 = -0.065 * volt : volt 
    vr = -0.0618 * volt : volt 
    vpeak = 0.0226 * volt : volt 
    vt = -0.057 * volt : volt 
    c = -0.0658 * volt : volt 
    klow = 1.0E-7 * kilogram**-2 * meter**-4 * second**6 * amp**3 : kilogram**-2 * meter**-4 * second**6 * amp**3 
    khigh = 3.3E-6 * kilogram**-2 * meter**-4 * second**6 * amp**3 : kilogram**-2 * meter**-4 * second**6 * amp**3 
    a = 1.2 * second**-1 : second**-1 
    b = 3.0E-9 * siemens : siemens 
    d = 1.0E-11 * amp : amp 
    C = 1.15E-10 * farad : farad 
    #iSyn = 1e-10*amp :  amp
    iSyn = sint(t) :  amp
    k = khigh :  kilogram**-2 * meter**-4 * second**6 * amp**3
''')


# Inputs
strongpop_iSyn = TimedArray([1e-10]*amp, dt=duration)

strongpop = NeuronGroup(1, model=stronglyAdapting_eqs, threshold = 'v > vpeak', reset = """v = c
u = u + d""")
strongpop.v = strongpop.v0
strongpop.u = 0.0
# Initialise a second time...
strongpop.v = strongpop.v0
strongpop.u = 0.0

if show_gui:

    # Display: Component(id=d1 type=Display)
    trace_d1__weaklyAdapting_v = StateMonitor(weakpop,'v',record=[0]) # weaklyAdapting v (Type: Line:  scale=0.001 (dimensionless) timeScale=0.001 (dimensionless))

    # Display: Component(id=d2 type=Display)
    trace_d2__stronglyAdapting_v = StateMonitor(strongpop,'v',record=[0]) # stronglyAdapting v (Type: Line:  scale=0.001 (dimensionless) timeScale=0.001 (dimensionless))

# Saving to file: TwoCells.dat, reference: of0
record_of0__w = StateMonitor(weakpop,'v',record=[0]) # w (Type: OutputColumn)
record_of0__s = StateMonitor(strongpop,'v',record=[0]) # s (Type: OutputColumn)

print("Running simulation for %s (dt = %s, # steps = %s)"%(duration,defaultclock.dt, steps))
run(duration)

# Saving to file: TwoCells.dat, reference: of0
all_of0 = np.array( [ record_of0__w.t, record_of0__w.v[0] , record_of0__s.v[0]  ] )
all_of0 = all_of0.transpose()
file_of0 = open("TwoCells.dat", 'w')
for l in all_of0:
    line = ''
    for c in l: 
        line = line + (' %f'%c if len(line)>0 else '%f'%c)
    file_of0.write(line+'\n')
file_of0.close()

if show_gui:

    import matplotlib.pyplot as plt

    # Display: Component(id=d1 type=Display)
    display_d1 = plt.figure("Weakly adapting PYR model 1 with 100 pA input")
    plot_weaklyAdapting_v = display_d1.add_subplot(111, autoscale_on=True)
    plot_weaklyAdapting_v.plot(trace_d1__weaklyAdapting_v.t/second,trace_d1__weaklyAdapting_v.v[0], color="#0000ff", label="weaklyAdapting v")
    plot_weaklyAdapting_v.legend()

    # Display: Component(id=d2 type=Display)
    display_d2 = plt.figure("Strongly adapting PYR model with 100 pA input")
    plot_stronglyAdapting_v = display_d2.add_subplot(111, autoscale_on=True)
    plot_stronglyAdapting_v.plot(trace_d2__stronglyAdapting_v.t/second,trace_d2__stronglyAdapting_v.v[0], color="#0000ff", label="stronglyAdapting v")
    plot_stronglyAdapting_v.legend()
    plt.show()
