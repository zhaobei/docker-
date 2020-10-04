import os
import sys

if __name__ == "__main__":
    tarball = sys.argv[1]
    print(tarball)

    workdir = '/data/images'
    os.system('rm -rf %s'%workdir)
    os.system('mkdir -p %s'%workdir)
    os.system('tar -zxvf %s -C %s'%(tarball, workdir))

    os.chdir(workdir)
    files = os.listdir(workdir)
    for filename in files:
        print(filename)
        os.system('docker load -i %s'%filename)
