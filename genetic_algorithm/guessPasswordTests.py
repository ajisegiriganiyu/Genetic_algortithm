# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:33:34 2019

@author: Ajisegiri Ganiyu
"""
import unittest
import datetime
import genetic
import random




def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}".format(
            candidate.Genes, candidate.Fitness, str(timeDiff)))

def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes)
               if expected == actual)

class GuessPasswordTests(unittest.TestCase):
    
    #test hello world
    def test_Hello_World(self):
        target = "For I am fearfully and wonderfully made."
        self.guess_password(target)
        
        
    def guess_password(self,target):
        self.geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
        startTime = datetime.datetime.now()
        
        def fnGetFitness(genes): 
            return get_fitness(genes, target)
        
        def fnDisplay(candidate): 
            display(candidate, startTime)
        
        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), 
                                optimalFitness, self.geneset, 
                                fnDisplay)
        self.assertEqual(best.Genes, target)
    
def test_Random(self):
    length = 150
    target = ''.join(random.choice(self.geneset) for _ in range(length))
    self.guess_password(target)
    
def test_benchmark(self):
    genetic.Benchmark.run(self.test_Random) 

if __name__ == '__main__':
    unittest.main()

