from firebase import firebase
url="https://penguinpro-XXXXX.firebaseio.com/"
firebase= firebase.FirebaseApplication(url)

cTemp="Hello Xyz"
fTemp="97"
humidity="98%"
result = firebase.post(url, {'cTemp':str(cTemp),'ftemp':str(fTemp), 'humidity':str(humidity)})

