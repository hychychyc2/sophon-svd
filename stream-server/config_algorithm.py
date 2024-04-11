
from samples.blank.config_logic import *
from samples.blank.blank import *
from samples.yolox_bytetrack_osd_encode.config_logic import *
from samples.yolox_bytetrack_osd_encode.yolox_bytetrack_osd_encode import *
from samples.license_plate_recognition.license_plate_recognition import *
from samples.license_plate_recognition.config_logic import *
from samples.yolov5_fastpose_posec3d.yolov5_fastpose_posec3d import *
from samples.yolov5_fastpose_posec3d.config_logic import *
from samples.yolov5.yolov5 import *
from samples.yolov5.config_logic import *
from samples.yolov8.yolov8 import *
from samples.yolov8.config_logic import *
from samples.retinaface.retinaface import *
from samples.retinaface.config_logic import *

map_type={16:'license_plate_recognition',15:'yolov5_fastpose_posec3d',14:'yolov5',13:'yolov8',12:'retinaface', 88:'yolox_bytetrack_osd_encode', 10000:'blank'}


class Algorithms:
    def blank_build_config(self,algorithm_name,stream_path,data,port,i):
        return blank_build_config(algorithm_name,stream_path,data,port,i)
    def blank_trans_json(self,json_data,task_id,Type,up_list):
        return blank_trans_json(json_data,task_id,Type,up_list)
    def blank_logic(self,json_data,up_list,rm_list):
        return blank_logic(json_data,up_list,rm_list)
    def yolox_bytetrack_osd_encode_build_config(self,algorithm_name,stream_path,data,port,i):
        return yolox_bytetrack_osd_encode_build_config(algorithm_name,stream_path,data,port,i)
    def yolox_bytetrack_osd_encode_trans_json(self,json_data,task_id,Type,up_list):
        return yolox_bytetrack_osd_encode_trans_json(json_data,task_id,Type,up_list)
    def yolox_bytetrack_osd_encode_logic(self,json_data,up_list,rm_list):
        return yolox_bytetrack_osd_encode_logic(json_data,up_list,rm_list)
    def license_plate_recognition_build_config(self,algorithm_name,stream_path,data,port,i):
        return license_plate_recognition_build_config(algorithm_name,stream_path,data,port,i)
    def license_plate_recognition_trans_json(self,json_data,task_id,Type,up_list):
        return  license_plate_recognition_trans_json(json_data,task_id,Type,up_list)
    def license_plate_recognition_logic(self,json_data,up_list,rm_list):
        return license_plate_recognition_logic(json_data,up_list,rm_list)
    
    def yolov5_fastpose_posec3d_build_config(self,algorithm_name,stream_path,data,port,i):
        return yolov5_fastpose_posec3d_build_config(algorithm_name,stream_path,data,port,i)
    def yolov5_fastpose_posec3d_trans_json(self,json_data,task_id,Type,up_list):
        return  yolov5_fastpose_posec3d_trans_json(json_data,task_id,Type,up_list)
    def yolov5_fastpose_posec3d_logic(self,json_data,up_list,rm_list):
        return yolov5_fastpose_posec3d_logic(json_data,up_list,rm_list)
    
    def yolov5_build_config(self,algorithm_name,stream_path,data,port,i):
        return yolov5_build_config(algorithm_name,stream_path,data,port,i)
    def yolov5_trans_json(self,json_data,task_id,Type,up_list):
        return  yolov5_trans_json(json_data,task_id,Type,up_list)
    def yolov5_logic(self,json_data,up_list,rm_list):
        return yolov5_logic(json_data,up_list,rm_list)
    
    def yolov8_build_config(self,algorithm_name,stream_path,data,port,i):
        return yolov5_build_config(algorithm_name,stream_path,data,port,i)
    def yolov8_trans_json(self,json_data,task_id,Type,up_list):
        return  yolov5_trans_json(json_data,task_id,Type,up_list)
    def yolov8_logic(self,json_data,up_list,rm_list):
        return yolov5_logic(json_data,up_list,rm_list)
    
    def retinaface_build_config(self,algorithm_name,stream_path,data,port,i):
        return retinaface_build_config(algorithm_name,stream_path,data,port,i)
    def retinaface_trans_json(self,json_data,task_id,Type,up_list):
        return  retinaface_trans_json(json_data,task_id,Type,up_list)
    def retinaface_logic(self,json_data,up_list,rm_list):
        return retinaface_logic(json_data,up_list,rm_list)