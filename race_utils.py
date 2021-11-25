import random

class SampleGenerator(object):
    
    def __init__(self):
        self.loaded = False
        self.samples = list()
        
    def random_sample(self):
        if (not self.loaded):
            sample_file = open('./sample_params.txt')
            all_lines = sample_file.readlines()
            for line in all_lines:
                self.samples.append(eval(line))
                
        samples_len = len(self.samples)
        
        random_index = random.randint(0, samples_len)
        
        return self.samples[random_index]