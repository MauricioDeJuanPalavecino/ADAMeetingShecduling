import sys

HOURS = ['t0', 't1', 't2', 't3', 't4', 't5']
PEOPLE_IDS = ['m1', 'm2', 'm3', 'm4', 'm5']
VISITOR_IDS = ['A0', 'A1', 'A2']
VISITOR_PEOPLE = {'A0': ['m1', 'm3', 'm5'], 
                  'A1': ['m1', 'm2', 'm3'], 
                  'A2': ['m2', 'm3', 'm4'], 
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
        #print 'Schedule for %s [Person (time)]:' % self.id 
        print ("Schedule for "+self.id)
        for p,t in self.schedule.items():
            print ("Este es p "+p+" Este es t "+t)

if __name__ == '__main__':
    sys.exit(main())