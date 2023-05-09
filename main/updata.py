

def logging(info):
    for i range(10):    
        with open('report.txt', 'a+') as f:
            print(info,file = f)