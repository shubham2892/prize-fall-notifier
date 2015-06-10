#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from gi.repository import Notify
from time import sleep


url = "http://www.amazon.in/gp/offer-listing/B00VBH9G8S/ref=dp_olp_new?ie=UTF8&condition=new"
threshold_prize = 95000

print("Fetching rates..")
while True:
  try:
    r = requests.get(url)
    while r.status_code is not 200:
      sleep(2)
      r = requests.get(url)

    soup = BeautifulSoup(r.text)
    data = soup.find("span",{"style":"text-decoration: inherit; white-space: nowrap;"}).contents[2]
    data_int = float(data.replace(',',''))
    
    if data_int < threshold_prize:
    	Notify.init("Scorer")
    	scorer = Notify.Notification.new("mac Book Pro Amazon:", data, "dialog-information")
    	scorer.show()
    
    sleep(500)

  except KeyboardInterrupt:
      break;
    
