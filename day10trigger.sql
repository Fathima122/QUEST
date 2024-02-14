##triggers
create table employee_demo(
emp_id int,
emp_name varchar(23),
emp_sal decimal(10,2)
);
select * from employee_demo;
select* from employee_demo_audit;
create table employee_demo_audit(
emp_id int,
emp_name varchar(23),
emp_sal decimal(10,2),
audit_action varchar(34),
audit_timestamp date
);
insert into employee_demo(emp_id,emp_name,emp_sal)values(1,'sasu',2345.8);
insert into employee_demo(emp_id,emp_name,emp_sal)values(23,'saintu',6785.8);
insert into employee_demo(emp_id,emp_name,emp_sal)values(3,'sainthjku',7685.8);
drop table employee_demo_audit;
-- create trigger on table employee_demo for insert statement 

create trigger trgafterinsert after insert on employee_demo for each row
insert into employee_demo_audit(emp_id,emp_name,emp_sal,audit_action,audit_timestamp)
values(new.emp_id,new.emp_name,new.emp_sal,'hyyy',now());
drop trigger trgafterinsert;

create trigger trgrafterdelete after delete on employee_demo for each row
insert into employee_demo_audit(emp_id,emp_name,emp_sal,audit_action,audit_timestamp)
values (old.emp_id,old.emp_name,old.emp_sal,'huiiii',now());

drop trigger trgbeforeinsert;
delete from employee_demo where emp_id=1;

create trigger trgbeforeinsert before insert on employee_demo for each row
insert into employee_demo_audit(emp_id,emp_name,emp_sal,audit_action,audit_timestamp)
values (new.emp_id,new.emp_name,new.emp_sal,'huiiii',now());
delete from employee_demo where emp_id=3;


create trigger trgrbeforedelete before delete on employee_demo for each row
insert into employee_demo_audit(emp_id,emp_name,emp_sal,audit_action,audit_timestamp)
values (old.emp_id,old.emp_name,old.emp_sal,'huiiii',now());
drop trigger  trgbeforeupdate;

create trigger trgbeforeupdate before update on employee_demo for each row
insert into employee_demo_audit(emp_id,emp_name,emp_sal,audit_action,audit_timestamp)
values (old.emp_id,old.emp_name,old.emp_sal,'huiiii',now());

update employee_demo set emp_id=88 where emp_id=23;

select * from customers;