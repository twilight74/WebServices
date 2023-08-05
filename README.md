
<h3 align="center">WebServices</h3>




<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



This project is an attempt to build three websites with three different frameworks, this implementation is such that the user or tester cannot distinguish which framework is related to which website.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Django
* Flask
* FastAPI



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This project is based on Docker concept and you can run this project in two ways
### Prerequisites

you should install docker on your system, you can do that by this link:

*
[https://docs.docker.com/engine/install/](https://docs.docker.com/get-docker/)

### Installation

For both methods, you must first download the project on your system

.. Clone the repo
   ```
   git clone https://github.com/twilight74/WebServices.git
   ```
#### Method number one

 Build containers one by one from docker files and see the result

1. Enter the djangoSimpleWebService and create the Django image with the following command
  ```
     docker build --tag django .

   ```

2.  Then you go back to the main folder of the program and enter flaskSimpleWebService and create the Flask website with the following command
   ```
    docker build --tag flask .
   ```
3.Then you go back to the main folder and enter fastApiSimpleWebService and create the Fast API website with the following command.

   ```
    docker build --tag fastapi .
   ```
4.Now you have built all three websites and you can use testRe to test the project.

  Enter testRe and create the test file with the following command
 
  ```
    docker build --tag test .
  ```
#### you should create network, use this command to do that:
 
  ```
    docker network create mynetwork

  ```

Now you can see the result by running the images 

##### django
 ```
     docker run --name django --network=mynetwork  django
 ```

##### flask
 ```
    docker run --name flask --network=mynetwork  flask
  ```
##### fastapi
 ```
    docker run --name fastapi --network=mynetwork  fastapi
  ```

##### test
 ```
    docker run --name test --network=mynetwork  test
  ```



#### The second method

This method is very simple and includes all the previous instructions


  Just enter the main folder and run the whole project with the following command

    ```
    docker compose up
  
    ```
  In this method, Docker Compose is used, with the help of a yaml file, we run all the Docker commands together, so to speak, we Dockerize the entire project together.
  

<p align="right">(<a href="#readme-top">back to top</a>)</p>








<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* django
* flask
* fastapi

<p align="right">(<a href="#readme-top">back to top</a>)</p>


