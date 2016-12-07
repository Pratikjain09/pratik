
# coding: utf-8

# In[215]:

import itertools


# In[216]:

import pandas as pd
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
f1_read = open( "sap-efrei-spring-2016.txt", "r" )
f11_read = open( "sap-efrei-spring-2016.txt", "r" )
f2_read = open( "data-visualization.txt", "r" )
f22_read = open( "data-visualization.txt", "r" )
f3_read = open( "moderndatabases-monsoon16.txt", "r" )
f33_read = open( "moderndatabases-monsoon16.txt", "r" )

f1_write_commits=open("commit1.txt","a")
f1_write_Date=open("date1.txt","a")
f2_write_commits=open("commit2.txt","a")
f2_write_Date=open("date2.txt","a")
f3_write_commits=open("commit3.txt","a")
f3_write_Date=open("date3.txt","a")


# In[217]:

def Text_Filter(f):
    f=pd.DataFrame(f.readlines())
    f=f.replace('\n','',regex=True)
    data=['commit','Author','Date']
    filter = f[0] != ""
    dfNew = f[filter]  
    dfNew = dfNew.rename(columns={0:'Messages'})
    a=[]
    for i,j in enumerate(dfNew['Messages']):
        if not any(unwanted_words in j for unwanted_words in data):
            a.append(j)
            
    a=pd.DataFrame(a)
    a = a.rename(columns={0:'Messages'})
    return(a)


# In[218]:

s1=Text_Filter(f1_read)
s2=Text_Filter(f2_read)
s3=Text_Filter(f3_read)


# In[219]:

for (msg1,msg2,msg3) in itertools.product(s1['Messages'],s2['Messages'],s3['Messages']):
    f1_write_commits.write(msg1)
    f2_write_commits.write(msg2)
    f3_write_commits.write(msg3)


# In[ ]:




# In[ ]:




# In[220]:

def Text_Filter(f):
    f=pd.DataFrame(f.readlines())
    f=f.replace('\n','',regex=True)
    data=['Date']
    filter = f[0] != ""
    dfNew = f[filter]  
    dfNew = dfNew.rename(columns={0:'Date'})
    a=[]
    for i,j in enumerate(dfNew['Date']):
        if any(unwanted_words in j for unwanted_words in data):
            a.append(j)
            
    a=pd.DataFrame(a)
    a = a.rename(columns={0:'Date'})
    return(a)


# In[221]:

h1=Text_Filter(f11_read)
h2=Text_Filter(f22_read)
h3=Text_Filter(f33_read)


# In[222]:

for (date1,date2,date3) in itertools.product(h1['Date'],h2['Date'],h3['Date']):
    f1_write_Date.write(date1)
    f2_write_Date.write(date2)
    f3_write_Date.write(date3)


# In[ ]:




# In[223]:

file1=open("commit1.txt")
file2=open("commit2.txt")
file3=open("commit3.txt")



# In[224]:

def word_count(file):
    wordcount={}
    for word in file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    for k,v in wordcount.items():
        print( k, v)


# In[225]:

word_count(file1)


# In[226]:

word_count(file2)


# In[227]:

word_count(file3)


# In[228]:

h1


# In[229]:

h2


# In[230]:

h3


# In[231]:

def Text_Filter(f):
    data=['Sun','Sat'] 
    dfNew = f.rename(columns={'Date':'Weekdays'})
    a=[]
    for i,j in enumerate(dfNew['Weekdays']):
        if not any(unwanted_words in j for unwanted_words in data):
            a.append(j)
            
    a=pd.DataFrame(a)
    a = a.rename(columns={0:'Weekdays'})
    return(a)


# In[232]:

def Text_Filter2(f):
    data=['Sun','Sat'] 
    dfNew = f.rename(columns={'Date':'Weekends'})
    a=[]
    for i,j in enumerate(dfNew['Weekends']):
        if any(unwanted_words in j for unwanted_words in data):
            a.append(j)
            
    a=pd.DataFrame(a)
    a = a.rename(columns={0:'Weekends'})
    return(a)


# In[233]:

def Text_Filter3(f):
    data=['Tue','Wed','Thu'] 
    dfNew = f.rename(columns={'Date':'Mid-Week days'})
    a=[]
    for i,j in enumerate(dfNew['Mid-Week days']):
        if any(unwanted_words in j for unwanted_words in data):
            a.append(j)
            
    a=pd.DataFrame(a)
    a = a.rename(columns={0:'Mid-Week days'})
    return(a)


# In[234]:

def Text_Filter4(f):
    data=['Tue','Wed','Thu'] 
    dfNew = f.rename(columns={'Date':'other_days'})
    a=[]
    for i,j in enumerate(dfNew['other_days']):
        if not any(unwanted_words in j for unwanted_words in data):
            a.append(j)
            
    a=pd.DataFrame(a)
    a = a.rename(columns={0:'other_days'})
    return(a)


# In[235]:

Weekdays1=Text_Filter(h1)
Weekends1=Text_Filter2(h1)
Mid_Weekdays_1=Text_Filter3(h1)
Other_days_1=Text_Filter4(h1)

Weekdays2=Text_Filter(h2)
Weekends2=Text_Filter2(h2)
Mid_Weekdays_2=Text_Filter3(h2)
Other_days_2=Text_Filter4(h2)

Weekdays3=Text_Filter(h3)
Weekends3=Text_Filter2(h3)
Mid_Weekdays_3=Text_Filter3(h3)
Other_days_3=Text_Filter4(h3)


# ## Weekdays and Weekends Counts for SAP

# In[236]:

sap=pd.DataFrame([[len(Weekdays1),len(Weekends1)]])
sap=sap.rename(columns={0:'Weekdays',1:'Weekends'})
sap


# # Difference in the midweek days commits and other days for SAP

# In[237]:

sap1=pd.DataFrame([[len(Mid_Weekdays_1),len(Other_days_1)]])
sap1=sap1.rename(columns={0:'Mid_Weekdays',1:'Other_days'})
sap1


# # Weekdays and Weekends Counts for Data Visualization

# In[238]:

data_viz=pd.DataFrame([[len(Weekdays2),len(Weekends2)]])
data_viz=data_viz.rename(columns={0:'Weekdays',1:'Weekends'})
data_viz


# ## Difference in the midweek days commits and other days for Data Visualization

# In[239]:

data_viz1=pd.DataFrame([[len(Mid_Weekdays_2),len(Other_days_2)]])
data_viz1=data_viz1.rename(columns={0:'Mid_Weekdays',1:'Other_days'})
data_viz1


# ## Weekdays and Weekends Counts for Modern Databases

# In[240]:

mdb=pd.DataFrame([[len(Weekdays3),len(Weekends3)]])
mdb=mdb.rename(columns={0:'Weekdays',1:'Weekends'})
mdb


# ## Difference in the midweek days commits and other days for Modern Databases

# In[241]:

mdb1=pd.DataFrame([[len(Mid_Weekdays_3),len(Other_days_3)]])
mdb1=mdb1.rename(columns={0:'Mid_Weekdays',1:'Other_days'})
mdb1


# In[ ]:




# In[ ]:




# In[ ]:



