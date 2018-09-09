
from firebase import firebase

def saveMACin_blacklist(MAC):
    if not check_if_mac_in_blacklist(MAC):
        return

    _firebase = firebase.FirebaseApplication('https://safewifi-a7dc0.firebaseio.com', None)
    result = _firebase.post('/MAC_BlackList', MAC)

def check_if_mac_in_blacklist(MAC):
    _firebase = firebase.FirebaseApplication('https://safewifi-a7dc0.firebaseio.com', None)
    result = _firebase.get('/MAC_BlackList', None)
    if result == None:
        return True
    else:
        return False


