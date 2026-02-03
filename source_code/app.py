from scam_detection import message_checker,honey_trap,json_file_creator

with open("test.txt","r") as f:
    initial_msg = f.read()

scam_detect = message_checker(initial_msg)

if scam_detect == "<scam>":
    history = honey_trap(initial_msg)

    out = json_file_creator(history)

    with open("details.json","w") as jf:
        jf.write(out)