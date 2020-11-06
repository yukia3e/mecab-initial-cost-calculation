BASE_DIR=$(cd $(dirname $0) && pwd)
IMAGE=$(grep "IMAGE:" $BASE_DIR/Dockerfile | sed -e "s/# IMAGE: \(.*\)/\1/g")
docker build -t $IMAGE $BASE_DIR
