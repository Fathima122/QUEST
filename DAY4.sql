use batch_shani;
create table student_details(
name varchar(12),
email varchar (14),
rollno int auto_increment,
ph int,
primary key (rollno)
);
insert into student_details (name,email,ph)
values ('arya','arya@gmail.com',23456);
insert into student_details (name,email,ph)
values ('mary','mary@gmail.com',54678);
insert into student_details (name,email,ph)
values ('nila','nila@gmail.com',467812);
insert into student_details (name,email,ph)
values ('karthik','karthik@gmail.com',123332);
insert into student_details (name,email,ph)
values ('leo','leo@gmail.com',674556);
select * from student_details;

create table tblmark(
mid int auto_increment,
rollno int references student_details(rollno),
malayalam int,
english int,
primary key (mid)
);
select * from tblmark;
insert into tblmark(rollno,malayalam,english)
values (2,56,78);
insert into tblmark(malayalam,english)
values (5,7);
insert into tblmark(rollno,malayalam,english)
values (6,6,88)  ;
-- sql like clause
select * from student_details where name like 'a%';
select * from student_details where name like '%a';
select * from student_details where name like '__a%';
select * from student_details where name like 'n%__';
select * from student_details where name like '%a%'; 

-- aggregate fnctns
-- 1)count
select  * from student_details;
select count(*) from student_details;
select * from tblmark;
select count(*) from tblmark;

-- 2) max and min
select min(english) from  tblmark;
select max(english) from tblmark;
select max(email) from student_details;


-- 3)sum
-- 4)avg
select sum(english) from tblmark;
select avg(english) from tblmark;
 
-- 5)-- limit
select * from tblmark limit 2;

 select max(english) from tblmark;
 select rollno from tblmark where english= (select max(english) from tblmark);
select name from student_details where rollno= ( select rollno from tblmark where 
english= (select max(english) from tblmark));
select max(malayalam) from tblmark;
select rollno from tblmark where malayalam=(select max(malayalam) from tblmark);
select name from student_details where rollno=(select rollno from tblmark where malayalam=(select max(malayalam) from tblmark)
);

