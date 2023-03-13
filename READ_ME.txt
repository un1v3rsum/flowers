-- Tasks 1 & 2 --
-- Downloading iris.csv from url, removing outliers & creating new columns --
1. From flowers project open /flowers directory and run "get_data.py"

-- Task 3 --
-- Storing new data into database --
1. From the same directory open and run "make_db.py"
2. Database "db.sqlite3" is created or overwritten -> same database also used in the API

-- Task 4 & 5--
-- Running the API from a docker container --

1. Open the terminal and type the command: "docker compose up --build" or start the container from docker desktop
2. Open your browser and type: "http://127.0.0.1:8000/flowers" -> opens table-view with filtering options
3. URL: ".../flowers/<int:id>" <- (type in an integer number) -> opens flower-view




