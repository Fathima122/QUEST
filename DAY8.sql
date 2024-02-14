#joins
converting multiple tables into single table
types
innerjoin- 
selfjoin
crossjoin
outerjoin-leftouter join and right outer join
select * from tblname1 inner join tblname on tblname1.rollno =tblname.rollno;
select * from tblname1 right join tblname on tblname1.rollno =tblname.rollno;--full details of tblname and common of tblname 1 ,null where there is no value
select * from tblname1 left join tblname on tblname1.rollno =tblname.rollno;--full details of tblname and common of tblname  ,null where there is no value
select * from tblname1 right join tblname on tblname1.rollno =tblname.rollno;--full details of tblname and common of tblname 1 ,null where there is no value
select e,empid,e.name,
m.name as manager
from emp e inner join emp m on e.empmgrid=m.empid;

select e.name EmpName,m.name Mngname from tblemp e inner join tblemp m on e.mid=m.eid;

create table workers(
worker_id int,
name varchar(12),
manager_id int 
);
select * from workers;
insert into workers
values (1,'raju',2);
insert into workers
values (2,'ram',2);
insert into workers
values (3,'babu',3);
insert into workers
values (4,'reka',3);
insert into workers
values (5,'kail',6);
insert into workers(worker_id,name)
values (6,'basil');
select w.name workername,m.name managername from  workers as w inner join workers as m on w.manager_id=m.worker_id; 
use practice_session;




