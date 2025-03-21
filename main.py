import schedule
import time
import job
'''
step1: 通过 schedule 模块，每小时执行一次 job 函数
step2: 在 job 函数中，调用 process_new_images 函数，处理新增的图片,并建一个数据库更新图片的路径
step3: 在 process_new_images 函数中，调用 action 函数，获取报文
step4: 在 save_messages_to_db 函数中，调用 save_dicts_to_db 函数，将报文插入数据库表

image_folder : 图片文件夹,包含所有图片
'''

if __name__ == '__main__':
    # 在每小时整点时执行 job 函数
    print("start")
    image_folder = r'/home/admin/down_img'
    # image_folder = r'G:/temp'
    schedule.every().hour.at(":00").do(job.job,image_folder)
    while True:
        schedule.run_pending()
        time.sleep(60)
        print("Waiting for the next job...")