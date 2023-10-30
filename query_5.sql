SELECT DISTINCT subjects.subject_name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.teacher_id
WHERE teachers.teacher_name = 'Jacob Hooper';
