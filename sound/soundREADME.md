# Sound Frequencies Database Overview
This README file describes the structure and contents of the Sound Frequencies data file. The data file was created so that all of the sound frequency data in Li, Alderete, and Badrulhisham (2020) (henceforth, ‘the article’) can be verified and explored independently. The data file is essentially a large data table in which the rows are sound structures (excepting special rows described below) and the columns are fields that give information about the sound structure, like its frequency in some corpus. The rest of this document simply describes content of the fields named in the column headers. When the field contents are a small set of types, they are given right after the field name. Also, there are no empty cells in the data table, but some fields are not relevant to some structures, and so specific symbols are used to fill these cells for search purposes.
## Field Contents
Note: features within each column/field are denoted with a `code block`.

- **Structure**:  
Any sound structure, including tones, segments, or sequences of segments in syllables or rimes, typically the focus of an investigation. Phonological units are transcribed with the Jyutping system. See also special rows. 

- **StructureType**: `syllable`, `rime`, `segment`, `tone`  
Describes the type of phonological structure so that its appropriate baseline can be called. For example, structures with structure type `syllable` are all atonal syllables, that is one of the licit Onset + Rime combinations. The special row Structure(`HKCAC`) with StructureType(`syllable`) has frequency data for the total number of syllables in this corpus, by type and token (see below). `rime` is the only other complex structure type, composed of the X1X2 portion of the syllable. Note that diphthongs are specified `rime`, because they are traditionally analyzed this way, and this is consistent with their analysis in the Cantonese syllable (see the article).

- **SyllableEncodingType**: `regular`, `colloquial`, `loan`, `impossible`  
Only relevant for structures with StructureType(`syllable`). Based on the Bauer and Benedict’s (1997) classification of how syllables are encoded (i.e., Regular syllables have standard Chinese characters, all other values do not). Structures that are not StructureType(`syllable`) are specified `###` for this field.

- **SyllableShape**: `CV`, `CVV`, `CVN`, `CVS`, `N`  
Only used for structures with StructureType(`syllable`). This gives the CV structure of the syllable, as described in the article. Structures that are not StructureType(`syllable`) are specified `###` for this field. Note that syllables with a null onset are specified as `CV`.

- **SyllabicRole**: `onset`, `nucleus`, `coda`, `rime`, `syllable`, `tone`  
Specified for all structures except the special rows. Describes the syllabic role of the structure, i.e., what function it plays in the syllable. Some structures can play more than one rule. For example, p/`onset` is the sound /p/ in the role of Onset, where as p/`coda` is /p/ in a Coda position at the end of a syllable. Note that the nasal /m/ can be either `onset`, `nucleus` (for syllabic nasal) or `coda`. Monophthongal vowels are always `nucleus` because they occupy the X1 slot of a syllable, and diphthongs are always `rime` because they fill up both X1X2. The six tone structures are specified `tone`, and the many atonal syllable structures are `syllable`. Note that segments in our counts are phonemes, meaning that allophones of the same phoneme are tallied in the same row.

- **HKCACTypeFrequencies**  
The type frequency of a given structure/role in HKCAC, and 0 if not present in the corpus.

- **HKCACTokenFrequencies**  
The token frequency of a given structure/role in HKCAC, and 0 if not present in the corpus.

- **HKCACTypeProbabilities**  
The probability of a given structure/role in HKCAC based on type frequency, and 0 if not present in the corpus.

- **HKCACTokenProbabilities**  
The probability of a given structure/role in HKCAC based on token frequencies, and 0 if not present in the corpus.

- **HKCanCorTypeFrequencies**  
The type frequency of a given structure/role in HKCanCor, and 0 if not present in the corpus.

- **HKCanCorTokenFrequencies**  
The token frequency of a given structure/role in HKCanCor, and 0 if not present in the corpus.

- **HKCanCorTypeProbabilities**  
The probability of a given structure/role in HKCanCor based on type frequency, and 0 if not present in the corpus.

- **HKCanCorTokenProbabilities**  
The probability of a given structure/role in HKCanCor based on token frequencies, and 0 if not present in the corpus.

- **IARPATypeFrequencies**  
The type frequency of a given structure/role in IARPA, and 0 if not present in the corpus.

- **IARPATokenFrequencies**  
The token frequency of a given structure/role in IARPA, and 0 if not present in the corpus.

- **IARPATypeProbabilities**  
The probability of a given structure/role in IARPA based on type frequency, and 0 if not present in the corpus.

- **IARPATokenProbabilities**  
The probability of a given structure/role in IARPA based on token frequencies, and 0 if not present in the corpus.

- **Notes**  
Any additional notes concerned with specific structure types are documented in this column.
## Special Rows
There are twelve special rows with total counts for the four different structure types that give total counts based on type and token frequencies in each corpus (i.e., three corpora by four structure types). Each special row has one of the corpora in the Structure field, and that row gives the total frequencies for just that corpus. The value for Structure Type gives the respective type of structure for the baseline number (e.g., StructureType(Syllable) counts up all the syllable types and tokens). For example, there is a row with Structure(HKCAC), StructureType(Syllable), and a number N in the HKCACTypeFrequency field. This number N is the total number of syllables in HKCAC counted by types. The type and token frequency fields are therefore context sensitive: there are values under HKCAC Type Frequency and Token Frequency for Structure(HKCAC), but the fields for other corpora, e.g., HKCanCorTypeFrequency, are specified 0, because they do not contribute anything to this corpus total. These values can be used to make calculations derived from frequencies. 
