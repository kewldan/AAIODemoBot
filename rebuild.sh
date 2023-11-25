docker container stop aaio-demo
docker container rm aaio-demo
docker image rm aaio-demoi
docker build -t aaio-demoi .
docker run -d --name aaio-demo aaio-demoi
docker container ls