# simple grade converter in python
grade_converter = raw_input('Enter Test score: ')
if int(grade_converter) >= 90:
  print ("A")
elif int(grade_converter) >= 80:
  print ("B")
elif int(grade_converter) >= 70:
  print ("C")
elif int(grade_converter) >= 65:
  print ("D")
else:
  print ("F")

