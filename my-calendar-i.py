class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        check = True
        for tuple in self.events:
            if tuple[1] <= end and tuple[1] > start:
                check = False
                break
            if tuple[0] >= start and tuple[0] < end:
                check = False
                break
            if tuple[0] <= start and tuple[1] > end:
                check = False
                break
        if check:
            self.events.append((start,end))
        return check



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)