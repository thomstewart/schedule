import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# authenticate with the database
cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred, {
  'projectId': 'schedules-10e1f',
})

db = firestore.client()

inp = input('What would you like to do? (insert, update, delete, or display): ')

if inp == 'insert':
    course = input('course: ')
    dep = input('department: ')
    time = input('time: ')
    ins = input('Instructor: ')
    #insert docs into database
    doc_ref = db.collection(u'classes')
    doc_ref.add({
        u'course': course,
        u'department': dep,
        u'time': time,
        u'instructor': ins
    })
elif inp == 'update':
    old_course = input('Current course name: ')
    old_time = input('Current time: ')
    db.collection(u'classes').document().where(u'course', u'==', old_course).where(u'course', u'==', old_time)

    
elif inp == 'delete':
    course = input("course: ")
    time = input("time: ")
    #doc_id = 
    db.collection(u'classes').document().where(u'course', u'==', course).where(u'course', u'==', time).delete()
    
elif inp == 'display':
    print(db.collection("classes").get())
    for i in db.collection("classes").get():
        print(i.course, i.department, i.time, i.instructor)
