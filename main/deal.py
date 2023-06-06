import random
import re
import multiprocessing
from main import ask
from urllib import parse

funcion= ask.Request
class Deal:
    def __init__(self,target):
        self.name=target
    
    #批量执行    
    def fileDeal(self):
        file_object = open(self.name.name,'r',encoding ="utf-8")
        lines = file_object.readlines()
        pool = multiprocessing.Pool(1)
        for url in lines:
            url=url.strip('\n')
            result=Deal(url).RequestHeadDeal()
            pool.apply(ask.Request, args=(result,))
        pool.close()
        pool.join()
  

    #请求协议处理：采用http还是http请求这里要修改一下 处理数据出现问题
    def RequestHeadDeal(self):
        target = self.name     
        if (":80" in target or ":443" not in target) and ("http" not in target):
            target = "http://" + target
        if ":443" in target and "://" not in target:
            target = "https://" + target
        parse1 = parse.urlparse(target)
        #print(parse1)
        port = str(parse1.port) 
        if not parse1.port:
            if parse1.scheme == 'http':
                port = '80'
            if parse1.scheme == 'https':
                port = '443'
        item = {
            'host': parse1.hostname,
            'port': port,
            'scheme': parse1.scheme,
            'path':parse1.path
        }
        #target=item['scheme'].strip()+':'+'//'+item['host'].strip()+':'+item['port'].strip()
        return item
        
def RequestHeader():
    random_ip = "10.0.{}.{}".format(random.randint(1, 254), random.randint(1, 254))
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Accept-Language": "en",
        "X-Forwarded-For": random_ip,
        "X-Real-IP" :random_ip,
    }
    return headers

#数据处理
def frameDataDeal(data):
    #print(data)
    vulnerabilities=str(data[3])
    vuln=vulnerabilities.split('|')
    
    result=str(data[0])
    #print(result)
    data=re.findall('\[ (.*) \]', result)
    #print(data)
    data=' '.join(data)
    #print(data)
    table=data.split('|')
    #print(table)
    table[1]=re.findall('m\[(.*)\]', table[1])
    table.append(vuln[6])
    
    #print(table)
    return table