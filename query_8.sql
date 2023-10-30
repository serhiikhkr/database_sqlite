SELECT teachers.teacher_name, AVG(grade) AS avg_grade
FROM teachers
JOIN subjects ON teachers.teacher_id = subjects.teacher_id
JOIN grades ON subjects.subject_id = grades.subject_id
GROUP BY teachers.teacher_name;
