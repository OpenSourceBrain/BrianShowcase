'''
This file has been generated from a LEMS based model at http://www.opensourcebrain.org/projects/morrislecarmodel
using the Brian export function of jNeuroML: https://github.com/NeuroML/jNeuroML


Brian simulator compliant Python export for:

Components:
    ml1 (Type: morrisLecarCell:  C=20.0 (none) I=65.0 (none) gL=2.0 (none) gCa=4.0 (none) gK=8.0 (none) VL=-50.0 (none) VCa=100.0 (none) VK=-70.0 (none) V1=0.0 (none) V2=15.0 (none) V3=10.0 (none) V4=10.0 (none) phi=0.1 (none) SEC=1.0 (SI time))
    net1 (Type: network)
    sim1 (Type: Simulation:  length=220.0 (SI time) step=0.05 (SI time))

'''
from brian import *

from math import *

# Adding simulation Component(id=sim1 type=Simulation) of network: net1 (Type: network)
#    Population ml1pop contains components of: Component(id=ml1 type=morrisLecarCell) 

SEC = 1.0 * second 
C = 20.0 
I = 65.0 
gL = 2.0 
gCa = 4.0 
gK = 8.0 
VL = -50.0 
VCa = 100.0 
VK = -70.0 
V1 = 0.0 
V2 = 15.0 
V3 = 10.0 
V4 = 10.0 
phi = 0.1 

ml1_eqs=Equations('''
    dV/dt = (I - IL - ICa - IK) / (C * SEC) : 1
    dN/dt = phi * (Nss - N) / (tauN * SEC) : 1
    Mss = 1 / (1 + exp(-2 * (V - V1) / V2)) : 1
    Nss = 1 / (1 + exp(-2 * (V - V3) / V4)) : 1
    tauN = 2 / (exp((V - V3) / (2 * V4)) + exp(-(V - V3) / (2 * V4))) : 1
    IL = gL * (V - VL) : 1
    ICa = gCa * Mss * (V - VCa) : 1
    IK = gK * N * (V - VK) : 1
''')

ml1pop = NeuronGroup(1, model=ml1_eqs)
ml1pop.V = VL
ml1pop.N = 1 / (1 + exp(-2 * ( VL - V3) / V4))

# Display: Component(id=d1 type=Display)
trace_d1_fn1 = StateMonitor(ml1pop,'V',record=[0]) # fn1 (Type: Line:  scale=1.0 (???null) timeScale=1.0 (???null))

# Display: Component(id=d2 type=Display)
trace_d2_fn1 = StateMonitor(ml1pop,'IL',record=[0]) # fn1 (Type: Line:  scale=1.0 (???null) timeScale=1.0 (???null))
trace_d2_fn2 = StateMonitor(ml1pop,'IK',record=[0]) # fn2 (Type: Line:  scale=1.0 (???null) timeScale=1.0 (???null))
trace_d2_fn3 = StateMonitor(ml1pop,'ICa',record=[0]) # fn3 (Type: Line:  scale=1.0 (???null) timeScale=1.0 (???null))

# Display: Component(id=d3 type=Display)
trace_d3_fn1 = StateMonitor(ml1pop,'N',record=[0]) # fn1 (Type: Line:  scale=1.0 (???null) timeScale=1.0 (???null))

defaultclock.dt = 0.05*second
run(220*second)

# Display: Component(id=d1 type=Display)
figure("Fig 6 from Morris and Lecar 1981: membrane potential")
plot(trace_d1_fn1.times/second,trace_d1_fn1[0], color="#000000")

# Display: Component(id=d2 type=Display)
figure("Currents: IL, IK & ICa")
plot(trace_d2_fn1.times/second,trace_d2_fn1[0], color="#4444FF")
plot(trace_d2_fn2.times/second,trace_d2_fn2[0], color="#FF22FF")
plot(trace_d2_fn3.times/second,trace_d2_fn3[0], color="#FF0000")

# Display: Component(id=d3 type=Display)
figure("N value")
plot(trace_d3_fn1.times/second,trace_d3_fn1[0], color="#4444FF")
show()
