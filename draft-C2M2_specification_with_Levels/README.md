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

In its [fullest form](../draft-C2M2_ER_diagrams/full-C2M2-ER-model.png),
C2M2 is an [entity-relationship system](../draft-CFDE_glossary/glossary.md#entity-relationship-model)
that models common properties of resources fundamental
to biomedical research like subjects, digital files,
events, samples, and project datasets. Essential
relationships between these fundamental resources are also formally described,
documenting (for example) the samples that were processed
to produce a particular data file; which subject a given sample was
drawn from (possibly obfuscated to protect patient privacy); or when
a particular blood pressure measurement was made.

Modeling and data wrangling are always difficult, even for
experts. Requiring every DCC to model their metadata using
all possible features of the [full C2M2 model](../draft-C2M2_ER_diagrams/full-C2M2-ER-model.png)
as a precondition for submitting metadata to CFDE would
be infeasible for several important reasons (apart from
creating avoidable and unnecessary onboarding delays).
Perhaps the most operationally relevant of these is that
the C2M2 model must remain as flexible as possible, especially
during its developmental phases, in order to accomodate mutual learning
between DCCs and CFDE as the process of data ingestion
develops. It is far more expensive and error-prone to
repeatedly change a complex model than it is to build
one gradually from a simpler core concept which is allowed
to stabilize before more specialized branches are allowed
to solidify.

With the design of C2M2, we are splitting the difference
between the ease of evolution inherent in a simple model and
the operational power provided to downstream applications by more
complicated but difficult-to-maintain frameworks.
DCCs with advanced, operationalized metadata modeling
systems of their own should not encounter arbitrary
barriers to CFDE support for more complicated relational
modeling of their metadata if they want it; CFDE will
maintain such support by iteratively refining the
[full C2M2 model](../draft-C2M2_ER_diagrams/full-C2M2-ER-model.png)
according to needs identified while working with
more operationally complex DCCs. Newer or smaller DCCs, by contrast, may
not currently have enough readily-available information
to feasibly describe their experimental resources using the
most complex C2M2 modeling level: CFDE will fully support
cases like these by offering simpler but still well-structured
metadata models, lowering some of the barriers to rapid
entry into the data ecosystem.

Simpler C2M2 metadata models must be maintained by
CFDE in such a way as to maximize interoperability with
more complex C2M2 variants, and the whole system should be
structured to minimize the negative side effects of model
changes. These considerations have led to the
creation of C2M2 [richness levels](../draft-CFDE_glossary/glossary.md#richness-levels):
parallel canonical variants of C2M2 which are benchmarked at
increasing levels of model complexity.

In addition to the full C2M2 model, CFDE presently offers
two less complex C2M2 variants: [Level 0](#level-0) (basic
metadata describing a collection of digital files) and
[Level 1](#level-1) (which introduces models for core experimental
resources like samples and subjects; search targets in the form
of annotations like the anatomical location of the source for
a human tissue sample; taxonomic data describing subjects
and sample source organisms; and basic support for arranging
experimental resources into sub-collections based on a
hierarchy of projects, studies or other similar subdivisions
of research ownership and responsibility).

(Proposals for Levels 2 and 3 currently exist in
[first-round rough brainstorm draft](../draft-C2M2_Levels_spreadsheets/Level_definitions.csv) only.)

### Level 0

C2M2 Level 0 defines a **minimal valid C2M2 instance.** Data submissions
at this richness level will be the easiest to produce, and will
support the simplest available functionality implemented by
downstream applications.

#### Level 0 submission process: overview

Metadata submissions at Level 0 will consist of a single TSV
file describing a **collection of digital
files** owned or managed by a DCC. The properties listed
for the Level 0 `file` entity (see immediately below for
diagram and definitions) will serve as the TSV's column
headers; each TSV row will represent a single file. The
Level 0 TSV itself thus represents a
**[manifest](../draft-CFDE_glossary/glossary.md#CFDE-asset-manifest)
or inventory** of digital files that a DCC wants to
introduce into the C2M2 metadata ecosystem.

This level encodes the most basic of file metadata:
its use by downstream applications will be
limited to informing the least specific level of data
accounting, querying and reporting.

|_Level 0 model diagram_|
|:---:|
|![Level 0 model diagram](../draft-C2M2_ER_diagrams/Level-0-C2M2-model.png "Level 0 model diagram")|

#### Level 0: the `file` entity and its properties

* `id_namespace` _+ discussion ..._
* `id` _+ discussion ..._
* `size_in_bytes` _+ discussion ..._
* `sha256` and `md5` _+ discussion ..._
* `uri` _+ discussion ..._
* `filename` _+ discussion ..._

#### Level 0 submissions: schema and example TSVs

The JSON Schema document specifying the Level 0 TSV is
**here**; example Level-0-compliant TSV submissions
can be found **here**, **here** and **here**.

### Level 1

_...introduces models for core experimental resources like_
* _samples and subjects_
* _search targets in the form of annotations like the anatomical source for a given tissue sample_
* _host species taxonomy for samples and subjects_
* _basic support for arranging experimental resources into sub-collections based on a hierarchy of projects or studies_

|_Level 1 model diagram_|
|:---:|
|![Level 1 model diagram](../draft-C2M2_ER_diagrams/Level-1-C2M2-model.png "Level 1 model diagram")|

#### Level 1: the `project` string

_A PATH-like fwdslash ("/")-delimited string, where the sequence
of /-delimited substrings describes the project containment hierarchy
attached to a file, subject or sample. DCCs will (optionally)
generate these strings in whatever way they see fit (as long as delimited
tokens don't contain slash characters). Note in particular that there is
no default assumption of any relationship whatsoever between the project
hierarchy proffered by a DCC in its data submission (via this field) and
any formal NIH project structure: in other words, DCCs are free to
subdivide their project space however they like at this level, and stuff
it in this field as a PATH. (More structured -- and programmatically
usable -- modeling of organizations, projects and studies associated with
C2M2 core entities will be specified in the full C2M2 model, but is not
required for Level 1 compliance.)_

#### Level 1: the `file` entity, revisited



#### Level 1: the `bio_sample` entity



#### Level 1: the `subject` entity



#### Level 1: basic foreign key support between entity types



#### Level 1 submissions: schema and example TSVs

The JSON Schema document specifying the Level 1 TSV
collection is **here**; example Level-1-compliant TSV
submissions can be found **here**, **here** and **here**.

### (Level 2)...

### (Level 3)...

### (...)

### Level N (the full C2M2 model)

_This final, most complex level needs a couple of things:_

1. _needs a better name than 'full C2M2'_
2. _MODEL DIAGRAM needs updating so corresponding fields exactly match Levels 1 and 2_
3. _JSON DATAPACKAGE SCHEMA needs updating so corresponding fields exactly match the updates to the model diagram_
4. _Levels 2 and 3 (and ...?) need to be finalized, then harmonized with this one_

|_The full C2M2 model_|
|:---:|
|![The full C2M2 model](../draft-C2M2_ER_diagrams/full-C2M2-ER-model.png "The full C2M2 model")|

#### ...

#### Level N submissions: schema and example TSVs

The JSON Schema document specifying the Level 1 TSV
collection is [here](../draft-C2M2_JSON_Schema_datapackage_specs/full_C2M2_datapackage_spec.json);
example Level-1-compliant TSV submissions can be found **here**, **here** and **here**.
