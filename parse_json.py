import json
  
# # JSON string
# employee ='{"id":"09", "name": "Nitin", "department":"Finance"}'
  
# # Convert string to Python dict
# employee_dict = json.loads(employee)
# print(employee_dict)
  
# print(employee_dict['name'])


with open("sample-1.json","r") as s1i:
    data = json.load(s1i)

va = data["a"]
vc = va["c"]

# print(f"1st va {va}")
# print(f"1st vc {vc}")

vc = 50

v2 = vc

del va["c"]
#print(f"2nd vc {vc}")

va["akki"] = 50

print(data)
# print(va)
# print(vc)
# print(v2)
# print(type(data))

# For creating and saving data to a new file
with open("sample-1-changed.json","w") as s1o:
    s1o.write(json.dumps(data))

# For saving data to the existing input file
# with open("sample-1.json","w") as s1o:
#     s1o.write(json.dumps(data))
