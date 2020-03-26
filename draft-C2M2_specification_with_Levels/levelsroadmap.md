# The Common Fund Data Ecosystem's Crosscut Metadata Model (CFDE C2M2)

This document introduces the Crosscut Metadata Model (C2M2),
a flexible standard for describing biomedical experimental
data. The Common Fund Data Ecosystem group is creating a new
infrastructure, with C2M2 as its central concept, through
which powerful cross-dataset searches, custom aggregation
of experimental data and scale-powered statistical analysis
methods will be made possible for the biomedical research
community at an unprecedented scope.

Using this new infrastructure, data coordinating centers
([DCCs](../draft-CFDE_glossary/glossary.md#DCCs)) can
share structured information ([metadata](../draft-CFDE_glossary/glossary.md#metadata))
about their experimental resources with the research
community, dramatically widening access to usable
observational data and accelerating discovery.

## DCC Metadata Submissions

DCCs will collect and provide metadata to CFDE describing
experimental resources within their purview. Each metadata
submission will take the form of a collection of tab-separated value
files (TSVs): precise formatting requirements for these TSV
collections will be specified by JSON Schema documents
implementing the [Data Package](http://frictionlessdata.io/docs/data-package/)
meta-specification published by the [Frictionless Data](http://frictionlessdata.io/)
group. These schemas will be used by the CFDE software
infrastructure to automatically validate submission format compliance
and metadata integrity during the [ingestion process](../draft-CFDE_glossary/glossary.md#DCC-data-ingestion-process).

CFDE will offer DCCs multiple alternatives for metadata submission
formats, all of which will be automatically interoperable with the
C2M2 ecosystem. These alternative formats are arranged in
levels tiered according to increasing complexity, reflecting
anticipated differences in the relative richness of metadata
available to different DCCs at any particular time. The general
expectation will be that the metadata submitted and managed by a
DCC will be able to transition, over time, through
increasingly rich modeling levels -- enabling increasingly powerful downstream
applications -- as the life cycle of DCC/CFDE technical interaction
progresses.

## C2M2 Richness Levels

In its [current form](../draft-C2M2_ER_diagrams/full-C2M2-ER-model.png),
C2M2 is an [entity-relationship system](../draft-CFDE_glossary/glossary.md#entity-relationship-model)
that models common properties of resources fundamental
to biomedical research like subjects, digital files,
events, samples, and project datasets. Essential
relationships between these fundamental resources are also formally described,
documenting (for example) the samples that were processed
to produce a particular data file; which subject a given sample was
drawn from (possibly obfuscated to protect patient privacy); or when
a particular blood pressure measurement was made.

While we know our current model is not yet rich enough to contain
all of the metadata required by all DCCs, there are also too many terms 
for most DCCs to easily work with. Modeling and data wrangling are always difficult, even for
experts. Requiring every DCC to model their metadata using
all possible features of the [current C2M2 model](../draft-C2M2_ER_diagrams/full-C2M2-ER-model.png)
as a precondition for submitting metadata to CFDE would
be impractical for several important reasons. 

First, many of the DCCs host human data, and for all but very basic file information, the
associated metadata is protected. Currently, the CFDE does not have protected
data access or an ATO to make these metadata searchable. Requiring 
DCCs to supply these terms would make it illegal for most DCCs to comply.
Secondly, from an operational standpoint the C2M2 model must remain as flexible as possible, especially
during its developmental phases, in order to accomodate mutual learning
between DCCs and CFDE as the process of data ingestion
develops. We don't want to lock ourselves in to our current
model topology before we've begun adding real data. 
It is far more expensive and error-prone to
repeatedly change a complex model than it is to build
one gradually from a simpler core concept which is allowed
to stabilize before more specialized branches are added. Finally, even if 
the issues with protected metadata were solved and the model was perfected, the
complexity of the overall model would create avoidable and unnecessary onboarding delays
for any new DCC.


With the design of C2M2, we are splitting the difference
between the ease of evolution inherent in a simple model and
the operational power provided to downstream applications by more
complicated and difficult-to-maintain frameworks.
DCCs with advanced, operationalized metadata modeling
systems of their own should not encounter arbitrary
barriers to CFDE support for more extensive relational
modeling of their metadata if they want it; CFDE will
maintain such support by iteratively refining the
[current C2M2 model](../draft-C2M2_ER_diagrams/full-C2M2-ER-model.png)
according to needs identified while working with
more operationally advanced DCCs. Newer or smaller DCCs, by contrast, may
not currently have enough readily-available information
to feasibly describe their experimental resources using the
most complex C2M2 modeling level: CFDE will support
cases like these by offering simpler but still well-structured
metadata levels, lowering some of the barriers to rapid
entry into the data ecosystem. We expect this concept of levels to 
be useful even after all current DCCs are onboarded, as when the CF funds new
Programs, they will all have ramp up phases where their data necessarily is 
less rich than the more mature DCCs.

Simpler C2M2 metadata levels must be maintained by
CFDE in such a way as to maximize interoperability with
more complex C2M2 variants, and the whole system should be
structured to minimize the negative side effects of overall model
changes. These considerations have led to the
creation of C2M2 [richness levels](../draft-CFDE_glossary/glossary.md#richness-levels):
concentric, canonical subsets of C2M2 which are benchmarked at
increasing levels of model complexity and detail, wherein each successive
modeling level is a value-added superset of all of the metadata
encompassed by the previous (less complex) level. 

Presently, CFDE presently offers two less complex C2M2 variants
in addition to the most complex current C2M2 model:
[Level 0](#level-0) (basic metadata describing a collection of digital files) and
[Level 1](#level-1). Level 1 introduces terms for core experimental
resources like samples and subjects; a rudimentary set of search targets
in the form of annotations like the anatomical location of
the source for a human tissue sample or taxonomic data describing
sample source organisms and study subjects; and basic support for arranging
experimental resources into sub-collections based on a
hierarchy of projects, studies or other similar subdivisions
of research ownership and responsibility. Levels 0 and 1 consist entirely of unprotected 
metadata terms, and therefore should be achieveable by all DCCs. These two levels also
are sufficient to support two minimal [Use Cases](https://nih-cfde.github.io/usecases/). 
Using only the metadata from Levels 1 and 2, a [researcher can find datasets from across the Common Fund that contain information about her tissue of interest, assayed using her method of choice](https://nih-cfde.github.io/usecases/use-cases/browse-and-filter.html). Similarly, a [staff at the NIH can compare the tissues, species and assay types available across DCCs](https://nih-cfde.github.io/usecases/use-cases/multi-compare-custodian.html). More complex Use Cases, such as the [abilty for a researcher to find datasets for patients with a specific disease, in a specific age range](putlinkhere.html) will require DCCs to submit Level 2, protected, metadata terms. However, this is limited by our access to protected data, as we cannot legally accept that data until certian security and administraive issues are solved.


## C2M2 Development Roadmap

---

### Level 0

C2M2 Level 0 defines a **minimal valid C2M2 instance.** Data submissions
at this level of metadata richness will be the easiest to produce, and will
support the simplest available functionality implemented by
downstream applications.

Full specification can be found in the accompanying Level_0_popout.assets_and_asset_manifest_deliverable.md doc.

---

### Level 1

_Introduces tables for core experimental resources like:_
* _samples and subjects_
* _search targets in the form of annotations like the anatomical source for a given tissue sample_
* _host species taxonomy for samples and subjects_
* _basic support for arranging experimental resources into sub-collections based on a hierarchy of projects or studies_

The full specification is currently under active development, and will be formalized and implemented in the first demo scheduled for June 2020.

---

### (Level 2)...

_Introduces tables for core experimental resources like:_
* _sex_		
* _age_	
* _disease_
* _health conditions_
* _vital stats: height, weight, bp, etc_	

We have a draft specification of Level 2, preliminary documents for the schema can be found here [[LINK](https://github.com/nih-cfde/specifications-and-documentation/blob/roadmap/draft-C2M2_Levels_spreadsheets/Level_definitions.csv)]. Finalization of Level 2 will be completed in order to acheive a CFDE portal demonstration in December 2020. Importantly, Level 2 can be used to represent protected data, which will require completion of several important administrative and policy milestones. 


---

### (Level 3)...

_Introduces tables for core experimental resources like:_
* _sequencing technology_				
* _geographic location_		
* _race/ethnicity (human)/strain (mouse)_			
* _sample collection date_	
* _SOP used for extraction or analysis process_


The full specification is outlined, but not under active development. It will be formalized in the coming months and implemented in a later demo. As with Level 2, it is dependent on protected data access. 

---

### (Level N)...

Based on feedback from the DCCs, and the terms that are important for searching their data, we anticipate the
need for further levels. However, until we begin getting metadata from the Programs, we cannot predict
what terms will be added, or what constellations of terms will be required to make a compliant model. However, 
we do not expect the number of levels to exceed 5, as some new terms will best fit as amendments to previously defined levels.

The full specification is expected, but not outlined or under active development. It will be outlined once DCCs have begun to submit data, and formalized in collaboration with our DCC partners. As with Level 2, implementation of these levels will be dependent on protected data access. 

---


