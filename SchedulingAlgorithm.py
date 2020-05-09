
class FCFS:
    """
    A class used to implement FCFS scheduling algorithm
    ...

    Methods
    -------
    enqueue(pList,process)
        inserts the new process into the process list queue
    dequeue(pList,quantum)
        removes the process from the process list queue

    """
    
    def __init__(self):
        pass
    
    def enqueue(self,pList,process):
        """Takes the new process object and inserts it into the end of process list

        Parameters
        ----------
        pList : list
            The list of process already present in the queue
        process : Process Object
            The new process which needs to be inserted in the queue

        """
        pList.append(process)       # For FCFS, inserting process to end of  process list

    def dequeue(self,pList,quantum):
        """Takes the quantum time elapsed and removes processes from the
           front of queue based on remaining cpu time required by that process.

        Parameters
        ----------
        pList : list
            The list of process already present in the queue
        quantum : int
            The time elapsed since last removal process
    
        Returns
        -------
        finished : list
            A list of rocesses removed during the current cycle
        quantum : int
            Quantum time updated after being used by each process (Usually 0)
        """
        
        finished = []
        indexToRemove = []
        
        # Iterating through each process
        for i in range(len(pList)):
            if pList[i].remTime <= quantum and quantum != 0:    # Checking if remaining time < quantum
                quantum -= pList[i].remTime                     # If yes, Quantum is updated
                pList[i].remTime = 0                            # Remaining time is made zero
                
                indexToRemove.append(i)                         # index is noted to remove from list
                
                print(pList[i].arrTime)                         # Printing arrival time for debugging
                
            elif quantum > 0 and quantum != 0:                  # If remaining time > quantum
                pList[i].remTime -= quantum                     # Remaining time is updated
                quantum = 0
        
        
        cnt = 0
        for i in indexToRemove:                                 # Removing process from process list
            finished.append(pList.pop(i-cnt))                   # Appending removed process to finished list
            cnt += 1
        
            
        return finished,quantum
