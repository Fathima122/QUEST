-- day9 assingment

-- Create the following table
-- EmployeeDetails(EmpId,FirstName,LastName,Salary,Department,Gender)
-- ProjectDetail(ProjectId,EmployeeId,ProjectName)

create table EmployeeDetails(
emp_id int,
firstname varchar(14),
lastname varchar(15),
salary int,
department varchar(16),
gender varchar(11),
primary key (emp_id)
);

create table ProjectDetail(
projectid int,
emp_id int references EmployeeDetails(emp_id),
projectname varchar(12)
); 
insert into EmployeeDetails(emp_id,firstname,lastname,salary,department,gender)values(1,'jonas','martin',500000,'history','male');
insert into EmployeeDetails(emp_id,firstname,lastname,salary,department,gender)values(2,'satin','tom',800000,'economics','male');
insert into EmployeeDetails(emp_id,firstname,lastname,salary,department,gender)values(3,'suresh','titan',600000,'computerscience','male');
insert into EmployeeDetails(emp_id,firstname,lastname,salary,department,gender)values(4,'kapish','mk',700000,'economics','male');
insert into EmployeeDetails(emp_id,firstname,lastname,salary,department,gender)values(5,'vikas','gary',700000,'economics','male');
insert into EmployeeDetails(emp_id,firstname,lastname,salary,department,gender)values(6,'ashish','mok',400000,'economics','male');
insert into EmployeeDetails(emp_id,firstname,lastname,salary,department,gender)values(7,'nikhil','ms',200000,'economics','male');

insert into ProjectDetail(projectid,emp_id,projectname)values(12,1,'forest fire');
insert into ProjectDetail(projectid,emp_id,projectname)values(13,2,'forest fire');
insert into ProjectDetail(projectid,emp_id,projectname)values(13,3,'sanskrit');
insert into ProjectDetail(projectid,emp_id,projectname)values(14,3,'sanskrit');
insert into ProjectDetail(projectid,emp_id,projectname)values(16,3,'jikkl');
delete from ProjectDetail where projectname='jikkl';
insert into ProjectDetail(projectid,emp_id,projectname)values(15,4,'sanskrit');
insert into ProjectDetail(projectid,projectname)values(17,'depression');


update projectdetail set projectname='tourist destination' where projectid=14;



select * from ProjectDetail;


-- 1. Write query to get all employee detail from "EmployeeDetail" table
select * from EmployeeDetails;

-- 2. write query to get only "FirstName" column from "EmployeeDetail" table
select firstname from EmployeeDetails;

-- 3,Write query for combine FirstName and LastName and display it as "Name" (also include white space between first name & last name)

select concat(firstname,' ',lastname)  name from EmployeeDetails ;

-- 4. Get all employee details from EmployeeDetail table whose "FirstName" end with 'h'
select * from EmployeeDetails where firstname like '%h';

-- 5. Get all unique "Department" from EmployeeDetail table.
select distinct department from EmployeeDetails;

-- 6. Get the highest "Salary" from EmployeeDetail table
select max(salary) from EmployeeDetails;

-- 7. Get the lowest "Salary" from EmployeeDetail table
select min(salary) from EmployeeDetails;

-- 8. Select all employee detail with First name "Vikas","Ashish", and "Nikhil"
select * from EmployeeDetails where firstname='vikas' or firstname='ashish' or firstname='nikhil';

-- 9. Select all employee detail with First name not "Vikas","Ashish", and "Nikhil"
select * from EmployeeDetails where firstname not in ('vikas','ashish','nikhil');

-- 10. Select first name from "EmployeeDetail" table prifixed with "Hello "
select concat('hello',firstname) from EmployeeDetails;

-- 11. Get employee details from "EmployeeDetail" table whose Salary less than 700000
select * from EmployeeDetails where salary<700000;

-- 12. Get employee details from "EmployeeDetail" table whose Salary between 500000 than 600000 
select * from EmployeeDetails where salary between 500000 and 600000;

-- 13. Select second highest salary from "EmployeeDetail" table 
select max(salary)  secndhighestsalary from EmployeeDetails where salary not in(select max(salary) from EmployeeDetails);

-- 14. Write the query to get the department and department wise total(sum) salary from
--  "EmployeeDetail" table.
select department,sum(salary) from EmployeeDetails group by department;

-- 16. Write the query to get the department, total no. of departments, total(sum) salary with
-- respect to department from "EmployeeDetail" table.
select department,count(distinct department) totaldepartments,sum(salary) from EmployeeDetails group by department;

-- 17. Get department wise maximum salary from "EmployeeDetail" table order by salary ascending
select department,max(salary) from EmployeeDetails group by department order by max(salary) ;

-- 18. Write down the query to fetch Project name assign to more than one Employee

select projectdetail.projectname from EmployeeDetails join projectdetail on EmployeeDetails.emp_id=projectdetail.emp_id
 group by projectname having count(projectdetail.emp_id)>1;
 
--  19. Get employee name, project name order by firstname from "EmployeeDetail" and
-- "ProjectDetail" for those employee which have assigned project already.
select EmployeeDetails.firstname,projectdetail.projectname from EmployeeDetails inner join projectdetail on 
EmployeeDetails.emp_id=projectdetail.emp_id order by firstname;

-- 20. Get employee name, project name order by firstname from "EmployeeDetail" and
-- "ProjectDetail" for all employee even they have not assigned project.

select EmployeeDetails.firstname,projectdetail.projectname from EmployeeDetails left join projectdetail on 
EmployeeDetails.emp_id=projectdetail.emp_id  order by firstname;

-- 21. Write a query to find out the project name which is not assigned to any employee
select projectname from projectdetail where emp_id is null;

-- 22. Write down the query to fetch EmployeeName & Project who has assign more than one project.
select EmployeeDetails.firstname,projectdetail.projectname from EmployeeDetails inner join projectdetail on 
EmployeeDetails.emp_id=projectdetail.emp_id group by EmployeeDetails.emp_id having count(projectname)>1;





