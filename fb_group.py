#!/usr/bin/env python

# from bs4 import BeautifulSoup
import requests
import json
from pyfacebook import GraphAPI
 
def read_creds(filename):
    '''
    Store API credentials in a safe place.
    If you use Git, make sure to add the file to .gitignore
    '''
    with open(filename) as f:
        credentials = json.load(f)
    return credentials
 
credentials = read_creds('credentials.json')
graph = GraphAPI(access_token=credentials['access_token'])
data=[]
# with open("data.txt", "r") as post:
    # data=post.readlines()
# for post in data:            
# graph.post_object(object_id="group id", connection="photos",data={"message": "#hacker #hacking","link":})
graph.post_object(object_id="1481356368863712", connection="photos",data={"caption":"#hacker", "message":"Posted by python", "url":"https://wallpaperaccess.com/full/6866658.png"})
