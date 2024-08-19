print("Animator.py loaded...")
import cv2
import os
print("> Imports complete")
frames_folder = "./plots"

video_name = "video.mp4"

def count_files(directory):
  file_count = 0
  for entry in os.listdir(directory):
    path = os.path.join(directory, entry)
    if os.path.isfile(path):
      file_count += 1
  return file_count

fps = 10 # Adjust fps as needed (e.g., 24, 30)
N = count_files(frames_folder)
# Get all frame filenames
frame_filenames = [os.path.join(frames_folder, f"plot__{i}.png") for i in range(N - 1)]  # 2001 for 0-2000 frames

# Check if any frames exist
if not frame_filenames:
    print("> Error: No frames found in the folder!")
    exit()

# Read the first frame to determine video properties:
first_frame = cv2.imread(frame_filenames[0])
height, width, channels = first_frame.shape

# Define the video writer:
fourcc = cv2.VideoWriter_fourcc(*'XVID') # Used for .mp4
video_writer = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

# Process and write frames:
for frame_filename in frame_filenames:
    frame = cv2.imread(frame_filename)
    # You can add pre-processing here (e.g., resizing, color correction)
    video_writer.write(frame)
