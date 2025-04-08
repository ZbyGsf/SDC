import schedule
import time
import job
'''
Step 1: Using the schedule module to execute the job function hourly
Step 2: In the job function, call the process_new_images function to process newly added images and create database updates for the image paths
Step 3: In the process_new_images function, call the action function to retrieve messages
Step 4: In the save_messages_to_db function, call the save_dicts_to_db function to insert messages into the database table

image_folder: The image folder containing all images
'''

if __name__ == '__main__':
    # 
    print("start")
    image_folder = r'your_path'
    # image_folder = r'G:/temp'
    schedule.every().hour.at(":00").do(job.job,image_folder)
    while True:
        schedule.run_pending()
        time.sleep(60)
        print("Waiting for the next job...")