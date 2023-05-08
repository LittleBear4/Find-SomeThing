from rich.console import Console
from pyfiglet import Figlet
from random import sample

console = Console()
def titlestyle():
    color_list = ['red', 'blue', 'yellow', 'green', 'magenta',' cyan','white']
    result = sample(color_list, k=1)
    color=result[0]
    console.print(Figlet(font='slant').renderText('Find-SomeThing'), style='bold {}'.format(color))
    print('''                                       
                                                  版本:测试版
                                                  作者:西瓜麻辣烫(雷石)
                                                  鸣谢:三米前有蕉皮(0x727)
    '''
    )
def red(info):
    console.print(info,style='bold red')
def green(info):
    console.print(info,style='bold green')
def yellow(info):
    console.print(info,style='bold yellow')

