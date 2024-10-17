class MyCalendarTwo:

    def __init__(self):
        self.over_lapping = []
        self.non_over_lapping = []
        

    def book(self, start: int, end: int) -> bool:
        for s, e in self.over_lapping:
            if not (end <= s or e <= start):
                return False
        for s,e in self.non_over_lapping:
            if not (end <= s or e<= start):
                self.over_lapping.append((max(s,start),min(e,end)))
        self.non_over_lapping.append((start,end))
        return True