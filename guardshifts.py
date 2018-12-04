# advent of code 2018 day 4 
import sys, datetime, re

with open(sys.argv[1]) as f:
    lines = f.readlines()

events = []
sleepCount = {}
sleepTrend = {}
for entry in lines:
    m = re.match(r"\[(\d{4})-(\d{2})-(\d{2})\s*(\d{2}):(\d{2})]", entry)
    event = {}
    event["timestamp"]=datetime.datetime(int(m.group(1)),int(m.group(2)),int(m.group(3)),int(m.group(4)),int(m.group(5)))
    
    detail = entry[19:]
    if detail.startswith("G"):
        event["type"] = 1
        m = re.match(r".*?(\d+)", detail)
        event["id"] = m.group(1)
        sleepTrend[event["id"]] = {}
        sleepCount[event["id"]] = datetime.timedelta()
    if detail.startswith("f"):
        event["type"] = 2
    if detail.startswith("w"):
        event["type"] = 3
    events.append(event)
    
events.sort(key=lambda x: x["timestamp"])
#state machine
state = None
for event in events:
    if state is None or event["type"] is 1: #shift start
        state = event
    elif event["type"] is 2: #sleep
        state = {"id":state["id"], "timestamp":event["timestamp"], "type":2}
    elif event["type"] is 3: #wake
        for minute in range(state["timestamp"].minute, event["timestamp"].minute):
            if minute not in sleepTrend[state["id"]]:
                sleepTrend[state["id"]][minute]=0
            sleepTrend[state["id"]][minute]+=1
        sleepCount[state["id"]] += event["timestamp"] - state["timestamp"]
        
longestSleeper = sorted(sleepCount.items(), key=lambda kv: kv[1])[-1][0]
mostSleptMinute = sorted(sleepTrend[longestSleeper].items(), key=lambda kv: kv[1])[-1][0]
print(f"part1 hash: {int(longestSleeper) * mostSleptMinute}")

mostPredictable = []
for sleeper in sleepTrend.items():
    if len(sleeper[1]) > 0:
        sleepiestMinute = sorted(sleeper[1].items(), key=lambda kv: kv[1])[-1]
        mostPredictable.append((sleeper[0], sleepiestMinute))

mostPredictable.sort(key=lambda x: x[1][1])
print(f'part2 hash: {int(mostPredictable[-1][0]) * mostPredictable[-1][1][0]}')
    