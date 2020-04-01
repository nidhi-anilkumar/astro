from astropy.io import fits
import matplotlib.pyplot as plt

hdus = fits.open('')
plt.plot(hdus[0].data)
plt.savefig('')