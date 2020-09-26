import re
import os
from subprocess import PIPE, Popen, STDOUT
import time

if __name__ == "__main__":
    p = Popen('docker images', shell=True, stdout=PIPE, stderr=STDOUT)
    for line in p.stdout.readlines():
        string = str(line)
        m = re.match(r'(^ufleet[^\s]*\s*)\s([^\s]*\s)', string)
        image_name = m.group(1).strip(' ')
        # tag
        itag = m.group(2)
        # tar包的名字
        tar_name = image_name.split('/')[-1]
        print(tar_name)
        tarball = tar_name + '.tar'
        ifull = image_name + ':' + itag
        # save
        cmd = 'docker save -o ' + tarball + ' ' + ifull
        print(os.system(cmd))
        os.system('mkdir -p /data/python_save_images/')
        # 将tar包放在临时目录
        print(os.system('mv %s /data/python_save_images/' % tarball))
        retval = p.wait()
