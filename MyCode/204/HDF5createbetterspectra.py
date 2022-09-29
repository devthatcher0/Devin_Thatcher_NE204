import h5py
import numpy as np

filelocation = input("Enter file location: ")
filelocation = filelocation.strip('"')
with h5py.File(filelocation, 'r') as f:
    data = np.array(f['raw_data'])
    spectra = []
    for a in range(np.size(data, 0)):
        pulse = data[a, 950:1100]
        baseline = data[a, :950]
        pulsemax = np.amax(pulse)
        pulsemin = np.average(baseline)
        pulseheight = pulsemax - pulsemin
        if pulseheight < 500:
            spectra.append(pulseheight)
    with open('spectradata.npy', 'wb') as f2:
        np.save(f2, np.array(spectra))