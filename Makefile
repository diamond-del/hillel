.PHONY: run
run:
	echo 'adsad2ad'
	echo '11111'
	@echo '2222'
	python main.py


.PHONY: check
check:
	@echo 'Starting code correction...'
	black .
	isort .
	pytest .
	flake8 .
	@echo 'Finish'
