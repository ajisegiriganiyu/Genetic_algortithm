# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:43:42 2019

@author: pmgoa
"""

import sys

HOURS = ['9:00AM', '10:00AM', '11:00AM', '12:00PM', '1:00PM', '2:00PM', '3:00PM', '4:00PM']
PEOPLE_IDS = ['A', 'B', 'C', 'D', 'E']
VISITOR_IDS = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7']
VISITOR_PEOPLE = {'S1': ['A', 'B', 'C'], 
                  'S2': ['A', 'D', 'E'], 
                  'S3': ['B', 'E', 'D'], 
                  'S4': ['D', 'E', 'A'], 
                  'S5': ['C', 'D', 'E'], 
                  'S6': ['A', 'D', 'C'], 
                  'S7': ['B', 'C', 'D']
                  }

def main():
    people = {}
    for id in PEOPLE_IDS:
        people[id] = Person(id)
    visitors = {}
    for id in VISITOR_IDS:
        visitors[id] = Visitor(id, VISITOR_PEOPLE[id], people)
    for v in visitors.values():
        v.printSchedule()

class Person:
    def __init__(self, id):
        self.id = id
        self.schedule = [False]*8  # False = free, True = busy
    def scheduleTime(self):
        # schedules next available hour and returns that hour
        for i in range(len(self.schedule)):
            if not self.schedule[i]:
                self.schedule[i] = True
                return HOURS[i]
        return 'unavailable'
    def unscheduleTime(self, index):
        self.schedule[index] = False

class Visitor:
    def __init__(self, id, people_requests, people):
        self.id = id
        self.schedule = {} # {person_id: hour}
        for p in people_requests:
            bad_times = set()  # times that Visitor is busy
            time = people[p].scheduleTime()
            while time in self.schedule.values():  # keep scheduling a time until you get one that works for both the Visitor and Person
                bad_times.add(time)
                time = people[p].scheduleTime()
            self.schedule[p] = time
            for t in bad_times:  # unschedule bad_times from Person
                people[p].unscheduleTime(HOURS.index(t))
    def printSchedule(self):
        print( 'Schedule for %s [Person (time)]:' % self.id)
        for p,t in self.schedule.items():
            print ('    %s (%s)' % (p,t))

if __name__ == '__main__':
    sys.exit(main())