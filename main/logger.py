

def logging(info):
    with open('report.txt', 'a+') as f:
        print(info,file = f)