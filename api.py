import requests
#api="https://fakestoreapi.com/products/1"
#data=requests.get(api)
#print(data.json())




#res=requests.get("https://jsonplaceholder.typicode.com/posts")
#print(res.json())
#res=res.json()
#for post in res:
#    print(post.get("id"))

api="http://localhost:3000/mobiles"
#send_data={
#    "userId":10,
#    "id":101,
#    "title":"new post",
#    "body":"this is sample text from python"}



#import json
#send_data={"id":'2',"name":"iphone","ram":"6gb","processor":"a18"}
#json_data=json.dumps(send_data)
#res=requests.post(api,data=json_data)
#print(res)
#print(res.json())






import json
new_mobile={"id":"3","name":"s26","ram":"12","processor":"sdgen8 elite"}
json_data=json.dumps(new_mobile)
res=requests.post(api,data=json_data)
print(res.json())
 