from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import heapq
WORD_RE = re.compile(r"\w+")

class MRMostUsedTitle(MRJob):
        
    # yield each word in the line

    def mapper_get_words(self, _, line):
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    def combiner_count_words(self, word, counts):
        yield (word, sum(counts))

    def reducer_count_words(self, word, counts):
        yield (word, sum(counts))



   
    def mapper_add_to_head(self,word,counts):
        heapq.heappush(self.h,(counts,word))
        #yield (word,counts)
        
    def mapper_pop_top_10(self):
       
        largest_value = heapq.nlargest(11,self.h)
        
        for count,word in largest_value:
            yield ('heap',(count,word))  



            
    def reducer_heap(self):
        self.h_unused = []
        
    def reducer_heap_count_words(self, key,word_counts):
        for wc in word_counts:
            heapq.heappush(self.h_unused, (wc[0],wc[1]))
    
    def reducer_pop_top_10(self):
        largest = heapq.nlargest(11,self.h_unused)
        words = [(word,  int(count)) for count, word in largest]
        yield (None, words)      


      
    def heap(self):
        self.h = []
        self.h_reducer = []

    #initializing steps
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   combiner=self.combiner_count_words,
                   reducer=self.reducer_count_words),
            MRStep(mapper_init = self.heap,
                   mapper = self.mapper_add_to_head,
                   mapper_final = self.mapper_pop_top_10,
                   reducer_init = self.reducer_heap,
                   reducer = self.reducer_heap_count_words,
                   reducer_final = self.reducer_pop_top_10)]
            
        
if __name__ == '__main__':
    MRMostUsedTitle.run()