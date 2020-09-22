import math
import numpy as np
import random


class Polygon:
    points = []
    vertices = []
    n = 16
    h = 16
    w = 16

    def __init__(self, **kwargs):
        points = kwargs.get('points')

        if points != None:
            self.points = points
        else:
            n = kwargs.get('n')
            w = kwargs.get('w')
            h = kwargs.get('h')
            if n: self.n = n
            if w: self.w = w
            if h: self.h = h
            self.generate()

        self.sort()

        

    def sort(self):
        center_point = [self.w / 2, self.h / 2]
        self.vertices = self.points.copy()

        def sort_by_angle(p1, p2):
            a = math.atan2(p1[1] - center_point[1], p1[0] - center_point[0]) * 180 / math.pi
            b = math.atan2(p2[1] - center_point[1], p2[0] - center_point[0]) * 180 / math.pi
            return a - b

        def cmp_to_key(mycmp):
            class K:
                def __init__(self, obj, *args):
                    self.obj = obj
                def __lt__(self, other):
                    return mycmp(self.obj, other.obj) < 0
                def __gt__(self, other):
                    return mycmp(self.obj, other.obj) > 0
                def __eq__(self, other):
                    return mycmp(self.obj, other.obj) == 0
                def __le__(self, other):
                    return mycmp(self.obj, other.obj) <= 0
                def __ge__(self, other):
                    return mycmp(self.obj, other.obj) >= 0
                def __ne__(self, other):
                    return mycmp(self.obj, other.obj) != 0
            return K

        self.vertices.sort(key=cmp_to_key(sort_by_angle))
    
    def generate(self):
        for _ in range(self.n):
            self.points.append([random.randint(1, self.w), random.randint(1, self.h)])
    
    