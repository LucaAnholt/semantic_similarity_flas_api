# semantic_similarity_flas_api

## Mounting data into docker files:
first create docker volume:

```
docker volume create --name ImageIndexTrackerVolume
```

Next spin up a container and add the local host files (db + text file tracking row index) into the mounted drive:

```
docker run -v ImageIndexTrackerVolume:/app/data guessink/guessink-api-scheduler
docker cp '<local path to db and text file i.e. blah/blah/data>' <docker container ID>:/data
```

e.g. for my local repo:

```
docker cp 'C:/Users/LucaAnholt/OneDrive - Engitix Ltd/Documents/react-native/semantic_similarity_api/semantic_similarity_flas_api/data' 4e2287a598ed542cbd6fdf6722671c0bdf1fb8009b128cbbaa1f0693f513fa61:/data
```

Then spin up the other docker image running to the full API using the same mount
```
docker run -ti -p 8080:8080 -v ImageIndexTrackerVolume:/app/data guessink/guessink-api-full-api
```

