import time
import random
class Frame:
 def __init__(self, frame_no, data):
  self.frame_no = frame_no
  self.data = data
  self.acknowledged = False
def send_frames(frames, window_size):
 print("\n--- Sending Frames ---")
 for i in range(window_size):
  if i < len(frames) and not frames[i].acknowledged:
   print(f"Sent Frame {frames[i].frame_no}: {frames[i].data}")
   print("Frames sent, waiting for acknowledgments...\n")
def receive_frames(frames, window_size):
 print("\n--- Receiving Frames ---")
 for i in range(window_size):
  if i < len(frames) and not frames[i].acknowledged:
   if random.random() < 0.2:
    print(f"Received Frame {frames[i].frame_no}: {frames[i].data} [ERROR]")
    frames[i].acknowledged = False
   else:
    print(f"Received Frame {frames[i].frame_no}: {frames[i].data} [OK]")
    frames[i].acknowledged = True
def sliding_window_protocol():
 window_size = int(input("Enter window size: "))
 message = input("Enter a message to send: ")
 frames = [Frame(i, message[i]) for i in range(len(message))]
 base = 0
 while base < len(frames):
  send_frames(frames[base:], window_size)
  time.sleep(2)
  receive_frames(frames[base:], window_size)
  while base < len(frames) and frames[base].acknowledged:
   base += 1
 if base < len(frames):
  print("\nResending unacknowledged frames...\n")
  time.sleep(2)
  print("\nAll frames sent and acknowledged!")
if __name__ == "__main__":
 sliding_window_protocol()