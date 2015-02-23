from reportlab.graphics.samples.scatter import Scatter
import Helper

__author__ = 'aleksander'
from plotly.graph_objs import *


def load_file():
    try:
        filepath = "/home/aleksander/Dropbox/Aleks/Cubing/Times/20150223/3x3.csv"
        with open(filepath) as f:
            content = f.readlines()
        return content
    except TypeError as e:
        print "A TypeError occurred while trying to load file.\nMessage: " + e.message
    except Exception as e:
        print "An exception occurred while trying to load file.\nMessage: " + e.message


def get_times():
    content = load_file()

    times = []

    for line in content:
        time = line[22:]
        min = time[0:2]
        sec = time[3:5]
        centi = time[6:8]
        seccenti = sec + "." + centi

        try:
            seccenti = float(seccenti)
            min = float(min)
            addsec = 0
            if min > 0:
                addsec = min * 60
            times.append(float(seccenti + addsec))
        except ValueError as e:
            print "ValueError in get_times(): " + e.message
        except Exception as e:
            print "Exception in get_times(): " + e.message

    #Reverse the list because Speedcube Timer lists them from last to first
    times.reverse()

    return times


def plot():

    #Make a trace for the times
    times = get_times()
    x = []
    for i in range(1, len(times) + 1):
        x.append(i)
    trace1 = Scatter(x=x, y=times)

    #Make a trace for the average of last 5
    averages = [0, 0, 0, 0]
    for i in range(4, len(times)):
        subtable = []
        for j in range(i-4, i+1):
            subtable.append(times[j])
        avg = Helper.get_avg(subtable)
        averages.append(avg)

    x = []
    for i in range(1, len(averages)+1):
        x.append(i)

    trace2 = Scatter(x=x, y=averages)

    data = Data([trace1, trace2])
    #py.plot(data, filename='basic-line')


class CubeTimePlotter:

    def __init__(self):
        self.times = get_times()

    def init(self):
        plot()
        print "Lifetime average:    " + str(Helper.get_lifetime_avg(self.times))
        print "Lifetime best:       " + str(Helper.get_lifetime_best(self.times))
        print "Lifetime best 5:     " + ', '.join(str(i) for i in Helper.get_lifetime_n_best(self.times, 5))
        print "Average of last 5:   " + str(Helper.get_avg_of_last_n(5, self.times))
        print "Average of last 10:  " + str(Helper.get_avg_of_last_n(10, self.times))
        print "Average of last 12:  " + str(Helper.get_avg_of_last_n(12, self.times))