SELECT 
      id AS [opiskelija tunnus],
      name AS nimi,
      group_id AS ryhma,
      ects AS ECTS
FROM Students st
WHERE ects = (
  SELECT MAX(ects)
  FROM Students
  WHERE group_id = st.group_id
)
ORDER BY ryhma;