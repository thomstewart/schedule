import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# authenticate with the database
cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred, {
  'projectId': 'schedules-10e1f',
})

db = firestore.client()

#insert docs into database
doc_ref = db.collection(u'classes')
doc_ref.add({
    u'course': u'cse310',
    u'department': u'cse',
    u'time': u'7:45',
    u'instructor': u'Brother Macbeth'
})

doc_ref.add({
    u'course': u'cse310',
    u'department': u'cse',
    u'time': u'3:15',
    u'instructor': u'Brother Macbeth'
})

doc_ref.add({
    u'course': u'cs225',
    u'department': u'cs',
    u'time': u'3:15',
    u'instructor': u'Brother McLaughlin'
})

doc_ref.add({
    u'course': u'cs213',
    u'department': u'cs',
    u'time': u'10:15',
    u'instructor': u'Brother Phillips'
})
  
doc_ref.add({
    u'course': 'math335',
    u'department': u'math',
    u'time': u'9:00',
    u'instructor': u'Brother Nelson'
})

doc_ref.add({
    u'course': u'rel235',
    u'department': u'rel',
    u'time': u'11:30',
    u'instructor': u'Brother Johnson'
})


