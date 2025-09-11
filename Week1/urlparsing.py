URL=input("Enter a URL:")
Protocol= URL[ :URL.find(':')]
d1= URL.find('.')
d2= URL.find('.', d1+1)
Domain=URL[d1+1:d2]
Page=URL[URL.find('/', d2) :]
print('Protocol is:', Protocol)
print('Domain is:', Domain)
print('Page is:', Page)