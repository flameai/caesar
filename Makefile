image:
	docker build -f ./build/Dockerfile -t caesar .

run: image
	docker-compose -f ./build/docker-compose.yml up web

linter:
	flake8 ./source

fix_lint:
	black ./source