import pandas as pd
import sys
from start.models import Topic,UploadTopics
i=0
workbook = pd.read_excel('uploads\media\sample.xlsx',engine='openpyxl')
#workbook.head()


while(i<10):
    q=Topic(topic_name=workbook['TOPICS'].iloc[i])
    q.save()
    i+=1

#print(workbook)