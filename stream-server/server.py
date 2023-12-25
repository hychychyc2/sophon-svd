from flask import Flask, request, jsonify
import requests
import argparse
import multiprocessing 
from multiprocessing import Process
import time
import json
import subprocess
import os
import signal
print(__name__)
app = Flask(__name__)
stream_path="/home/hyc/data/sophon-stream"
current_directory = os.getcwd()
process_pools={}
infos={}
Types={}
# in_thresh=3
# out_thresh=5
port=10001
map_type={16:'license_plate_recognition'}
def build_config(data):
    global port
    print(data)
    algorithm_name=map_type[data['Algorithm'][0]["Type"]]
    config_path=stream_path+'/samples/'+algorithm_name+'/config/'
    # stream_run_path=stream_path+"/samples/build"

    # cmd="cp -rf "+config_path+' '+stream_run_path
    # result = subprocess.run(cmd, shell=True)
    # print("Return Code:", result.returncode)
    demo_config_path=config_path+algorithm_name+'_demo.json'
    http_config_path=config_path+'http_push.json'
    det_config_path=config_path+'yolov5_group.json'
    with open(demo_config_path, 'r') as file:
    # 使用 json.load 将文件内容转换为字典
        json_data = json.load(file)
    # print(data["InputSrc"]["StreamSrc"]["Address"])
    json_data["channels"]=[json_data["channels"][0]]
    json_data["channels"][0]["url"]=data["InputSrc"]["StreamSrc"]["Address"]
    json_data["channels"][0]["sample_interval"]=data["Algorithm"][0]["DetectInterval"]
    json_data["channels"][0]["source_type"]=data["InputSrc"]["StreamSrc"]["Address"][:4].upper()
    with open(demo_config_path, 'w') as file:
        json.dump(json_data, file, indent=2)
    with open(http_config_path, 'r') as file:
    # 使用 json.load 将文件内容转换为字典
        json_data = json.load(file)
    # print(data["InputSrc"]["StreamSrc"]["Address"])
    json_data["configure"]["route"]="/flask_test/"+data['TaskID']
    json_data["configure"]["port"]=port

    with open(http_config_path, 'w') as file:
        json.dump(json_data, file, indent=2)
    with open(det_config_path, 'r') as file:
    # 使用 json.load 将文件内容转换为字典
        json_data = json.load(file)
    if(data["Algorithm"][0]["DetectInfos"]!=None):
        sx=min([i['X'] for i in data["Algorithm"][0]["DetectInfos"][0]["HotArea"]])
        sy=min([i['Y'] for i in data["Algorithm"][0]["DetectInfos"][0]["HotArea"]])
        tx=max([i['X'] for i in data["Algorithm"][0]["DetectInfos"][0]["HotArea"]])
        ty=max([i['Y'] for i in data["Algorithm"][0]["DetectInfos"][0]["HotArea"]])
        json_data["configure"]["roi"]={"left":sx,"top":sy,"width":tx-sx,"height":ty-sy}
        with open(det_config_path, 'w') as file:
            json.dump(json_data, file, indent=2)
    else:
        if("roi"in json_data["configure"].keys()):
            del json_data["configure"]["roi"]
        with open(det_config_path, 'w') as file:
            json.dump(json_data, file, indent=2)
    return demo_config_path,data['TaskID'],data['Algorithm'][0]["Type"]

def build_client(task_id,Type,result_url):
    global port
    # import pdb; pdb.set_trace()
    
    # client_app.run(debug=True, host='0.0.0.0', port=8000)
    cmd=["python3","client.py","--task_id="+str(task_id),"--type="+str(Type),"--port="+str(port),"--url="+str(result_url)]
    port+=1
    # cmd="python client.py --task_id="+str(task_id)+" --type="+str(Type)

    print(cmd)
    log_path=str(task_id)+"_client.log"
    with open(log_path, "w") as log_file:
        process = subprocess.Popen(cmd, shell=False, stdout=log_file, stderr=subprocess.STDOUT)
    return process
def build_client_2(task_id,Type):
    # import pdb; pdb.set_trace()
    client_app = Flask(__name__)
    @client_app.route('/flask_test/<string:task_id>', methods=['POST'])
    def receive_request6(task_id):
        json_data = request.json
        results={}
        frame_id=str(json_data["mFrame"]["mFrameId"])
        results["FrameIndex"]=frame_id
        # print(json_data.keys())
        if("mSubObjectMetadatas" in json_data.keys()):
            # print(json_data["mSubObjectMetadatas"][0]["mRecognizedObjectMetadatas"][0]["mLabelName"])
            names=[str(i["mRecognizedObjectMetadatas"][0]["mLabelName"]) for i in json_data["mSubObjectMetadatas"]]
        else:
            names=[]
        src_base64=json_data["mFrame"]["mSpData"]
        results["SceneImageBase64"]=src_base64
        results["AnalyzeEvents"]=[]
        results["TaskID"]=task_id
        # save_base64_image(src_base64,'gg3.jpg')
        base64s=[]
        up_list=[]
        for name in names:
            # print(name)
            # print(infos.keys())
            print(infos)
            if name in infos[task_id].keys():
                infos[task_id][name]["in"]+=1
                # print(infos[name]["in"])
                if infos[task_id][name]["in"]==in_thresh:
                    up_list.append(name)      
            else :
                infos[task_id][name]={}
                infos[task_id][name]["in"]=1
                if infos[task_id][name]["in"]==in_thresh:
                    up_list.append(name)
        # print(names)
        
        boxes=[]
        if("mSubObjectMetadatas" in json_data.keys()):
            for indx in range(len(json_data["mDetectedObjectMetadatas"])):
                tmp=json_data["mDetectedObjectMetadatas"][indx]
                tmp2=json_data["mSubObjectMetadatas"][indx]
                if tmp2["mRecognizedObjectMetadatas"][0]["mLabelName"] in up_list:
                    result={}
                    x1,y1=tmp["mBox"]["mX"],tmp["mBox"]["mY"]
                    x2=x1+tmp["mBox"]["mWidth"]
                    y2=y1+tmp["mBox"]["mHeight"]
                    boxes.append((x1,y1,x2,y2))
                    # print(tmp2["mFrame"]["mSpData"])
                    # save_base64_image(tmp2["mFrame"]["mSpData"],'gg.jpg')
                    # result["ImageBase64"]=crop_image_base64(src_base64, (x1,y1,x2,y2))
                    result["ImageBase64"]=tmp2["mFrame"]["mSpData"]
                    # print(result["ImageBase64"])
                    # save_base64_image(result["ImageBase64"],'gg2.jpg')

                    result["Box"]={"LeftTopY": y1,
                                    "RightBtmY": y2,
                                    "LeftTopX": x1,
                                    "RightBtmX": x2 }
                    result["Type"]=Types[task_id]
                    result["Extend"]={}
                    result["Extend"]["VehicleLicense"]=tmp2["mRecognizedObjectMetadatas"][0]["mLabelName"]
                    results["AnalyzeEvents"].append(result)
        rm_list=[]
        print(infos)
        for key in infos[task_id].keys():
            if key not in names:
                if "out" in infos[task_id][key].keys():
                    infos[task_id][key]["out"]+=1
                    if infos[task_id][key]["out"]>=out_thresh:
                        rm_list.append(key)          
                else:
                    infos[task_id][key]["out"]=1
        
        for key in rm_list:
            del infos[task_id][key]
        print(infos)
        print(up_list)

        if(len(up_list)):
            # response = requests.post(url, json=results, headers=headers)
            # print(response)
            with open("results/"+frame_id+".json", 'w') as file:
                json.dump(results, file, indent=2)
        # print(json_data)
        return jsonify({"message": "Request received and processed successfully", "response": 1})

        
    client_app.run(debug=True, host='0.0.0.0', port=8000)
        # print(1)
        # cmd=["python","client.py","--task_id="+str(task_id),"--type="+str(Type)]
        # print(cmd)
        # process = subprocess.Popen(cmd)
        # return process
def build_task(demo_config_path,task_id,Type,result_url):
    if(task_status(task_id)["Status"]==1):
        return "Task is already running."
    print(demo_config_path)
    print("Worker process started")
    time.sleep(3)
    stream_run_path=stream_path+"/samples/build"
    client_process = build_client(task_id,Type,result_url)   
    # client_process = Process(target=build_client_2,args=(task_id,Type))
    # client_process.start()       
    # client_process.join() 
    # client_process=Flask(__name__)
    os.chdir(stream_run_path)
    cmd=[stream_run_path+"/main","--demo_config_path="+demo_config_path]
    print(cmd)
    log_path=str(task_id)+"_stream.log"
    with open(log_path, "w") as log_file:
        stream_process = subprocess.Popen(cmd, shell=False, stdout=log_file, stderr=subprocess.STDOUT)    
    os.chdir(current_directory)
    # print("Return Code:", process.returncode)
    # print("Worker process completed")
    
    process_pools[task_id]=(stream_process,client_process)
    # with open('v.txt','w') as f:
    #     f.write(str(len(process_pools)))
    infos[task_id]={}
    Types[task_id]=Type
    # 启动进程
    # process.start()
    # process.join()
    return 0
def task_status(task_id):
    if(task_id in process_pools.keys()):
        res={}
        res["TaskID"]=task_id
        # print(int(process_pools[task_id][0].poll()==None))
        res["Status"]=int((process_pools[task_id][0].poll()==None))
        return res
    return {"Status":"No task"}
def task_list():
    ans=[]
    for key in infos.keys():
        ans.append(task_status(key))
    return ans
def del_task(task_id):
    if(task_status(task_id)["Status"]==1):
    # os.kill(process_pools[tasks_ids[task_id]].pid, signal.SIGINT)
        process_pools[task_id][0].kill()
        process_pools[task_id][1].kill()
        del process_pools[task_id]
        del infos[task_id]
        del Types[task_id]
        # process_pools[tasks_ids[task_id]][1].terminate()
        return 0
    else:
        return "No task or task ended"


@app.route('/task/delete', methods=['POST'])
def receive_request2():
    print(request.json)
    ans=del_task(str(request.json['TaskID']))
    if(ans == 0):
        return jsonify({"Code": 0, "Msg": "success"})
    else:
        return jsonify({"Code": -1, "Msg": str(ans)})
@app.route('/task/query', methods=['POST'])
def receive_request3():
    ans=task_status(str(request.json['TaskID']))
    if(ans['Status']==1):
        return jsonify({"Code": 0, "Msg": "success","Result":ans})
    else:
        return jsonify({"Code": 1, "Msg": "fail"})

@app.route('/task/list', methods=['POST'])
def receive_request66():
    # print(infos)
    return jsonify({"Code": 0, "Msg": "success","Result":task_list()})

@app.route('/task/create', methods=['POST'])
def receive_request():
    # 获取来自客户端的 JSON 数据
    demo_config_path,task_id,Type= build_config(request.json)
    print(request.json["Reporting"]["ReportUrlList"])
    stream_run_path=stream_path+"/samples/build"
    # 在这里处理接收到的数据
    ans=build_task(demo_config_path,task_id,Type,request.json["Reporting"]["ReportUrlList"])
    if(ans==0):
    # 返回响应给客户端
        return jsonify({"Code": 0, "Msg": "success"})
    else:
        return jsonify({"Code": -1, "Msg": str(ans)})
def argsparser():
    parser = argparse.ArgumentParser(prog=__file__)
    parser.add_argument('--stream_path', type=str, default='/home/hyc/data/sophon-stream', help='path of stream')
    args = parser.parse_args()
    return args
if __name__ == '__main__':
    args = argsparser()
    stream_path=args.stream_path
    app.run(debug=False, host='0.0.0.0', port=8001)


