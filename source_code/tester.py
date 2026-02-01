from scam_detection import json_file_creator

with open("test.txt","r") as f:
    inp = f.read()

out = json_file_creator(inp)

print(out)