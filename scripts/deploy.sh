#!/bin/bash
IMAGE_NAME="tiro"
CONTAINER_NAME="tiro"

container_id=$(docker ps -aqf "name=${CONTAINER_NAME}")
if [ ! -z "${container_id}" ]; then
    docker stop ${CONTAINER_NAME}
    docker rm "${container_id}"
fi

# 이미지 빌드
docker build -t "${IMAGE_NAME}" .

# 새 컨테이너 실행
docker-compose up -d