from gif_maker import VideoToGif
# from goprocam import GoProCamera, constants
import os

path = os.path.dirname(__file__)
os.chdir(path)

# goproCamera = GoProCamera.GoPro()
# goproCamera.shoot_video(10)
# goproCamera.downloadLastMedia(custom_filename='video.MP4')

videotogif = VideoToGif()
videotogif.saveGif(video_name = 'video.MP4')


print('İŞLEM TAMAM')