from datetime import datetime
class MyGreeter:
    def __init__(self,now=datetime.now()):
        self.now=now
        
    def Client(self):
        n=self.now
        if datetime(n.year,n.month,n.day,12,0,0,0) >= n and datetime(n.year,n.month,n.day,6,0,0,0) < n:
            return 'Good morning'

        if datetime(n.year,n.month,n.day,18,0,0,0) >= n and datetime(n.year,n.month,n.day,12,0,0,0) < n:
            return 'Good afternoon'

        if datetime(n.year,n.month,n.day,18,0,0,0) < n  or datetime(n.year,n.month,n.day,6,0,0,0) >= n:
            return 'Good evening'

#c = MyGreeter()
#print(c.Client())