select * from users_schema.users;
insert into users_schema.users (first_name,last_name,email) values('sadik',"zrelli","samuel@gmail.com") ;
insert into users_schema.users (first_name,last_name,email) values('abdel',"rahim","abdelrahim@gmail.com") ;
insert into users_schema.users (first_name,last_name,email) values('bouhmid',"hamid","bouhmid@gmail.com") ;
select * from users_schema.users where (email="samuel@gmail.com");
select * from users_schema.users where (id=3);
update users_schema.users set last_name="Pancake" where id=3;
select * from users_schema.users where (id=3);
delete from users_schema.users where (id=2);
select * from users_schema.users where (id=2); # rip bouhmid
SELECT * FROM users_schema.users
ORDER BY first_name;
SELECT * FROM users_schema.usersdojos
ORDER BY  first_name desc;