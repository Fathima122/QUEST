
-- create database practice_Session;
use practice_Session;
-- create table example(
-- name varchar(12),
-- roll_no int,
-- email varchar(15),
-- ph int
-- );

-- create table example1(
-- name varchar(12),
-- roll_no int,
-- email varchar(15),
-- ph int
-- );
create table example2(
name varchar(12) not null,
roll_no int,
email varchar(15),
ph int
);
create table example22(
name varchar(12) not null,
roll_no int,
email varchar(15),
ph int
);
insert into example22(roll_no,email)
values(12,'anu@gmailcom');
insert into example22(name,roll_no,email)
values('anu',122,'anu@gmailcom');
select * from example22;
insert into example2;
values('anu',121,'anu@gmail.com',6778);
insert into example2 (roll_no,email,ph)
values (23,'anujj@gmail.com',6789);
insert into example2 (name,roll_no,ph)
values ('ammu',12,6785669);
select * from example2;
select * from example2 order by name;
select * from example2 order by email;
select * from example2 order by name desc;
select * from example2 order by email desc;



delete from example2 where name='ammu';
drop table example2;
-- drop table example1;

-- alter table example rename to example_taken;
-- alter table example_taken add place varchar(7);
alter table example_taken drop place; 
insert into example_taken 
values('anu',12,'anu@gmail.com',2146789);
select * from example_taken;
insert into example_taken 
values (33,234577,'anju@gmail.com','anju');
insert into example_taken
values('manu',16,'manu@gmail.com',5456788);

insert into example_taken (name,roll_no,email,ph)
values ('ammu',45,'ammu@gmail.com',456778);
insert into example_taken (name,roll_no,email,ph)
values ('fan',34,'fanu@gmail.com,',3688794);
insert into example_taken (name,email,ph)
values('ram',123,6765677);
insert into example_taken (name,roll_no,email,ph)
values(67,'renju',77677,'renju@gmail.com');
insert into example_taken
values('was');
alter table  example_taken rename column name to name_id;

insert into example_taken (ph)
values (956578)
select * from example_taken where name ='anu';
select * from example_taken where roll_no=16;
select name,email from example_taken;
select name,email from example_taken where name='anu';
select name,ph from example_taken where ph=5456788;
select *,name from example_taken where name='anu';


 update example_taken set name='manu',ph=46688  where email='manu@gmail.com' ;
 update example_taken set name='fanu' where ph=3688794;
  update example_taken set name='ammu' where  email='ammu@gmail.com';
  update example_taken set name='anu'where name='anju';
  
  delete from example_taken where roll_no=12;
   delete from example_taken where ph=0;
  
  create table p1(
  name varchar(10),
  rollno int,
  email varchar(12) 
  );
  
  insert into p1(name,rollno)
  values('raju',567)
insert into p1(name,rollno)
values('jana',567887)

 create table p2(
  name varchar(13),
  rollno int not null,
  email varchar(11) not null 
  );
  drop table p2;
  insert into p2(rollno)
  values(32);
  insert into p2(name,rollno,email)
  values('ramya',55,'ramya@gmail.com');
  select * from p2;
  insert into p2(
  insert into p2(name,email)
  values('raya','raya@gmail.com');
  create table p3(
  name varchar(13),
  rollno int unique,
  email varchar(11) unique 
  );
  select * from p3;
insert into p3(name,email)
values('amy','amy@gmail.com');  
insert into p3(name,email)
values('arya','arya@gmail.com');  

  insert into p3(name,rollno)
  values('anna',56);
  

  insert into p3(email,rollno)
  values('anna@gmail.com',89);
  insert into p3(name)
  values('anna');
insert into p3(email)
values('anna@gmail.com');

 
    create table p4(
  name varchar(17),
  rollno int  not null unique,
  email varchar(21)  not null unique 
  );
  insert into p4(name,rollno,email)
  values('kiran',67,'kiran@gmail.com');
  select * from p4;
  
  insert into p4(rollno,email)
  values(66,'manu@gmail.com');
  insert into p4(rollno,email)
  values(6,'manu@gmail.com');
  
  update p4 set email='ananya@gmail.com' where rollno=66;
  update p4 set name='ananya',email='ananyatt@gmail.com' where rollno=66;
  update p4 set email='ananyatt@gmail.com',name='ananyatt' where rollno=66;
insert into p4(email)
values('ananyatt@gmail.com');
  insert into p4(email)
  values('jj@gmail.com');
    insert into p4(email)
  values('jk@gmail.com');
  
    insert into p4(rollno)
    values(678);
    insert into p4(rollno)
    values(889);
    create table p5(
  name varchar(13) unique not  null,
  rollno int  not null unique,
  email varchar(21)  
  );
  insert into p5(rollno,email)
  values(22,'kl@gmail.com');
  select * from p5;
  
   insert into p5(rollno,email)
  values(12,'mnop@gmail.com'); 
    insert into p5(name,rollno)
  values('annama',34);
create table p6(
rollno int,
place varchar(12) default 'pala',
email varchar(23)
);
insert into p6(place)
values('sweden');
insert into p6(rollno)
values(43);
select * from p6;

create table p7(
rollno int,
place varchar(12) default 'pala' unique ,
email varchar(23)
);
insert into p7(rollno)
values(63);
select * from p7;
insert into p7(rollno)
values(4378);
create table p8(
age int,
place varchar(12)
check (age>=23)
);
drop table p8;

insert into p8(age)
values (22);
select * from p8;

create table p9(
rollno int,
age int,
place varchar(12),
primary key (rollno)
);
select * from p9;

insert into p9(age)
values (12);
insert into p9(age)
values (13);

create table p10(
rollno int auto_increment,
age int,
place varchar(12),
primary key (rollno)
);
insert into p10(age,rollno)
values (22,24);
insert into p10(age)
values (24);
insert into p10(age,place)
values (25,'eklm');
insert into p10(age,rollno,place)
values (26,2,'pala');
insert into p10(age)
values (24);
insert into p10(age,place,rollno)
values (24,'omen',53);
select * from p10;
insert into p10(age,place)
values (22,'palakad');
insert into p10(age,place,rollno)
values (24,'omen',5);
insert into p10(age,place)
values (22,'palakad');
insert into p10(age,place)
values (22,'palayil');

delete from p10 ;
drop table p10;
truncate table p10;
create table mark_id(
mark int auto_increment,
name varchar(7),
email varchar (12),
rollno int references student_details (rollno),
primary key (mark)
);
insert into mark_id(name,email,rollno)
values ('arya','arya@gmail.com',5);
select * from mark_id
drop table mark_id;

select roll_no from example_taken where name like  'f%';
select *  from example_taken where name like  'a%';
select * from example_taken where ph like  '6%';
select * from example_taken where name like  '%n';
select name from example_taken where email like  '%3';
select email from example_taken where name like  '%n%';
select * from example_taken where name like  '__m%';
select * from example_taken where name like  'a%__';
select * from example_taken where name like  'f%__';
select * from example_taken where name like  'm%__';

insert into example_taken(name)
values ('nj');
update example_taken


select count(*) from example_taken;
select count(*) from p9;
select max(roll_no) from example_taken;
select max(name) from example_taken;
select min(name) from example_taken;

select sum(roll_no) from example_taken;
select sum(email) from example_taken;
select sum(ph) from example_taken;
select avg(ph) from example_taken;
select name from example_taken limit 3;

select avg(email) from example_taken;







select * from p5;
select * from p10;


select * from p7;
select rollno as rollno_id from p10;

select * from example2 inner join example22 on example2.name=example22.name;
select * from example2 left join example22 on example2.name=example22.name ;

select * from example2 inner join example_taken on example2.name=example_taken.name inner join example22 on example_taken.name=example22.name;


select * from example2 left join example22 on example2.name=example22.name;
select * from example_taken left join example2 on example_taken.name=example2.name ;

select * from example2 right join example_taken on example2.email=example_taken.email;


delimiter #
create procedure get_s5 (in a int)
begin
select * from s5;
select count(roll_no) from s5;
end#
delimiter ;
call get_s5(2);




