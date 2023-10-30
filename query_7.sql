SELECT students.student_id, student_name, grade
FROM students
JOIN grades ON students.student_id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.subject_id
JOIN groups ON students.group_id = groups.group_id
WHERE groups.group_name = 'C' AND subjects.subject_name = 'Gaffer';
