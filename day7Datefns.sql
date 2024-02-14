-- normalisation
use batch_shani;
create  table Department(
ep_id int,
dep_name varchar(12),
dep_location varchar(13),
primary key (ep_id)
);

insert into Department
values (1001,'finance','sydney');
insert into Department
values (2001,'Audit','melbourne');
insert into Department
values (3001,'marketing','perth');
insert into Department
values (4001,'production','brisbane');
select * from Department;

create table employ(
emp_id int,
emp_name varchar(12),
job_name varchar (13),
manager_id int,
hire_date date,
salary int,m,
commission int,
ep_id int references Department(ep_id)
);
select * from employ;
insert into Employ(emp_id,emp_name,job_name,hire_date,salary,ep_id)
values(68319,'kayling','president','1991-11-18',6000,1001);
insert into Employ(emp_id,emp_name,job_name,manager_id,hire_date,salary,ep_id)
values(66928,'blaze','manager',68319,'1991-05-01',2750,3001);
insert into Employ(emp_id,emp_name,job_name,manager_id,hire_date,salary,ep_id)
values(67832,'clare','manager',68319,'1991-06-09',2550,1001);
insert into Employ(emp_id,emp_name,job_name,manager_id,hire_date,salary,ep_id)
values(65646,'jonas','manager',68319,'1991-04-02',2957,2001);
insert into Employ(emp_id,emp_name,job_name,manager_id,hire_date,salary,ep_id)
values(67858,'scarlet','analyst',65646,'1997-04-19',3100,2001);
insert into Employ(emp_id,emp_name,job_name,manager_id,hire_date,salary,ep_id)
values(69062,'FRANK','analyst',65646,'1991-12-03',3100,2001);
insert into Employ(emp_id,emp_name,job_name,manager_id,hire_date,salary,ep_id)
values(63679,'SANDRINE','clerk',69062,'1990-12-18',3100,2001);
insert into Employ(emp_id,emp_name,job_name,manager_id,hire_date,salary,commission,ep_id)
values(64989,'ADELYN','SALESMAN',66928,'1991-02-20',1700,400,3001);
insert into Employ(emp_id,emp_name,job_name,manager_id,hire_date,salary,commission,ep_id)
values(65271,'WADE','SALESMAN',66928,'1991-02-22',1350,600,3001);
insert into Employ(emp_id,emp_name,job_name,manager_id,hire_date,salary,commission,ep_id)
values(66564,'MADDEN','SALESMAN',66928,'1991-09-28',1350,1500,3001);
insert into Employ(emp_id,emp_name,job_name,manager_id,hire_date,salary,commission,ep_id)
values(68454,'TUCKER','SALESMAN',66928,'1991-09-08',1600,0,3001);
insert into Employ(emp_id,emp_name,job_name,manager_id,hire_date,salary,ep_id)
values(68736,'ADNRES','CLERK',67858,'1997-05-23',1200,2001);
insert into Employ(emp_id,emp_name,job_name,manager_id,hire_date,salary,ep_id)
values(69000,' JULIUS',' CLERK',66928,'1991-12-03',1050,3001);
insert into Employ(emp_id,emp_name,job_name,manager_id,hire_date,salary,ep_id)
values(69324,'MARKER',' CLERK',67832,'1992-01-23',1400,1001);
select * from employ;
drop table employ;

create table salary(
grade int  auto_increment,
min_salary int,
max_salary int,
primary key (grade)
);
select * from salary;
insert into salary(min_salary,max_salary)
values(800,1300);
insert into salary(min_salary,max_salary)
values(1301,1500);
insert into salary(min_salary,max_salary)
values(1501,2100);
insert into salary(min_salary,max_salary)
values(2101,3100);
insert into salary(min_salary,max_salary)
values(3101,9999); 

-- Write a query in SQL to list the employees with Hire date in the format like February 22, 1991.
select emp_name from employ where hire_date='1991-02-22';

-- Write a query in SQL to list the employees who does not belong to department 2001.
 select emp_name from employ where ep_id not in (2001);
 
 -- Write a query in SQL to display the unique department with jobs.
 select distinct  ep_id ,job_name from employ;
 
 
 -- Write a query in SQL to list the employees who joined before 1991
select emp_name  from employ where  hire_date <'1991-02-20';


--  Write a query in SQL to display the average salaries of all the employees who works as ANALYST. 
select avg(salary) from employ where job_name='analyst';

-- Write a query in SQL to list the name of the employees, those having six characters to their name
select emp_name from employ where length(emp_name)=6;


-- Write a query in SQL to list the employees whose salaries are less than 3500.
select emp_name from employ where salary<3500;

-- Write a query in SQL to list the details of the employees whose salary is more than the salary of JONAS.

select salary from employ where emp_name='jonas';
select * from employ where salary>(select salary from employ where emp_name='jonas');

-- Write a query in SQL to list the employees who works in the same designation as FRANK.

select job_name from employ where emp_name='frank';
select emp_name from employ where job_name=(select job_name from employ where emp_name='frank');

-- Write a query in SQL to list the employees of department ID 2001 who works in the designation
-- same as department ID 1001.
select job_name from employ where ep_id=1001;   
select emp_name from employ where ep_id=2001 and job_name in(select job_name from employ where ep_id=1001) ;   


-- Write a query in SQL to list the employees whose salary is same as the salary of FRANK or
-- SANDRINE. List the result in descending order of salary.
select salary from employ where emp_name ='frank' or emp_name ='sandrine';
select emp_name from Employ where salary in (select salary from Employ where 
emp_name='Frank' or emp_name='Sandrine'  order by salary desc);

select job_name from employ where emp_name='marker';
select salary from employ where emp_name='adelyn';
select  emp_name,salary,job_name from employ where job_name=(select job_name from employ where emp_name='marker') or 
salary>(select salary from employ where emp_name='adelyn');

-- Write a query in SQL to list the employees whose designation is same as the designation ofSANDRINE or ADELYN.
select job_name from employ where emp_name='sandrine' or emp_name='adelyn';
select emp_name from employ where job_name in (select job_name from employ where emp_name='sandrine' or emp_name='adelyn');

-- Write a query in SQL to list any job of department ID 1001 those that are not found in departmentID 2001.
select job_name from employ where job_name not in (ep_id=2001);
select job_name from employ where ep_id=1001 and job_name not in (select job_name from employ where job_name not in (ep_id=2001));

--  Write a query in SQL to find the highest paid employees in the department MARKETING.
select e.salary,e.emp_name,e.job_name from employ e inner join department d on e.ep_id=d.ep_id 
where dep_name='marketing' order by salary desc;


-- Write a query in SQL to list the details of the senior employees as on year 1991.
select * from employ where hire_date=(select min(hire_date) from employ where extract(year from hire_date)=1991);

-- Write a query in SQL to list the employees who joined in 1991 in a designation same as the most
-- senior person of the year 1991.
select emp_name from employ where job_name=(select job_name from employ where hire_date=(select min(hire_date) from employ
 where extract(year from hire_date)=1991)and extract(year from hire_date)=1991);

                                            date fns

select current_date() ;
-- ------------return current date


select current_timestamp();
-- returns current date with time
select current_time();
-- returns ony current time
-- 4)select cur_date();
-- returns only currentdate

select adddate('2017-06-15',interval 10 day);
select adddate('2023-11-16',interval -10 month);
select adddate('2023-11-16 20:57:12',interval 3 minute);

select adddate('2017-06-15',interval -10 day);

select adddate('2017-06-15',interval 2 year);

select addtime('2017-06-15  09:34:21','50');
select addtime('2023-11-16 20:39:12','12');
select addtime('2023-11-16 20:39:12','12:12:12');

select addtime('2017-06-15  09:34:21','1:50');
select datediff('2023-11-16','2023-10-12');
select datediff('2023-10-12','2023-11-1');

select date('2017-12-3');
select datediff('2017-05-5','2017-04-30');

select date_add('2017-06-15',interval 10 day);
select date_add('2017-06-12',interval 5 year);
select date_add('2012-12-22 2:12:3', interval  2 second);
select date_add('2017-06-12',interval -5 month);

select date_format('2017-06-15','%m'); 
select date_format('2017-06-15','%M'); --  --month name
-- select date_format('2017-06-15','%y');    17
-- select date_format('2017-06-15','%Y');  2017

-- select date_format('2017-06-15','%d');  15
-- select date_format('2017-06-15','%D'); IST
-- select date_format('2017-06-15','%D');  15TH
-- select date_format('2017-06-15','%m %D %Y');


SELECT date_sub('2017-06-15 3:23:1', interval 10 hour);
SELECT date_add('2017-06-15 3:23:1', interval -10 hour);

SELECT monthname('08-12-3');
-- select dayname('201706-12');
select dayname('08-12-3');
select dayofmonth('08-12-3'); 
-- select dayofweek();
-- select dayofyear();
select now();
select substring('sqltutorial',5,5)as ccc;









