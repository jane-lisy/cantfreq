# Word Frequencies Database Overview
This README file describes the structure and contents of the Word Frequencies data file. The data file was created so that all of the word frequency data in Li, Badrulhisham, & Alderete (2020) can be verified and explored independently. The data file is essentially a large data table in which the rows are words and the columns are fields that give information about the words, like its frequency in some corpus. The rest of this document simply describes content of the fields named in the column headers.
## Field Contents
- **OrthographicRepresentationTraditional**  
Standard orthographic representation of a word using traditional Chinese characters or transliterated words (for words without standard characters). The words from IARPA have been converted to traditional characters with HanziConv (Yue, 2016).

- **OrthographicRepresentationSimplified**  
Standard orthographic representation of a word using simplified Chinese characters or transliterated words (for words without standard characters). The words from HKCAC and HKCanCor have been converted to simplified characters with HanziConv (Yue, 2016).

- **PhonologicalRepresentationJyutping**  
The Jyutping representation of the word, as in 香港人 'HongKonger' hoeng1gong2jan4, IPA:\[hœŋ55kɔŋ25jan21\]. If further parsing is required, we recommend the `parse_jyutping()` function from PyCantonese (Lee, 2015).

- **NumberOfSyllables**  
Syllable count of a word.

- **PartOfSpeech**  
Part of speech category based on tag set from HKCanCor. This is only given for words from HKCanCor because they are already provided. Words without a part of speech tag provided are tagged with `###`.

- **HKCACFrequency**  
The frequency of a word in HKCAC, 0 if not present in this corpus.

- **HKCACProbability**  
The probability of a word in HKCAC, 0 if not present in this corpus.

- **HKCanCorFrequency**  
The frequency of a word in HKCanCor, 0 if not present in this corpus.

- **HKCanCorProbability**  
The probability of a word in HKCanCor, 0 if not present in this corpus.

- **IARPAFrequency**  
The frequency of a word in IARPA, 0 if not present in this corpus.

- **IARPAProbability**  
The probability of a word in IARPA, 0 if not present in this corpus.

- **TotalFrequency**  
The frequency of a word in all corpora.

- **TotalProbability**  
The probability of a word in all corpora combined.

- **HKFrequency**  
The frequency of a word in HKCAC and HKCanCor (both Hong Kong Cantonese) tallied.

- **HKProbability**  
The probability of a word in HKCAC and HKCanCor combined.
## References
Lee, Jackson L. (2015). PyCantonese: Cantonese linguistic research in the age of big data. Talk at the Childhood Bilingualism Research Centre, Chinese University of Hong Kong. September 15. 2015. doi: http://pycantonese.org/

Yue, Bernard. (2016). Simplified and Traditional Chinese Character Conversion, v0.3.2. doi: https://github.com/berniey/hanziconv
