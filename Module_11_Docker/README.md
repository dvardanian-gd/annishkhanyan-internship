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

## Task 2: Part 1
### Step 1

A Docker (hosted) repository was created in Nexus Repository Manager:
![1](screenshots_2/1.png)

### Step 2
Docker was authenticated against the Nexus Docker registry:
![2](screenshots_2/2.png)

### Step 3

The locally built image(spring-petclinic-app:latest) was tagged and pushed to Nexus:
![3](screenshots_2/3.png)


The image was uploaded in the Nexus UI.
![4](screenshots_2/4.png)

## Part 2
### Step 1
A private repository was created in Amazon ECR.
![5](screenshots_2/5.png)

### Step 2

Docker was authenticated to ECR:
![6](screenshots_2/6.png)

### Step 3
The same Docker image was tagged and pushed to ECR:
![7](screenshots_2/7.png)


The image appeared successfully in the ECR repository.
![image](screenshots_2/image.png)

### Step 4

Initially, the security scan failed with the error 
```UnsupportedImageTypeException```.
![10](screenshots_2/10.png)

This happened because the Docker image was built as a multi-architecture image. Amazon ECR basic scanning does not support Image Index artifacts, which caused the scan to fail.

To resolve this issue I used this command:
```
docker build --platform linux/amd64 -t spring-petclinic:1.0.0 .
```
After rebuilding and pushing the image again, the security scan completed successfully.
![8](screenshots_2/8.png)
![9](screenshots_2/9.png)
The scan results showed no Critical or High severity vulnerabilities. Most of the detected vulnerabilities were Medium or Low severity and originated from the base Ubuntu image, not from the application itself. This is common when using general-purpose operating system base images.

To reduce such findings in the future, possible approaches include using smaller base images, rebuilding images regularly to apply security updates.