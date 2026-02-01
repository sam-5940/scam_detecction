from ollama import chat

def message_checker(message):

    messages = [{"role": "user", "content": message}]

    reply = chat(model="scam-detector",messages=messages)

    reply = reply["message"]["content"].strip()

    return reply

def honey_trap(initial_msg):
    messages = [{"role": "user", "content": initial_msg}]
    history = f"target: {initial_msg}\n"

    while True:
        reply = chat(model="honeypot-agent", messages=messages)
        reply = reply["message"]["content"].strip()

        if reply == "<info_extracted>":
            history += "<info_extracted>\n"
            break

        print(reply)

        # agent reply
        history += f"agent: {reply}\n"
        messages.append({"role": "assistant", "content": reply})

        # target response
        response = input("target: ")
        history += f"target: {response}\n"
        messages.append({"role": "user", "content": response})

    return history

def json_file_creator(msg):
    messages = [{"role": "user", "content": msg}]
    reply = chat(model="json-extractor", messages=messages)
    reply = reply["message"]["content"].strip()
    return reply




