import sqlite3
import pandas as pd


# Connecting to database and extracting data into from each table into a dataframe
conn = sqlite3.connect('C:\\Users\\Luke Edgar\\OneDrive\Documents\\db.sqlite3')
SurvR_df = pd.read_sql_query ('SELECT * FROM surveys_response',conn)

SurvQT_df2 = pd.read_sql_query('SELECT questionTextID, factorID_id, positive_p FROM surveys_question_text',conn)

SurvS_df3 = pd.read_sql_query('SELECT surveyID, userID_id, creationDate, completionDate FROM surveys_survey', conn)

SurvF_df4 = pd.read_sql_query('SELECT factorID , factorName , studyID_id FROM surveys_factor', conn)

SurvQ_df5= pd.read_sql_query ('SELECT questionID, questionTextID_id, surveyID_id FROM surveys_question',conn)

SurvU_df6 = pd.read_sql_query ('SELECT userID, userGroup, age, location, hireDate FROM surveys_user', conn)

conn.close()

# Changing the column names of dataframes to merge all dataframes
SurvR_df = SurvR_df.rename(columns = {"questionID_id" : "questionID"})
SurvQT_df2 = SurvQT_df2.rename (columns = {"questionTextID_id" : "questionTextID", "factorID_id" : "factorID"})
SurvS_df3 = SurvS_df3.rename (columns = {"factorID_id" : "factorID", "userID_id" : "userID"})
SurvF_df4 = SurvF_df4.rename (columns = {"surveyID_id" : "surveyID"})
SurvQ_df5 = SurvQ_df5.rename (columns = {"questionTextID_id": "questionTextID" , "surveyID_id" : "surveyID"})


# Merging dataframes into a single data warehouse called dw_df
dw_df1 = pd.merge(SurvR_df, SurvQ_df5, on = 'questionID', how = 'inner')
dw_df2 = pd.merge(SurvQT_df2, dw_df1, on = 'questionTextID', how = 'inner')
dw_df3 = pd.merge(SurvS_df3, dw_df2, on = 'surveyID', how = 'inner')
dw_df4 = pd.merge(SurvF_df4, dw_df3, on = 'factorID', how = 'inner')
dw_df = pd.merge(SurvU_df6, dw_df4, on = 'userID', how = 'inner')
                                            

#Changing response column into a numeric datatype

dw_df['response'] = pd.to_numeric(dw_df['response'], errors= 'coerce').astype('Int64')

# Flipping values in response where positive_p is 0 so that they are negative values

dw_df.loc[dw_df['positive_p']==0,['response']] = 6 - dw_df.loc[dw_df['positive_p']==0,['response']]

# Changing creationDate column to a datetime data type
dw_df['creationDate'] = pd.to_datetime(dw_df['creationDate'])

# creating dataframe into a csv document 
data_warehouse = dw_df.to_csv('C:\\Users\\Luke Edgar\\OneDrive\Documents\\CSC_486_DataMiningMethods\\data_warehouse.csv', mode = 'a', index = False)



