# Krishna-Ramesh-Wisconsin-Autonomous-Perception-Coding-Challenge

## Methodology: I initially had the idea that I would have to do some type of object detection to detect all the cones in the image. However, I soon realized that I would only really need to find the first 4 cones since they will each give me 2 points that could then be used to create 2 lines. After some research online to see what techniques could be done for this object detection I came across template matching, which would be tricky since the cones are not all the same size because of the viewpoint of the image. Multi scale template matching would be possible, but I also found a color filter technique. I thought this would be a much more efficient approach since there would be no matching to between images - just image manipulation to let the red/orange color of the cones stay while everything else in the image gets taken out. Using the online resources, I wrote the code, and using the 4 points, made 2 lines and drew them on the image. 

## I entertained the idea of multi scale template matching but decided that it would be less efficient than masking the image by color. If time is not an issue, then template matching would have been fine, but if this was to be run on a moving robot that has to find the cones in real time, then image masking would be the more efficient approach while not sacrificing too much accuracy. 

## Libraries Used: 
  - cv2 for reading/writing image and image manipulation
  - numpy for arrays
  - matplotlib to view the images and their modifications
