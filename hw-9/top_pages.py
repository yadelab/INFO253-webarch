from mrjob.job import MRJob


# This class will run and count all of the words in this log file. You will need to figure out
# which pages have the most hits so you need to revise this mapper/reducer to find out how which
# pages have the most hists. Each line is a client connecting to the server in the format:
# V,[page id],[title],[path of page hit]
class MRWordCounter(MRJob):

	# Write your mapper class here
    def mapper(self, key, line):
        for word in line.split():
            yield word, 1

    # Write your reducer class here
    def reducer(self, word, occurrences):
        yield word, sum(occurrences)

if __name__ == '__main__':
    MRWordCounter.run()