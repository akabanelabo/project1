import time
import math

class Timer():
    def __init__(self):
        # 開始時刻
        self.startTime = time.time()
        # 都度の時間
        self.elapsedTime = 0.0

    def start(self):
        # 開始時刻
        self.startTime = time.time()
        # 都度の時間
        self.elapsedTime = 0.0        

    def update(self):
        self.elapsedTime = time.time()-self.startTime
        now = math.floor(self.elapsedTime)
        return now
