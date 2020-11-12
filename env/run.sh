BASEDIR=$(cd $(dirname $0)/.. && pwd)

CONTAINER="mecabCostCalc"

if [ $(docker ps -a | grep $CONTAINER | wc -l) == "1" ]; then
    docker rm -f $CONTAINER
fi
docker run --name $CONTAINER \
           -v $BASEDIR:/var/mecab:rw \
           -dt yukia3/mecab-initial-cost-calculation

