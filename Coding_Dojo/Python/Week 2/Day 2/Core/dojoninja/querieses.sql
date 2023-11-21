INSERT INTO dojos (name) VALUES
('Dojo 1'),
('Dojo 2'),
('Dojo 3');
DELETE FROM dojos WHERE id IN (1, 2, 3);
INSERT INTO dojos (name, created_at, updated_at) VALUES
('Dojo 4'),
('Dojo 5'),
('Dojo 6');

INSERT INTO ninjas (name,dojo_id) VALUES
('Ninja 1',4),
('Ninja 2',4),
('Ninja 3',4);

INSERT INTO ninjas (name, created_at, updated_at, dojo_id) VALUES
('Ninja 4',5),
('Ninja 5',5),
('Ninja 6',5);

INSERT INTO ninjas (name, created_at, updated_at, dojo_id) VALUES
('Ninja 7',6),
('Ninja 8',6),
('Ninja 9',6);

SELECT * FROM ninjas WHERE dojo_id = 4;
SELECT * FROM ninjas WHERE dojo_id = 6;
SELECT dojos.* FROM dojos
JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = 9;
SELECT ninjas.*, dojos.name AS dojo_name
FROM ninjas
JOIN dojos ON ninjas.dojo_id = dojos.id
WHERE ninjas.id = 6;
SELECT ninjas.*, dojos.name AS dojo_name
FROM ninjas
JOIN dojos ON ninjas.dojo_id = dojos.id;


