from models.timeStats import TimeStats
class Process:
    # Class Atributes
    valueA : int
    valueB : int
    operation: str
    remainingTime : int
    elapsedTime : int
    blockedTime : int
    processID : str
    stats : TimeStats
    error : bool
    
    # Class constructor
    def __init__(self,valueA,valueB,operation,time,processID) -> None:
        self.valueA = valueA
        self.valueB = valueB
        self.operation = operation
        self.remainingTime = time
        self.processID = processID
        self.elapsedTime = 0
        self.blockedTime = 0
        self.error = False
        self.stats = TimeStats()
        
    # Class Methods
    def setElapsedTime(self,t : int):
        self.elapsedTime = t
    
    def setBlockedTime(self,t : int):
        self.blockedTime = t
    
    def toString(self):
        return str(self.valueA) + self.operation + str(self.valueB) + " = " + str(self.remainingTime)
    
    def getTime(self) -> int:
        return self.remainingTime
    
    def getElapsedTime(self) -> int:
        return self.elapsedTime
    
    def getBlockedTime(self) -> int:
        return self.blockedTime
    
    def getID(self) -> str:
        return self.processID
    
    def getOperation(self) -> str:
        return self.operation
    
    def getStatus(self) -> str:
        if(self.blockedTime > 0):
            return str(self.blockedTime)
        if(self.error):
            return "Error"
        if(self.remainingTime == 0):
            return "Terminado"
        if(self.stats.getArrivalTime() == -1 ):
            return "Nuevo"
        return "Listo"
    
    def getFullOperation(self) -> str:
        return str(self.valueA) + self.operation + str(self.valueB)
    
    def getResult(self) -> int | str:
        if(self.error):
            return "Error"
        if(self.remainingTime > 0):
            return ""
        if(self.operation == "+"):
            return self.valueA + self.valueB
        elif(self.operation == "-"):
            return self.valueA - self.valueB
        elif(self.operation == "*"):
            return self.valueA * self.valueB
        elif(self.operation == "/"):
            return self.valueA / self.valueB
        elif(self.operation == "%"):
            return self.valueA % self.valueB
        elif(self.operation == "^"):
            return self.valueA ** self.valueB