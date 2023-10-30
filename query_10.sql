SELECT DISTINCT subjects.subject_name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.teacher_id
JOIN grades ON subjects.subject_id = grades.subject_id
JOIN students ON grades.student_id = students.student_id
WHERE students.student_name = 'April Snyder' AND teachers.teacher_name = 'Caleb Clark';
