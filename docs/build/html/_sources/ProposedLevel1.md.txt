## Proposed Technical Specification
  
### Level 1
  
The specifications for this level are for informational use only and are still under internal 
development and are not yet finalized. Do not use this version for creating CFDE manifests.
  
_...introduces models for core experimental resources like_
* _samples and subjects_
* _search targets in the form of annotations like the anatomical source for a given tissue sample_
* _host species taxonomy for samples and subjects_
* _basic support for arranging experimental resources into sub-collections based on a hierarchy of projects or studies_
  
_...also introduces two containers for aggregating experimental resources & metadata:_
* _`project` describes administrative/funding/contract/etc. hierarchy governing ownership/management/purview/responsibility of/for subcollections of experimental resources and metadata_
* _`collection` allows any (non-cyclic) groupings to be assigned to subcollections of experimental resources and metadata (independently of contract or funding or ownership or accountability/reporting structures encoded by `project`): similar in concept to "dataset" but without implying the existence of a formally-prepared publication-level data package -- any coherent and meaningful grouping can be encoded here_
  
|_Level 1 model diagram_|
|:---:|
|![Level 1 model diagram](https://nih-cfde.org/wp-content/uploads/2020/05/Level-1-C2M2-model.png "Level 1 model diagram")|
  
#### Level 1 technical specification: the `file` entity, revisited
  
_added properties_
  
#### Level 1 technical specification: introducing the `bio_sample` entity
  
_added entity: list and define properties_
  
#### Level 1 technical specification: introducing the `subject` entity
  
_added entity: list and define properties_
  
#### Level 1 technical specification: using the `project` table
  
_describe the `project` table_
  
#### Level 1 technical specification: using the `collection` table
  
_describe the `collection` table_
  
#### Level 1 technical specification: using association tables to encode inter-entity relationships
  
_describe TSV encoding of `bio_sample`<->`subject`<->`file`<->`bio_sample` association pairs_
  
#### Level 1 technical specification: using terms from controlled vocabularies: usage tables
  
_enumerate CVs; describe usage tables and outline plan for addressing versioning; discuss parser script, to be executed somewhere in bdbag-preparation stage, which will inflate bare CV terms cited in entity fields into corresponding CV usage tables, loading term-decorator data from relevant CV OBO reference files_
  
#### Level 1 metadata submission examples: schema and example TSVs
  
A JSON Schema document specifying the Level 1 TSV
collection is [here](https://github.com/nih-cfde/specifications-and-documentation/blob/master/draft-C2M2_JSON_Schema_datapackage_specs/C2M2_Level_1.datapackage.json); an example Level-1-compliant TSV submission can be found **here** (as a collection of TSV files) and **here** (as a packaged BDBag archive).
