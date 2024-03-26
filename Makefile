image:
	docker build -f ./build/Dockerfile -t caesar .

run: image
	docker-compose -f ./build/docker-compose.yml up web

clean:
	docker-compose -f ./build/docker-compose.yml -f ./build/docker-compose.test.yml rm -s -v -f

linter:
	ruff check ./src

fix_lint:
	ruff check ./src --fix

test: test_image
	docker-compose -f ./build/docker-compose.test.yml up test
