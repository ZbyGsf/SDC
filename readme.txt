###########
总体逻辑
#-----------
后台长时间运行 main.py API_getpicture.py API_getresult.py 文件。
API_getpicture 用于接收推送的图片
API_getresult 用于查询数据库的内容
main 用于处理接收到的图片，并将处理结果保存到数据库中
############

###########
main.py
#-----------
step1: 在main.py 中，使用 schedule 模块，每小时执行一次 job 函数
step2: 在 job 函数中，调用 process_new_images 函数，处理新增的图片,并建一个‘图片路径数据库’更新图片的路径
step3: 在 process_new_images 函数中，调用 action 函数，处理图片。每张图片的结果都是一个字典，所有字典作为一个list返回
step4: 在 process_new_images 函数中，调用 save_dicts_to_db 函数，并建一个‘识别结果数据库’ 保存识别结果
#------------
input 
#-----------
image_folder : 图片文件夹,包含所有图片（绝对路径）
#-----------
output
#-----------
porecessed_images.db : 一个数据库，里面包含所有的处理过了的图片，通过对这个数据库的不断更新，来筛选没处理的图片
object_result.db : 一个数据库，里面包含处理的结果，以字典的格式写入。每张图片处理的结果保存为字典，字典格式如下
                    {'deviceId':deviceId, 
                    'year': year, 'month': month, 'day': day, 
                    'hour': hour, 'picture_url' : picture_url
                    'foam':num1,'branch':num2,'bag':num3,'bottle':num4
                    'result' : result ,'recordId' : recordId
                    }
其中，result是一个numpy数组主要用于保存每个检测框， result.shape = [5,N] , 依次为： 垃圾种类，top, left, bottom, right
############

###################################################################################################
job.py
#--------------------------------------------------------------------------------------------------

###################################################################################################

###################################################################################################
read_img_dir.py
#--------------------------------------------------------------------------------------------------
###################################################################################################

###################################################################################################
action.py
#--------------------------------------------------------------------------------------------------
###################################################################################################

#################
API_getpicture.py
#----------------
用于接收推送的图片
port=23333
@app.route("/image", methods=["POST"])
################

################
API_getresult.py
#---------------
用于查询数据库的内容
port=5000
@app.route('/get_data', methods=['POST'])
################

