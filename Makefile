.PHONY: all build push \
				build-python build-cron build-bower build-rpc build-app build-nginx build-frontend \
				push-python push-cron push-bower push-rpc push-app push-nginx push-frontend

all: build
	
build: build-python build-cron build-bower build-rpc build-app build-nginx build-frontend

build-python:
	docker build -t beget/sprutio-python -f Dockerfile ./

build-cron:
	docker build -t beget/sprutio-cron -f Dockerfile.cron ./

build-bower:
	docker build -t beget/sprutio-bower -f Dockerfile.bower ./

build-rpc:
	docker build -t beget/sprutio-rpc -f rpc/Dockerfile rpc/

build-app:
	docker build -t beget/sprutio-app -f app/Dockerfile app/

build-nginx:
	docker build -t beget/sprutio-nginx -f Dockerfile.nginx ./

build-frontend:
	docker run -v $(PWD)/app/public:/app -w /app beget/sprutio-bower bower install --allow-root
	docker build -t beget/sprutio-frontend -f app/public/Dockerfile app/public/

push: push-cron push-rpc push-app push-nginx push-frontend

push-cron:
	docker push beget/sprutio-cron

push-rpc:
	docker push beget/sprutio-rpc

push-app:
	docker push beget/sprutio-app

push-nginx:
	docker push beget/sprutio-nginx

push-frontend:
	docker push beget/sprutio-frontend

# EOF
