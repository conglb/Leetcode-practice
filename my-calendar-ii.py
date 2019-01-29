class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.double = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if self.checkTriple(start, end):
            self.events.append((start, end))
            for tuple in self.events:
                if end <= tuple[1] and  end > tuple[0]:
                    e = end
                    b = max(begin, tuple[0])
                    self.double.append((b, e))
                    continue
                if start >= tuple[0] and start < tuple[1]:
                    b = start
                    e = min(tuple[1], end)
                    self.double.append((b, e))
                    continue
                if tuple[0] >= start and tuple[1] < end:
                    b = tuple[0]
                    e = tuple[1]
                    self.double.append((b, e))
            return True

    def checkTriple(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        check = True
        for tuple in self.double:
            if tuple[1] <= end and tuple[1] > start:
                check = False
                break
            if tuple[0] >= start and tuple[0] < end:
                check = False
                break
            if tuple[0] <= start and tuple[1] > end:
                check = False
                break
        return check




# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)