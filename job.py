from utils.read_img_dir import process_new_images 
def job(image_folder):
    print("Job is executed at the top of the hour!")
    process_new_images(image_folder)
    print("Job is done!")

