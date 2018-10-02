docker build -t snowboy:latest  -f docker/Dockerfile .
docker tag snowboy:latest registry.cmic.site:5000/sg/snowboy:latest
docker push registry.cmic.site:5000/sg/snowboy:latest
docker rmi $(docker images -f "dangling=true" -q)