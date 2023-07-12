"# fastapi" 

## Create virtual environment
python3 -m venv dev-env

## Activate virtual environment
.\venv\Scripts\activate

## Deactive virtual environment
deactivate

## install requirement
pip install -r requirements.txt

## Add package list into requirements
pip freeze > requirements.txt

## Run app
uvicorn main:app --reload