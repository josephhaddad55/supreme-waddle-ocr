lint:
	docker run -e RUN_LOCAL=true -v ${PWD}:/tmp/lint github/super-linter

build:
	docker build -t ocr-reader .

run: build
	docker run --rm ocr-reader
