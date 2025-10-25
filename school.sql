

--this is my schema

DROP TABLE IF EXISTS student;

CREATE TABLE students (
    id serial PRIMARY KEY,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    age INTEGER,
    subject INTEGER
);


DROP TABLE IF EXISTS subjects;

CREATE TABLE subjects (
    id serial PRIMARY   KEY,
    subject varchar(255) NOT NULL
);

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id serial PRIMARY KEY,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    age INTEGER,
    subject varchar(255)
);
--csv files and sql connection --
\COPY students FROM 'data/student.csv' DELIMITER ',' CSV HEADER;
\COPY subjects FROM 'data/subjects.csv' DELIMITER ',' CSV HEADER;
\COPY teachers FROM 'data/teachers.csv' DELIMITER ',' CSV HEADER;

SELECT * FROM students, subjects, teachers;
