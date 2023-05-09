import argparse
from main import deal
from main import frame
from main import ask
from main import Update
#命令行参数
def parse_args():   
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', dest='url', help='Target Url')
    parser.add_argument('-f', '--file', dest='file', help='Target Url File', type=argparse.FileType('r'))
    parser.add_argument('-m', '--middleware', dest='middleware', help='Target middleware',action='store_true')
    parser.add_argument('-p', '--poc', dest='poc', help='Proof of concept',action='store_true')
    parser.add_argument('-o', '--outputurl', dest='outputurl', help='Output file name')
    parser.add_argument('-i', '--install', dest='install', help='finger install',action='store_true')
    parser.add_argument('-up', '--update', dest='update', help='Update the yaml file',action='store_true')
    return parser.parse_args()
    
 
#程序入口点 
def entrance():
    args = parse_args()
    if args.file:
        file=args.file
        if not args.middleware and not args.poc:
            frame.check_frame(file).fileDeal()
            file=deal.Deal(file).fileDeal()            
        elif args.middleware:
            frame.check_frame(file).fileDeal()
        elif args.poc:    
            file=deal.Deal(file).fileDeal()
        
    if args.url:
        url=args.url
        if not args.middleware and not args.poc:    
            frame.API2(url)
            target=deal.Deal(url).RequestHeadDeal()
            ask.Request(target)
        elif args.middleware:
            frame.API2(url)
        elif args.poc: 
            target=deal.Deal(url).RequestHeadDeal()
            ask.Request(target)

    
    if args.install:
        frame.install()
        
    if args.update:
        Update.CheckEnv()