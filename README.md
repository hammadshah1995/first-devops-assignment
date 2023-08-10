Step 1 Application Identification
    I created a simple chat app using OpenAi Api and used Python and OpenAi Library for it.

Step 2 Dependencies
    I made a DockerFile inside the folder where my python app was located
    My base image was python so I used "FROM python:3.11.4" and 3.11.4 was the version of python in my computer so I used it.
    The other dependency was openai==0.27.8 so I used The RUN command fo it
    RUN pip install openai==0.27.8
    My code was located in the working directory so I copied it using .
    I made a folder name /home/app and used mkdir command for it
    I made this folder my working directory and copied my code inside it
    For running 


Step 3    
