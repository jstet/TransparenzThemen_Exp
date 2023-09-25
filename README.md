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

## Open Questions
- How to handle requests that belong to the same topic of campaigns but were not made with it?
- The templating system in its current and past versions has to be understood properly to only include the descriptions and not the identical template texts

