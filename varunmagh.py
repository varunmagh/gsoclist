import requests
import json
import csv
import io

students_list = []
i = 1
# We run through the API and through it's every page to scrape records (100 per page)
while i<=15:
    #URL of the API - (Exposed by the GSoC website)
    url = "https://summerofcode.withgoogle.com/api/program/current/project/?page={}&page_size=100".format(i)
    
    #JSONContent stores the data in a list
    JSONContent = requests.get(url).json()
    
    #Dictionary to store records
    temp = {}

    j = 1
    #Loop for scraping all the records on the page
    while j<=100:
        #Checking if the j is not greater than length of JSONContent
        if not (0 <= j <= len(JSONContent['results'])): 
            j=-1
            print("End has reached")
            break
        if 'error' not in JSONContent:
            #Storing the record in dictionary with keys
            temp = {'Name' : JSONContent['results'][j-1]['student']['display_name'],'Organization' : JSONContent['results'][j-1]['organization']['name'],'Project' : JSONContent['results'][j-1]['organization']['precis']}
        else:
            j = -1
            print("End has reached")
            break
        #Adding the dictionary in students_list
        students_list.append(temp)
        j += 1

    if j==-1 :
        break   
    i+=1

keys = students_list[0].keys()
#keys for csv file writing

with io.open("output1.csv", "w", encoding="utf-8") as a_file:
    dict_writer = csv.DictWriter(a_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(students_list)
a_file.close()