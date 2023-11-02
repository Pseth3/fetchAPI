# fetchAPI
This project demonstrates design and implementation of a simple fetch API using Python and Docker

## Steps to run the code

* Clone the repository
    `git clone https://github.com/Pseth3/fetchAPI.git`

* Go inside the fetchAPI directory
    `cd fetchAPI`

Note: You should have Docker installed on your machine

* Build a docker image for the fetch app application
    `sudo docker build -t fetchapp .`

* You can see the image by running the following command
    `sudo docker ps`

* Run a docker container of the image that you have created
    `sudo docker run -p 5000:5000 fetchapp`

Note: The above command starts the fetchAPI service inside a docker container and exposes it on port 5000 of your machine
      The base url to access the application will be - `http://localhost:5000`

The application is now accessable on the base URL
