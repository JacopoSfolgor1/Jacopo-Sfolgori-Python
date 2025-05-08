'''8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() 
that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.'''

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

sent_messages = send_messages(text_messages)

print("Original text messages list:")
show_messages(text_messages)

print("Sent messages list:")
show_messages(sent_messages)