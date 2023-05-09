#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = EASY

# 导入必要的模块
import os
import requests
import zipfile
import random
import io
import shutil

from main import output

user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/68.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) '
            'Gecko/20100101 Firefox/68.0',
            'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/68.0']

head = {
    "User-Agent": random.choice(user_agents)
}

    
 
# 定义一个检查环境的类
class CheckEnv:
    def __init__(self):
        self.path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) #绝对路径Find
        self.update() # 更新
        
    #更新指纹库
    def update(self):
        home=self.path
        library = os.path.join(home, 'lib')
        min_file="library-main/lib"
        max_file="library-main"
        auth = ('username', 'password')
        url = 'https://github.com/LittleBear4/library/archive/master.zip'
        output.updateTitle()
        try:
            response = requests.get(url)
            content = io.BytesIO(response.content)
            with zipfile.ZipFile(content) as zip_file:
                zip_file.extractall('./')       
            shutil.rmtree(library)
            d_folder = shutil.move(min_file,home)
            shutil.rmtree(max_file)
            output.updateResult()
        except:
            print("网络出现问题无法访问，请重试")
            print("或者手动下载并替换lib:")
            print("https://github.com/LittleBear4/library/archive/master.zip")