# Project-management-tool
Task : Create project management tool

Table 1 : Employee
  Attributes : 
    eid = Employee ID,
    ename = Employee First name,
    lname = Employee Last name,
    dob = Date of Birth,
    eemail = Employee email ID,
    desig = Designation
    
Table 2 : Project
  Attributes :
    pid = Project ID,
    pname = Project Name,
    pmanager = Project Manager,
    startdate = Project Start date,
    enddate = Project end date,
    eids = Employee IDs of employees working on project
    
Front end functionalities : http://localhost:8000/
  1. List all employee details
  2. Add new employee
  3. List all project details
  4. Look up an employee using the employee's first or last names, case insensitive search
  5. All projects that the employee is a part of is listed in projects table
  
Django Admin page : http://localhost:8000/admin/
  - Username : admin
  - Password : 123456
  
Admin page functionalities : 
  1. CRUD operations on employee table
  2. CRUD operations on project table, select existing employees based on their IDs to assign them to projects, employees can work on multiple projects
  
- Database  : SQLite
- Editor used : Visual studio code
- Branch : Uploaded to master branch
  
To run project : 
  1. python manage.py makemigrations
  2. python manage.py migrate
  3. python manage.py runserver
  
