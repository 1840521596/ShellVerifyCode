import paramiko
import os
import sys
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR)

host = "192.168.123.124"
port = 22
timeout = 30
user = "test"
password = "123123"
server_path = '/var/dayima/messager/logs/stdout.log'
local_path = BASE_DIR + '/verify_code.log'


def save_verify_code():
    code_array = []
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, user, password)  # 连接远程主机，SSH端口号为22
        stdin, stdout, stderr = ssh.exec_command('cat /var/dayima/messager/logs/stdout.log | grep 15537757776')  # 执行命令
        for line in stdout:
            verify_info = line.strip("\n")
            # print(verify_info)
            verify_code = re.findall(r"\d\d\d\d", verify_info)
            # print(verify_code[-1])
            code_array.append(verify_code[-1])
        # print(stdout.readlines())
        ssh.close()
        return code_array[-1]
    except Exception as e:
        print(e)


# def sftp_down_file():
#     try:
#         t = paramiko.Transport((host, port))
#         t.connect(username=user, password=password)
#         sftp = paramiko.SFTPClient.from_transport(t)
#         sftp.get(server_path, local_path)
#         t.close()
#     except Exception as e:
#         print(e)


if __name__ == '__main__':
    print(save_verify_code())
