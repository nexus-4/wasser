import cv2
import os

path_video          = '/Users/usul/Documents/Projetos-Pessoais/wasser/raw_videos/DJI_20250919101734_0019_D.mp4' # Replace with the video file path
folder_destination  = 'cattle_dataset_frames' # Replace with the destination folder path

# Create the destination folder if it doesn't exist
if not os.path.exists(folder_destination):
    os.makedirs(folder_destination)

# Read a video from a file
video = cv2.VideoCapture(path_video)

if not video.isOpened():
    print("Error opening video file")
    exit()
else:
    print("Video file opened successfully")

# Get video properties
frame_count  = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps          = video.get(cv2.CAP_PROP_FPS)
print(f"Total frames: {frame_count}, FPS: {fps}")

frame_counter     = 0
interval_seconds  = 2
jump_frames       = int(fps * interval_seconds)

# Loop to read each frame of the video
while video.isOpened():
    ret, frame = video.read()

    if not ret:
        print("End of video reached or error reading the frame")
        break
    
    if frame_counter % jump_frames == 0:
        # Format the frame number with leading zeros
        filename = f"frame_{frame_counter:04d}.jpg" # frame_0001.jpg, frame_0002.jpg, etc.

        filepath = os.path.join(folder_destination, filename)

        # Save the frame to the disk
        cv2.imwrite(filepath, frame)
        print(f"Saved {filename}")
    
    frame_counter += 1

video.release()
print("Video processing completed")

