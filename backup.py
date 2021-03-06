e_min = [(30,7,27),(35,6,36),(40,5,56),(45,5,23),(50,4,56),(55,4,34),
         (60,4,15),(65,3,59),(70,3,44),(75,3,32),(80,3,21),(85,3,11)]
e_min_pace = [[vdot, datetime.timedelta(minutes=minutes, seconds=seconds)] for vdot, minutes, seconds in e_min]

e_max = [(30,8,14),(35,7,21),(40,6,38),(45,6,3),(50,5,34),(55,5,10),
         (60,4,49),(65,4,31),(70,4,15),(75,4,1),(80,3,49),(85,3,38)]
e_max_pace = [[vdot, datetime.timedelta(minutes=minutes, seconds=seconds)] for vdot, minutes, seconds in e_max]

m = [(30,7,3),(31,6,52),(32,6,40),(33,6,30),(34,6,20),(35,6,10),
     (36,6,1),(37,5,53),(38,5,45),(39,5,37),(40,5,29),(41,5,22),
     (42,5,16),(43,5,9),(44,5,3),(45,4,57),(46,4,51),(47,4,46),
     (48,4,41),(49,4,36),(50,4,31),(51,4,27),(52,4,22),(53,4,18),
     (54,4,14),(55,4,10),(56,4,6),(57,4,3),(58,3,59),(59,3,56),
     (60,3,52),(61,3,49),(62,3,46),(63,3,43),(64,3,40),(65,3,37),
     (66,3,34),(67,3,31),(68,3,29),(69,3,26),(70,3,24),(71,3,21),
     (72,3,19),(73,3,16),(74,3,14),(75,3,12),(76,3,10),(77,3,8),
     (78,3,6),(79,3,3),(80,3,1),(81,3,0),(82,2,58),(83,2,56),
     (84,2,54),(85,2,52)]
m_pace = [[vdot, datetime.timedelta(minutes=minutes, seconds=seconds)] for vdot, minutes, seconds in m]

t = [(30,6,24),(35,5,40),(40,5,6),(45,4,38),(50,4,15),(55,3,56),
     (60,3,40),(65,3,26),(70,3,14),(75,3,4),(80,2,54),(85,2,46)]
t_pace = [[vdot, datetime.timedelta(minutes=minutes, seconds=seconds)] for vdot, minutes, seconds in t]

i = [(30,5,55),(31,5,45),(32,5,35),(33,5,27),(34,5,20),
     (35,5,12),(40,4,42),(45,4,16),(50,3,55),(55,3,37),
     (60,3,23),(65,3,10),(70,2,59),(75,2,49),(80,2,41),(85,2,33)]
i_pace = [[vdot, datetime.timedelta(minutes=minutes, seconds=seconds)] for vdot, minutes, seconds in i]

r = [(30,5,35),(35,4,45),(40,4,20),(45,3,55),(50,3,35),(55,3,20),
     (60,3,5),(65,2,50),(70,2,40),(75,2,30),(80,2,20),(85,2,15)]
r_pace = [[vdot, datetime.timedelta(minutes=minutes, seconds=seconds)] for vdot, minutes, seconds in r]

m = [(30,4,49,17),(35,4,16,3),(40,3,49,45),(45,3,28,26),(50,3,10,49),(55,2,56,1),
     (60,2,43,25),(65,2,32,35),(70,2,23,10),(75,2,14,55),(80,2,7,38),(85,2,1,10)]
m_time = [[vdot, datetime.timedelta(hours=h, minutes=m, seconds=s)] for vdot, h, m, s in m]