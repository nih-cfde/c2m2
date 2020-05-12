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
community, widening and deepening access to usable
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

In its [fullest form](../draft-C2M2_ER_diagrams/Level-2-C2M2-model.png),
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
all possible features of the [full (Level 2) C2M2 model](../draft-C2M2_ER_diagrams/Level-2-C2M2-model.png)
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
complicated and difficult-to-maintain frameworks.
DCCs with advanced, operationalized metadata modeling
systems of their own should not encounter arbitrary
barriers to CFDE support for more extensive relational
modeling of their metadata if they want it; CFDE will
maintain such support by iteratively refining the
[full C2M2 model](../draft-C2M2_ER_diagrams/Level-2-C2M2-model.png)
according to needs identified while working with
more operationally advanced DCCs. Newer or smaller DCCs, by contrast, may
not currently have enough readily-available information
to feasibly describe their experimental resources using this
most complex C2M2 modeling level: CFDE will support
cases like these by offering simpler but still well-structured
metadata models, lowering some of the barriers to rapid
entry into the data ecosystem.

Simpler C2M2 metadata Levels must be maintained by
CFDE in such a way as to maximize interoperability with
more complex C2M2 variants, and the whole system should be
structured to minimize the negative side effects of model
changes. These considerations have led to the
creation of C2M2 [richness levels](../draft-CFDE_glossary/glossary.md#richness-levels):
concentric, canonical variants of C2M2 which are benchmarked at
increasing levels of complexity and detail, wherein each successive
level is a value-added superset of all of the metadata
encompassed by the previous (less complex) level.

Accordingly, CFDE presently offers two less complex C2M2 variants
in addition to the full (Level 2) C2M2 model:
[Level 0](#Level-0) (basic metadata describing a collection of digital files) and
[Level 1](#Level-1) (which introduces models for core experimental
resources like biosamples and subjects, and the core relationships between them; a rudimentary set of search targets
in the form of annotations like the anatomical location of
the source for a human tissue sample or taxonomic data describing
biosample source organisms and study subjects; and basic support for arranging
experimental resources into sub-collections based on a
hierarchy of projects, experimental datasets or other similar subdivisions
of research ownership and responsibility).

_Level 2 currently requires work to (a) expand and finalize a [brainstorm-level checklist of supported concepts](../draft-C2M2_Levels_spreadsheets/Level_definitions.csv) followed by (b) harmonization of that checklist with an ongoing [draft ER model](../draft-C2M2_ER_diagrams/Level-2-C2M2-model.png)._

--------------------------------------------------------------------------------

### Level 0

C2M2 Level 0 defines a **minimal valid C2M2 instance.** Data submissions
at this level of metadata richness will be the easiest to produce, and will
support the simplest available functionality implemented by
downstream applications.

#### Level 0 submission process: overview

Metadata submissions at Level 0 will consist of a single TSV
file describing a **collection of digital
files** owned or managed by a DCC. The properties listed
for the Level 0 `file` entity (see below for
diagram and definitions) will serve as the TSV's column
headers; each TSV row will represent a single file. The
Level 0 TSV itself thus represents a
**[manifest](../draft-CFDE_glossary/glossary.md#CFDE-asset-manifest)
or inventory** of digital files that a DCC wants to
introduce into the C2M2 metadata ecosystem.

This level encodes the most basic file metadata:
its use by downstream applications will be
limited to informing the least specific level of data
accounting, querying and reporting.

|_Level 0 model diagram_|
|:---:|
|![Level 0 model diagram](../draft-C2M2_ER_diagrams/Level-0-C2M2-model.png "Level 0 model diagram")|

#### Level 0 technical specification: properties of the `file` entity

**Required: `id_namespace` `id` `sha256|md5`**

|property|description|
|:---:|:---|
| `id_namespace` | String **identifier assigned by CFDE to the DCC managing this `file`**. The value of this property will be used together with `id` (assigned to each `file` by the DCC that owns it) as a **paired-key structure formally identifying Level 0 `file` entities** within the total C2M2 data space.|
| `id` | Unrestricted-format **string identifying this `file`, assigned by the DCC managing it**. Can be any string as long as it **uniquely identifies each `file`** within the scope of a single Level 0 metadata submission. |
| `size_in_bytes` | The **size of this `file` in bytes**. This varies (even for "copies" of the same `file`) across differences in storage hardware and operating system. CFDE does not require any particular method of byte computation: file size integrity metadata will be provided in the form of checksum data in the `sha256` and/or `md5` properties. `size_in_bytes` will instead underpin automatic reporting of basic storage statistics across different C2M2 collections of DCC metadata.|
| `sha256` | **CFDE-preferred** file checksum string: the output of the SHA-256 cryptographic hash function after being run on this `file`. One or both of `sha256` and `md5` is required. |
| `md5` | **Permitted** file checksum string: the output of the MD5 message-digest algorithm after being run as a cryptographic hash function on this `file`. One or both of `sha256` and `md5` is required. (CFDE recommends SHA-256 if feasible, but we recognize the nontrivial overhead involved in recomputing these hash values for large collections of files, so if MD5 values have already been generated, CFDE will accept them.) |
| `persistent_id` | **A persistent, resolvable URI generated by a DCC** (using, e.g., the CFDE minid server) **and permanently attached to this `file`**, to serve as a permanent address to which landing pages (which summarize metadata associated with this `file`) and other relevant annotations and functions can eventually be attached, including (optionally) resolution to a network location from which the `file` can be downloaded. **Actual network locations must not be embedded directly within this identifier**: one level of indirection is required in order to allow network addresses to change over time as files are moved around. |
| `filename` | A filename with no prepended PATH information. |

#### Level 0 metadata submission examples: Data Package JSON Schema and example TSVs

A JSON Schema document -- implementing [Frictionless
Data](https://frictionlessdata.io/)'s "[Data
Package](https://frictionlessdata.io/data-package/)" container meta-specification --
defining the Level 0 TSV is
[here](../draft-C2M2_JSON_Schema_datapackage_specs/C2M2_Level_0.datapackage.json);
an example Level-0-compliant TSV submission collection can be found
[here](../draft-C2M2_example_submission_data/HMP__sample_C2M2_Level_0_bdbag.contents/file.tsv)
(just the `file.tsv` portion) and
[here](../draft-C2M2_example_submission_data/HMP__sample_C2M2_Level_0_bdbag.tgz)
(as a packaged BDBag archive).

--------------------------------------------------------------------------------

### Level 1

C2M2 Level 1 models **basic experimental resources and associations between them**.
This level of metadata richness is more difficult to produce than Level 0's flat
inventory of digital files. As a result, Level 1 metadata offers users more powerful
downstream tools than are available for Level 0 datasets, including
   * faceted searches on a (small) set of biologically relevant features (like anatomy
   and taxonomy) of experimental resources like `biosample`s and `subject`s
   * organization of summary displays using subdivisions of experimental metadata
   collections by `project` (grant or contract) and `collection` (any scientifically
   relevant grouping of resources)
   * basic reporting on changes in metadata over time, tracking (for example)
   creation times for `file`s and `biosample`s

C2M2 Level 1 is designed to offer an intermediate tier of difficulty, in terms of
preparing compliant submissions, between Level 0's basic digital inventory
and the full intricacy of Level 2 C2M2 (the most powerful and flexible research-asset
metadata model that can be meaningfully generalized to represent multiple CFDE datasets).
Accordingly, we have reserved several modeling concepts -- requiring the most effort
to produce and maintain -- for Level 2. The following are **not modeled at Level 1**:
   * any and all **protected data**
   * documentation of  **experimental protocols**
   * event-based resource generation/**provenance networks**
   * detailed information on **organizations and people** governing the research
   being documented
   * a **comprehensive suite** of options to model **scientific attributes of
   experimental resources**
      * full collection of features like anatomy, taxonomy, and assay type,
      plus formal vocabularies to describe them
      * prerequisite to offering research users deep and detailed search possibilities

#### Level 1 submission process: overview

_You're not going to have to give us all of the tables shown in the diagram
below. We'll compute some of that. Here's the breakdown of what we absolutely
need from you to construct a compliant Level 1 submission, and also all the
optional things that we'll accept in such a submission, if you have them handy._

_Also note that while this specification describes a collection of TSV files,
if you would prefer to populate (fewer, simpler) higher-level documents
like spreadsheet forms instead of generating fully-inflated specification-compliant
TSVs, we can work with you to automatically translate such documents into compliant
TSV collections prior to submission and ingest into the CFDE core systems._

* _Gold: internal CVs/dictionaries and their foreign-key relationships_
* _Blue: containers and their containment relationships_
* _Green: external controlled vocabularies (term & display-decoration tracking tables)
and their foreign-key relationships_
* _Black: core entities and the direct associative relationships between them (plus
`subject` <-> `subject_role_taxonomy`, which doesn't deserve its own color)_

|_Level 1 model diagram_|
|:---:|
|![Level 1 model diagram](../draft-C2M2_ER_diagrams/Level-1-C2M2-model.png "Level 1 model diagram")|

#### Level 1 technical specification

##### Core entities

   * `file` _revisited (additions: also cf. below, §"Common fields" and §"Controlled
   vocabularies and term tables")_
   * `biosample` _introduced (also cf. below, §"Common fields" and §"Controlled vocabularies and
   term tables")_
   * `subject` _introduced (also cf. below, §"Common fields" and §"Taxonomy and the `subject` entity")_

##### Common fields

   * `id_namespace` _and_ `id`
   * `persistent_id`
   * `creation_time`
   * `abbreviation`, `name` _and_ `description`

##### Core containers

   * `project`
      * _explain "primary project" FK in_ `file`/`biosample`/`subject`
   * `collection`
      * _note decoupling from_ `project`

##### Controlled vocabularies and term tables

   * _enumerate CVs_
   * _describe term tables_
   * _outline plan for addressing versioning_
   * _discuss parser script on offer_
      * _to be executed during bdbag-preparation stage_
      * _will inflate bare CV terms cited in entity fields into corresponding CV
      term-usage tables_
      * _auto-loads and populates display-layer term-decorator data (name,
      description) from relevant CV OBO reference files_

##### Taxonomy and the `subject` entity

   * `subject_granularity`: `subject` _multiplicity specifier_
   * `subject_role`: _constituent relationship to intra-_`subject` _system_
   * `ncbi_taxonomy`: _examples of how to map taxa to_ `subject` _constituents_

##### Association tables and inter-entity relationships

   * _enumerate relationship/association definitions_
   * _note ingest-stage flattening for rapid service of roll-up queries for
   display layer_

#### Level 1 metadata submission examples: Data Package JSON Schema and example TSVs

A (_presently out of sync with diagram; update imminent_) JSON Schema document --
implementing
[Frictionless Data](https://frictionlessdata.io/)'s
"[Data Package](https://frictionlessdata.io/data-package/)"
container meta-specification --
defining the Level 1 TSV collection is
[here](../draft-C2M2_JSON_Schema_datapackage_specs/C2M2_Level_1.datapackage.json);
an example Level-1-compliant TSV submission collection can be found **here** (as a
bare collection of TSV files) and **here** (as a packaged BDBag archive).

--------------------------------------------------------------------------------

### Level 2 (the full C2M2 model)

1. _**New modeling concept checklist:**_
	* clinical **visit data**
	* modular **experimental flow (`protocol`)**
	   * relatively _passive documentation_ of standard protocols and custom procedures
	   * rigorous and detailed stepwise modeling is _not_ anticipated
	* resource (entity) **provenance (`[data|material]_event` network)**
	* structured addressbook for documenting and linking **organizations
	(`common_fund_program`) and people** to C2M2 metadata
	* any C2M2 handling of **protected data**
	* full elaboration of scientific attributes of C2M2 entities using
	**controlled-vocabulary metadata decorations**
	   * i.e., substrate data for facet-search targets
	   * e.g., Level 1's `anatomy`, `assay_type`, `ncbi_taxonomy`, etc.)
	   * [enumerate requirements and scope for more complex modeling of scientific
	   metadata_]
2. _might need a **better name** than 'full C2M2' or 'Level 2'_
3. _**diagram & JSON Schema need updating** to harmonize with drafts for Levels 0 and 1_

|_The full C2M2 model_|
|:---:|
|![The full C2M2 model](../draft-C2M2_ER_diagrams/Level-2-C2M2-model.png "The full Level 2 C2M2 model")|

#### ...

#### Level 2 submissions: schema and example TSVs

The JSON Schema document specifying the full Level 2 C2M2 TSV
collection is [here](../draft-C2M2_JSON_Schema_datapackage_specs/full_C2M2_datapackage_spec.json);
example Level-2-compliant TSV submissions will be found **here**.
