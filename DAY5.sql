use batch_shani;
-- aggregrate enhances>>>>>>>>>>>>>1. order by  2. group by

-- order by         sorting the columns

select* from tblmark order by rollno;                    -- sorted rollno in ascending order
select* from tblmark order by rollno desc;                   -- sorted rollno in desending order

-- group by   used to combine the selection results by one oe more column


create table purchase(
p_id int auto_increment,
name varchar(15),
items varchar(15),
quantity int,
primary key(p_id)
);

insert into purchase (name,items,quantity) values('arun','pen',5);
insert into purchase (name,items,quantity) values('arun','pencil',4);
insert into purchase (name,items,quantity) values('kiran','pen',3);
insert into purchase (name,items,quantity) values('arun','pencil',1);
insert into purchase (name,items,quantity) values('ammu','pen',8);
insert into purchase (name,items,quantity) values('ammu','pencil',5);

select*from purchase;
select items,sum(quantity) from purchase group by items;
select items,sum(quantity) from purchase group by items having sum(quantity)>15;
select*from purchase where items='pen' order by quantity;

select *from students;
select*from tblmark;
select rolno,max(eng) from tblmark;