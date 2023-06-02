

def logging(info):
    with open('report.txt', 'a+',encoding='utf-8') as f:
        print(info,file = f)