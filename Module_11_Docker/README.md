# Module 11: Docker
## Task 1
Repository: https://github.com/anna-ishkhanyan/spring-petclinic.git

This task demonstrates containerization of the Spring petClinic application.

### Step 1 
Cloned the repository of the app:
```
git clone https://github.com/spring-projects/spring-petclinic.git
cd spring-petclinic
```

### Step 2

The application is first built locally, producing a JAR file.
![1](screenshots/1.png)
![2](screenshots/2.png)


After the build the artifact is saved at target directory.

### Step 3 

This Dockerfile uses the already built JAR file and runs it inside a minimal JRE image.

![2.1](screenshots/2.1.png)


Building:
![3](screenshots/3.png)

Running:
![4](screenshots/4.png)
![5](screenshots/5.png)


### Step 4
At this step Multi-Stage Dockerfile is created.

This approach builds the application inside the Docker image, then copies only the final JAR into a minimal runtime image.
![6](screenshots/6.png)

Building: 
![7](screenshots/7.png)

Running:
![8](screenshots/8.png)


Application becomes available at:

http://localhost:9090

### Step 5

Docker Compose is used to start two containers automatically: Spring PetClinic application and MySQL database

docker-compose.yml
![9](screenshots/9.png)

### Step 6 
Running with docker compose:
![10](screenshots/10.png)
Result:
![11](screenshots/11.png)