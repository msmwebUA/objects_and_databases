SELECT ar.name as artist, followers, al.name as album, tracks
FROM artist ar
JOIN album al
ON ar.id = al.artist_id
ORDER BY artist, album;