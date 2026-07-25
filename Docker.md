## Build a new image
1. Do something in your running container
   1. e.g install curl
2. Exit the container
3. Commit current status of container
   1. `docker commit <container-id> <new-image-name>`
4. Build and push a new image
   - Option 1. If you want to upload your image to DockerHub
      1. Re-tag the image
         1. `docker tag <new-image-name> <your-user-name>/<new-image-name>`
      2. Then you will find a new image `<your-user-name>/<new-image-name>:latest`
      3. Push the image to DockerHub
         1. `docker push <your-user-name>/<new-image-name>:latest`
   - Option 2. Or you can simply commit a image as `<your-user-name>/<new-image-name>:<tag>`****