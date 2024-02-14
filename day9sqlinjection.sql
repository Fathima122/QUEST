-- stored procedure

select * from student_details where name= '' and email='bb' or 1=1;     -- --sql injection 
delimiter  //
create procedure get_s2  (in var int)
begin
select * from s2 limit var;
select count(rollno) as total_student from s2;
end//
delimiter ;
insert into s2(email)values (md5('akk@hmail.com'));
select email from s2 where email=md5('akk@hmail.com');

call get_student_details(4);
encryption
hashing algm

insert into student_details (name,email)
values('john','john@gmail.com');
insert into student_details (name,email) 
values('john',md5('john@gmail.com'));
select * from student_details where email=md5('john@gmail.com');

create table ord(
order_no int,
orderdate date,
requireddate date,
shippeddate date,
ststus varchar(33),
comments varchar(100),
customerno int,
primary key (order_no)
);


create table orddetails(
order_no int references ord(order_no),
productcode varchar(78),
quantityordered int,
priceeach decimal(10,4),
orderlinenumber int
);

insert into ord(order_no,ststus)values(1,'pending');
insert into ord(order_no,ststus)values(2,'completed');
insert into ord(order_no,ststus)values(3,'completed');
insert into ord(order_no,ststus)values(4,'pending');
select * from ord;

insert into orddetails(order_no,quantityordered,priceeach)values(1,2,99.5);
insert into orddetails(order_no,quantityordered,priceeach)values(2,6,.150);
insert into orddetails(order_no,quantityordered,priceeach)values(3,1,235.8);
insert into orddetails(order_no,quantityordered,priceeach)values(3,4,300);
select * from orddetails;

select  ststus,sum(quantityordered*priceeach)totalamount from ord  inner join orddetails  on ord.order_no=orddetails.order_no group by ststus;
