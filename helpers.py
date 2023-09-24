import requests

root_url = "https://fragdenstaat.de/api/v1/"

level_of_precision = 0.05

def calculate_sample_size(population_size, level_of_precision):
    """
    Calculate the sample size for a given population size and level 
    precision using Slovin's formula.
    """  
    e = level_of_precision
    N = population_size
    
    sample_size = N / (1 + N * e**2)
    sample_size = round(sample_size)
    
    return sample_size

def get_total_count():
    url = f"{root_url}request/"
    
    response = requests.get(url)

    data = response.json()
    
    total_count = data["meta"]["total_count"]
    

    return total_count