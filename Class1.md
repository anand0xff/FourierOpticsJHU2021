### 171.755  Fourier Optics Class #1
###  Intro, requirements, class software, scalar field, far field

**Introductions: Anand, Laurent, students**.  
**Class roster:	Personal name, family name, supervisor & topic (?), preferred email**. 
**Course outline on github anand0xff**

#### Soon after Class #1, and before Class #2, you need to have the following: 

- anaconda with python 3.8 on your laptop into a conda envirionment (I call mine py38)
- install astropy using conda
- Install [poppy](https://poppy-optics.readthedocs.io/en/stable/installation.html).  We only use it's matrixDFT routine (see code/testMFT.py) to explore numerical transforms.
- Install [hcipy](https://github.com/ehpor/hcipy), which implements physical units in optics nicely (and more)
- Reading and writing FITS files (using astropy.io.fits)
- Familiarity with DS9, image display stretches (sqrt, linear, log,..) and e.g
  matplotlib's imshow and plotting, or equivalent.  samplePSF.fits provided.
- a github account and an accepted invitation to join this repo.

After class, finish the problem sets associated with the class and turn in a
pdf file of your work by emailing it to jhu.fourier@gmail.com

- **This address is only for the homework files**. For anything else,
contact Anand or Laurent by email, or in person.
- **We are unsure of how much time the assigned work will require**, so early feedback is welcome.
	
	

We will often assign problem sets and/or reading - 
attempt the problems and read the material **before the next class**.
The goal of your reading is to acquiant you with the relevant ideas, framework,
vocabulary, and formalism.  The problems then give you an opportunity to try working
these before the lecture.  In class discussion of the assigned reading is likely.

We understand absences due to observing or other factors, and will help you catch up.

-

### Class 1: Theoretical and numerical Fourier machinery 
#### The 5-cent tour in this class here  - to be covered in depth later

**Remember the goal of the pre-class work is to think about the
  concepts/questions, you are not expected to have complete answers ready for the 
  in-class discussion.**

- We aim to unify theoretical and numerical views of Fourier optics.  These
  will be examined in much more depth in later classes.
- We will mention the mathematical definition of the Fourier transform and link
  it to an important property of an optical system.
- We set up code to calculate the response of an optical telescope to an
  infinitely distant, monochromatic, unpolarized  point source.


#### Theoretical work in preparation for Class #2
	
Look up concepts of Fourier transforms and Fourier optics, and [re]familiarize
yourself with the key concepts/phrases in this section.
##### The 1-dimensional Fourier transform of a function f(x)

   Write down one of the forms of the forward and reverse transforms, and think
   about the nature of the forward transform formula.  I refer to the two
   domains' coordinates as x and k, often interpreted as spatial and spatial
   frequency (or time and frequency)  coordinates.  In quantum mechanics k is
   thought of as a momentum space.  (Bracewell p6, or this link to a [pdf from
   a
   course](https://www2.ph.ed.ac.uk/~wjh/teaching/Fourier/documents/properties.pdf)
   at Cambridge)
	
   What kind of 1-d functions (real, complex, ...) are amenable to being
   transformed?  Here I use the notation f(x) for the function F(k) for its
   forward transform.  (This is a quick overview, we're not looking for all the
   mathematical prequisites of the function)
    
   Are the domains of f and F (the spaces that x or k live in) real or complex?

   Are f and F, deep down, equivalent descriptions of the same information?
   Does the Fourier transform of a function lose informaton that was present in
   the original function?   What's the clinching argument that supports your
   conclusion?
	
##### Incoherent vs. coherent emission of light from distinct points an extended object.

   Does an atom on one side of a (non-rotating) star emit spectral line
   radiation in phase with (coherent with) another atom of the same element on
   the other side of the star, both emitting light in the same spectral line?
   Do the two atoms communicate with each other to collaborate on releasing
   radiation coherent with each other? How is this different from a gas in a
   laser cavity where many atoms contribute to coherent radiation?

 **We only consider looking at objects made up of points that do not radiate
    coherently with respect to other points of the object.**
    
    
##### Fraunhofer or far field diffraction 

   Diffraction of a monochromatic unpolarized plane wave (e.g. from a distant
   unreolved star) through an aperture, and the "Fresnel length" that helps
   decide when the far field (a.k.a. Fraunhofer) limit calculations are valid.  

   What are the physical units of coordinates in the **aperture** plane?  The
   image plane?  (Recall that you're "taking a picture of a point-like star"
   here).  Also note that the terms aperture and **pupil** are used
   interchageably here.


   We assert that the far field diffraction pattern (its ** image plane field
   strength ** is the Fourier transform of the wave's field strength in the
   aperture plane.  We'll derive this later.

   What is the diffraction limit or [angular] resolution of a telescope?  In a
   perfect image from a circular telescope, the intensity is described by an **Airy disk**.  The first zero of this azimuthally symmetric function occurs
   at a radius of 1.22.  How does this translate into a real-world perfect
   image at a given wavelength, with a particular telescope diameter?

   Describing light numerically/mathematically: a plane wave of monochromatic
   light (in a homogenous or non-dispersive medium or vacuum, with spatial
   coordinates (x,y,z) is a propagating oscillation of the electric and magnetic
   fields.  
   
   One of the fields - let's say the electric field,  can be expressed by the
   real part of a complex number that has a (real) **amplitude**  A and a
   unit-strength **phasor** exp(i(kz - wt + phi(x,y))).  Here we use w
   instead of the usual Greek omega. phi(x,y) is the (real) **phase**
   (out-of-plane corrugation) of the **wavefront**.  A wavefront is a
   surface of constant phase.  The wave moves in the z direction at
   speed w/k (why is that so? What is actually moving?).
   Wikipedia has a nice [animated review](https://en.wikipedia.org/wiki/Plane_wave)
   of this.

   We often drop the "purely propagating" multiplicative factor, exp(i(kx - wt)),
   of the phasor, and just work on the in-plane phase disturbances exp(i
   phi(x,y)).  This will be justified later.  With this shorthand the wave's 
   ** complex amplitude ** is written  A exp(i phi(x,y)).
    
   What mathematical/numerical operation must you perform on a complex array
   describing the wave's complex amplitude to get a real array proportional to
   the intensity (brightness) that a CCD or IR array might detect?
			
   The concept of the pupil (or aperture) plane of an optical system (in the
   x,y plane), and its illumination by monochromatic light from a distant star.
   One resource is [ApJ vol.  552 pp.397-408,
   2001](https://ui.adsabs.harvard.edu/#abs/2001ApJ...552..397S/abstract)
   Section 2.1 equation 1 and surrounding very short text.
	
   Describing the pupil quantitatively (e.g. equation 2 of the above paper):  if
   you create a numpy array that represents a circular aperture telescope
   without a secondary obstruction, what are the physical dimensions you assign
   (in your mind) to this in-memory array --- what physical thing does the
   numerical array span?  What physical quantity is represented by a complex
   number (an element) of this numerical array?
   
   
   	
   **Numerical Exercise 1: familiarity with matrixDFT (see testMFT.py)** 
   
   Create a real 2-D 100 x 100 pupil array
   (e.g. by using makedisk() from TestDFT.py), unity over a
   circular pupil, zero elsewhere, and a zero-filled
   real phase array of the same size.  Call makedisk() with radius=50.0
	
   Create a complex array representing the "complex amplitude" of a flat wave
   arriving at the pupil from a 'straight-on' (i.e. on-axis) very distant
   source (phase=0 everywhere): 
	
   	pupilarray = pupil * np.exp(1j * phase)
	# Calculate the Fourier transform of pupilarray:

  	import poppy.matrixDFT as matrixDFT
  	mft = matrixDFT.MatrixFourierTransform()
  	imagefield = mft.perform(pupilarray, focalplane_size, focalplane_npix)
  	
  
  	### the pupil field is complex ###
  	### the image field is complex ###
  	### ALL FIELDS ARE COMPLEX.    ###  even if they have zero imaginary values
  	### INTENSITY is REAL, >= 0    ###
	    
   using 100 and 400 for focalplane_size (in resolution elements lambda/D, implicit) and focalplane_npix (pur number, integer).  Write the
   imagefield absolute value and phase (the np_array.angle property) into a
   2-slice fits cube (for example)  and look at them.  
   
   I count two reals, p and q, in one complex python number p+1j*q

- How many distict real numbers are there in an arbitrary complex pupilarray?
- How many real numbers are in the imagefield complex array in the two cases
  you just calculated?

-  How do you calculate the image intensity array from the imagefield array
   (in python)?  All the image intensity array's elements are, of course, positive or zero.
	
-  What physical dimensions do you give to the image array sample pitch
   (incorrectly but frequently called 'image pixel size')?  It helps to know
   the theoretical structure of a perfect point spread function of a circular
   telescope.  Remind yourself of the term "resolution limit" from the
   theoretical part above.

