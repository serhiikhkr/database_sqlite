SELECT AVG(grade) AS avg_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.subject_id
JOIN teachers ON subjects.teacher_id = teachers.teacher_id
JOIN students ON grades.student_id = students.student_id
WHERE teachers.teacher_name = 'Taylor Johnson' AND students.student_name = 'Stephanie Lawrence';
