### 171.755 Class 6: Anand.  Speckle noise, high suppression (planet-imaging)

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

####  "Office hours" in Bloomberg 206 (arrange by email). 
#### Airy pattern units can be confusing...   
I found this concise and clear clear definition of the [Airy pattern's arguments](http://web.ipac.caltech.edu/staff/fmasci/home/astro_refs/PSFtheory.pdf)



#### Speckles in high contrast images  
[Speckle Decorrelation and Dynamic Range in Speckle Noise-limited Imaging](https://ui.adsabs.harvard.edu/abs/2002ApJ...581L..59S/abstract).   
[The Structure of High Strehl Ratio Point-Spread Functions](https://ui.adsabs.harvard.edu/abs/2003ApJ...596..702P/abstract).  



#### Fourier joke:

The mean tilt of a wavefront across an apertture does what to the intensity centroid of the image?  It's actuallly a "theorem" in optics - I refer to it in a [1995 speckle paper](https://ui.adsabs.harvard.edu/abs/1995AJ....110..430S/abstract), the reference is [Tyler 1994](https://ui.adsabs.harvard.edu/abs/1994JOSAA..11..358T/abstract).  Explore steps of phase across the apertture.  Where does aliiasing come in to confuse the limit?


#### 0. Homework from Class 6:

**Pencil and paper**. To do this homework you will need some of the symmetry  properies of the transforms of real functions.  
Last week: show that the Fourier transform of a real function is Hermitian, annd working on symmetry of FTs,, application to first order speckles.  
Exercises in psf expansion symmetries, effects on morphology, and Strehl raatio

**Running and playing with code**    
- Single ripple -- increasing amplitude?  
- Two  ripples -  interaction?  Big ripples?  A zillion ripples?
**Discuss**. 

#### 1: Smoothnesss  of function vs. asymptotic behaviour  of transform

Top hat transform decays as 1/k.  
hat * hat ~ 1/k^2.   
hat * hat * hat ~ 1//k^3   
Jinc ~ 1/k^(-3.2),  so  Airy PSF (intensity) ~ 1/k^3 so Encircled energy ~ 1/.  
** Integrral is C^0 function ~ transform asymptoticallly 1/k. C^n integral -> transform ~1/k^n. (C: Lipschitz continuity)**   

#### 2: Smoothness of aperture boundary

Compare square pupil  with  circular pupil.  Curvature of boundary.  Develop "Shaped pupil" for very dark areas of PSF.   [Jaquinot \& Roizen-Dossier](https://ui.adsabs.harvard.edu/abs/1964PrOpt...3...29J/abstract),   [Nisenson \& Papaliolios](https://ui.adsabs.harvard.edu/abs/2001ApJ...548L.201N/abstract),   [Kasdin et al.](https://ui.adsabs.harvard.edu/abs/2003ApJ...582.1147K/abstract).

#### 3: Aliasing, Spatially filtered wavefront sensing   

#### 4: Wavefront aberrration effects on shaped pupils?
flip side - field stops!

#### 5: Apodized pupils:  PSF, FWHM, speckle behaviour 



