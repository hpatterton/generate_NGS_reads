import random

class ConvertSequence:
    
    def __init__(self):
        pass

    def __del__(self):
        pass

    def GenerateSequenceReadFragments(self,template_sequence,sequence_read_fragment_length_min,sequence_read_fragment_length_max,sequence_depth):
        random.seed()
        total_length = 0
        list_of_fragments = []
        while(total_length < len(template_sequence)*sequence_depth):
            fragment_length = random.randint(sequence_read_fragment_length_min,sequence_read_fragment_length_max)
            start = random.randint(0,len(template_sequence)-fragment_length-1)
            list_of_fragments.append(template_sequence[start:start+fragment_length])
            total_length += fragment_length
        return(list_of_fragments)
