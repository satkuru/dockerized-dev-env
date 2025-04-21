**To build docker image:**  
docker build -t fastapi-image .  
**To run the continer in detached mode with volumn mapping:**  
docker run --name fastapi-continer -p 80:80 -d -v $(pwd):/code fastapi-image
**To stop the continer:**  
docker stop fastapi-container
**To remove the container:**  
docker rm fastapi-continer
**To remove the built docker image:**  
docker rmi fastapi-image
**To use docker-compose:**  
docker compose up --build -d
**To stop docker compose services:**  
docker compose stop
**To remove docker compose service continers:**  
docker compose down
