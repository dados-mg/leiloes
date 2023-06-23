include config.mk

.PHONY: help start list validate create update resource-create build compare clean data

help: ## Informa breve descrição dos comando
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'

start: ## Inicia ambiente para trabalho com conjunto
	@echo 'Iniciando ambiente...'
	@docker run -it -v /$(PWD):/dataset -e CKAN_HOST=$(CKAN_HOST) -e CKAN_KEY=$(CKAN_KEY) gabrielbdornas/dtamg:latest bash

list: ## Lista pacotes instalados em ambiente virtual python
	@echo 'Lista pacotes python instalados...'
	@pip list

validate: ## Valida dataset e todos os seus recursos
	@echo 'Validando conjunto...'
	@python scripts/validate.py

report: ## Gerando Relatório de Validação
	@echo 'Gerando relatório validação html...'
	@livemark build index.md --target index.html

create: ## Cria dataset e todos os seus recursos em instância do CKAN
	@echo 'Criando conjunto...'
	@dpckan --datastore dataset create

update: ## Atualiza dataset e todos os seus recursos em instância do CKAN
	@echo "Atualiza conjunto..."
	@dpckan --datastore dataset update

data:
	@echo "Convertendo arquivos excel para csv"
	@python ./scripts/convert_csv.py

resource-create: ## Cria recursos em instância do CKAN
	@echo "Criando no CKAN recursos inexistentes..."
	@python ./scripts/create_resource.py $(CKAN_HOST)

build: datapackage.json ## Constroi arquivo datapackage.json a partir do arquivo datapackage.yaml

datapackage.json: datapackage.yaml $(SCHEMAS_FILES)
	@echo "Construindo datapackage.json..."
	@frictionless describe --type package --json $< > $@

compare: ## Compara recursos existentes na pasta data com os incluído no datapackage.json
	@echo 'Comparando recursos pasta data e datapackage.json...'
	@python ./scripts/compare.py

clean: ## Limpa arquivos CSV e datapackage.json
	@echo 'Limpando arquivos CSV e datapackage.json...'
	@rm -rf data/*.csv
	@rm -rf datapackage.json
