create table product_details (
Id int primary key auto_increment,
Name varchar(50),
Price float not null,
Total_Sale int not null,
City varchar(100) not null,
Rating float not null,
Age_Group varchar(15) not null
);

select * from product_details;