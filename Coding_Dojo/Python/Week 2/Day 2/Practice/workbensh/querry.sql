SET SQL_SAFE_UPDATES = 0;
SELECT * FROM my_db.names;
insert into names (name) values ("bouhmid");
insert into names (name) values ("abdelrahim");
insert into names (name) values ("nawfel");
insert into names (name) values ("ala");
delete from names where (name="bouhmid");
update names set name="abdelrahim" where (name="bouhmid");