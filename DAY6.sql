use batch_shani;
create table saslesman(
salesman_id int,
name varchar (12),
city varchar (15) not null,
commission float,
primary key (salesman_id)
);
-- drop table saslesman;
insert into saslesman (salesman_id,name,city,commission)
values (5001,'James Hoog','New York',0.15);
insert into saslesman (salesman_id,name,city,commission)
values (5002,'Nail Knte','paris',0.13);
insert into saslesman (salesman_id,name,city,commission)
values (5005,'Pit Alex','London',0.11);
insert into saslesman (salesman_id,name,city,commission)
values (5006,'Mc Lyon','paris',0.14);
insert into saslesman (salesman_id,name,commission)
values (5003,'Lauson Hen',0.12);
insert into saslesman (salesman_id,name,city,commission)
values (5007,'Paul Adam','Rome',0.13);
select * from saslesman;


create table customer(
customer_id int,
cust_name varchar(15),
city varchar (12),
grade varchar(3) not null,
salesman_id  int references saslesman(salesman_id),
primary key (customer_id)
);

insert into customer (customer_id,cust_name,city,grade,salesman_id)
values (3002,'Nick Rimando','New York','100',5001)
insert into customer (customer_id,cust_name,city,grade,salesman_id)
values (3005,'Graham Zusi','California','200',5002)
insert into customer (customer_id,cust_name,city,salesman_id)
values (3001,'Brad Guzan','London',5005)
insert into customer (customer_id,cust_name,city,grade,salesman_id)
values (3004,'Fabian Johns','Paris','300',5006)
insert into customer (customer_id,cust_name,city,grade,salesman_id)
values (3007,'Brad Davis','New York','200',5001)
insert into customer (customer_id,cust_name,city,grade,salesman_id)
values (3009,'Geo Camero','Berlin','100',5003)
insert into customer (customer_id,cust_name,city,grade,salesman_id)
values (3008,'Julian Green','London','300',5002)
insert into customer (customer_id,cust_name,city,grade,salesman_id)
values (3003,'Jozy Altidor','Moscow','200',5007)
select * from customer; 


create table orders(
ord_no int,
purch_amt decimal (10,4),
ord_date date,
customer_id  int references customer(customer_id),
salesman_id  int references saslesman(salesman_id),
primary key (ord_no)
);
insert into orders (ord_no,purch_amt,ord_date,customer_id,salesman_id)
values (70001,150.5,'2012-10-05',3005,5002);
delete from orders  where ord_no=70001;
insert into orders (ord_no,purch_amt,ord_date,customer_id,salesman_id)
values (70009,270.65,'2012-09-10',3001,5005);
delete from orders  where ord_no=70009;

insert into orders (ord_no,purch_amt,ord_date,customer_id,salesman_id)
values (70002,65.26,'2012-10-05',3002,5001);
insert into orders (ord_no,purch_amt,ord_date,customer_id,salesman_id)
values (70004,110.5,'2012-10-05',3009,5003);
insert into orders (ord_no,purch_amt,ord_date,customer_id,salesman_id)
values (70007,948.5,'2012-08-17',3005,5002);
insert into orders (ord_no,purch_amt,ord_date,customer_id,salesman_id)
values (70005,2400.6,'2012-09-10',3007,5001);
insert into orders (ord_no,purch_amt,ord_date,customer_id,salesman_id)
values (70008,5760,'2012-07-27',3002,5001);
insert into orders (ord_no,purch_amt,ord_date,customer_id,salesman_id)
values (70010,1983.43,'2012-09-10',3004,5006);
insert into orders (ord_no,purch_amt,ord_date,customer_id,salesman_id)
values (70003,2480.4,'2012-10-10',3009,5003);
insert into orders (ord_no,purch_amt,ord_date,customer_id,salesman_id)
values (70012,250.45,'2012-06-27',3008,5002);
insert into orders (ord_no,purch_amt,ord_date,customer_id,salesman_id)
values (70011,75.29,'2012-08-17',3003,5007);
insert into orders (ord_no,purch_amt,ord_date,customer_id,salesman_id)
values (70013,3045.6,'2012-04-25',3002,5001);
select * from orders;
drop table orders;
drop table orders;
--                                                           basic

     --                                                    questions 


-- 1.Write a SQL statement to display names and city of salesman, who belongs to the city
-- of Paris .

select name,city from saslesman where city='paris';

-- 2.Write a SQL statement to display all the information for those customers with a grade of
-- 200

select * from customer where grade=200;

-- 3.Write a SQL query to display the order number followed by order date and the purchase
-- amount for each order which will be delivered by the salesman who is holding the ID
-- 5001.

select ord_no,ord_date,purch_amt from orders where salesman_id=5001;

-- 4.Write a SQL statement to find those salesmen with all information who come from the city
-- either Paris or Rome

select * from saslesman where city='paris' or city='rome';

-- 5.Write a query to filter those salesmen with all information who comes from any of the cities
-- Paris and Rome

select * from saslesman where city='paris' or city='rome';

-- 6.Write a query to produce a list of salesman_id, name, city and commision of each
-- salesman who live in cities other than Paris and Rome.
select * from saslesman where city not in ('paris','rome');

-- 7.Write a query to sort out those customers with all information whose ID value is within any
-- of 3007, 3008 and 3009.

select * from customer where customer_id between 3007 and  3009 order by cust_name;

-- 8.Write a SQL statement to find those salesmen with all information who gets the
-- commission within a range of 0.12 and 0.14

select * from saslesman where commission between 0.11 and 0.15; 

-- Write a query to filter all those orders with all information which purchase amount value is
-- within the range 500 and 4000 except those orders of purchase amount value 948.50 and
-- 1983.43

select * from orders where purch_amt between 500 and 4000 and purch_amt not in (948.5,1983.43) ; 

-- 9.Write a SQL statement to find those salesmen with all other information and name started
-- with any latter within 'A' and 'K'.

select * from saslesman where name between 'a' and 'k';

-- Write a SQL statement to find that customer with all information whose name begin with
-- the letter 'B'.

select * from customer where cust_name  like 'b%';

-- 10.Write a SQL statement to find those salesmen with all information whose name containing
-- the 1st character is 'N' and the 4th character is 'l' and rests may be any character.

select * from saslesman where name like 'n%__l%'; 

--                                                  Aggregate Functions

--                                                    questions 
-- 1.Write a SQL statement to find the total purchase amount of all orders.

select sum(purch_amt) from orders;

-- 2.Write a SQL statement to find the average purchase amount of all orders.

select avg(purch_amt) from orders;

-- 3.Write a SQL statement to find the number of salesmen currently listing for all of their
-- customers.

select count(salesman_id) from saslesman;

-- 4. Write a SQL statement find the number of customers who gets at least a gradation for
-- his/her performance

select count(customer_id)  from customer where grade>=1;

-- 5.Write a SQL statement to get the maximum purchase amount of all the orders.


select max(purch_amt) from orders;

-- 6.Write a SQL statement which selects the highest grade for each of the cities of the
-- customers.

select city,max(grade) from customer group by city;

-- 7.Write a SQL statement to find the highest purchase amount ordered by the each
-- customer with their ID and highest purchase amount.

select customer_id,max(purch_amt) from orders group by customer_id;

-- 8.Write a SQL statement to find the highest purchase amount ordered by the each
-- customer on a particular date with their ID, order date and highest purchase amount.

select max(purch_amt),customer_id,ord_date  from orders group by ord_date;

-- 9.Write a SQL statement to find the highest purchase amount on a date '2012-08-17' for
-- each salesman with their ID.

select max(purch_amt),ord_date,salesman_id from orders group by ord_date having ord_date ='2012-08-17';
 

