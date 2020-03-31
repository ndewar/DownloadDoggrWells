<div itemscope itemtype="https://schema.org/Person"><a itemprop="sameAs" content="https://orcid.org/0000-0002-2750-2866" href="https://orcid.org/0000-0002-2750-2866" target="orcid.widget" rel="noopener noreferrer" style="vertical-align:top;"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" style="width:1em;margin-right:.5em;" alt="ORCID iD icon">orcid.org/0000-0002-2750-2866</a></div>

# DownloadDoggrWells
Script to download files for oil and gas wells from the California Geologic Energy Management (formerly known as DOGGR)
Division's well finder web application.

To use the script, download a results.csv for your area by selecting the wells with a rectangle on the following web app:
https://maps.conservation.ca.gov/doggr/wellfinder/

Then download the script and update the variables inside it as needed.

Use of the script would be to execute the following from a terminal:<br/>
**$ python DownloadDoggrWells.py <br/>**

This will download into the current folder all of the wells with the APIs in the results.csv for the county numbers 
coded in the script
