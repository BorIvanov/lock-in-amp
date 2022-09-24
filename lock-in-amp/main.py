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
axis[0, 0].plot(x, y1)
axis[0, 0].set_title("real signal")
axis[0, 0].set_xlabel("time(s)")
axis[0, 0].set_ylabel("amplitude")
axis[0, 0].set_ylim(-10, 10)

# plotting the sine wave with furrier transform [1, 0]
j, q = FFT(y1, 10000)
axis[1, 0].plot(j, q)
axis[1, 0].set_title("signal FT")
axis[1, 0].set_xlabel("frequency Hz")
axis[1, 0].set_ylabel("amplitude")
axis[1, 0].set_ylim(0, 30)

# creating the reference signal ( same as the input signal freq but with amplitude of 100) [0, 1]
x, y = g_sin(t=time1, amp=5, f0=200, fs=50000, phi=0)
reference = y
axis[0, 1].plot(x, reference)
axis[0, 1].set_title("reference signal A=100")
axis[0, 1].set_xlabel("time(s)")
axis[0, 1].set_ylabel("amplitude")
axis[0, 1].set_ylim(-8, 8)

# reference signal * noisy signal [1, 1]
Am = y1*reference*reference
axis[1, 1].plot(x, Am)
axis[1, 1].set_title("Ref * Noise")
axis[1, 1].set_xlabel("time(s)")
axis[1, 1].set_ylabel("amplitude")
axis[1, 1].set_ylim(-150, 150)

# plot the signal after the bandpass [0, 2]
j, q = FFT(Am, 10000)
axis[0, 2].plot(j, q)
axis[0, 2].set_title("noisy FT")
axis[0, 2].set_xlabel("frequency Hz")
axis[0, 2].set_ylabel("amplitude")
axis[0, 2].set_ylim(0, 400)

# go trough lowpass filter to retrieve the original signal [1, 2]
b, a = sg.butter(3, (lpf_cut/nyq), 'lowpass')  # cut at 1004
real_sign = Am/12
sns = sg.filtfilt(b, a, real_sign)
axis[1, 2].plot(x, sns)
axis[1, 2].set_title("lowpass signal")
axis[1, 2].set_xlabel("time(s)")
axis[1, 2].set_ylabel("amplitude")
axis[1, 2].set_ylim(-2, 2)

# [0, 3]
j, q = FFT(sns, 10000)
#draw(j, q, 'LPF FT', 'frequency Hz', 'amplitude', 0, 30)

# Combine all the operations and display
plt.show()