# Dockerized Chat App with OpenAI

## Step 1: Application Identification

I developed a basic chat application using the OpenAI API, utilizing Python and the OpenAI library.

## Step 2 and 3: Dependencies and DockerFile

1. I created a Dockerfile within the directory containing my Python application.
2. The base image was Python, version `3.11.4`, which matched the Python version on my computer.
3. I added the dependency `openai==0.27.8` using the `RUN` command.
4. My application code was in the working directory, so I copied it using `COPY .`.
5. I established a directory named `/home/app` using the `mkdir` command, making it my working directory.
6. I copied my code into the new directory.
7. Finally, I used `CMD ["python", "project1.py"]` to run the application.

## Step 4: Build Docker Image

1. I employed the `docker build` command to create an image from the Dockerfile:
   ```bash
2.  Docker build -t firstdevopsassignment:latest .
3.  I then used `docker images` command to check the image being present in the list of images
4.  Then I created the container using docker run command
        "docker run -it firstdevopsassignment" the flag -it meant that container was being run in interactive mode

## Step 5: Push to Docker Hub

1. Docker Desktop was installed on my system and was Logged in with my account
2. Inorder to push the docker image to the DockerHub/Repository I first had to put the tag and my    docker username on the image
        
3. docker tag firstdevopsassignment hammadshah5/openaiapp:v1.0
        here hammadshah5 is my docker username
        openaiapp is the name of the repository within the Docker Hub account.
        v1.0 is the specific tag I assigned to the image

4. docker push hammadshah5/openaiapp:v1.0
        I useed the docker push command to push this image to DockerHub online


## Step 6: Push to Docker Hub