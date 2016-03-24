#!/usr/bin/env python
print
print "Windrock Programmer's Forum\n"
print "Challenge:"
print "The hands on an analog clock occasionally cross as they revolve around"
print "the dial. Your task is to write a program that determines how many times"
print "the hands cross in one 12-hour period, and compute a list of those times.\n"
print "My Assumptions:\n"
print "The clock starts at midnight."
print "The clock stops at 11:59 (just before noon)."
print "The minute hand moves one tick every minute."
print "The hour hand moves one tick every 12 minutes."
print "A 'crossing' occurs when the minute hand moves past the hour hand and"
print "the hour hand does not move."
print
cross_count = 0
for hr in range(0,12):
    prev_hr_pos = 0
    for min in range(0, 60):
        if min == 0:
            prev_hr_pos = 0;
            continue
        cur_hr_pos = (hr * 5) + (min / 12)
        prev_min = (min + 59) % 60
        if prev_min == cur_hr_pos and cur_hr_pos == prev_hr_pos:
            print str(hr).zfill(2) + ":" + str(min).zfill(2)
            cross_count += 1
        prev_hr_pos = cur_hr_pos
print
print "Hands crossed " + str(cross_count) + " time(s).\n"
