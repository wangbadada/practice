# 创建函数： def[函数名] （[参数]）：[函数代码块]
'''
def print_lol(the_list,level):
     for each_item in the_list:
         if isinstance(each_item,list):
             print_lol(each_item,level+1)
         else:
             for tab_stop in range(level):
                 print("\t",end='')
             print(each_item)
movies=["The Holy Grail",1975,"Terry Jones&Terry Gilliam",91,
	 ["Graham Chapman",
 	 ["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]

print_lol(movies,0)
'''

#open()打开数据作为单个文本行
'''
data=open('sketch1.txt')
for each_line in data:
    (role,line_spoken)=each_line.split(':',1)
    print(role,end='')
    print(' said: ',end='')
    print(line_spoken,end='')
data.close()
'''
#异常处理
'''
try:
    data=open('missing.txt')
    print(data.readline(),end='')
except IOError:
    print('File error')
finally:
    if 'data' in locals():
        data.colse()
        '''

'''try:
    data=open('missing.txt')
    print(data.readline(),end='')
except IOError as err:
    print('File Error: '+str(err))
finally:
    if 'data' in locals():
        data.close()'''
'''try:
    data=open('its.txt','w')
    print("it is...",file=data)
except IOError as err:
    print('File Error: '+str(err))
finally:
    if 'data' in locals():
        data.close()'''

'''try:
    with open('its.txt','w') as data:
        print('it is...',file=data)
except IOError as err:
    print('File Error:'+str(err))'''
'''man=[]
other=[]
try:
    data=open("sketch1.txt")
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(":",1)
            line_spoken=line_spoken.strip()
            if role=='Man':
                man.append(line_spoken)
            elif role=='Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')'''
'''try:
    man_file = open('man_data.txt','w')
    other_file = open('other_data.txt','w')

    print(man, file=man_file)
    print(other, file=other_file)
except IOError as err:
    print('File error: '+str(err))
finally:
    if 'man_file' in locals():
        man_file.close()
    if 'other_file' in locals():
        other_file.close()'''
'''try:
    with open('man_data.txt','w') as man_file:
        print('man',file=man_file)
    with open('other_data.txt','w') as other_file:
        print('other',file=other_file)
except IOError as err:
    print('File Error: '+str(err))
finally:
    man_file.close()
    other_file.close()'''


'''
man=[]
other=[]
try:
    data=open("sketch1.txt")
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(":",1)
            line_spoken=line_spoken.strip()
            if role=='Man':
                man.append(line_spoken)
            elif role=='Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')

try:
    man_file=open('man_data.txt','w')
    other_file=open('other_data.txt','w')
    print(man,file=man_file)
    print(other,file=other_file)
    man_file.close()
    other_file.close()
except IOError:
    print('File Error.')'''


#indent缩进
#isinstance判断each_item是否为列表
'''def print_lol(the_list,indent=False,level=0):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t',end='')
                print(each_item)'''

#standard output（标准输出）这是使用“print()”BIF时代码写数据的默认位置。这通常是屏幕。
# 在python中，标准输出是指“sys.stdout”，可以从标准库的‘sys’模块导入。
# 向print_lol()函数增加第4个参数，用来标识把数据写入哪个位置。
# 一定要为这个参数提供一个缺省值sys.stdout，这样如果调用这个函数时没有指定文件对象则会依然写至屏幕。
import sys
def print_lol(the_list,indent=False,level=0,fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t',end='',file=fh)
            print(each_item,file=fh)
man=[]
other=[]
try:
    data=open("sketch1.txt")
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(":",1)
            line_spoken=line_spoken.strip()
            if role=='Man':
                man.append(line_spoken)
            elif role=='Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')
try:
    with open('man_data.txt','w') as man_file:
        print_lol(man,fh=man_file)
    with open('other_data.txt','w') as other_file:
        print_lol(other,fh=other_file)
except IOError as err:
    print('File Error: '+str(err))
finally:
    man_file.close()
    other_file.close()