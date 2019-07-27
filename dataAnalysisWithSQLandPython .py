#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[3]:


import sqlalchemy


# In[2]:


import ibm_db_sa


# In[3]:


get_ipython().run_line_magic('sql', 'ibm_db_sa://tft75821:zqclf4b487vwx^4h@dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net/BLUDB')


# In[4]:


import pandas


# In[5]:


#You can verify that the table creation was successful by retrieving the list of all tables in your schema and checking whether the SCHOOLS table was created


# Query system catalog to get a list of tables and their properties: 

# In[7]:


get_ipython().run_line_magic('sql', 'select * from syscat.tables')


# In[13]:


get_ipython().run_line_magic('sql', "select TABSCHEMA, TABNAME, CREATE_TIME from syscat.tables where tabschema not in ('sysibm', 'syscat', 'sysstat', 'sysibmdb', 'systools', 'systools')")


# In[17]:


get_ipython().run_line_magic('sql', "select * from syscat.tables where tabname = 'school'")


# In[16]:


#The SCHOOLS table contains a large number of columns. How many columns does this table have?


# In[18]:


get_ipython().run_line_magic('sql', "select * from syscat.columns where tabname = 'school'")


# In[23]:


get_ipython().run_line_magic('sql', "select distinct(NAME), COLTYPE, LENGTH from SYSIBM.SYSCOLUMNS where TBNAME = 'SCHOOL'")


# In[24]:


#How many Elementary Schools are in the dataset?


# In[26]:


get_ipython().run_line_magic('sql', 'select count(*) from school  where "Elementary, Middle, or High School" = \'ES\'')


# If the column name have mixed cases, double quote should used, otherwise it will give an error

# In[27]:


get_ipython().run_line_magic('sql', 'select max(safety_score) from school')


# In[28]:


#Which schools have highest Safety Score?
get_ipython().run_line_magic('sql', 'select name_of_school from school where safety_score = (select max(safety_score) from school)')


# In[29]:


#What are the top 10 schools with the highest "Average Student Attendance"?
get_ipython().run_line_magic('sql', 'select name_of_school, average_student_attendance from school order by average_student_attendance desc nulls last limit 10')


# In[31]:


#Retrieve the list of 5 Schools with the lowest Average Student Attendance sorted in ascending order based on attendance
get_ipython().run_line_magic('sql', 'select name_of_school, average_student_attendance from school order by average_student_attendance nulls last limit 5')


# In[32]:


get_ipython().run_line_magic('sql', 'select name_of_school, average_student_attendance from school order by average_student_attendance fetch first 5 rows only')


# In[33]:


#Now remove the '%' sign from the above result set for Average Student Attendance column
get_ipython().run_line_magic('sql', "select name_of_school, replace(average_student_attendance, '%', '') from school order by average_student_attendance fetch first 5 rows only")


# In[35]:


#Which Schools have Average Student Attendance lower than 70%?
get_ipython().run_line_magic('sql', "select name_of_school, average_student_attendance from school where average_student_attendance < '70%'")


# In[40]:


#Get the total College Enrollment for each Community Area
total_enrollment = get_ipython().run_line_magic('sql', 'select community_area_name, sum(college_enrollment) as total_enrollment from school group by(community_area_name)')


# In[41]:


total_enrollment


# In[42]:


#Get the 5 Community Areas with the least total College Enrollment sorted in ascending order
get_ipython().run_line_magic('sql', 'select community_area_name, sum(college_enrollment) as total_enrollment from school group by(community_area_name) order by total_enrollment fetch first 5 rows only')


# In[90]:


#Get the hardship index for the community area which has College Enrollment of 4638
get_ipython().run_line_magic('sql', 'select hardship_index from chicago_socioeconomic_data as CD inner join school as CPS on CD.ca = CPS.community_area_number where college_enrollment = 4368')


# In[77]:


get_ipython().run_line_magic('sql', 'select college_enrollment from school order by college_enrollment desc limit 1')


# In[97]:


get_ipython().run_line_magic('sql', 'select ca, community_area_name, hardship_index from chicago_socioeconomic_data    where ca in    ( select community_area_number from school order by college_enrollment desc limit 1 )')


# In[99]:


get_ipython().run_cell_magic('sql', '', 'select hardship_index \n   from chicago_socioeconomic_data CD, school CPS \n   where CD.ca = CPS.community_area_number \n      and college_enrollment = 4368')


# In[ ]:




