import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)


# Normal GET requests
response = requests.get('https://httpbin.org/get')

print(response)
#print(response.content)
#print(response.text)


print(type(response.json()))
pp.pprint(response.json())

# Downloading Files
# img = requests.get('https://www.skymetweather.com/content/wp-content/uploads/2020/03/Uttar-Pradesh-rains-1200-1.jpg')
# # print(img.content)

# with open('varsha.jpg','wb') as image:
#     image.write(img.content)


# Normal POST requests
post_r = requests.post('https://httpbin.org/post', data = {'some':'none'})
print(type(post_r.json()))
pp.pprint(post_r.json())
