# 532-PyTorch-Docker-Project

This is the final submission for Arvind Govindarajan.

The Dockerfile can be used to build a Docker image with a Python entrypoint.
To build the docker file run the following command when in the root directory:
  > docker build --tag name-for-image .
 
After the image is built, which takes about 10 minutes with a stable internet connection, you can run the docker by:
  > docker run --name name-for-image -p 5000:5000 name-for-image
  
This will expose the port 5000 and will allow grader to pass images to test.  
The images are available in the imgs folder. To pass the images to the server, move into the imgs directory and run:
  > curl -F "file=@butterfly.jpeg" http://0.0.0.0:5000/upload


*NOTE TO GRADER*:
*The docker image is too large to be uploaded on Github and I am currently waiting on the upload to Drive. I may update the README file past 11:59 but only to update the link for the docker image. Thank you.*
