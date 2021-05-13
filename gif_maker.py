import cv2
from PIL import Image
import os


path = os.path.dirname(__file__)
os.chdir(path)

class VideoToGif:

    def saveGif(self, video_name, resolution = 20, output_name = 'video.gif'):

        cap = cv2.VideoCapture(video_name)

        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(frame_count)

        scale_percent = resolution / 100
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH ) * scale_percent
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * scale_percent
        fps =  cap.get(cv2.CAP_PROP_FPS)
        dim = (int(width), int(height))

        video = []
        counter = 0
        while(cap.isOpened()):
            status, frame = cap.read()
            if status and counter % 10 == 0:
                frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                cv2.imshow('frame', frame)
                video.append(Image.fromarray(frame))
            counter += 1
            
            if counter == frame_count-1:
                break
        video[0].save('cikti.gif', save_all = True, append_images = video)
        cap.release()
        cv2.destroyAllWindows()