import time
import cv2
import os
import cv2 as cv


output_loc="C:\Users\suhas\OneDrive\Documents\BE PROJECT PRANALI\Sample codes\Pothole Detection using openCV\frames"

try:
    os.mkdir(output_loc)
except OSError:
    pass
# Log the time
time_start = time.time()
# Start capturing the feed
cap = cv2.VideoCapture('sample_video.avi')
try:
    video = cv2.VideoCapture('sample_video.avi')
except:
    print "Could not open video file"
    raise
print video.grab()
# Find the number of frames
video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
print ("Number of frames: ", video_length)
count = 0
print ("Converting video..\n")
# Start converting the video
while cap.isOpened():
    # Extract the frame
    ret, frame = cap.read()
    # Write the results back to output location.
    cv2.imwrite("frame%d.jpg" % count, frame)
    count = count + 1
    # If there are no more frames left
    if (count > (video_length-1)):
        # Log the time again
        time_end = time.time()
        # Release the feed
        cap.release()
        # Print stats
        print ("Done extracting frames.\n%d frames extracted" % count)
        print ("It took %d seconds forconversion." % (time_end-time_start))
        break


    
