import paramiko
# animal_number = 'R20-091'
# block_number = '00'


def runQA(animal_number, block_number):
    p = paramiko.SSHClient()
    p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    p.connect("155.***.**.***", port=22, username="qa", password="123")

    transport = p.get_transport()
    channel = transport.open_session()
    channel.exec_command(f"cd /v/raid10/users/asingh/QA/Scripts \n source ./QA_venv/bin/activate \n bash QA.sh {animal_number} {block_number} \&>/v/raid10/users/histoqa/QA/logs/{animal_number}_{block_number}_output.txt \&")
#     \&>/v/raid10/users/histoqa/QA/logs/{animal_number}_{block_number}_output.txt \&
    # for line in stdout:
    #     print(line)
    # for line in stderr:
    #     print(line)

    # print("Completed")


# runScripts()
