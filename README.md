# fetchAPI
This project demonstrates design and implementation of a simple fetch API using Python and Docker.
Follow the steps to deploy the fetch API on your machine.
the specifications of the API can be found at

    `https://github.com/fetch-rewards/receipt-processor-challenge`

## Prequisites
Docker should be installed on the machine

## Steps to run the code
* Open a terminal on your machine

* Clone the repository

    `git clone https://github.com/Pseth3/fetchAPI.git`

* Go inside the fetchAPI directory

    `cd fetchAPI`

Note: You should have Docker installed on your machine

* Build a docker image for the fetch app application

    `docker build -t fetchapp .`

* You can see the image by running the following command

    `docker images`

* Run a docker container of the image that you have created

    `docker run -p 5000:5000 fetchapp`

Note: The above command starts the fetchAPI service inside a docker container and exposes it on port 5000 of your machine
      The base url to access the application will be - 
      
      base url - `http://localhost:5000`

The application is now accessable on the base URL

## Steps to stop the application
* To stop the docker from running  send a system interrupt

    `ctrl+c`

* Delete the image and any running instances of the image

    `docker image rm fetchapp -f`
