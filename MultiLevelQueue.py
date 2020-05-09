
from collections import OrderedDict
from Queue import Queue
from SchedulingAlgorithm import FCFS

class MultiLevelQueue:
    """
    A class used to represent an Multilevel Queue Scheduling Instance
    ...

    Attributes
    ----------
    queue_dict : OrderedDict
        A ordered dictionary to store Queue instances for each process types (Foreground, Background etc)
    QTypes : list
        A list of process types to initialise with decreasing priority of process types
    SchdAlgo : list
        A list of scheduling algorithm for corresponding process types
    completed_process : list
        A list for storing finished process for each MLQ instance

    Methods
    -------
    initQueues()
        Initialises the dictionary with Queue instances for different process types
    addProcess(process)
         Adds a new process to appropriate Queue based on process type
    removeProcess(quantum)
        Removes a processs based on time elapsed (quantum)
    checkProcessExists()
        Checks whether each queue in dictionary has any processes to execute
    .

    """
    def __init__(self,QTypes,SchdAlgo):
        """
        Parameters
        ----------
        QTypes : list
            The list mentioning each process types
        
        SchdAlgo : list
            The scheduling algorithm to be used for each process type
        """
        self.queue_dict = OrderedDict()
        
        self.QTypes = QTypes
        self.SchdAlgo = SchdAlgo
        
        self.completed_process = []
    
    
    def initQueues(self):
        """Initialises queue_dict with objects of Queue class using QTypes.
           key = Type of Process (Foreground,Background)
           value = Queue Object
           
           Uses SchdAlgo to assign respective queues their scheduling algorithm.                  
        """
        for i in range(len(self.QTypes)):                                       # Iterating through Queue types
            self.queue_dict[self.QTypes[i]] = Queue(self.QTypes[i])             # Assigning Queue Objects
            
            if self.SchdAlgo[i] == 'FCFS':                                       # Checking scheduling algorithm to use
                self.queue_dict[self.QTypes[i]].SchedulingAlgo = FCFS()         # Assigning scheduling algorithm instance to each queue created
            #else:
            #    self.queue_dict[self.QTypes[i]].SchedulingAlgo = SJF()

    def addProcess(self,process):
        """Selects the appropriate queue from dictionary using process type 
           and calls the queue_enqueue method of that queue instance. 
           
        Parameters
        ----------
        proces : object
            An object of Process class representing a new process
            
        """
        queue = self.queue_dict[process.type]                                   # Selecting appropriate queue object based on process type
        queue.queue_enqueue(process)                                            # Inserting the process 
    
    
    def removeProcess(self,quantum):
        """Removes the processes starting from the first queue present in dictionary.
           Since its ordered dictionary, the first key will have highest priority.
           
           queue_dequeue of respecting Queue objects are called.
           
           Removed process are stored in completed_process
    
        Parameters
        ----------
        quantum : int
            An integer representing the time elapsed
            
        """
        for qu in self.queue_dict:                                              # Iteratng through each queue instance high -> low priority
            if not self.queue_dict[qu].isEmpty() and quantum != 0:              # if process list is not empty
                removed,quantum = self.queue_dict[qu].queue_dequeue(quantum)    # Remove process based on time elapsed
                if removed:
                    self.completed_process.extend(removed)                      # adding removed process to completed_process
                    
                
    
    def checkProcessExists(self):
        """Checks whether there are processes left to execute in the MLQ instance. 
    
        Returns
        -------
        bool :
            True if there are processes left, False if all queues have empty process list.
            
        """
        for qu in self.queue_dict:
            if not self.queue_dict[qu].isEmpty():
                return True
        
        return False
             
        
        
    
        
        