class Time:
    def __init__(self,min,hr,sec):
        self.min=min
        self.hr=hr
        self.sec=sec
    def __add__(self,other):
        tmin=0
        thr=0
        tsec=0
        tsec=(self.sec+other.sec)%60
        rem=(self.sec+other.sec)//60
        tmin=((self.min+other.min)%60)+rem
        rem=(self.min+other.min)//60
        thr=self.hr+other.hr+rem
        return Time(tsec,tmin,thr)
    def __str__(self):
        return f"{self.min}: {self.sec}: {self.hr}"
t1=Time(23,4,5) 
t2=Time(12,8,9)
print(t1+t2)





