-- ______________________ STUDENTS TABLE __________________________
CREATE TABLE students (
    admid SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    cls INTEGER NOT NULL,
    sec CHAR(1) NOT NULL,
    roll INTEGER NOT NULL,
    mob VARCHAR(10),
    father VARCHAR(100),
    mother VARCHAR(100),
    address VARCHAR(500),
    bgroup CHAR(2),
    aaparId CHAR(15)
);

-- _______________________ FEE TABLE _______________________________
CREATE TABLE fee (
    admid INTEGER PRIMARY KEY,
    name VARCHAR(100),
    FOREIGN KEY (admid) REFERENCES students(admid)
);

CREATE OR REPLACE FUNCTION insert_fee_trigger()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO fee (admid, name)
    VALUES (NEW.admid, NEW.name);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER after_student_insert_fee
AFTER INSERT ON students
FOR EACH ROW
EXECUTE FUNCTION insert_fee_trigger();

-- _______________________ STUDENT-ATTENDANCE _______________________________
CREATE TABLE attendance (
    admin INTEGER,
    name VARCHAR(100),
    FOREIGN KEY (admin) REFERENCES students(admid) ON DELETE CASCADE
);

CREATE OR REPLACE FUNCTION insert_attendance_row()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO attendance (admin, name)
    VALUES (NEW.admid, NEW.name);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER after_student_insert_attendance
AFTER INSERT ON students
FOR EACH ROW
EXECUTE FUNCTION insert_attendance_row();

-- __________________ TEACHER ___________________
CREATE TABLE teachers (
    tid SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    subject VARCHAR(50) NOT NULL,
    cls INT NOT NULL,
    sec CHAR(1) NOT NULL,
    mob VARCHAR(10),
    address VARCHAR(500)
);

-- __________________ TEACHER-ATTENDANCE ___________________
CREATE TABLE teacher_attendance (
    tid INT,
    name VARCHAR(100),
    FOREIGN KEY (tid) REFERENCES teachers(tid)
);

CREATE OR REPLACE FUNCTION insert_teacher_attendance()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO teacher_attendance (tid, name)
    VALUES (NEW.tid, NEW.name);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER after_teacher_insert
AFTER INSERT ON teachers
FOR EACH ROW
EXECUTE FUNCTION insert_teacher_attendance();
