import os
import requests
import yaml
import socket
import urllib3
from main import deal
from main import output


proxy={"http":"http://127.0.0.1:8080"}



def Request(target_url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    output.Tag(target_url)
    #打开yaml    
    for filename in os.listdir("lib"):
        with open(os.path.join("lib", filename), 'r',encoding = 'utf-8') as f:
            #print(filename)文件名
            data = f.read()
            #print (data)文件中的数据
            cfg=yaml.load(data,Loader=yaml.FullLoader)
            #yaml数据
            path=((cfg['rules'])[0])['poc']
            body=((cfg['rules'])[0])['body']
            method=((cfg['rules'])[0])['method']
            icon=((cfg['rules'])[0])['check']
            name=(cfg['name']) 
            
            try:
                #Clickhouse
                if 'Clickhouse' in filename:
                    for path in path:
                        url=target_url+path
                        response = requests.get(url=url, headers=deal.RequestHeader(),verify=False,timeout=5.1)
                        if  response.status_code==204:
                            flag=True
                            output.output(flag,name,url)
                            break
                        else:
                            flag=False
                    if flag == False:
                        output.output(flag,name,url)            
            
                #jmx-console
                elif 'jmx-console' in filename:
                    for path in path:
                        url=target_url+path

                        response = requests.get(url=url, headers=deal.RequestHeader(),verify=False,timeout=5.1)
                        #遇到401怎么办？
                        if icon in response.text:
                            flag=True
                            output.output(flag,name,url)
                            break
                        else:
                            flag=False       
                    if flag == False:
                        output.output(flag,name,url)
                    
                # swagger        
                elif 'Swagger' in filename or 'cas' in filename:
                    for path in path:
                        url=target_url+path
                        response = requests.get(url=url, headers=deal.RequestHeader(),verify=False,timeout=5.1)
                        if icon in response.text and response.status_code==200:
                            flag=True
                            output.output(flag,name,url)
                    if flag == False:
                        output.output(flag,name,url)
                
                #Nocas
                elif 'noauth' in filename:
                    for path in path:
                        url=target_url+path
                        headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
                            "User-Agent": "Nacos-Server"
                        }
                        response = requests.get(url=url, headers=headers,verify=False,timeout=5.1)
                        if ('pageNumber' in response.text and 'password' in response.text) or '管理配置' in response.text:
                            flag=True
                            output.output(flag,name,url)
                            break
                        else:
                            flag=False
                    if flag == False:
                        output.output(flag,name,url) 
 
                #请求
                else:
                    for path in path:
                        #get请求
                        if body is None:
                            url=target_url+path
                            response = requests.get(url=url, headers=deal.RequestHeader(),verify=False,timeout=5.1)
                            if icon in response.text:
                                flag=True
                                output.output(flag,name,url)
                                break
                            else:
                                flag=False
                        else:
                            #post请求
                            url=target_url+path+check
                            response = requests.post(url=url, headers=deal.RequestHeader(),verify=False,timeout=5.1)
                            if icon in response.text:
                                flag=True
                                output.output(flag,name,url)
                                break
                            else:
    
                                flag=False
                    if flag == False:
                        output.output(flag,name,url)            
            except:
                output.ERROR(url)
    