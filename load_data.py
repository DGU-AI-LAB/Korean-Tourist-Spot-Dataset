
# coding: utf-8

# # KTS(Korean Tourist Spot) Dataset Load

# ### Class Definition

# In[1]:


#image, label, likes, text, hashtag
category = {"nature-scene": ["beach", "cave", "island", "lake", "mountain"],
            "person-made": ["amusement park", "palace", "park", "restaurant", "tower"]}


# ### Load Total Raw Heterogeneous Data(text - json & images - jpg)

# In[2]:


from PIL import Image
import numpy as np
import json
import os

def load_data(mode):
    if mode != "train" and mode != "valid" and mode != "test" and mode != "total":
        return None
    
    else:        
        data = np.array([]) # initialization
        
        for key, val in category.items():
            for v in val:
                json_dir = os.path.join("kts/" + mode, key, v, v + ".json")
                image_folder_dir = os.path.join("kts/" + mode, key, v, "images")

                with open(json_dir, encoding="UTF-16") as f:
                    js = json.load(f)
                f.close()

                for j in js:
                    image_file_dir = os.path.join(image_folder_dir, j["img_name"] + ".jpg")
                    image = Image.open(image_file_dir)
                    j["image"]   = image   
                    
                js = np.asarray(js)
                data = np.append(data, js)
        return data


# In[3]:


data = load_data("train")


# In[4]:


print(len(data))

