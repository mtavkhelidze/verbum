DOCKER_USER ?= mtavkhelidze
NGINX_IMAGE_NAME ?= verbum-nginx
CLIENT_IMAGE_NAME ?= verbum-client
export

TOPTARGETS := all clean
SUBDIRS := nginx client

$(TOPTARGETS): $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)


.PHONY: $(TOPTARGETS) $(SUBDIRS)
