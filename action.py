import os
from yolo import YOLO
from PIL import Image
import re
from urllib.parse import unquote

def predict(image_path):
    #----------------------------------------------------------------------------------------------------------#
    #   count               指定了是否进行目标的计数
    #   crop                指定了是否在单张图片预测后对目标进行截取
    #----------------------------------------------------------------------------------------------------------#
    count           = True
    output_list = []
    yolo = YOLO()
    for single_image_path in image_path:
        output_dict = {}
        '''
        从路径中读取 经纬度、日期、时间
        "{year_month_day}/{deviceId}/{hour}_{recordId}.jpg"
        '''
        parts = single_image_path.split('/')
        year = parts[-3][:4]
        month = parts[-3][4:6]
        day = parts[-3][6:8]
        deviceId = parts[-2]
        hour = parts[-1].split('_')[0]
        recordId = parts[-1].split('_')[1].split('.')[0]
        print(year, month, day, deviceId, hour,recordId)
        # 使用变量来存储中间结果，提高代码的可读性和可维护性
        output_dict = {'deviceId': deviceId, 
                    'year': year, 'month': month, 'day': day, 
                    'hour': hour,'recordId':recordId}
        with open(single_image_path, 'rb') as f:    
            image = Image.open(r''+single_image_path)
            respic,classes_nums,results = yolo.detect_image(image,count=True)
            #改名保存respic，在原有的路径下加_res保存
            new_name = single_image_path.split('.')[0]+'_res.jpg'
            new_name = new_name.replace("down_img", "img")
            if not os.path.exists(os.path.dirname(new_name)):
                os.makedirs(os.path.dirname(new_name))
            respic.save(new_name,quality=50)
            #将图片的路径转为url
            respic_url = new_name.replace("/home/admin/img", "http://47.107.69.67:8081/images")
            output_dict['respic_url'] = respic_url
            #数据类型转为str
            classes_nums = [str(i) for i in classes_nums]
            output_dict['foam'] = classes_nums[0]
            output_dict['branch'] = classes_nums[1]
            output_dict['bag'] = classes_nums[2]
            output_dict['bottle'] = classes_nums[3]
            output_dict['result'] = results
        output_list.append(output_dict)
    return output_list

if __name__ == "__main__":
    pass


