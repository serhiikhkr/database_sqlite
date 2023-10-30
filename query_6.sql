SELECT student_name
FROM students
JOIN groups ON students.group_id = groups.group_id
WHERE groups.group_name = 'B';
