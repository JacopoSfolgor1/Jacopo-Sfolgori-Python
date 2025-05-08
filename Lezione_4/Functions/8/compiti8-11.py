'''8-11. Archived Messages: Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.'''

def show_messages(messages: list):
    for message in messages: 
        print(message)



def send_messages(text_messages):
    sent_messages = []
    while text_messages:
        current_message = text_messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)
    return sent_messages

text_messages = ["Ciao", "come va", "che fai"]

print("Original Messages:")
show_messages(text_messages)

sent_messages = send_messages(text_messages[:])

print("Original text messages list:")
show_messages(text_messages)

print("Sent messages list:")
show_messages(sent_messages)