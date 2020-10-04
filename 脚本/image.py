import os
import re
from subprocess import PIPE, Popen, STDOUT


def save_docker():
    save_file = str(input("请输入保存镜像地址的绝对路径>>>>>>"))
    os.system('mkdir -p %s' % save_file)
    p = Popen('docker images', shell=True, stdout=PIPE, stderr=STDOUT)
    for line in p.stdout.readlines():
        string = str(line)
        m = re.match(r'(^[^\s]*\s*)\s([^\s]*\s)', string)
        image_name = m.group(1).strip(' ')
        itag = m.group(2)
        tar_name = image_name.split('/')[-1]
        tarball = tar_name + '.tar'
        ifull = image_name + ':' + itag

        cmd = 'docker save -o ' + tarball + ' ' + ifull
        print(os.system(cmd))

        os.system('mv %s %s' % (tarball, save_file))
        retval = p.wait()


def load_images():
    tarball = str(input("请输入load镜像地址的绝对路径>>>>>>"))
    os.chdir(tarball)
    files = os.listdir(tarball)
    for filename in files:
        print(filename)
        os.system('docker load -i %s' % filename)


if __name__ == '__main__':
    i = 0
    while i < 3:
        print("保存当前harbor中的全部镜像请摇1")
        print("load 某一文件中的全部镜像请摇2")
        worker = int(input(">>>>>>>"))
        if worker == 1:
            save_docker()
        elif worker == 2:
            load_images()
        else:
            print("输入有误请重新输入，如果停止可使用control + c 停止程序")
            i += 1
