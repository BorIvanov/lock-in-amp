from func import *

sampl_f = 50000
A = 10
nyq = 0.5 * sampl_f  # calculate the Nyquist frequency
low_cut = 999
high_cut = 1001
lpf_cut = 1.5
time1 = 10
fig, axis = plt.subplots(2, 3)

# creating a noisy sine wave
x, y1 = g_sin(t=time1, amp=1, f0=0.1, fs=sampl_f, phi=0)
x, y2 = g_sin(t=time1, amp=1, f0=5, fs=sampl_f, phi=0)
x, y3 = g_sin(t=time1, amp=2, f0=6, fs=sampl_f, phi=0)
x, y4 = g_sin(t=time1, amp=0.1, f0=8, fs=sampl_f, phi=0)
x, y5 = g_sin(t=time1, amp=0.7, f0=80, fs=sampl_f, phi=0)
x, y6 = g_sin(t=time1, amp=2, f0=69, fs=sampl_f, phi=0)
noise = wgn(y1, 1)
y1 = noise + y1 + y2 + y3 + y4 + y5 + y6 - y1*noise

# Creating a noisy sine wave [0, 0]
#draw(x, y1, 'real signal', 'time(s)', 'amplitude', -10, 10)
axis[0, 0].plot(x, y1)
axis[0, 0].set_title("creating a noisy sine wave")

# plotting the sine wave with furrier transform [1, 0]
j, q = FFT(y1, 10000)
#draw(j, q, 'signal FT', 'frequency Hz', 'amplitude', 0, 30)
axis[1, 0].plot(j, q)
axis[1, 0].set_title("Sine with Fourier")

# creating the reference signal ( same as the input signal freq but with amplitude of 100) [0, 1]
x, y = g_sin(t=time1, amp=5, f0=200, fs=50000, phi=0)
reference = y
#draw(x, reference, 'reference signal A=100', 'time(s)', 'amplitude', -8, 8)
axis[0, 1].plot(x, reference)
axis[0, 1].set_title("reference signal")

# reference signal * noisy signal [1, 1]
Am = y1*reference*reference
#draw(x, Am, 'Am signal', 'time(s)', 'amplitude', -150, 150)
axis[1, 1].plot(x, Am)
axis[1, 1].set_title("reference signal * noisy signal")

# plot the signal after the bandpass [0, 2]
j, q = FFT(Am, 10000)
#draw(j, q, 'noisy FT', 'frequency Hz', 'amplitude', 0, 400)
axis[0, 2].plot(j, q)
axis[0, 2].set_title("signal after bandpass")

# go trough lowpass filter to retrieve the original signal [1, 2]
b, a = sg.butter(3, (lpf_cut/nyq), 'lowpass')  # cut at 1004
real_sign = Am/12
sns = sg.filtfilt(b, a, real_sign)
#draw(x, sns, 'lowpass signal', 'time(s)', 'amplitude', -2, 2)
axis[1, 2].plot(x, sns)
axis[1, 2].set_title("OG signal after LPF")

# [0, 3]
j, q = FFT(sns, 10000)
#draw(j, q, 'LPF FT', 'frequency Hz', 'amplitude', 0, 30)


# Combine all the operations and display
plt.show()