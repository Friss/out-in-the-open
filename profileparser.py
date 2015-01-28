from bs4 import BeautifulSoup
from ftfy import fix_text
import json
import requests

def parseProfile(profileUrl):
  r  = requests.get(profileUrl)

  if len(r.history):
    # Hit a non existant profile.
    # They redirect 302 when a profile doesn't exist
    return None

  responseText = r.text
  soup = BeautifulSoup(responseText)

  data = {}

  data['profile_url'] = profileUrl

  data['name'] = soup.find('h1', id="profile-name").text
  data['about'] = soup.find('div', class_="quick-about").text

  data['picture'] = soup.find('img', class_="img-responsive")['src']

  collections = ["vital_medical_conditions", "emergency_contacts", "allergies", "physicians", "insurance_informations", "other_informations"]

  for collection in collections:
    collectionArray = []
    infoDiv = soup.find('div', collection=collection)
    if infoDiv:
      for infoRow in infoDiv.find_all("div", class_="row"):
        infoRowDict = {}
        for info in infoRow.find_all("h5"):
          information = fix_text(info.parent.text).split(':')
          if len(information) == 2:
            infoRowDict[information[0].replace(" ", "_").lower()] = information[1]
          else:
            # Insurace information's name doesn't have a ':'
            infoRowDict['name'] = information[0].replace('Name', '')

        if len(infoRowDict):
          collectionArray.append(infoRowDict)

    data[collection] = collectionArray


  ###
  # Personal Info doesn't have a collection and they use the 'emergency-contacts-pane' class twice so little hack around
  ###
  personalinfo = soup.find('div', class_="personal-info-pane")
  collectionArray = []
  infoRow = {}
  for info in personalinfo.find_all("h5"):
    information = fix_text(info.parent.text).split(':')
    infoRow[information[0].replace(" ", "_").lower()] = information[1]
  collectionArray.append(infoRow)

  data['personal_info'] = collectionArray

  return data


def main():
  data = {'profiles': []}

  x = 1
  urlBase = "https://www.example.com/profile/"
  while(x < 20700):
    profile = parseProfile(urlBase+str(x))
    if profile:
      data['profiles'].append(profile)
    else:
      print("Profile %s doesn't exist!" % x)
      break
    x+=1
  print json.dumps(data, sort_keys=True)

main()
