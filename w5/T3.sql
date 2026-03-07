SELECT ar.name, SUM(al.tracks) as total_tracks
FROM artist ar
JOIN album al
ON ar.id = al.artist_id
GROUP BY ar.name
ORDER BY ar.name;