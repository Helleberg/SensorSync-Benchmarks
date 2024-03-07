import time

def performanceTest():
    print("Counter loop started")
    startTime  = time.time()
    endTime = startTime + 10
    count = 0
    while time.time() < endTime:
        count += 1
    print("Count: ", count)
    
performanceTest()