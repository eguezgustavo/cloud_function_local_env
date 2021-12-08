build:
	-docker rmi test_cloud_function
	docker build -t test_cloud_function -f some_cloud_function/Dockerfile .

run:
	docker compose up -d

test:
	docker compose up -d --no-recreate
	docker compose exec some_cloud_function pip install -r /test_requirements.txt
	docker compose exec some_cloud_function pytest people_app_tests

remove:
	docker compose down
