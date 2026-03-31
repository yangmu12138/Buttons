import time
import socket
import io
from PIL import Image
import numpy as np
import cv2
import concurrent.futures
from PIL import ImageDraw, ImageFont
class Buttons_functions_get_ip:
    def __init__(self):
        self.udp_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
        self.steer_addr=("0.0.0.0",8080)
        self.steer_ip=self.get_moter_ip(self.steer_addr)
    def get_ip(self,addr):
        self.udp_socket.bind(addr)
        _,ip=self.udp_socket.recvfrom(32)
        if len(ip)>0:
            return ip

    def get_moter_ip(self,addr):
        return_ip_v=self.get_ip(addr=addr)
        return return_ip_v

class Buttons_functions_video_stream:
    def __init__(self,t=None):
        self.fused_image=image_fuse
        self.t=t
        self.cam_addr=[("0.0.0.0",9089),("0.0.0.0",9091)]
        self.vision_cache_list=self.video_stream_capture

    def cam_1(self):
        addr=self.cam_addr[0]
        s_1= socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
        s_1.bind(addr)
        data, _ = s_1.recvfrom(100000)
        bytes_stream = io.BytesIO(data)
        image = Image.open(bytes_stream)
        img = np.asarray(image)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img=cv2.flip(img,1)
        return img

    def cam_2(self):
        addr=self.cam_addr[1]
        s_2= socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
        s_2.bind(addr)
        data, _ = s_2.recvfrom(100000)
        bytes_stream = io.BytesIO(data)
        image = Image.open(bytes_stream)
        img = np.asarray(image)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img=cv2.flip(img,1)
        return img

    def capture_(self):
        with concurrent.futures.ThreadPoolExecutor()as executor:
            picture_1=executor.submit(self.cam_1)
            picture_2=executor.submit(self.cam_2)
            img_1=picture_1.result()
            img_2=picture_2.result()
        return img_1,img_2

    def fuse_(self,img_1,img_2):
        image_1=img_1
        height_1,width_1=image_1.shape[:2]
        cut_position_1=width_1//3
        new_img_1=image_1[:,cut_position_1:]
        image_2=img_2
        height_2,width_2=image_2.shape[:2]
        cut_position_2=width_2//3
        new_img_2=image_2[:,:cut_position_2]
        fuse_image=cv2.hconcat([new_img_2,new_img_1])
        return fuse_image

    def image_fuse(self):
        image_=self.capture_()
        image_1=image_[0]
        image_2=image_[1]
        fused_image=fuse_(img_1=image_1,img_2=image_2)
        return fused_image

    def video_stream_capture(self):
        num_=self.t
        vision_cache=[]
        for _ in range(num_):
            fused_image=self.image_fuse()
            self.vision_cache.append(fused_image)
        return vision_cache

#transform words to image
def words_2_img(input_):
	width,height=240,180
	background_color=(255,255,255)
	image=Image.new('RGB',(width,height),background_color)
	draw=ImageDraw.Draw(image)
	font=ImageFont.truetype("arial.ttf",36)
	text=input_
	text_color=(0,0,0)
	text_position=(30,60)
	draw.text(text_position,text,fill=text_color,font=font)
	image.save(folder+text+'.png')
	image.show()


class Buttons_functions_send_order:
    def __init__(self,order,addr):
        self.order=order
        self.addr=addr
        self.udp_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)

    def send_order(self):
        self.udp_socket.sendto(self.order.encode('utf-8'),self.addr)
   
def get_message():
    pass


class Buttons_adjust:
    def __init__(self,message):
        self.auto_run=None
        self.steer_run=None
        self.message=message
        
    def judge(self):
        if self.message!=None:
            self.steer_run(state=self.message)
        else:
            self.auto_run()
        
   