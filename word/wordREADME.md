# Word Frequencies Database Overview
This README file describes the structure and contents of the Word Frequencies data file. The data file was created so that all of the word frequency data in Li, Alderete, and Badrulhisham (2020) can be verified and explored independently. The data file is essentially a large data table in which the rows are words and the columns are fields that give information about the words, like its frequency in some corpus. The rest of this document simply describes content of the fields named in the column headers.
## Field Contents
- **OrthographicRepresentationTraditional**  
Standard orthographic representation of a word using traditional Chinese characters or transliterated words (for words without standard characters). The words from IARPA have been converted to traditional characters with name.converstion tool (ref).

- **OrthographicRepresentationSimplified**  
Standard orthographic representation of a word using simplified Chinese characters or transliterated words (for words without standard characters). The words from HKCAC and HKCanCor have been converted to simplified characters with name.converstion tool (ref).

- **PhonologicalRepresentationJyutping**  
The Jyutping representation of the word, as in xxxgive.example

- **PhonologicalRepresentationIPA**  
The IPA-inspired representation of the word, as in xxxgive.example

- **NumberOfSyllables**  
Syllable count of a word.

- **PartOfSpeech**  
Part of speech category based on tag set from HKCanCor. This is only given for words from HKCanCor because they are already provided.  

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
