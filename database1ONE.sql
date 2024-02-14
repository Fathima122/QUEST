create database batch_shani; 
show databases;
use batch_shani;
 -- create table student(
--  rollno int,
--  name varchar(12),
--  email varchar(15),
--  ph int
--  );

create table student1(
 rollno int,
 name varchar(12),
 email varchar(15),
 ph int
 );

create table hhjj(
 rollno int auto_increment,
 name varchar(12),
 email varchar(15),
 ph int,
 primary key (rollno)
 );
 insert into hhjj
 values(23,'5678','anna@gmail.com','56767')
 insert into hhjj
 values (12,45565,6667,'546576');
select * from hhjj;
create table kkjj(
 rollno int auto_increment,
 name varchar(12) default 'arya',
 email varchar(15),
 ph int,
 primary key (rollno)
 );
 insert into kkjj
 values (23,65567,'anna@gmail.com',5678);
  insert into kkjj
 values (13,567,'arya',5678);
 select * from kkjj;
drop table student1


alter table student add place varchar(30);
alter table student modify place varchar(12);
alter table student drop place;
alter table student rename to stud;

-- -----------------------------------DML
insert into stud (rollno,name,email,ph)
values (101,'anu','anu@gmail.com',24343);

select * from stud;

insert into stud (rollno,name,email,ph)
values (102,'arun','arun@gmail.com',24355543);

select * from stud;

insert into stud (rollno,name,email,ph)
values (102,'arun','arun@gmail.com',24355543);

select name from stud
insert into stud (rollno,name,email)
values (103,'anju','anju@gmail.com');
select * from stud

insert into stud 
values (104,'shani','shani@gmail.com',67434554);
select * from stud

insert into stud (rollno,name,email,ph)
values (105,'kiran','kiran@gmail.com',9037019336);
select * from stud

select * from student where name ='anju';

update student set email='anjumm@gmail.com' where ph=24343;


select * from student; 


delete from student where rollno=101;
--                                                    constraints 
-- not null, unique ,check ,default, create index
 

create table s1(
rollno int(9) not null,
name varchar(60) not null,
ph int,
email varchar(60)
);

create table s2(
rollno int(4) not null,
name varchar(45) not null,
ph int unique,
email varchar(70) not null unique
);

insert into s2(ph)
values (456);
insert into s2(email)
values ('anna@gmail.com');
insert into s2(email,ph)
values ('anna@gmail.com',577);
 
 select * from s2;
 
insert into s1(rollno,name,ph)
values (12,'anu',789);
-- insert into s1(ph)
-- values (6678);

 
select * from s1

--                                default
create table s3(
rollno int,
place varchar(34) default 'eklm'
);

insert into s3(rollno,place)
values(101,'pala');


insert into s3(rollno)
values(103);
select * from s3;







