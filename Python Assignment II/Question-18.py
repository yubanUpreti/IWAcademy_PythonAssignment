import json

print(json.__dir__())
print('')
print(json.__doc__)
print('')


dictionary_data = {'name':'Youban Uprety', 'age':'26'}

json_data = json.dumps(dictionary_data)

print('')
print(f"Python Dictionary Converted to  JSON : {json_data}")
print('')

python_data = json.loads(json_data)
print('')
print(f"JSON Converted to  Python Dictionary : {python_data}")
print('')


