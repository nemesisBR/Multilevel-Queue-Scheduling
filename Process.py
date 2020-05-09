

class Process:
    """
    A class used to represent a Process
    ...

    Attributes
    ----------
    type : str
        the type of process (Foreground,Background etc)
    arrTime : int
        arrival time of the process
    priority : int
        the number indicating priority of the process
    burstTime : int
        the number indicating the required cpu time
    waitTime : int
        the number indicating the wait time for the process
    remTime : int
        the number indicating the required cpu time remaining

    """
    def __init__(self,type,arrTime,priority,burstTime):
        self.type = type
        self.arrTime = arrTime
        self.priority = priority
        self.burstTime = burstTime
        self.waitTime = None
        self.remTime = burstTime
