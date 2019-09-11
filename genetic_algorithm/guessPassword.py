# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:33:34 2019

@author: Ajisegiri Ganiyu
"""

import datetime
import genetic

#test hello world
def test_Hello_World():
    target = "For I am fearfully and wonderfully made."
    guess_password(target)

def display(genes, target, startTime):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(genes, target)
    print("{0}\t{1}\t{2}".format(genes, fitness, str(timeDiff)))

def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes)
               if expected == actual)


def guess_password(target):
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    startTime = datetime.datetime.now()
    def fnGetFitness(genes): 
        return get_fitness(genes, target)
    def fnDisplay(genes): 
        display(genes, target, startTime)
    
    optimalFitness = len(target)
    genetic.get_best(fnGetFitness, len(target), optimalFitness, geneset, fnDisplay)


if __name__ == '__main__':
    test_Hello_World()