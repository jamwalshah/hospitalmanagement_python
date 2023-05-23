# hospitalmanagement_python
Hospial Management using **mysql.connector** in python, with **streamlit** library

# installing Requirements
```
pip install mysql-connector-python  # for MySQL-Python connection
pip install streamlit               # to use streamlit library
pip install streamlit-extras        # for switching/redirecting pages
pip install pandas                  # for using pandas to fetch data as dataframe ans display as streamlit table
pip install streamlit-authenticator # to use authentication in streamlit, but not used yet

```
# command to run project
```
streamlit run index.py
streamlit run https://github.com/jamwalshah/hospitalmanagement_python/index.py
```
# Problem Statement
To convert traditional hospital management system which can
	handle mapping for hospital resources (doctor & nurse) to patients admitted 
	in the hospital, so that it becomes hassle-free for reception staff 
	as well as the higher management of hospital to track doctors, nurses & patients
  
# Objective
<ol>
  <li> implement a role based hospital management system </li>
	<li> signup not allowed as this app needs to be restricted to assigned users only </li>
  <li> patients & nurses not allowed to login </li>
  
  ---
  
  | Role | Access Level |
  | :--- | :---        |
  | admin | has all access for R/W of docs, nurses, patients | 
  | doctor | has access to view patients only | 
  | manager | has access to only view staff members in hospital viz. Doctors & nurses | 
  | receptionist | has access to admit and discharge the patients while mapping them to allocated doctor & nurse | 
  | tpa | has access to view patients only | 
  
</ol>

# Roles
| role		 | user	 | doctor	 | nurse	 | patient	 | 
| :--- | :---: | :---: | :---:	 | :---: | 
| admin		 | CRUD	 | CRUD		 | CRUD		 | CRUD		 | 
| doctor	 | ----	 | ----		 | ----		 | -R-- 	 | 
| manager	 | ----	 | -R--		 | -R--		 | ----		 | 
| receptionist	 | ----	 | -R--		 | -R--		 | CRUD		 | 
| tpa		 | ----	 | ----		 | ----		 | -R--		 | 
