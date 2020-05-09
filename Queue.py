class Queue:
    """
    A class used to represent an Queue for for storing processes
    ...

    Attributes
    ----------
    processList : list
        The list which would store the process currently in line for execution
    priority : str
        The type of process (Foreground,Background etc)
    SchedulingAlgo : object
        The object for corresponding scheduling algorithm to be used in this queue (FCFS,SJF etc)

    Methods
    -------
    queue_enqueue(pList,process)
        Uses the scheduling algorithm object to insert process into process list
    queue_dequeue(pList,quantum)
         Uses the scheduling algorithm object to remove process from process list
    size()
        Returns the size of process list
    isEmpty()
        Checks whether the process list is empty or not
    front()
        Returns the first element in process list if its not empty.

    """
    def __init__(self,type):
        """
        Parameters
        ----------
        type : str
            The type of process (Foreground,Background etc)
        """
        self.processList = []
        self.priority = type
        self.SchedulingAlgo = None
    
    
    def size(self):
        """Returs the total number of processes left for execution.
    
        Returns
        -------
        int : 
            The length of process list
        """
        return len(self.processList)
    
    def isEmpty(self):
        """Checks whether all processes have been executed or not.
    
        Returns
        -------
        bool :
            True if processList has 0 length , False otherwise.
        
        """
        return self.size() == 0
    
    def front(self):
        """Returns the first process in list 
    
        Returns
        -------
        object :
            The first process if process list is not empty else None
            
        """
        return self.processList[0] if not self.isEmpty else None
    
    def queue_enqueue(self,process):   
        """Uses the queue's scheduling algorithm enqueue method to insert
           the new process into the process list.

        Parameters
        ----------
        process : object
            The Process class object defining the new process to insert.
        
        """
        self.SchedulingAlgo.enqueue(self.processList,process)

    def queue_dequeue(self,quantum):
        """Takes the quantum time elapsed and removes processes from the 
           process list using scheduling algorithim;s dequeue method.

        Parameters
        ----------
        quantum : int
            The time elapsed
    
        Returns
        -------
        removed : list
            A list of rocesses removed during the current cycle
        quantum : int
            Quantum time updated after being used by each process (Usually 0)
        """
        removed,quantum = self.SchedulingAlgo.dequeue(self.processList,quantum)
        
        return removed,quantum
    

