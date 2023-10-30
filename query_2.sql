SELECT students.student_id, student_name, AVG(grade) AS avg_grade
FROM students
JOIN grades ON students.student_id = grades.student_id
WHERE grades.subject_id = 3
GROUP BY students.student_id, student_name
ORDER BY avg_grade DESC
LIMIT 1;
