SELECT DISTINCT subjects.subject_name
FROM subjects
JOIN grades ON subjects.subject_id = grades.subject_id
JOIN students ON grades.student_id = students.student_id
WHERE students.student_name = 'April Snyder';
