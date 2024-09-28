import psutil


CPU_thresholds = 80
Memory_thresholds = 80
Disk_thresholds = 80

def check_cpu_threshold():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_thresholds:
        print(f"cpu usage is high:{cpu_usage}%")
    return cpu_usage

def check_memory_threshold():
    memory_info = psutil.virtual_memory()
    memory_used = memory_info.percent
    if memory_used > Memory_thresholds:
        print(f"memory usage is high:{memory_used}%")
    return memory_used

def check_disk_threshold():
    disk_info = psutil.disk_usage('/')
    disk_used = disk_info.percent
    if disk_used > Disk_thresholds:
        print(f"disk usage is high:{disk_used}%")
    return disk_used

def check_running_process():
    no_of_running_process = len(psutil.pids())
    return no_of_running_process

def sys_health():
    cpu = check_cpu_threshold()
    memory = check_memory_threshold()
    disk = check_disk_threshold()
    process = check_running_process()

    monitoring_health = {
        'cpu usage' : cpu,
        'memory usage' : memory,
        'diskk usage' : disk,
        'total processes' : process
    }

    return monitoring_health
report = sys_health()


print(report)
