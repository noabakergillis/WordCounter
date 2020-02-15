# WordCounter
Hi!
Thanks for taking a look at my project.
This project counts the words in any given input (a string, a text file, or a URL). WordCounter.py returns the
number of instances in an input of a given word, and UniqueWords.py returns the number of unique words in the input.
I utilize the python dictionary as my primary data structure to store the counts in a pickle file.
I tried to focus on optimizing space, since the project instructions specified that I would possibly be dealing with large
inputs. To handle this, I first made sure to use a memory (and time) efficient data structure. Secondly, I checked
to see how large the input files were. If they contained over a certain number of lines, I split the files into
multiple files on disk, and loaded and stored the dictionary between files in order to not take up working memory.
I also made sure to utilize the memory-friendly generator class, instead of storing arrays in memory.
The pickle file also works to ensure that the data is persistent between runs.
The WordCounter.py includes a start_over() function, which deletes the pickle file so that the user can start fresh
with a new input. The two programs both interact with the same dictionary in the pickle file.
These programs are best run from the console. To run the WordCounter:

python WordCounter.py input searchword

To run the UniqueWords:

python UniqueWords.py input
