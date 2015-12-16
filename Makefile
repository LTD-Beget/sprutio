.PHONY: python cron bower rpc app nginx

all: python cron bower rpc app nginx

python:
	docker build -t beget/fmcore-python -f Dockerfile ./
	docker push beget/fmcore-python

cron:
	docker build -t beget/fmcore-cron -f Dockerfile.cron ./
	docker push beget/fmcore-cron

bower:
	docker build -t beget/fmcore-bower -f Dockerfile.bower ./
	docker push beget/fmcore-bower

rpc:
	docker build -t beget/fmcore-rpc -f rpc/Dockerfile rpc/
	docker push beget/fmcore-rpc

app:
	docker run -v $(PWD)/app/public:/app -w /app beget/fmcore-bower bower install --allow-root
	docker build -t beget/fmcore-app -f app/Dockerfile app/
	docker push beget/fmcore-app

nginx:
	docker build -t beget/fmcore-nginx -f Dockerfile.nginx ./
	docker push beget/fmcore-nginx

