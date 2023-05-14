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