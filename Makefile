.PHONY: run clean

setup: requirements.txt
	pip install -r requirements.txt

run_print:
	python app.py print-info --number 0
	python app.py print-info --number 4
	python app.py print-info --number -5
	python app.py print-info --number 10

run_to_msgpack:
	python app.py info-to-binary numbers.msgpack 4 6 10 11 45 10000

test:
	pytest --verbose .

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
