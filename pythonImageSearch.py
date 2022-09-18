from statistics import median, stdev
from urllib import response
import requests
import urllib
 


completeURL = ''
totaloccurence = 0
#format https://www.googleapis.com/customsearch/v1?key=AIzaSyBbjulpjDiA0pD6dQ44x1PpghtO63kcjvU&cx=d40bbed7650794c73&q=https://i.imgur.com/HBrB8p0.png

# 'https://animecorner.me/wp-content/uploads/2022/08/chisato_lr_ep_7.png'
tmpurl = 'https://www.googleapis.com/customsearch/v1?'
 
def image_search(q):
   
    params = {
        'key': 'AIzaSyBbjulpjDiA0pD6dQ44x1PpghtO63kcjvU',
        'cx': 'd40bbed7650794c73',
        'searchType': 'image',
        'filter': 0,
        'maxResults': 20,
        'pageSize': 2,
        'q': q #+ '-filetype:'+ filetype,
        
    }

    print("Image URL: " + q)
    completeURL = tmpurl+urllib.parse.urlencode(params)
       
        
    with urllib.request.urlopen(completeURL) as url:
        
        myfile = url.read()

        with open("search.json","wb") as binary_file: 
            binary_file.write(myfile)           

        binary_file.close()


    
    return completeURL

def get_title_data(url):
    import requests, json
    
    response = json.loads(requests.get(url).content)
    title_data = [item.get("title", None).encode("utf-8") for item in response["items"]]
    #print(title_data)
    return title_data


def off_line_get_title_data():
    import requests, json
    
    f = open('search.json', 'rb')
    response = json.load(f)
    title_data = [item.get("title", None).encode("utf-8") for item in response["items"]]
    #print(title_data)
    #print("title data type: ", type(title_data[0]))
    
    return title_data

def search_youtube(title):
    
    youtubeparams = {
        'key': 'AIzaSyBbjulpjDiA0pD6dQ44x1PpghtO63kcjvU',
        'cx': 'd40bbed7650794c73',
        'relatedSite': 'www.youtube.com/*',
        'q': title #+ '-filetype:'+ filetype,
    }
    completeURL = tmpurl+urllib.parse.urlencode(youtubeparams)
        
    with urllib.request.urlopen(completeURL) as url:
        
        myfile = url.read()

        with open("search_youtube.json","wb") as binary_file: 
        
            binary_file.write(myfile)           

        binary_file.close()

 
def repeatsSubstring(string):
    import re
    
    for x in range(1, len(string)):
        substring = string[:x]

        if substring * (len(string)//len(substring))+(substring[:len(string)%len(substring)]) == string:
            #print(substring)
            return "break"

    #print(string)

def freq(str):
    import re
    import pandas as pd
    
    # break the string into list of words
    str = str.split()        
    str2 = []
    
    #split string with special char
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    for i in str:
        if regex.search(i):
            #print("find bitches : ", i)
            s = re.split(r'\W',i)
            str = str + s
            str.remove(i)
        
    
    # loop till string values present in list str
    for i in str:            
        # checking for the duplicacy
        if i not in str2 and i != '':
            # insert value in str2
            str2.append(i)
              

    median_query = []
    output_query = []
  
    for i in range(0, len(str2)):
        # count the frequency of each word(present
        # in str2) in str and print
        print('Frequency of', str2[i], '= ', str.count(str2[i]))
        median_query.append(str.count(str2[i]))
        
     
    for i in range(0, len(str2)):
        for j in range(0, len(str2)):
            if str2[i] in str2[j] and i !=j:
                #print("string: ", str2[j] , "substring: " , str2[i])
                median_query[i] = median_query[i] +  median_query[j]

    
    #print(median_query[0])

    #check any substring are contains in str2
   # for i in range(0, len(str2)):
    #print(str2)
    mean = int(sum(median_query) / len(str2))
    stat = (( median(median_query) + stdev(median_query) )+ (median(median_query) + stdev(median_query)) )/ mean
    print("stat: ",stat)
    for i in range(0, len(str2)):
        if  median_query[i] > int(stat) and str2[i].isalpha():
            output_query.append(str2[i])
            
    #print("median: ", int(mean + stdev(median_query)))
    
    
    print("output query = " , output_query)
 
            
   
    
def title_frequency(title_array):
     
    arr = b''.join(title_array).decode('utf-8')
    freq(arr)
    
    
def off_line_search():
    title_frequency(off_line_get_title_data())
    
def on_line_search():
    completeURL = image_search("https://upload.wikimedia.org/wikipedia/en/thumb/8/87/CUHK.svg/1200px-CUHK.svg.png")
    title_frequency(get_title_data(completeURL))
    #search_youtube(get_title_data(completeURL)[0])

#off_line_search()
on_line_search()

