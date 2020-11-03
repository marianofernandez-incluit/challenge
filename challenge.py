class Jug:
    def __init__(self, capacity,state="empty",gallons=0): 
        self.capacity = capacity
        self.state = state 
        self.gallons = gallons 

    def getState(self):
        if self.gallons == 0:
            self.state="empty"
        elif self.gallons < self.capacity:
            self.state="partially full"
        elif self.gallons==self.capacity: 
            self.state="full"
        else:
            self.state="error"
        return self.state   

    
    def emptyJug(self):
        self.__gallons= 0   
        self.getState()
        return True

    def fillJug(self):
        if self.gallons== 0:
            self.gallons= self.capacity  
            self.getState()
            return True
        else:
            return False
    
    def transferToJug(self,amount,toJug):
        emptySpace=toJug.capacity-toJug.gallons
        if emptySpace >= amount:
            self.gallons=self.gallons-amount
            toJug.gallons=toJug.gallons+amount
            return True
        else: 
            return False

def solution(jugA,jugB,myGoal):
    step = 0
    fromJug=fromJugCap=jugA
    toJugCap=toJug=jugB
    goal=myGoal
    while ((fromJug  is not goal) and (toJug is not goal)):
        if step >20:
            print("No solution")
            break
        temp = min(fromJug, toJugCap-toJug)
 
        # Pour water
        toJug = toJug + temp
        fromJug = fromJug - temp
        if step==0:
            print("Steps")
        else:
            print(step,"-> Jug A:",fromJug,"Jug B:",toJug)
 
        if ((fromJug == goal) or (toJug == goal)):
            print("Solved !!!")
            break

        step =  step + 1

        # If first jug is empty, fill it
        if fromJug == 0:
            fromJug = fromJugCap
            print(step,"-> Jug A:",fromJug,"Jug B:",toJug)
            step =  step + 1
 
        # If second jug is full, empty it
        if toJug == toJugCap:
            toJug = 0
            print(step,"-> Jug A:",fromJug,"Jug B:",toJug)
            step =  step + 1
        
    return step


def inputNumber(message):
      while True:
        try:
            userInput = int(input(message)) 
            if userInput < 0:  
                print("Sorry, input must be a positive integer, try again")
                continue
                break      
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput 
            break 


def main():
    jug1 = inputNumber("Input size for the first jug, then press enter: ")
    jug2 = inputNumber("Input size for the second jug, then press enter: ")
    goal = inputNumber("Input goal, then press enter: ")
    print("Scenario")
    print("Jug A -----> ",jug1)
    print("Jug B -----> ",jug2)
    print("Goal  -----> ",goal)
    print("----------------")
    solution(jug1,jug2,goal)
    print("----------------")
    solution(jug2,jug1,goal)

if __name__ == '__main__':
	main()
            
                      
