# FourierOpticsJHU2021
Anand Sivaramakrishnan,  anand@stsci.edu
Laurent Pueyo, pueyo@stsci.edu

First class 1:30-2:45 pm Tuesday Aug 31 2021,  Bloomberg 511.  We will arrange a double slot that suits everyone then, and meet once a week from there on.  The first class will likely not last the full period.


#### Course Content

We focus on the practical application of Fourier transforms in modern
observational astronomy.  Fourier transforms provide a framework for
understanding much of astronomical instrumentation and its observational
methods: imaging cameras, spectrographs, coronagraphs, interferometers,
time-series analysis, correlation methods, filtering, and many object detection
methods.  We will treat direct and synthetic imaging, discussing instruments
that span the electromagnetic spectrum from radio to ultraviolet.

### Course requirements

#### Textbook

1. The best textbook for this class is still:

     R.N. Bracewell, "The Fourier Transform and Its Applications" (Third Edition, Mcgraw-Hill, 2000).

   This book is unfortunately out of print and has been so for some time. The
   remaining stock is expensive. If you can find a copy somewhere, borrow it,
   or buy it second-hand if you can.  This book is very good, and former
   versions of this class used it extensively.
   If you can obtain a copy in any format it will be a valuable reference for you in the
   future. Some assigned reading and problem sets will come from this book.
   
2. Useful background paper:
  
     John D. Monnier & Ronald J. Allen, "Radio & Optical Interferometry:  Basic
   Observing Techniques and Data Analysis".

   This is Chapter 7 of Volume 2 from an (outrageously) expensive anthology titled
   "Planets, Stars and Stellar Systems", published in late 2012 by Springer. Our
   chapter treats interferometry both in optical/IR astronomy and in radio
   astronomy from a unified viewpoint, focusing on the physical foundations and
   the corresponding practical issues that beginning researchers need to know.
   Available as a preprint on astro-ph at:  http://arxiv.org/abs/1201.2963
 
   
3. Articles:  Mostly via ADS.
  

#### Course structure:

   This course meets weekly. If you are taking this course for credit, 
   regular attendance and in-class participation is expected.  Unavoidable
   absences (such as observing runs) should be discussed with us beforehand.

   
#### Grade

  There will be no tests and no final exam for this course. Your grade for this
  course will be determined by equally weighted contributions from:

- Participation in the discussion of the problem sets attempted before class
- Turning in homework post-discussion
- Oral presentation and term paper


#### Problem sets and assigned reading - homework first, lecture second
#####  (We can change this for 2021 class - I just copied this section as well)

In the earlier part of the course we will assign problem sets and/or reading
that must be attempted and/or done ** before the next class **.
The goal of your reading is to acquiant you with the relevant ideas, framework,
vocabulary, and formalism.  The problems then give you an opportunity to try working
these before the lecture.

1. Attempt every problem before class. This prep work is essential for
   the ** in-class discussion amongst yourselves and with us** 
   early in the class.
   Air your confusion/clarity on concepts and details, and help each other.
   Discussion is part of learning in the class.  
   
3. Complete your homework and turn it in by the start of the following class
   (email to ** jhu.fourieroptics@gmail.com ** or hardcopy).
   Before class ends we will assign the pre-class homework for the following class, 
   until we drop homework for your term paper preparation.

#### Term Paper and Oral Presentation:

  A term paper is required.  Topics will generally be taken from the
  historical/research literature on coronography, interferometry, and aperture
  synthesis in radio and optical astronomy.  You may suggest your own topic.
  **The subject matter must be approved by Anand and Laurent**.

  Choose your topic early in the class; first full drafts are due before
  the Thanksgiving break, and ought to be 4 - 5 pages long (single-spaced) plus
  figures. You may use any text processor/formatter you please, but if you have
  no preference, use LaTeX2e with a "class" file from one
  of the common astronomy journals (e.g. aastex.cls).

  A stand-up presentation on the topic of your term paper is required.
  You will have about 30 minutes to present and respond to questions 
  from the audience.
  We will do this in the last class.

  ** Start discussing topics as early as possible **

#####  Term paper milestones (week starting on dates below)
+ Topic with suggested section titles
    - Due week of Class #4.  Sep 20.  
	- What is the tie in to course matter? E.g., Appropriate survey/new ideas?
	- Potentially publishable? (start discussing early)
+ Rough draft 2-3 pages
    - Due week of Class #6.  Oct 04.    
	- Demonstrate relevance, feasibility
	- Almost final section definitions, section entries with substance/detailed plan
+ First full draft submission, 4-5 pages.  Nov 19.  
	- Before Thanksgiving break
+ Final paper due at presentation.  Nov 29.  

### Class Schedule
Mondays of the week are used here - in the first scheduled class we decide on which day of the week we meet for 2h 30 min (with a short break in the middle)
We will have a couple of guest lectures from active specialists.

| Date   | Class #  | Notes    | Topics                                                                   |  Homework
|:------:|:-------:|-----------|--------------------------------------------------------------------------|-----------------------------------------------------------|
|Aug 31  | #1      |Anand      | Course structure, meeting date, martixdft & hcipy,  pocket interferometer, coherence, FT defs   |   upload, run a test DFT, testhcipy
|Sep 06  | #2      |Laurent    | Justify Fourier transform, using sky-telescope aperture    |    dft:sampling, aliasing, numpix variation,... , prep for Fourier thms show&tell
|Sep 13  | #3      |Laurent    | Image formation for 'one dish' telescope                   |    ?
|Sep 20  | #4      |Laurent    | Image formation for long baseline interferometer           |   Labeyrie interferometer numerical example?
|Sep 27  | #5      |Jens       | (A away 27-30)  NRM+KP principles, (reduction example?)    |   Test analysis of binary w/CANDID or Jens' pkg?
|Oct 04  | #6      |Anand      | Lyot principles, BLC 'perfect' grey APLC                   |   student CoDR reviews of BLC, FQPM Self-coherent, vortex, Bracewell Nuller
|Oct 11  | #7      |Anand      | CoDR RFA student micro-presentations/discussion                             |       
|Oct 18  | #8      |Anand      | TBD                            |       
|Oct 25  | #9      |Anand/Laurent   | TBD                       |       
|Nov 01  | #10     |Laurent    | TBD                            |       
|Nov 08  | #11     |Laurent    | TBD                            |       
|Nov 15  | #12     |           | TBD                            |       
|Nov 24  |         |	       | THANKSGIVING                   |       
|Nov 29  | #13     |Class      | Term paper presentations       |       


### On-line course evaluation:  NEED CURRENT INFORMATION

The 2018 class used: 

	From: ASEN Course Evals <ASENCourseEvals@jhu.edu>
	Date: Monday, November 19, 2018 at 12:05 A
	Subject: Teacher Course Evaluations are Now Available for Fall 2018 Term!
 
	Fall 2018 teacher course evaluations are now available for your students to complete online. They will receive an email asking them to complete a short 10-15 question survey for each of the following courses in which they are enrolled:
	
	- Any Arts & Sciences (AS) course section with a minimum enrollment of at least 5 undergraduate students. All AS independent study, research, and internship based courses are excluded regardless of the number of students enrolled.
	
	- Any Engineering (EN) course with a minimum enrollment of at least 5 students. All EN department seminar, independent study, research, and internship based courses are excluded regardless of the number of students enrolled.

	Each evaluation should take approximately 5-10 minutes to complete.
