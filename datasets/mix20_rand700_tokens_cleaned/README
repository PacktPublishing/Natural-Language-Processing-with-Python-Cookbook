
=======

Introduction

This README v1.0 (July 1, 2002) comes from the directory
http://www.cs.cornell.edu/people/pabo/movie-review-data.

Please make sure to read the "Rating Information - WARNING" section
below to determine which datasets are most appropriate for your use.

=======

Citation Info 

Some of this data was used in Bo Pang, Lillian Lee, and Shivakumar
Vaithyanathan, ``Thumbs up?  Sentiment classification using machine
learning techniques", in the proceedings of the 2002 Conference on
Empirical Methods in Natural Language Processing (EMNLP-2002).  That
paper describes some decision choices in constructing the corpora.

@InProceedings{Pang+Lee+Vaithyanathan:02a,
  author =       {Bo Pang and Lillian Lee and Shivakumar Vaithyanathan},
  title =        {Thumbs up?  Sentiment Classification using Machine Learning Techniques},
  booktitle =    "Proceedings of the 2002 Conference on Empirical Methods in Natural
Language Processing (EMNLP)",
  year =         2002
}

=======

Data Format Summary 

The original source was the Internet Movie Database (IMDb) archive of
the rec.arts.movies.reviews newsgroups at http://reviews.imdb.com/Reviews.

- movie.zip: all html files from the IMDb archive at the time we
  accessed it. A subset of these files was chosen for creating 
  training and testing corpora (see Pang et al 2002 for rationale).

- mix20_rand700_tokens.zip: contains this readme and the folder ``tokens'', 
  with the roughly 1400 processed down-cased text files used in
  Pang/Lee/Vaithyanathan 2002; the name of the two subdirectories 
  in that folder, ``pos'' and ``neg'', indicates indicates the true
  classification (sentiment) of the component files according to our
  automatic rating classifer (see Rating Decision section below).
  Preliminary steps were taken to remove rating information from the
  text files, but the process was noisy; *BE SURE TO READ THE ``RATING
  INFORMATION'' SECTION BELOW*.

  File names consist of a cross-validation tag plus the name of the
  original html file.  The three folds used in the emnlp paper
  experiments were:

     fold 1: files tagged cv000 through cv232, in numerical order
     fold 2: files tagged cv233 through cv465, in numerical order     
     fold 3: files tagged cv466 through cv698, in numerical order

  Hence the file cv114_tok-16533.txt, for example, was a part of
  fold 1, and extracted from the file 16533.html in html.zip.

- mix20_rand700_tokens_cleaned.zip: further refined versions of
 the above text files, with more filtering of rating information and 
 some further cleaning up of html tags.

=======

Rating Information - WARNING

  It is important to note that for some of the files used in our emnlp
  experiments, some rating information, such as a number of stars
  (e.g. * * * *), got through our filters, which in effect means that 
  the correct classification could be inferred from the stray 
  rating information rather than the review, which is not what is 
  intended.  The algorithms and feature sets used in
  Pang/Lee/Vaithyanathan 2002 cannot take great advantage of this
  information, because only unigram and bigram feature presence, not
  feature frequency, was employed (see the paper for more
  information).  See Appendix B for performance on the cleaned data set.

  HOWEVER, other feature selection and classification algorithms can
  potentially accidentally use the rating information in making the
  categorization decision, which would lead to artificially inflated
  results.

  Hence, IF you are using algorithms that can take advantage of stray
  rating information, YOU SHOULD USE mix20_rand700_tokens_cleaned,
  NOT THE EMNLP DATA.

  The reviews in mix20_rand700_tokens_cleaned have been
  passed through further automatic filters.  Potential sources of
  remaining errors include

      - reviews containing rating information in several places;
      
      - reviews where the range (e.g. 5-star maximum instead of 4)
        wasn't specified in an expected manner, causing a
        classification of "positive" instead of "neutral", say.  But
        since we only considered positive vs. negative sentiments, we
        do not view this as a serious issue

      - incorrect removal of extraneous boilerplate sometimes resulted
        in portions of the review due to the occurrence of unexpected
        tags. 

=======

Rating Decision (Appendix A)

This section describes how we determined whether a review was positive
or negative.

The original html files do not have consistent formats -- a review may
not have the author's rating with it, and when it does, the rating can
appear at different places in the file in different forms.  We only
recognize some of the more explicit ratings, which are extracted via a
set of ad-hoc rules.  In essence, file's classification is decided
based on the first rating we were able to identify.

- For ratings specified in stars, we assume a maximum of four stars
unless the author specified otherwise (e.g. "*** out of *****");

- For ratings specified in numbers, the maximum rating must be
specified explicitly.

- With a five-star system (or compatible number systems):
	four stars and up are considered positive, 
	two stars and below are considered negative; 
- With a four-star system (or compatible number system):
	three stars and up are considered positive, 
	one star and below are considered negative.  

We attempted to recognize half stars, but they are specified in an
especially free way, which makes them difficult to recognize.  Hence,
we may lose a half star occasionally; but this only results in 2.5
stars in five star system (1.5 stars in four star system) being
categorized as negative, which is still reasonable.


=======

Performance on data sets  (Appendix B)

- On cleaned data set (mix20_rand700_tokens_cleaned.zip)

Features	   # features    NB      ME      SVM

unigrams (freq.)	16162	79.0	n/a	73.0
unigrams         	16162   81.0    80.2   	82.9
unigrams+bigrams     	32324   80.7    80.7   	82.8
bigrams          	16162   77.3    77.5   	76.5
unigrams+POS            16688   81.3    80.3   	82.0
adjectives       	2631    76.6    77.6  	75.3
top 2631 unigrams	2631    80.9    81.3   	81.2
unigrams+position       22407   80.8    79.8   	81.8


- On original data set (mix20_rand700_tokens.zip)

We discovered a slight bug in end-of-file handling in our original Naive
Bayes code that affected (sometimes negatively, sometimes positively)
the first decimal place (i.e., tenths of a percent) of the results
reported in our EMNLP 2002 paper.  Here are the results:

		    *corrected*	   *in paper*
Features	    	NB*   	 NB	 ME   	SVM 

unigrams (freq.)	79.0	78.7	n/a	72.8
unigrams		81.5	81.0	80.4	82.9	
unigrams+bigrams	80.5	80.6	80.8	82.7
bigrams			77.3	77.3	77.4	77.1
unigrams+POS		81.5	81.5	80.4	81.9
adjectives		76.8	77.0	77.7	75.1
top 2633 unigrams	80.2	80.3	81.0	81.4
unigrams+position	80.8	81.0	80.1	81.6
