
# coding: utf-8

# In[ ]:


#Q1-1


# In[9]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
T = 1
k = 0.082
N = 1
b = 0.1
a = 0.1
#P = np.arange(0.01, 2.0, 0.01)
V = np.linspace(0.11, 2, 200)
P = (N*k*T)/(V-b*N)-a*((N/V)**2)

V1 = np.linspace(0.11, 2, 200)
P1=T/V1

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure() and then ax = fig.add_subplot(111)
fig, ax = plt.subplots(figsize=(10,10))

ax.plot(V, P, '-*r', label='van der Waals gas')

ax.set(ylabel='P (some unit)', xlabel='V (some unit)',
       title='PV curve for van der Waals gas, T=1')
ax.legend()
ax.grid()

fig.savefig("test.png")
plt.show()


# In[ ]:


#Q1-2


# In[8]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
T = 1
k = 0.082
N = 1
b = 0.1
a = 0.1
#P = np.arange(0.01, 2.0, 0.01)
V = np.linspace(0.11, 2, 200)
P = (N*k*T)/(V-b*N)-a*((N/V)**2)

V1 = np.linspace(0.11, 2, 200)
P1=T/V1

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure() and then ax = fig.add_subplot(111)
fig, ax = plt.subplots(figsize=(10,10))

ax.plot(V, P, '-*r', label='van der Waals gas')

ax.plot(V1, P1, '-*y', label='ideal gas')

ax.set(ylabel='P (some unit)', xlabel='V (some unit)',
       title='PV curve for van der Waals gas, T=1')
ax.legend()
ax.grid()

fig.savefig("test.png")
plt.show()


# In[ ]:


#Q1-3


# In[10]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting

T = 3.613
k = 0.082
N = 1
b = 0.1
a = 0.1
#P = np.arange(0.01, 2.0, 0.01)
V = np.linspace(0.11, 2, 200)
P = (N*k*T)/(V-b*N)-a*((N/V)**2)
Tc= 8*a/(27*b*k)
T1 = 1
V1 = np.linspace(0.11, 2, 200)
P1 = (N*k*T1)/(V1-b*N)-a*((N/V1)**2)

T2 = 6
V2 = np.linspace(0.11, 2, 200)
P2 = (N*k*T2)/(V2-b*N)-a*((N/V2)**2)
# Note that using plt.subplots below is equivalent to using
# fig = plt.figure() and then ax = fig.add_subplot(111)
fig, ax = plt.subplots(figsize=(10,10))

ax.plot(V, P, '-*r', label='T=3.613,T=Tc')
ax.plot(V1, P1, '-*b', label='T=1, T<Tc')
ax.plot(V2, P2, '-*y', label='T=6, T>Tc')

ax.set(ylabel='P (some unit)', xlabel='V (some unit)',
       title='PV curve for different T')
ax.legend()
ax.grid()

fig.savefig("test.png")

plt.show()


# In[ ]:


#Q1-4


# In[12]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
T = 3.6
k = 0.082
N = 1
b = 0.1
a = 0.1
#P = np.arange(0.01, 2.0, 0.01)
V = np.linspace(0.05, 0.15, 200)
P = (N*k*T)/(V-b*N)-a*((N/V)**2)

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure() and then ax = fig.add_subplot(111)
fig, ax = plt.subplots(figsize=(10,10))

ax.plot(V, P, '-*r', label='T=3.6')
#ax.plot(V1, P1, '-*b', label='T=0.1, T<Tc')
#ax.plot(V2, P2, '-*y', label='T=0.1, T>Tc')

ax.set(ylabel='P (some unit)', xlabel='V (some unit)',
       title='PV curve, peculiar')
ax.legend()
ax.grid()

fig.savefig("test.png")
plt.show()


# In[ ]:


# This singular point is caused by equ:P = (N*k*T)/(V-b*N)-a*((N/V)**2).
# At some value of V, the demominator in thefirst term will be 0 so there is a singular point occurs.
# Or you can say this value is the minimum of the volume of this van der Waals fluid.


# In[ ]:


#Q1-5


# In[15]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

T = [3,3.6,4]
V = np.linspace(0.15, 20,501)
k = 0.082
N = 1
b = 0.1
a = 0.1
col = ['-*r','-*g','-*b','-*w','-*b']
#µ-P diagram for different T
fig3,ax = plt.subplots(figsize=(10,10))
for i in range(len(T)):
    u = np.zeros(len(V))
    P = (N*k*T[i])/(V-b*N)-a*((N/V)**2)
    for j in range(len(V)-1):
        u[j+1] = u[j] + V[j] * (P[j+1]-P[j])
    ax.plot(P,u,label =('T=',T[i]))
    ax.legend()
    ax.grid()


ax.set(xlabel = 'P(some unit)', ylabel = '$\mu$(some unit)',title ='$\mu$-P diagram')
fig3.savefig("fig3.png")

plt.show()

