# ucu-data-ops2

# run docker engine with minikube
https://gist.github.com/juancsr/5927e6660d6ba5d2a34c61802d26e50a
> minikube start
> eval $(minikube docker-env)
> echo "`minikube ip` docker.local" | sudo tee -a /etc/hosts > /dev/null

> minikube start
# to stop but do not delete the minikube cluster
> minikube stop
> minikube ip
> minikube delete
# to pause k8s related containers
> minikube pause
> minikube tunnel


> kubectl get nodes -o wide
> kubectl describe node minikube
> kubectl {command} {object_type} {object_name} {params}
> kubectl api-resources
# runnable objects
> kubectl get all
> kubectl api-resources
> kubectl apply -f .
> kubectl run redis-db --image=redis:alpine
> kubectl get pods -o wide
> kubectl get pods redis-db -o yaml
> kubectl describe pods redis-db
> kubectl edit pods redis-db
> kubectl create deployment redis-deployment --image=redis
> watch -n 1 'kubectl get all'
> kubectl edit deployment redis-deployment
> kubectl apply -f k8s/redis-deployment.yaml
# namespaces
> kubectl get ns
> kubectl get all -n default
> kubens test
# clusters
> kubectx

# images
> docker images
> docker history <image-tag>
> docker inspect <image-id>
> docker build -f Dockerfile -t ansu0122/data-ops:flask-redis-1.0 .
> docker tag <image-id>|<image-name> [namespace/]<repo-name>:<image-tag>
> docker push [namespace/]<repo-name>:<image-tag>
> docker image rm 357127334564
> docker image -q
> docker rmi $(docker image -q)

# containers
> docker create --name nginx1 nginx:1.20
> docker start nginx1
> docker run -d --name nginx2 nginx:1.20
> docker run -it --name nginx2 nginx:1.20 bash
> docker run -d -p 8050:8050 --name flask-redis ansu0122/data-ops:flask-redis-1.0
> docker attach nginx3
> docker ps -a -q
> docker exec -it nginx2 bash
> docker exec -it nginx2 env
> docker logs <container-id|container-name>
> docker logs -f <container-id|container-name>
> docker inspect <container-id|container-name>
# remove all stopped containers
> docker container prune
> docker rm $(docker ps -a -q)
> docker kill $(docker ps -a -q)

# bind mount
> docker run -v <directory-on-host-machine>:<mount-point-in-container> <img>

# volume
> docker volume create my-volume
> docker volume inspect my-volume
> docker run -v <volume-name>:<mount-point-in-container> <img>

# network
> docker network ls
> docker network create my-net
> docker network inspect my-net
> docker run --net my-net <image>

# compose 
> docker compose up -d
> docker compose down
