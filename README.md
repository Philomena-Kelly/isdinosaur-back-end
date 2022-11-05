# IsDinosaur Backend

Creates an inbetween API to connect IsDinosaur front end to Wikipedias API. The API takes in a search term and searches for the page on wikipedia. It returns if the search term is classified as a dinosaur.

> *Note, this currently checks if Wikipedia specifies the creature under the clade **Dinosauria** and links to the dinosaur Wikipedia page in the biobox. Given this, it only returns true for prehistoric dinosaurs.*
<br>

## Search Dinosaur
***

**Endpoint:** GET '/search'

**Request body:** JSON object 

`{ "answer": string }`

| *Subject is a **required** argument in order to return the search term. If the **subject** is null, the response will be no.* 

**Response body:** JSON object
```
{
    "answer" : "yes" **OR** "no"
}
```  
