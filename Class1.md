### 171.755  Fourier Optics Class #1
###  Intro, requirements, class software, scalar field, far field

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

