
from firebase import firebase

def saveMACin_blacklist(MAC):
<<<<<<< HEAD
    _firebase = firebase.FirebaseApplication('https://safewifi-a7dc0.firebaseio.com', None)
    g = { str(MAC): 'Suspected' }
    _firebase.delete('/ARP_MAC_BlackList/' + MAC,None) 
    _firebase.patch('/ARP_MAC_BlackList',g)   
=======
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

>>>>>>> 2900a8f523a076976fc88448a39cc961cdd30e2f

