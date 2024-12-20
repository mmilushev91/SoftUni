class Email:
  def __init__(self, sender, receiver, content):
    self.sender = sender
    self.receiver = receiver
    self.content = content
    self.is_sent = False
  
  def send(self):
    self.is_sent = True
  
  def get_info(self):
    return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

command = input()

emails = []

while command != "Stop":
  sender, receiver, content = command.split()
  
  email = Email(sender, receiver, content)
  emails.append(email)
  
  command = input()

indexes = [int(idx) for idx in input().split(", ")]

for i in range(len(emails)):
  if i in indexes:
    emails[i].send()
  
  print(emails[i].get_info())
