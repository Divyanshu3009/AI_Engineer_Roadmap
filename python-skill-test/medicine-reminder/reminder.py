import datetime as dt
import time

list_of_med = []
def setup():
    med = {"name" : input("Enter med name:"),
           "time" : int(input("Time for taking med: \n1 for morning, \n2 for afternoon, \n3 for night \n:")),
           "condition" : int(input("Enter 1 for Before eating,\nEnter 2 for After eating \n:"))
           }
    list_of_med.append(med)


def grouping():
        grouped_data = {}
        for i in list_of_med:
            key = i["time"],i["condition"]
            if key not in grouped_data:
                grouped_data[key]=[]
            grouped_data[key].append(i["name"])   
        return grouped_data  
            

def timer():
    return {
        1:dt.time(8,30),
        2:dt.time(13,22),
        3:dt.time(22,00)
    }


def reminder_loop(groups):
    time_map = timer()
    while True:
        now = dt.datetime.now().time().replace(second=0, microsecond=0)
        
        for (t, cond), meds in groups.items():
            if now == time_map[t]:
                if cond == 2:
                    ans = input("Have you eaten? (y/n):")
                    if ans.lower()!="y":
                        print("Snoozing for 30 minutes...")
                        time.sleep(1800)
                        
                print("Take medicines:",",".join(meds))
                time.sleep(60)
                
        time.sleep(20)
        


def start():
    while True:
        a = input("Add medicine? (Y/N): ").lower()
        if a == "y":
            setup()
        elif a == "n":
            if not list_of_med:
                exit()
            break
        else:
            print("Invalid input")

    groups = grouping()
    reminder_loop(groups)

start()