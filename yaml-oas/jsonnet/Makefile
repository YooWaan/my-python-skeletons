
DEF_FILE=oas.jsonnet
OAS_JSON=swagger.json
OAS_YAML=swagger.yaml

gen:
	jsonnet $(DEF_FILE) > $(OAS_JSON)
	cat $(OAS_JSON) | yq -p json '.' > $(OAS_YAML)

lint:
	docker run --rm --tty -v "$(PWD):/data:ro"  ibmdevxsdk/openapi-validator:latest $(OAS_YAML)

html: html-redoc html-elements
	@echo "done"

html-redoc:
	docker run --rm -v $(PWD):/spec redocly/cli build-docs $(OAS_YAML) --output=redoc-api.html

html-elements:
	go run oas-doc.go $(OAS_JSON) > elements-api.html
