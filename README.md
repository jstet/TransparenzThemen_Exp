# Topic modelling experiments on FDS data

## Update Data
1. Clone repo and install requirements
2. Run get_sample.py to update data

## Run tests
```
python3 -m pytest tests.py -s
```

## Findings
- Document length distribution has a long tail. Most of the documents are quite short.
#### Campaigns
- It is necessary to exclude campaigns from the model. This is because FOI requests made with these campaigns often have identical text, which leads to the formation of strongly separated campaign clusters. As a result, when a campaign external request shares a word with a description of a campaign request, it is grouped into the campaign cluster. Furthermore, slight variations within campaigns, such as those related to jurisdictions in campaign 15, can cause the separation of clusters based on just a single word difference.
- Because of the latter finding, to calculate a representative sample size, one should subtract the FOI request belonging to campaigns from the total population, but /api/v1/campaign/ does not contain this information. Based on some random samples I took, there seem to be many campaign requests.
### Templating System
- Sometimes, (for example https://fragdenstaat.de/api/v1/request/278169/), the letter templates (\["law"\]\["letter_start"\] and \["letter_end"\]) are part of the description. If that's the case, we have to remove this text to avoid clusters to be formed for these templates.
- Sometimes, sentences like "Nach §5 Abs. 1 Satz 5 IFG NRW bitte ich Sie um eine Antwort in elektronischer Form (E-Mail)." or
"Ich möchte Sie um Empfangsbestätigung bitten und danke Ihnen für Ihre Mühe!" are not part of template when it is included in the description. Did the template change?
### Umlaute
- Why are incorrect words, for example "fr" which is "für" originally, in the documents?
### Common words such as "Antrag","Abs"
- Add them to stopwords?

## Open Questions
- How to handle requests that belong to the same topic of campaigns but were not made with it?
- The templating system in its current and past versions has to be understood properly to only include the descriptions and not the identical template texts

## Ideas
- Split into paragraphs and only include most important paragraph
- Finetune a german legal/FOI request BERT

# Refusal Reason Classification
- is irrelevant has to be false
- is_sender has to be public body
- request resolution = refused
- How to detect whether a message contains a refusal reason?
    - lots of messages by state are just clarification requests or delay notices
    - status change is not reliable, example: https://fragdenstaat.de/api/v1/request/285252/
    - refusal reason can be in file attachment or in email itself
        - keyword based detection?
    - https://fragdenstaat.de/api/v1/request/251702/: status is waiting for answer but the state already gave a refusal reason. no way to pick message that contains it
- assume refusal reason entered by user is correct and use this for classification

## Possible solution:
- make api request with a foi request id, loop through all messages by state and 
    1. look for keywords to determine if email contains reason
    2. if nothing is found, look for keywords like "find attached"
## Sample Mechanism
- Scrape https://fragdenstaat.de/anfragen/?page=2&status=abgelehnt&campaign=-
- detect last page of list, pick random, then pick random request, then navigate to it, then extract id

