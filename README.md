Project Description
Flask web application to display a university timetable based on student levels, connected to a PostgreSQL database and containerized using Docker.

Steps to Setup and Run
Clone Repository:

bash
Copy code
git clone <repository_url>
cd <repository_folder>
Build Docker Image:

bash
Copy code
docker build -t university-timetable-app .
What it does: Creates a Docker image for the Flask app.
Run Application with Docker:

bash
Copy code
docker run -p 5000:5000 university-timetable-app
What it does: Runs the Docker container and maps port 5000 for the application.
Access Application:

Open your browser and go to:
http://localhost:5000
Docker Compose (Alternative):

bash
Copy code
docker-compose up --build
What it does: Builds and starts both Flask and PostgreSQL containers simultaneously.
Database Setup
Access PostgreSQL Container (if using Docker Compose):

bash
Copy code
docker exec -it <db_container_name> psql -U <db_user> -d <db_name>
What it does: Opens a terminal for database operations.
Create and Populate Table:

sql
Copy code
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    course_name VARCHAR(100),
    course_code VARCHAR(20),
    level VARCHAR(20),
    start_time TIME,
    end_time TIME,
    day_of_week VARCHAR(20)
);

INSERT INTO courses (course_name, course_code, level, start_time, end_time, day_of_week)
VALUES
('Course 1', 'C101', 'Undergraduate', '09:00', '10:30', 'Monday'),
('Course 2', 'C102', 'Graduate', '11:00', '12:30', 'Tuesday'),
('Course 3', 'C103', 'Undergraduate', '13:00', '14:30', 'Wednesday');
What it does: Creates the courses table and populates it with data.
Key Commands
Stop Docker Containers:

bash
Copy code
docker stop <container_id>
What it does: Stops a running container.
Remove Docker Containers:

bash
Copy code
docker rm <container_id>
What it does: Deletes a container.
Check Running Containers:

bash
Copy code
docker ps
What it does: Lists active containers.
Check All Containers:

bash
Copy code
docker ps -a
What it does: Lists all containers (active and stopped).
