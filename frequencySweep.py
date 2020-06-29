import matplotlib.pyplot as plt
import math

def frequencyAndPwmSweep(startf, stopf, duration, dc, sps=10000):
    deltaf = stopf - startf
    samples = sps * duration
    time = [t for t in range(samples)] # time changing over time (lol)
    phase = [(startf * (t / sps) + deltaf * ((t / sps)**2 / 2) / duration) % 1 for t in time] # phase changing over time, from 0 to 1
    signal = [math.sin(2 * math.pi * p) for p in phase]
    pwm = [0 if p > dc else 1 for p in phase]
    return (time, signal, pwm)

startf = 1
stopf = 5
duration = 2
dc = 0.3

t, s, p = frequencyAndPwmSweep(startf, stopf, duration, dc)
plt.plot(t, s)
plt.plot(t, p)

plt.show()