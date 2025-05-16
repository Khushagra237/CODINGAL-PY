student_data = {'id1': {'name': ['Sara'], 'class': ['V'], 
'subject_integration' : ['Math', 'Science', 'English']},
'id2':
{'name': ['Sara'], 'class': ['V'],
'subject_integration' : ['Math', 'Science', 'English']},
'id3':
{'name': ['Vartika'], 'class': ['V'],
'subject_integration' : ['Math', 'Science', 'English']},
'id4':
{'name': ['Surya'], 'class': ['V'],
'subject_integration' : ['Math', 'Science', 'English']},
}

result = {}
for key, value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result) 
    