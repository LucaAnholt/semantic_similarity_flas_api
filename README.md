# semantic_similarity_flas_api

## Mounting data into docker files:
first create docker volume:

```
docker volume create --name ImageIndexTrackerVolume
```

Next spin up a container and add the local host files (db + text file tracking row index) into the mounted drive:

```
docker run --rm -v ImageIndexTrackerVolume:/data -v /mnt/c/Users/LucaAnholt/semantic_similarity_flas_api/data:/src alpine sh -c "cp -r /src/* /data/"
```
or non-wsl local:

```
docker run --rm -v ImageIndexTrackerVolume:/data -v C:/Users/LucaAnholt/semantic_similarity_flas_api/data:/src alpine sh -c "cp -r /src/* /data/"
```

or for server:

```
 sudo docker run --rm -v ImageIndexTrackerVolume:/data -v /semantic_similarity_flas_api/data:/src alpine sh -c "cp -r /src/* /data/"
```

Then run docker compose: 
```
docker-compose up
```

### If you need to update the server code...
ssh into the server and stop all running containers and delete them:

```
docker stop $(docker ps -a -q)
```
and then 
```
docker rm $(docker ps -a -q)
```
Then, cd into the semantic_similarity_api folder in the root as sudo user and run:
```
sudo git pull
sudo docker-compose build --no-cache
```
