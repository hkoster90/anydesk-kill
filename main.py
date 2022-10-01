import psutil
import time

def get_current_processes():
    return {p.name(): p.info for p in psutil.process_iter(['name', 'username', 'pid'])}

def get_process_id(process_name:str="anydesk")->int|None:
    procs = get_current_processes()
    procs_names = procs.keys()
    pid = None
    for proc in procs_names:
        if process_name in proc.lower():
            pid = procs[proc]["pid"]
    return pid

def kill_process(pid:int):
    if psutil.pid_exists(pid=pid):
        psutil.Process(pid=pid).kill()

if __name__ == "__main__":
    while True:
        pid =  get_process_id()
        if pid != None:
            kill_process(pid=pid)
        time.sleep(10)