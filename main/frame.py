import os
import sys
import multiprocessing
from main import deal
from main import output



        
class check_frame:
    def __init__(self,target):
        self.name=target
     #文件处理   
    def fileDeal(self):
        output.FrameTitle()
        file_object = open(self.name.name,'r',encoding ="utf-8")
        lines = file_object.readlines()
        pool = multiprocessing.Pool(1)
        for url in lines:
            url=url.strip('\n')
            result=deal.Deal(url).RequestHeadDeal()
            #print(result)
            pool.apply(check_frame.API, args=(result,))
        pool.close()
        pool.join()
    #请求
    def API(target_url):
        #去掉目标后缀/
        #print(target_url)
        if target_url[-1] == '/':
            target_url=target_url[0:-1]
        #print(target_url)
        main = "observer_ward.exe"
        f = os.popen('cd Finger &'+main+" -t {}".format(target_url))    
        data = f.buffer.read().decode(encoding='utf8')
        #print(data)
        data =data.split('\r\n')
        #print(data)
        content=deal.frameDataDeal(data)
        output.FrameOutPut(content)
        f.close()    
        #print (data)
def API2(target_url):
        #去掉目标后缀/
    output.FrameTitle()    
    #print(target_url)
    main = "observer_ward.exe"
    f = os.popen('cd Finger &'+main+" -t {}".format(target_url))    
    data = f.buffer.read().decode(encoding='utf8')
        #print(data)
    data =data.split('\r\n')
        #print(data)
    content=deal.frameDataDeal(data)
    #print(content)
    output.FrameOutPut(content)
    f.close()    
        #print (data)
        
        
def install():
    main = "observer_ward.exe"
    f = os.popen('cd Finger &'+main+" -u ")
    data = f.buffer.read().decode(encoding='utf8')  
    #print (data)
    data =data.split('\n')  
    print(data[10])
    print(data[11]) 