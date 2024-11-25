import subprocess
import os

# sum(VmSize), sum(VmRSS)
def get_values(pid: int):

    res = subprocess.run(
        ['grep', '-E', 'VmSize|VmRSS', f'/proc/{pid}/status'],
        capture_output=True,
        text=True
    )

    lines = res.stdout.split('\n')

    vmsize = vmrss = None

    for line in lines:
        if 'VmSize' in line:
            vmsize = line.split()[1]
        elif 'VmRSS' in line:
            vmrss = line.split()[1]

    # print('VmSize: ', vmsize)
    # print('VmRSS: ', vmrss)

    return vmsize, vmrss



if __name__ == "__main__":

    sum_vmsize = sum_vmrss = 0
    for p in os.listdir('/proc/'):
        try:
            vmsize, vmrss = get_values(pid=p)
            sum_vmsize += int(vmsize)
            sum_vmrss += int(vmrss)
        except:
            continue


    print('VmSize sum: ', sum_vmsize)
    print('VmRSS sum: ', sum_vmrss)
