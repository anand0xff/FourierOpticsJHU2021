### 171.755 Class 6: Anand

#### Admin 

####  Term paper topic & title/definition:  

I am available for discussion any day the rest of the week.  We can meet in Bloomberg 206 (or on the patio) to finalize the titles/topics.  Set up a time, if needed, by email (anand@stsci.edu).

+ title/topic definition  
	- What is the tie in to course matter? E.g., Appropriate survey/new ideas/explanation of something interesting?
	- Is it potentially publishable?  
+ Section headings, with a sentence or two describing the section content. 
+ Rough draft 2-3 pages
   - Due week of Class #7, Friday Oct 15.    
	- Demonstrate relevance, feasibility
	- Almost final section definitions, section entries with substance/detailed plan
+ First full draft submission, 4-5 pages.  Nov 19.  
	- Before Thanksgiving break
+ Final paper due at presentation.  Nov 29.  

####  "Office hours" in Bloomberg 206 (arrange by email)

####  Two nulling interferometers
[Bracewell  nuller](https://ui.adsabs.harvard.edu/abs/1978Natur.274..780B/abstract)  Principle.  
[Angel & Woolf](https://ui.adsabs.harvard.edu/abs/1997ApJ...475..373A/abstract). Improvement. 
	

#### Perfect & imperfect high dynamic range coronagraphs
Perfect:   
[Phase maskcoronagraph](https://ui.adsabs.harvard.edu/abs/1997PASP..109..815R/abstract)
[Band-limited coronagraph](https://ui.adsabs.harvard.edu/abs/2002ApJ...570..900K/abstract). "inside out interferometer".  
[Vortex coronagraph](https://ui.adsabs.harvard.edu/abs/2005ApJ...633.1191M/abstract).  
[Four quadrant phase mask coronagraph](https://ui.adsabs.harvard.edu/abs/2000PASP..112.1479R/abstract)

Imperfect but widespread:  
[Apodized pupil Lyot coronagraph](https://ui.adsabs.harvard.edu/abs/2002A%26A...389..334A/abstract)



#### Speckles in high contrast images


[Speckle Decorrelation and Dynamic Range in Speckle Noise-limited Imaging](https://ui.adsabs.harvard.edu/abs/2002ApJ...581L..59S/abstract).   
[The Structure of High Strehl Ratio Point-Spread Functions](https://ui.adsabs.harvard.edu/abs/2003ApJ...596..702P/abstract).  
 [Low-Order Aberrations in Band-limited Lyot Coronagraphs](https://ui.adsabs.harvard.edu/abs/2005ApJ...634.1416S/abstract)


#### Homework from Class 6:

**Pencil and paper**. To do this homework you will need some of the symmetry  properies of the transforms of real functions.  

First, show that the Fourier transform of a real function is Hermitian.

Next, convince yourself that the integral of a function over one domain is the value of its transform at its origin in the  other domain.  We did this in class as soon as we had the FT definition written on the board.

In Class6/SpeckleExpansion\_math.pdf:   
	- Derive Equation 8, starting from the three terms in Equation 7 multiplied by the pupil field function A(x)  
	- The first order term (equation 10) has an "i" multplying everything in it.  Convince yourself that this term is real, in spite of that "i".  
	-  What  is the noise implication of the "pinned" speckle term p1 for high contrast imaging?
	-  Is the second order halo term zero at a location  in the image in k-space where a(k) = 0 (e.g. in a dark Airy ring)?  So is the ASF a multiplying factor in the second order halo term?
	-  The RHS of equation 15 is unclear - it has the variance of  the  phase error (technically it should read   
	"-\epsilon^2 {\sigma_\phi}^2)"   

**Running and playing with code**  After class I will push a few drivers  that use the uils.py on the repo.  These will create phase ripple aberrations over circular apertures.    Investigate the behavior of single phase ripple errors - sines, cosines (symmetric & antisymmetric), arbitrary sinusoids, with various amplitudes (in radians).  "Smmall is of course << 1 raadian.  Large is up to a radian or so ripple amplitude.  Two different ripples show curious interractions.

When displaying PSFs, use a fractional power, such  as 0.1, or slightly larger, to see  PSF structure clearly.  I expand the plots for clarity, so you will see rings and speckles clearly. 
