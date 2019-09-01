#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import json
import time


# In[ ]:


#image, label, likes, text, hashtag
category = {"nature-scene": ["beach", "cave", "island", "lake", "mountain"],
            "person-made": ["amusement park", "palace", "park", "restaurant", "tower"]}


# In[ ]:


train_start = 1
train_end = 701


# In[ ]:


valid_start = 701
valid_end = 801


# In[ ]:


test_start = 801
test_end = 1001


# In[ ]:


def delete_data(start, end):
    for key, val in category.items():
        for v in val:
            print(v)
            print(" read data ")     

            json_dir = key + "/" + v + "/" + v + ".json"
            img_dir = key + "/" + v + "/images/"

            with open(json_dir, encoding='UTF-16') as f:
                data = json.load(f)
            f.close()        

            print(" delete json data")
            data = data[start-1 : end-1]

            print(" delete image file")

            for cnt in range(1, 1001):
                if cnt < start or end <= cnt: 
                    os.remove(img_dir + str(cnt) + ".jpg")

            print(" save .json file")
            with open(json_dir, mode='w', encoding='UTF-16', errors='ignore') as f:
                feed = json.dumps(data, ensure_ascii=False, indent=2)
                f.write(feed)


# In[ ]:


mode = input()
start = 0
end = 0

if mode == "train":
    delete_data(train_start, train_end)
elif mode == "valid":
    delete_data(valid_start, valid_end)
elif mode == "test":
    delete_data(test_start, test_end)

