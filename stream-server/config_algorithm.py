
from samples.license_plate_recognition.license_plate_recognition import *
from samples.license_plate_recognition.config_logic import *
from samples.yolov5_fastpose_posec3d.yolov5_fastpose_posec3d import *
from samples.yolov5_fastpose_posec3d.config_logic import *
map_type={16:'license_plate_recognition',15:'yolov5_fastpose_posec3d'}


class Algorithms:
    def license_plate_recognition_build_config(self,algorithm_name,stream_path,data,port):
        return license_plate_recognition_build_config(algorithm_name,stream_path,data,port)
    def license_plate_recognition_trans_json(self,json_data,task_id,Type,up_list):
        return  license_plate_recognition_trans_json(json_data,task_id,Type,up_list)
    def license_plate_recognition_logic(self,json_data,up_list,rm_list):
        return license_plate_recognition_logic(json_data,up_list,rm_list)
    def yolov5_fastpose_posec3d_build_config(self,algorithm_name,stream_path,data,port):
        return yolov5_fastpose_posec3d_build_config(algorithm_name,stream_path,data,port)
    def yolov5_fastpose_posec3d_trans_json(self,json_data,task_id,Type,up_list):
        return  yolov5_fastpose_posec3d_trans_json(json_data,task_id,Type,up_list)
    def yolov5_fastpose_posec3d_logic(self,json_data,up_list,rm_list):
        return yolov5_fastpose_posec3d_logic(json_data,up_list,rm_list)
    