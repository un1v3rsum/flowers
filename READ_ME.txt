-- Tasks 1 & 2 --
-- Downloading iris.csv from url, removing outliers & creating new columns --
1. Open and run "get_data.py"

-- Task 3 --
-- Storing new data into database --
1. Open and run "make_db.py"

-- Task 4 --
-- Running the API --
1. Open the terminal -> working directory should be in the "flowers" project folder
2. Run the virtual environment by typing command: ". .venv/bin/activate"
3. Run the server by typing command: "python manage.py runserver"
4. Migrate django's models by typing command: "python manage.py migrate"
5. Open your browser and type: "http://127.0.0.1:8000/flowers" -> opens table-view with filtering options
6. URL: ".../flowers/<int:id>" <- (type in an integer number) -> opens flower-view

-- TASK 5 --
-- Docker container --
