from mrjob.job import MRJob


# This class will run and count all of the words in this log file. You will need to figure out
# which pages have the most hits so you need to revise this mapper/reducer to find out how which
# pages have the most hists. Each line is a client connecting to the server in the format:
# V,[page id],[title],[path of page hit]

class MRWordCounter(MRJob):

	# Write your mapper class here
    def mapper(self, key, line):
		a = line.split()
		
		for word in a:
			yield word,1

    # Write your reducer class here
    def reducer(self, word, occurrences):
    	#f = lambda a: a if a >= 400 else None
    	tot = sum(occurrences)
    	if tot > 400:
    		yield word, tot
        



if __name__ == '__main__':
    MRWordCounter.run()