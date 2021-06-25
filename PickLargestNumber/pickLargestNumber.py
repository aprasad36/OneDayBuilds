import numpy as np
import random
from tqdm import tqdm
import sys

def oneRun():
    envelope1 = np.random.normal(110, 1)
    envelope2 = np.random.normal(110, 1)
    t = np.random.normal(0, 1)
    #python shenanigan
    randomchoice = random.choice((envelope1, envelope2))
    #print(f"Picked: {randomchoice}, t-value: {t}")
    if (randomchoice < t):
        if (randomchoice == envelope1):
            randomchoice = envelope2
        else:
            randomchoice = envelope1
    #print(f"Chose {randomchoice}, truevalue:{max(envelope1, envelope2)}")
    return randomchoice == max(envelope1, envelope2)

def multipleRuns(total):
    correct = 0
    for run in tqdm(range(total)):
        if oneRun():
            correct += 1
    return correct / total

if len(sys.argv) < 2:
    numruns = 1000000
else:
    numruns = int(sys.argv[1])
percent = multipleRuns(numruns)
print(f"We got {percent*100}%")
