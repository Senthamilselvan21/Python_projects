"""
syntax: dictname={key1:data1,key2:data2,........keyn:datan}
    dictname={} --empty dictionary
"""

empdetails={'name':'muniraj','empid':900,'salary':5000}
print(empdetails['name'])
empdetails['name']='raman'
print(empdetails)
keys=empdetails.keys()
print(keys)
values=empdetails.values()
print(values)
ename=empdetails.get('name')
print(ename)
print(empdetails.pop('salary'))

pdata=empdetails.items()
print(pdata)
print(empdetails.popitem())
print(empdetails)
print(empdetails.clear())
print(empdetails)
del empdetails
#print(empdetails)




