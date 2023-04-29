import math

class ddosDetection:
    def __init__(self):
        self.pktCnt = 0
        self.ddosDetected = 0 # 1 indicates ddosDetected is true , 0 : false
        self.counter = 0 # if 10 times consecutively, entropy value is less than 1, then indicate to controller that DDOS Attack is detected
        self.ipList_Dict = {}
        self.sumEntropy = 0

    def calculateEntropy(self, ip):
        # Calculate entropy when pkt count reaches 100
        self.pktCnt += 1
        if ip in self.ipList_Dict:
            self.ipList_Dict[ip] += 1
        else:
            self.ipList_Dict[ip] = 0

        if self.pktCnt == 50:
            self.sumEntropy = 0
            self.ddosDetected = 0
            print("Window size of 50 pkts reached, calculate entropy")
            for ip, value in self.ipList_Dict.items():
                prob = abs(value / float(self.pktCnt))
                if prob > 0.0:
                    ent = -prob * math.log(prob, 2)
                    self.sumEntropy += ent
            print("Entropy Value = ", self.sumEntropy)
            if 0 < self.sumEntropy < 2:
                self.counter += 1
            else:
                self.counter = 0
            if self.counter == 10:
                self.ddosDetected = 1
                print("Counter = ", self.counter)
                print("DDOS ATTACK DETECTED")
                self.counter = 0
            self.cleanUpValues()

    def cleanUpValues(self):
        self.pktCnt = 0
        self.dest_ipList = []
        self.ipList_Dict = {}
        self.sumEntropy = 0
