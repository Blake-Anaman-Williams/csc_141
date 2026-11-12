messages = ["Hello", "How are you?", "Good morning"]
sent_messages = []

def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)