import matplotlib.pyplot as plt
import pandas as pd

dw_dfcsv = pd.read_csv('C:\\Users\\Luke Edgar\\OneDrive\\Documents\\CSC_486_DataMiningMethods\\data_warehouse.csv') 
sub_dwdf = dw_dfcsv[dw_dfcsv['studyID_id'] == 3]
sub_dwdf['creationDate'] = pd.to_datetime(sub_dwdf['creationDate'])
plt.hist(sub_dwdf['response'])
plt.show()

respmeans = sub_dwdf.groupby( [ 'creationDate' , 'factorID' , 'factorName' ], as_index=False ).mean().loc[:,['creationDate', 'factorID' , 'response' , 'factorName' ] ]

factor11 = respmeans[respmeans['factorID'] == 11]
factor12 = respmeans[respmeans['factorID'] == 12]
factor13 = respmeans[respmeans['factorID'] == 13]
factor14 = respmeans[respmeans['factorID'] == 14]
factor15 = respmeans[respmeans['factorID'] == 15]

timeseries= plt.figure()
ax = timeseries.add_subplot(1,1,1)
plt.title("Mean responses for factorID 11")
ax.plot(factor11['creationDate'], factor11['response'], '-k')
timeseries.show()

timeseries= plt.figure()
ax = timeseries.add_subplot(1,1,1)
plt.title("Mean responses for factorID 12")
ax.plot(factor12['creationDate'], factor12['response'], '-b')
timeseries.show()

timeseries= plt.figure()
ax = timeseries.add_subplot(1,1,1)
plt.title("Mean responses for factorID 13")
ax.plot(factor13['creationDate'], factor13['response'], '-r')
timeseries.show()

timeseries= plt.figure()
ax = timeseries.add_subplot(1,1,1)
plt.title("Mean responses for factorID 14")
ax.plot(factor14['creationDate'], factor14['response'], '-g')
timeseries.show()

timeseries= plt.figure()
ax = timeseries.add_subplot(1,1,1)
plt.title("Mean responses for factorID 15")
ax.plot(factor15['creationDate'], factor15['response'], '-c')
timeseries.show()