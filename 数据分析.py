import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

def main(data_path_c):
    x_ticks=os.listdir(data_path_c) # 获取图像横轴
    m=len(x_ticks) # 获取矩阵纵向维度
    n=0
    a,b=0,0 # a=n;b=m
    num,num1=0,0
    c=0
    # lst=[] # 初始化一个列表
    
# 获取矩阵横向维度，创建列表的目的是为了防止每天的观测站数量不一，并取最大值，后面可获得哪天的观测站有未工作的
    for i in x_ticks:
        path=str(data_path+'/'+i)
        l=os.listdir(path) # 获取图像纵轴
        num=len(l)
        if num1<=num:
            num1=num
        if num1>num or i==x_ticks[len(x_ticks)-1]:
            y_ticks=l
    c=len(y_ticks)
    s=c
    for l in range(0,c):
        y_ticks[l]='station'+format(str(s),'0>2s')
        s=c-l-1
    n=num1
    a=n-1
    data_matrix=np.zeros((n,m)) # 创建一个矩阵

    for items1 in x_ticks:
        station_path=str(data_path+'/'+items1)
        x1=os.listdir(station_path) # 获取图像纵轴
        # station_num=len(y_ticks) # 获取观测站的数量
        # lst.append(station_num) # 获取每一天观测站的数量
        for items2 in x1:
            picture_path=str(station_path+'/'+items2)
            picture_list=os.listdir(picture_path)
            picture_num=len(picture_list)
            data_matrix[a,b]=picture_num
            a-=1
            if a<0:
                a=n-1
        b+=1        
    plt.figure(figsize=(m/2,n/2))
    sns.heatmap(data_matrix,xticklabels=x_ticks,yticklabels=y_ticks,annot=True,cmap='Greens',vmin=0,vmax=24)
    plt.show()

def replace_left_slash(input_str):
    output_str = input_str.replace('\\','/')
    return output_str

if __name__=='__main__':
    # data_path=input(rf'F:\marine_rubbish_online')
    # data_path=replace_left_slash(data_path)
    data_path=rf"F:\marine_rubbish_online_data"
    main(data_path)