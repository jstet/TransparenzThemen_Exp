import matplotlib.pyplot as plt
import random
import requests
import pandas as pd

from helpers import calculate_sample_size, get_total_count, root_url

### Calculating sample size ###

population_size = get_total_count()
level_of_precision = 0.05

sample_size = calculate_sample_size(population_size, level_of_precision)
print(f"The required sample size is: {sample_size}")

### Retrieving sample ###

objects_per_page = 50
total_pages = population_size // objects_per_page

sampled_objects = []
sampled_ids = set()

while len(sampled_objects) < sample_size:
    random_page = random.randint(1, total_pages)
    
    url = f"{root_url}request/?offset={random_page}"
    response = requests.get(url)
    request_lst = response.json()["objects"]
    
    if len(request_lst) > 0:
        request = random.choice(request_lst)
        
        # Check if ID is already in the sampled IDs set
        if request["id"] not in sampled_ids:
            sampled_ids.add(request["id"])
            sampled_objects.append({"id": request["id"], "description": request["description"]})
    
    # Calculate the relative progress
    progress = len(sampled_objects) / sample_size * 100
    print(f"Sampled {len(sampled_objects)} out of {sample_size} objects. Progress: {progress:.2f}%")

### Saving sample to CSV ####

df = pd.DataFrame(sampled_objects)

# Save the DataFrame to a CSV file
filename = "./data/sample.csv"
df.to_csv(filename, index=False)

print(f"Sampled objects saved to {filename}.")