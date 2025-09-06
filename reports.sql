-- Event Popularity Report
SELECT e.title, COUNT(r.student_id) AS registrations
FROM events e
LEFT JOIN registrations r ON e.event_id = r.event_id
GROUP BY e.event_id
ORDER BY registrations DESC;

-- Student Participation Report
SELECT s.name, COUNT(a.event_id) AS events_attended
FROM students s
JOIN attendance a ON s.student_id = a.student_id
WHERE a.status = 1
GROUP BY s.student_id;

-- Top 3 Active Students
SELECT s.name, COUNT(a.event_id) AS events_attended
FROM students s
JOIN attendance a ON s.student_id = a.student_id
WHERE a.status = 1
GROUP BY s.student_id
ORDER BY events_attended DESC
LIMIT 3;
