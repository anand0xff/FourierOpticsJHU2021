#! /usr/bin/env python
""" 
	matrixDFT exercising driver for Fourier Optics 2017 class
	anand@stsci.edu 2018

"""

import sys, os, time
import numpy as np
from astropy.io import fits
import poppy.matrixDFT as matrixDFT


def makedisk(s, ctr=None, radius=None):
    return make_ellipse(s, ctr=ctr, ellpars = (radius,radius,0.0))


def makegauss(s, ctr=None, sigma=None):
    # choose a pixel-centric center default for odd-sizes, pixelcornercentric for even
    if ctr is None:
        ctr = (s/2.0, s/2.0)
	
    xx = np.linspace(-ctr[0]+0.5, s-ctr[0]-0.5, s) 
    yy = np.linspace(-ctr[1]+0.5, s-ctr[1]-0.5, s)
    (x,y) = np.meshgrid(xx, yy.T)
    gauss = np.exp(-0.5*x*x/sigma - 0.5*y*y/sigma)
    return gauss


def make_ellipse(s, ctr=None, ellpars = None):
    """
    rotated ellipse function using Alex' modern array index use

    s = integer, number of pixels on a side of square array
    ellpars = (semimajor, semiminor, rotation in degrees)
    s = 20: default ctr is [10.5,10.5] in DS9, i.e. a pixel corner (even case)
    s = 21: [11.0, 11.0] in DS9, i.e. central pixel is center of ellipse
    semimajor is horiz in DS9
    rot = 30: CCW rotation, semimajor points to 2 o'clock
    """
    # choose a pixel-centric center default for odd-sizes, pixelcornercentric for even
    if ctr is None:
        ctr = (s/2.0, s/2.0)
	
    # print "s", s, "ctr", ctr
    xx = np.linspace(-ctr[0]+0.5, s-ctr[0]-0.5, s) 
    yy = np.linspace(-ctr[1]+0.5, s-ctr[1]-0.5, s)
    (x,y) = np.meshgrid(xx, yy.T)
	
    deg = -np.pi/180.0    # minus sign seen here ... any reason?  anand
    semimajor, semiminor, theta = ellpars
    esq = (x*np.cos(theta/deg) - y*np.sin(theta/deg))**2 / semimajor**2 + \
          (y*np.cos(theta/deg) + x*np.sin(theta/deg))**2 / semiminor**2
    array = np.zeros((s,s))
    array[esq<1] = 1
    return array


def example():
    """
    Generate Point Spread Functions (PSFs) of perfect circular
    unobstructed telescope using a Matrix Fourier Transform (not an FFT).
    anand@stsci.edu
    """

    # create output directory if it does not exist
    pathname = os.path.dirname(".")
    fullPath = os.path.abspath(pathname)
    odir = fullPath + '/_testMFT_odir'
    if not os.path.exists(odir):
        os.makedirs(odir)

    # instantiate an mft object:
    ft = matrixDFT.MatrixFourierTransform()
	
    #create a pupil array & write to fits file
    narray = 101
    radius = 50
    pupil = makedisk(narray, radius=radius)
    fits.PrimaryHDU(data=pupil).writeto(odir+"/pup.fits", overwrite=True)

    # create a point source's image 
    # calculate the complex amplitude and write the intensity (PSF) file out
    fov_reselt = 9 # field of view, units of lam/D
    pixperreselt = 5 # number of pixels per lambda/D resolution element
    npix = int(fov_reselt * pixperreselt)
    imagefield = ft.perform(pupil, fov_reselt, npix)
    image_intensity = (imagefield*imagefield.conj()).real
    psf = image_intensity / image_intensity.max()  # peak intensity unity

    # write a fits file of PSF
    hdu = fits.PrimaryHDU( )
    hdu.header['fov']= (fov_reselt, 'field of view in lam/D')
    hdu.header['pixelscl']= (pixperreselt, 'nr of image samples per lam/D')
    hdu.header['normaliz']= ('Unity peak', 'PSF normalization method')
    hdu.header['filter']= ('Monochromatic', 'bandpass name')
    hdu.header['src']= ('testMFT.py', 'anand0xff')
    hdu.data = psf.astype(np.float32)  # peak intensity unity
    hdu.writeto(odir+'/psf_{}.fits'.format(pixperreselt), overwrite = True)


if __name__ == "__main__":
	
    example()
