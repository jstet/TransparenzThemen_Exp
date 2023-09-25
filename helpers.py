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


def remove_letter_templates(request):
    temp = request["description"]
    
    letter_start = request["law"]["letter_start"]
    letter_end = request["law"]["letter_end"]
    # sometimes templates contain email text, sometimes they don't. Has this been updated?
    email_text = "Nach §5 Abs. 1 Satz 5 IFG NRW bitte ich Sie um eine Antwort in elektronischer Form (E-Mail)."
    greetings = "Mit freundlichen Grüßen"
    received = "Ich möchte Sie um Empfangsbestätigung bitten und danke Ihnen für Ihre Mühe!"
    letter_end = letter_end.replace(email_text, "").replace(greetings, "").replace(received, "").strip()

    temp = temp.strip()
    temp = temp.replace(letter_start, "")
    temp = temp.replace(letter_end, "").replace(email_text, "").replace(greetings, "").replace(received, "")
    return temp

