import numpy as np
from scipy.fftpack import fft
from scipy import signal as sg
from matplotlib import pyplot as plt


def draw(x, y, title, xlable, ylable, L, H):
    '''
    draw
    Parameters
    ----------
    x : numpy array
    abscissa
    y : numpy array
    ordinate
    Returns
    -------
    '''
    # canvas settings
    plt.close()
    if L != H:
        plt.ylim(L, H)
        plt.title(title)
        plt.xlabel(xlable)
        plt.ylabel(ylable)
        plt.plot(x, y)
        plt.grid()
        plt.show()


def g_sin(t, amp, f0, fs, phi):
    '''
    generate sinusoid
    Parameters
    ----------
    t : float
    time length of the generated sequence
    amp : float
    amplitude
    f0 : float
    frequency of sinusoid in Hz
    fs : float
    sampling rate per second
    phi : float
    initial phase in deg
    Returns
    -------
    anonymous : list[numpy array, numpy array]
    [abscissa, a sinusoid signal]
    '''
    T = 1/fs
    N = t/T
    x = 2*np.pi*np.arange(N)*T
    return [np.arange(0, t, T), amp*np.sin(f0*x+phi*np.pi/180)]


def g_square_wave(t=1, amp=1, f0=10, fs=500, K=50):
    '''
    generate square wave
    Parameters
    ----------
    t : float
    time length of the generated sequence
    amp : float
    amplitude
    f0 : float
    frequency of sinusoid in Hz
    fs : float
    sampling rate per second
    K : int
    order of fourier series
    Returns
    -------
    anonymous : list[numpy array, numpy array]
    [abscissa, a square wave]
    '''
    T = 1/fs
    N = t/T
    x = 2*np.pi*np.arange(N)*T
    y = np.zeros(len(x))
    k = 2*np.arange(1, K)-1
    for i in range(len(x)):
        y[i] = amp*np.sum(np.sin(k*f0*x[i])/k)
    return [np.arange(0, t, T), 4*y/np.pi]


def FFT(s, fs):
    '''
    fast fourier transform
    Parameters
    ----------
    s : numpy array
    signal
    fs : float
    sampling rate per second
    Returns
    -------
    '''
    X = fft(s)
    mX = np.abs(X)  # magnitude
    pX = np.angle(X)  # phase
    return [np.arange(int(fs/2)), mX[range(int(fs/2))]/fs]
    # draw(np.arange(int(fs/2)), mX[range(int(fs/2))]/fs,
    # 'Input signal in frequency domain', 'frequency(Hz)', 'amplitude', 0, 0)


def wgn(x, snr):
    '''
    generate Gauss white noise
    Parameters
    ----------
    x : numpy array
    signal
    snr : float
    signal-to-noise ratio
    Returns
    -------
    anonymous : numpy array
    Gauss white noise
    '''
    snr = 10**(snr/10.0)
    xpower = np.sum(x**2)/len(x)
    npower = xpower / snr
    return np.random.randn(len(x)) * np.sqrt(npower)
