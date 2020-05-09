import time
from Process import Process
from MultiLevelQueue import MultiLevelQueue

if __name__ == '__main__':
    
    #Defining Queue Priority and Scheduling Algo to be used
    QTypes = ['FG','BG','UG']           # High Priority -> Low Priority
    SchdAlgo = ['FCFS','FCFS','FCFS']
    
    #Creating Multilevel Queue
    mlq = MultiLevelQueue(QTypes,SchdAlgo)

    #Initializing MultiLevel Queue    
    mlq.initQueues()
    
    #Defining Process Attributes
    arrTimes = [0,1,3,4,5,8,15,25]
    burstTimes = [5,4,7,3,3,11,3,4] 
    types = ['BG','FG','UG','FG','BG','UG','BG','FG']
    priorities = [1,2,3,4,5,6,7,8]
    
    # List for storing created processes
    process_created = []
    
    #Creating Process
    for i in range(8):
        process_created.append(Process(types[i],arrTimes[i],priorities[i],burstTimes[i]))
    
    
    #Adding Process to Queue
    for process in process_created:
        mlq.addProcess(process)
    
    
    #Starting Execution
    quantum = 2
    
    while mlq.checkProcessExists():
        time.sleep(quantum)        
        mlq.removeProcess(quantum)
    
    # Program prints arrival times in the order of processes removed

    
    
