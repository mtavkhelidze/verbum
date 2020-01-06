.PHONY: all clean

IMAGE_NAME = ${DOCKER_USER}/${CLIENT_IMAGE_NAME}

all: docker-image-build

clean: docker-image-clean

docker-image-build:
	@docker build -t $(IMAGE_NAME) .

docker-image-clean:
	@docker image rm --force $(IMAGE_NAME)
