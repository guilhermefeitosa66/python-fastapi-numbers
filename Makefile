local-setup:
	if [ ! -d "venv" ]; then python -m venv venv; fi
	bash -c "source venv/bin/activate"
	pip install --upgrade pip
	pip install -r requirements.txt

local-run:
	uvicorn main:app --host 0.0.0.0 --port 8000 --reload

docker-build:
	docker-compose build --no-cache

docker-run:
	docker-compose up
