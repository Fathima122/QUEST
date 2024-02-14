use batch_shani;
--                                             check  

create table s4(
place varchar (60),
age int
check (age>=20)
);


drop table s4;
insert into s4 (place,age)
values('A',23);
insert into s4 (place,age)
values('B',20
insert into s4 (place,age)
values('C',10);

select * from s4;

create table s5(
roll_no int,
name varchar (60),
primary key (roll_no)
);
insert into s5 (name)
values('anna');
insert into s5 (name)
values('anu');
insert into s5 (roll_no)
values(12);
insert into s5 (name)
values('ammu');
select * from s5;
 
 create table s6(
roll_no int  auto_increment,
name varchar (60),
primary key (roll_no)
);
 insert into s6 (name) 
 values ('anu');
  insert into s6 (name) 
 values ('anna');
select * from s6;
-- delete from s6;      without cndtn table all deleted and when again inserting maintain the continuity of rollno due to autoincrmnt
-- truncate table s6;   start from 1 in case of autoincrement
--                                                fnctns
--  aggregate fnctns
-- date fnctns
-- scalar fnctns
--                              aggregate fnctns

--                 operators
-- 1)and 
-- 2)or
-- 3)between
-- 4)in
-- 5)not in 
select * from student;
select * from student where name='kiran' and rollno=103 ;
select * from student where name='kiran' or rollno=103 ;
select * from student where name in ('kiran','anju') ;
select * from student where rollno not in (103,105);
select * from student where rollno between 103 and 105 ;

select distinct ph,email from student;
select distinct rollno from student;
-- alias-- 
select name as StudentName ,email as mail from student ;
alter table student change column phone ph int;

alter table student change column ph phone int;