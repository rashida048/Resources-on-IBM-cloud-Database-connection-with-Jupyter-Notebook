#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[2]:


import ibm_db_sa


# In[3]:


get_ipython().run_line_magic('sql', 'ibm_db_sa://tft75821:zqclf4b487vwx^4h@dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net/BLUDB')


# In[4]:


#retrieve first 10 rows of the crime data table
get_ipython().run_line_magic('sql', 'select * from chicago_crime limit 10')


# In[5]:


#Number of crimes recorded in the Crime data table
get_ipython().run_line_magic('sql', 'select count(*) from chicago_crime')


# In[6]:


#How many crimes involved an arrest
get_ipython().run_line_magic('sql', 'select count(*) from chicago_crime where arrest = True')


# In[7]:


get_ipython().run_line_magic('sql', "select community_area_name from chicago_socioeconomic_data where community_area_name like 'B%'")


# In[8]:


get_ipython().run_line_magic('sql', 'select * from chicago_socioeconomic_data limit 5')


# In[30]:


#Which schools in Community Areas 10 to 15 are healthy school certified?
get_ipython().run_line_magic('sql', "select name_of_school, community_area_number from school where community_area_number BETWEEN 10 and 15 AND healthy_school_certified='Yes'")


# In[23]:


get_ipython().run_line_magic('sql', 'select * from school limit 5')


# In[11]:


#What is the average school Safety Score?
get_ipython().run_line_magic('sql', 'select avg(safety_score) from school')


# In[12]:


#List the top 5 Community Areas by average College Enrollment [number of students]
get_ipython().run_line_magic('sql', 'select community_area_name, college_enrollment from school order by college_enrollment desc limit 5')


# In[13]:


#Use a sub-query to determine which Community Area has the least value for school Safety Score?
get_ipython().run_line_magic('sql', 'select community_area_name, safety_score from school where safety_score = (select min(safety_score) from school)')


# In[16]:


get_ipython().run_cell_magic('sql', '', 'select per_capita_income_ \n   from chicago_socioeconomic_data CD, school CPS \n   where CD.ca = CPS.community_area_number \n      and safety_score = 1')


# In[15]:


get_ipython().run_line_magic('sql', 'select * from chicago_socioeconomic_data limit 5')


# In[ ]:




