import os
import math
import datetime
import cv2

class FrameExtractor():
    '''
    Class used for extracting frames from a video file.
    '''
    def __init__(self, video_path):
        self.video_path = video_path
        self.vid_cap = cv2.VideoCapture(video_path)
        self.n_frames = int(self.vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = int(self.vid_cap.get(cv2.CAP_PROP_FPS))
        
    def get_video_duration(self):
        duration = self.n_frames/self.fps
        print(f'Duration: {datetime.timedelta(seconds=duration)}')
        
    def get_n_images(self, every_x_frame):
        n_images = math.floor(self.n_frames / every_x_frame) + 1
        print(f'Extracting every {every_x_frame} (nd/rd/th) frame would result in {n_images} images.')
        
    def extract_frames(self, every_x_frame, img_name, dest_path=None, img_ext = '.jpg'):
        if not self.vid_cap.isOpened():
            self.vid_cap = cv2.VideoCapture(self.video_path)
        
        if dest_path is None:
            dest_path = os.getcwd()
        else:
            if not os.path.isdir(dest_path):
                os.mkdir(dest_path)
                print(f'Created the following directory: {dest_path}')
        
        frame_cnt = 0
        img_cnt = 0

        while self.vid_cap.isOpened():
            
            success,image = self.vid_cap.read() 
            
            if not success:
                break
            
            if frame_cnt % every_x_frame == 0:
                img_path = os.path.join(dest_path, ''.join([img_name, '_', str(img_cnt), img_ext]))
                cv2.imwrite(img_path, image)  
                img_cnt += 1
                
            frame_cnt += 1
        
        self.vid_cap.release()
        cv2.destroyAllWindows()
#######################################loop on each downloaded vedio
        
videos = os.listdir('test_data/Real/')  #### In place of 'Videos' replace it by the folder name where all the video data is placed
for ind, vedio in enumerate(videos):
    try:
        path = 'test_data/Real/'+ vedio  #### In place of 'Videos' replace it by the folder name where all the video data is placed
        fe = FrameExtractor(path)
        fe.get_video_duration()
        fe.get_n_images(every_x_frame = 30) ### Adjust the frame rate as per the length of video
        fe.extract_frames(every_x_frame = 30, img_name = str(ind) + 'real', dest_path = 'test_data/Real_frames')
    except Exception as e:
        print(e)

videos = os.listdir('test_data/Fake/')  #### In place of 'Videos' replace it by the folder name where all the video data is placed
for ind, vedio in enumerate(videos):
    try:
        path = 'test_data/Fake/' + vedio  #### In place of 'Videos' replace it by the folder name where all the video data is placed
        fe = FrameExtractor(path)
        fe.get_video_duration()
        fe.get_n_images(every_x_frame = 60) ### Adjust the frame rate as per the length of video
        fe.extract_frames(every_x_frame = 60, img_name = str(ind) + 'fake', dest_path = 'test_data/Fake_frames')
    except Exception as e:
        print(e)