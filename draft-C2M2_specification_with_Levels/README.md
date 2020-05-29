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
| `id_namespace` | String **identifier given by CFDE to the DCC managing this `file`**. The value of this property will be used together with `id` (assigned to each `file` by the DCC that owns it) as a **paired-key structure formally identifying Level 0 `file` entities** within the total C2M2 data space.|
| `id` | Unrestricted-format **string identifying this `file`, assigned by the DCC managing it**. Can be any string as long as it **uniquely identifies each `file`** within the scope defined by the accompanying `id_namespace` value. |
| `persistent_id` | **A persistent, resolvable URI generated by a DCC** (using, e.g., the CFDE minid server) **and permanently attached to this `file`**, to serve as a permanent address to which landing pages (which summarize metadata associated with this `file`) and other relevant annotations and functions can eventually be attached, including (optionally) resolution to a network location from which the `file` can be downloaded. **Actual network locations must not be embedded directly within this identifier**: one level of indirection is required in order to allow network addresses to change over time as files are moved around. |
| `size_in_bytes` | The **size of this `file` in bytes**. This varies (even for "copies" of the same `file`) across differences in storage hardware and operating system. CFDE does not require any particular method of byte computation: file size integrity metadata will be provided in the form of checksum data in the `sha256` and/or `md5` properties. `size_in_bytes` will instead underpin automatic reporting of basic storage statistics across different C2M2 collections of DCC metadata.|
| `sha256` | **CFDE-preferred** file checksum string: the output of the SHA-256 cryptographic hash function after being run on this `file`. One or both of `sha256` and `md5` is required. |
| `md5` | **Permitted** file checksum string: the output of the MD5 message-digest algorithm after being run as a cryptographic hash function on this `file`. One or both of `sha256` and `md5` is required. (CFDE recommends SHA-256 if feasible, but we recognize the nontrivial overhead involved in recomputing these hash values for large collections of files, so if MD5 values have already been generated, CFDE will accept them.) |
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

_Build the black (core entity) and blue (containment relationship) tables
shown in the diagram below. We'll give you copies of the gold tables to include
with your submission: you'll reference IDs from these tables in the (blue and black) tables
you're building directly. Once you've built the core entity tables,
the green tables can be built automatically using our
[term-scanner script](../draft-C2M2_external_CV_term_table_generator_script/build_term_tables.py), which will
collect all relevant CV terms used throughout your core tables and will create the
corresponding green tables, using data loaded from versioned, whole-CV reference
documents (like OBO files)._

_In the case of any unpopulated tables (no_ `collection` _records, for example, are
required for model compliance), please create the relevant TSV files anyway,
with just one tab-separated header line containing the empty table's column
names. (In contrast to simply omitting the blank table file, the recommended practice
instead explicitly distinguishes the case in which no data is being submitted
for a given table from the case in which a table has been omitted by mistake.)_

_Color key:_

* _Gold: CFDE-internal controlled vocabularies/dictionaries and their foreign-key relationships_
   * _Note: for representational clarity, gold FK arrows are implied (but not drawn)
from all_ `id_namespace` _fields to the header block of the_ `id_namespace` _table._
* _Green: external CVs (term & display-decoration tracking tables) and their foreign-key relationships_
* _Blue: containers and their containment relationships_
* _Black: core entities and the direct associative relationships between them (plus_
`subject` _<->_ `subject_role_taxonomy` _)_

|_Level 1 model diagram_|
|:---:|
|![Level 1 model diagram](../draft-C2M2_ER_diagrams/Level-1-C2M2-model.png "Level 1 model diagram")|

#### Level 1 technical specification

##### Core entities

   * **`file` revisited** _(superset additions: cf. below, §"Common entity fields" and also §"Controlled
   vocabularies and term tables")_
   * **`biosample` introduced** _(also cf. below, §"Common entity fields" and §"Controlled vocabularies and
   term tables")_
      * _Level 1 models_ `biosample`_s as abstract materials that are directly consumed
      by one or more analytic processes. Simple provenance relationships -- between each
      such_ `biosample` _and the_ `subject` _from which it was originally derived, as well
      as between each_ `biosample` _and any_ `file`_s analytically derived from it -- are
      represented using association tables, with one such table dedicated to each
      relationship type (cf. below, §"Association tables: inter-entity linkages").
      Actual DCC-managed provenance metadata will sometimes (maybe always) represent more complex and
      detailed provenance networks: in such situations, chains of "_`this` _produced_
      `that`_" relationships too complex to model at Level 1 will need to be
      transitively collapsed. As an example: let's say a research team collects a
      cheek-swab sample from a hospital patient; subjects that swab sample to several
      successive preparatory treatments like centrifugation, chemical ribosomal-RNA
      depletion and targeted amplification; then runs the final fully-processed
      remnant material through a sequencing machine, generating a FASTQ sequence
      file as the output of the sequencing process. In physical terms our team
      will have created a series of distinct material samples, connected one to another
      by (directed) "_`X` `derived_from` `Y`_" relationships, represented as a (possibly
      branching) graph path (in fully general terms, a directed acyclic graph) running
      from a starting node set (here, our original cheek-swab sample) through intermediate
   	nodes (one for each coherent material product of each individual preparatory process)
   	to some terminal node set (in our case, the final-stage, immediately-pre-sequencer
   	library preparation material). C2M2 Level 2 offers metadata structures to model
   	this entire process in full detail, including representational support for all
   	intermediate_ `biosample`_s, and for the various preparatory processes involved.
   	For the purposes envisioned to be served by Level 1 C2M2 metadata, on the other hand,
   	only_ `subject` _<->_ `some_monolothic_stuff` _<->_ `(FASTQ) file` _can and should be
   	explicitly represented._
         * _The simplifications here are partially necessitated by the fact that
   	   event modeling has been deliberately deferred to C2M2 Level 2: as a result,
   	   the notion of a well-defined "chain of provenance" is not modeled at
   	   this C2M2 Level. (More concretely: Level 1 does not represent
   	   inter-_`biosample` _relationships.)_
         * _The modeling of details describing experimental processes has also been
         assigned to Level 2._
         * _With both of these (more complex) aspects of experimental metadata
         masked at C2M2 Level 1, the most appropriate granularity at which a Level 1_
         `biosample` _entity should be modeled is as an abstract "material phase"
         (possibly masking what is in reality a chain of multiple distinct materials)
         that enables an analytic (or observational or other scientific) process (which
         originates at a_ `subject` _) to move forward and ultimately produce one or
         more_ `file`_s._  
      * _In practice, a Level 1 C2M2 instance builder facing such a situation
   	might reasonably create one record for the originating_ `subject` _; create one_
   	`biosample` _entity record; create a_ `file` _record for the FASTQ file produced
   	by the sequencing process; and hook up_ `subject` _<->_ `biosample` _and_
   	`biosample` _<->_ `file` _relationships via the corresponding association tables
   	(cf. below, §"Association tables: inter-entity linkages")._
         * _In terms of deciding (in a well-defined way) specifically which native DCC
         metadata should be attached to this Level 1_ `biosample` _record, one
         might for example choose to import metadata (IDs, etc.) describing the
         final pre-sequencer material. The creation of specific rules governing maps
         from native DCC data to (simplified, abstracted) Level 1 entity records
         is of necessity left up to the best judgment of the serialization staff
         creating each DCC's Level 1 C2M2 ETL instance; we recommend consistency,
         but beyond that, custom solutions will have to be developed to handle
         different data sources. CFDE staff will be available to help navigate any
         complexity encountered when establishing a map between the native details
         of DCC sample metadata and the approximation that is the C2M2 Level
         1_ `biosample` _entity._
         * _Note in particular that this example doesn't preclude attaching multiple_
         `biosample`_s to a single originating_ `subject`_; nor does it preclude modeling a
         single_ `biosample` _that produces multiple_ `file`_s._
         * _Note also that the actual end-stage material prior to the production of a_
         `file` _might not always prove to be the most appropriate metadata source from
         which to populate a corresponding_ `biosample` _entity. Let's say a
         pre-sequencing library prepration material_ `M` _is divided in two to
         produce derivative materials_ `M1` _and_ `M2` _, with_ `M1` _and_ `M2` _then
         amplified separately and sequenced under separate conditions producing_
         `file`_s_ `M1.fastq` _and_ `M2.fastq` _. In such a case -- depending on
         experimental context -- the final separation and amplification processes
         producing_ `M1` _and_ `M2` _might reasonably be ignored for the purposes
         of Level 1 modeling, instead attaching a single (slightly upstream)_
         `biosample` _entity -- based on metadata describing_ `M` _-- to both_ `M1.fastq`
         _and_ `M2.fastq`_. As above, final decisions regarding detailed rules
         mapping native DCC data to Level 1 entities are necessarily left to
         DCC-associated investigators and serialization engineers; CFDE staff will be available as needed to offer
         feedback and guidance when navigating mapping issues._
   * **`subject` introduced** _(also cf. below, §"Common entity fields" and §"Taxonomy and the `subject` entity")_
      * _The Level 1_ `subject` _entity is a generic container meant to represent any biological
      entity from which a Level 1_ `biosample` _can be generated (the notion of_ `biosample`_s
      being generated by other_ `biosample`_s is more appropriately modeled at C2M2
      Level 2: cf. §"_`biosample` **introduced**_", immediately above)_
      * _Alongside shared metadata fields (cf. below, §"Common entity fields") and inter-entity
      associations (cf. below, §"Association tables: inter-entity linkages"), C2M2
      Level 1 models two additional details specific to_ `subject` _entities:_
         * _internal structural configuration (defined in the_ `subject_granularity` _table
         and specified for each_ `subject` _record via a foreign key field in the_ `subject` _table),
         e.g.: "single organism," "microbiome," "cell line"_
         * _taxonomic assignments attached to subcomponents ("roles," defined in the_
         `subject_role` _table) of_ `subject` _entities, e.g. "cell line ancestor ->
         NCBI:txid9606" or "host (of host-pathogen symbiont system) -> NCBI:txid10090":
         this is accomplished via the_ `subject_role_taxonomy` _trinary association table
         (cf. below, §"Association table: taxonomy and the_ `subject` _entity: the_ `subject_role_taxonomy` _table")_
      * _all other_ `subject`_-specific metadata -- including any protected data -- is deferred by
      design to Level 2_

##### Common entity fields

The following properties all have the same meaning and function across
the various entities they describe (`file`, `biosample`, `project`, etc.).

|property|description|
|:---:|:---|
| `id_namespace` | String **identifier given by CFDE to the DCC managing this entity**. The value of this property will be used together with `id` (assigned to each entity by the DCC that owns it) as a **paired-key structure formally identifying Level 1 entities** within the total C2M2 data space.|
| `id` | Unrestricted-format **string identifying this entity, assigned by the DCC managing it**. Can be any string as long as it **uniquely identifies each entity** within the scope defined by the accompanying `id_namespace` value. |
| `persistent_id` | **A persistent, resolvable URI generated by a DCC and permanently attached to this entity**, to serve as a permanent address to which landing pages (which summarize metadata associated with this entity) and other relevant annotations and functions can eventually be attached, including (optionally) resolution to a network location from which the entity can be viewed, downloaded, or otherwise directly investigated. **Actual network locations must not be embedded directly within this identifier**: one level of indirection is required in order to allow network addresses to change over time as entity data is moved around. |
| `creation_time` | An ISO 8601 / RFC 3339 (subset)-compliant timestamp documenting this entity's creation time (or, in the case of a `subject` entity, the time at which the `subject` was first documented by the `project` under which the `subject` was first observed): **`YYYY-MM-DDTHH:MM:SS±NN:NN`**, where<br><ul><li>**`YYYY`** is a four-digit Gregorian **year**</li><li>**`MM`** is a zero-padded, one-based, two-digit **month** between `01` and `12`, inclusive</li><li>**`DD`** is a zero-padded, one-based, two-digit **day** of the month between `01` and `31`, inclusive</li><li>**`HH`** is a zero-padded, zero-based, two-digit **hour** label between `00` and `23`, inclusive (12-hour time encoding is specifically prohibited)</li><li>**`MM`** and **`SS`** represent zero-padded, zero-based integers between `00` and `59`, inclusive, denoting Babylonian-sexagesimal **minutes** and **seconds**, respectively</li><li>**`±`** denotes exactly one of `+` or `-`, indicating the direction of the offset from GMT (Zulu) to the local time zone (or `-` in the special case encoded as `-00:00`, in which the local time zone is unknown or not asserted)</li><li>**`NN:NN`** represents the **hours:minutes** differential between GMT/Zulu and the local time zone context of this `creation_time` (qualified by the preceding `+` or `-` to indicate offset direction), with `-00:00` encoding the special case in which time zone is unknown or not asserted (`+00:00`, by contrast, denotes the GMT/UTC/Zulu time zone itself)</li></ul><br>Apart from the **time zone** segment of `creation_time` (**`±NN:NN`**, just described) and the **year** (**`YYYY`**) segment, **all other constituent segments of `creation_time` named here may be rendered as `00` to indicate a lack of available data** at the corresponding precision.<ul><li>_We are aware (and unconcerned) that this technically renders one particular_ **`HH:MM:SS`** _value --_ "`00:00:00`" _-- ambiguous. Forestalling this ambiguity (by allowing select omissions of constituent sub-segments of_ `creation_time` _string values as an alternative mechanism to denote missing data, or by introducing nonstandard and increasingly artificial special-case encodings like_ "`99:99:99`"_) was determined to be of less immediate concern than maintaining the technical advantages conferred by the (stronger) constraint of requiring a fixed-length_ `creation_time` _string that remains fully conformant with (a constrained subset of) the RFC 3339 standard. The canonical C2M2 interpretation of_ "`00:00:00`" _is thus explicitly defined to be "_**`HH:MM:SS`** _information unknown" and not "exactly midnight."_</li></ul> |
| `abbreviation`, `name` and `description` | _Values which will be used, unmodified, for contextual display throughout portal and dashboard user interfaces: severely restricted, whitespace-free_ `abbreviation` _(must match_ `/[a-zA-Z0-9_]*/`_); terse but flexible_ `name` _; abstract-length_ `description` |

##### Containers

C2M2 Level 1 offers two ways -- `project` and `collection` -- to denote groups of
related metadata entity records representing core (`file`/`subject`/`biosample`)
experimental resources.

   * `project`
      * _unambiguous, unique, named, most-proximate research/administrative
      sphere of operations that **first generates** each experimental resource
      (_`file`/`subject`/`biosample`_) record_
      * _conceptually rooted in -- but not necessarily mapped one-to-one from
      -- a corresponding hierarchy of grants, contracts or other **important
      administrative subdivisions of primary research funding**_ 
      * `project` _attribution is **required** for core resource entity types: use
      (binary, explicit, namespace-decoupled) "primary project" FK in_
      `file`/`biosample`/`subject` _entity records to encode these attributions_
      * `project`s _**can be nested** (via the_ `project_in_project` _association
      table: cf. below, §"Association tables: expressing containment relationships")
      into a hierarchical (directed, acyclic) network, but one and only one_
      `project` _node in one and only one_ `project` _hierarchy can be attached
      to each core entity record._
   * `collection`
      * _**contextually unconstrained:** a generalization of the "dataset" concept
      which additionally and explicitly supports the inclusion of elements
      (C2M2 metadata entities) representing_ `subject`_s and_ `biosample`_s_
      * _**wholly optional**: Level 1 C2M2 serialization of DCC metadata need not
      necessarily include any_ `collection` _records or attributions_
      * _**membership** of C2M2 entities in_ `collection`_s is encoded using the
      relevant association tables (cf. below, §"Association tables: expressing containment relationships")_
      * _used to describe the **federation of any set of core resource entities (and,
      recursively, other**_ **`collection`**_**s)** across inter-_`project` _boundaries
      (or across inter-DCC boundaries, or across any other structural
      boundaries used to delimit or partition areas of primary purview or
      provenance, or crossing no such boundaries at all)_
      * _unconstrained with respect to "defining entity"_
         * _**may optionally** be attributed to a (defining/generating) C2M2_ `project` _record_
            * _this attribution is **optional and (when null) will not always even
            be well-defined**: the power to define new_ `collection`_s,
            on an ongoing basis, will be offered to all (approved? registered?) members
            of the interested research community at large, without being specifically
            restricted to researchers or groups already operating under the
            auspices of a well-defined_ `project` _entity in the C2M2 system._
         * _this configuration is meant to facilitate data/metadata reuse and
         reanalysis, as well as to provide a specific and consistent anchoring
         structure through which authors anywhere can create (and study and cite)
         newly-defined groupings of C2M2 resources, independently of their original
         provenance associations._

##### Association tables: expressing containment relationships

   * `project_in_project`
   * `collection_defined_by_project`
   * `collection_in_collection`
   * `file_in_collection`
   * `subject_in_collection`
   * `biosample_in_collection`
   
   _These tables are used to express basic containment relationships like "this_ `file` _is in
   this_ `collection`_" or "this_ `project` _is a sub-project of this other_
   `project`_." The record format for all of these tables specifies four fields:_
   
   * _two (an_ `id_namespace` _and an_ `id`_) encoding a foreign key representing
   the **containing**_ **`project`** _**or**_ **`collection`**_, and_
   * _two (another_ {`id_namespace`, `id`} _pair) acting as a foreign key
   referencing the table describing the **contained resource (or
   subcollection)**._
   
   _Please see the relevant sections of the_
   [Level 1 JSON Schema](../draft-C2M2_JSON_Schema_datapackage_specs/C2M2_Level_1.datapackage.json)
   _to find all table-specific field names and foreign-key constraints._

##### Association tables: inter-entity linkages

   * `file_describes_subject`
   * `file_describes_biosample`
   * `biosample_from_subject`
   
   _As with the containment association tables, records in these three tables
   will contain four fields, encoding two foreign keys: one (binary) key per
   entity involved in the relationship being asserted by each record._
   
   _Table names define relationship types, and are by design somewhat nonspecific.
   Note in particular that the relationships represented here **may** mask
   transitively-collapsed versions of more complex relationship networks in the native
   DCC metadataset. The specification of precise rules governing native-to-C2M2
   metadata mappings (or approximations) are left to DCC serialization staff and
   relevant investigators; CFDE staff will be available as needed to offer
   feedback and guidance when navigating these issues._
   
   _Please see the relevant sections of the_
   [Level 1 JSON Schema](../draft-C2M2_JSON_Schema_datapackage_specs/C2M2_Level_1.datapackage.json)
   _to find all table-specific field names and foreign-key constraints._

##### Association table: taxonomy and the `subject` entity: the `subject_role_taxonomy` table

   _The (trinary: three-key)_ `subject_role_taxonomy` _association table enables
   the attachment of taxonomic labels (NCBI Taxonomy Database identifiers, of the form_
   `/^NCBI:txid[0-9]+$/` _and stored for reference locally in the C2M2_
   `ncbi_taxonomy` _table) to C2M2_ `subject` _entities in a variety of
   ways, depending on_ `subject_granularity`_, using_ `subject_role` _values to specify
   the qualifying semantic or ontological context that should be applied to
   each taxonomic label._

   * `subject_granularity` (`subject` _multiplicity specifier):_
      * _for each_ `subject` _record, pick one of
   [these values](../draft-C2M2_internal_CFDE_CV_tables/subject_granularity.tsv)
   and attach its_ `id` _to the_ `subject` _record using the_ `granularity` _foreign
   key provided in the_ `subject` _entity table_
   * `subject_role`: _constituent relationship to intra-_`subject` _system:_
      * _each_ `subject_granularity` _corresponds to a subset of
      [these values](../draft-C2M2_internal_CFDE_CV_tables/subject_role.tsv),
      each of which can be labeled independently with NCBI Taxonomy Database
      IDs via_ `subject_role_taxonomy`.
   * `subject_role_taxonomy`: _Putting it all together: this association table
   stores three keys per record, connecting components of_ `subject` _entities
   (_`subject_role`_s) to taxonomic assignments:_
      * _A (binary:_ `{ subject.id_namespace, subject.id }`_) key identifying a C2M2_ `subject` _entity record_
      * _A (unitary:_ `{ subject_role.id }`_) ID denoting a_ `subject_role` _contextual qualifier_
      * _A (unitary:_ `{ ncbi_taxonomy.id }`_) ID denoting an NCBI Taxonomy Database entry_

   _Please refer to the definition of_ `subject_role_taxonomy` _in the_
   [Level 1 JSON Schema](../draft-C2M2_JSON_Schema_datapackage_specs/C2M2_Level_1.datapackage.json)
   _to find all technical details (field names and foreign-key constraints)._

##### Controlled vocabularies and term tables

   * _CVs in use at Level 1:_
      * _**assay\_type (OBI):** used to describe **types of material** that can be Level
      1_ `biosample`_s_
      * _**anatomy (Uberon):** used to specify the **physiological source location**
      in or on the_ `subject` _from which a_ `biosample` _was derived_
      * _**data\_type (EDAM):** used to categorize the abstract **information content** of
      a_ `file` _(e.g. "this is sequence data")_
      * _**file\_format (EDAM):** used to denote the **digital format or encoding** of
      a_ `file` _(e.g. "this is a FASTQ file")_
      * _**ncbi\_taxonomy (...NCBI Taxonomy :):** used to **link**_ **`subject`** _**entity
      records to taxonomic labels** (cf above, §"Association table: taxonomy and the_ `subject`
      _entity: the_ `subject_role_taxonomy` _table")_
   * _**general guidance on usage:** for the moment, just do the best you can
   by picking through the given CVs; leave blank CV-field values for any records that
   wind up causing you any sort of trouble._
      * `#c2m2-internal-note: See the wish list (two bullets below) for initial notes on improving the
      engineering solutions for this topic after the demo. Too many important issues remain
      to be studied, argued, decided, implemented and tested for us to make CV management
      more than a quick and intellectually unsatisfying kludge and still meet our June development
      deadline. (Note that once we've actually built a few C2M2 metadata instance
      collections, we can then compare notes to help us all get a much better collective
      grip on some of the problems that will need solving in this area.)`
   * [CV term scanner script](../draft-C2M2_external_CV_term_table_generator_script/build_term_tables.py):
   	_auto-builds (green) CV term tables_
      * _executed during bdbag-preparation stage, after core TSVs have been built_
      * _inflates (bare) CV terms cited in core-entity table fields into corresponding CV
      term-usage tables_
      * _auto-loads and populates display-layer term-decorator data (name,
      description) from relevant (versioned) CV reference files_
      * _usage:_
         * _change "_`USER-DEFINED PARAMETERS`_" section to match your local directory
      configuration_
         * _make sure the prerequisite files are in the right directories_
         * _then just run the script without arguments_
   * `#c2m2-internal-note: `**`wish list:`**` Everything listed here `**`must`**` be carefully
   addressed well in advance of the final full-production phase of C2M2 development.
   Handling these issues will take place `**`independently of and in parallel to our
   June demo development process`**` (or after it concludes). Any progress made on these
   topics before the demo will be binned into one of two categories: `**`(a) Data
   refinements`**` to ETL instances which do not affect the underlying Level 1 model structure,
   i.e., changes to field values and concomitant updates to the relevant Deriva
   catalogs; `**`or (b) model-altering implementation decisions`**` (including but not limited
   to the replacement of any of the currently-selected CV ontologies, as well as any
   changes that would alter entity field-format syntax (or add new fields), e.g.
   URI encoding/handling) `**`whose execution will be deferred`**` until immediately after
   the demo concludes.)`
      * _explicit **version control** policy for reference CVs_
      * _detailed plan for handling app-layer aggregations of CV-term query
      results to **best serve users' search requests**:_
         * _**LCA computation** and implicit matching of terms via shared ontological lineage_
         * _keyword-set association/**tagging**/decoration_
         * _**synonym handling**_
         * _etc._
      * _"assay type" seems like a bad gloss for "type of material," since it sounds like
      it denotes "experiment type" and not "a category of physical object." Flagged
      for renaming._
      * _policy specifying (or standardizing or prohibiting or ...?) a **term-addition
      request process** between CFDE and CV owners (active and ongoing between HMP
      and OBI, e.g.: terms are being added on request; CV managers are responsive),
      driven by usage needs identified by DCC clients_
      * _are **URIs better than bare CV terms** in terms of C2M2 field values?_
         * _what sort of URI support do CVs already provide?_
         * _how deeply can we leverage their own preexisting constructs without
         having to handle maintenance, synchrony, version, etc., issues ourselves?_
         * _can we establish a uniform URI policy to cover all C2M2-referenced CVs,
         or will we need to establish multiple policies for different CVs?_
      * _establish and execute some sort of survey process to create
      consensus on **which particular CVs look like the best final selections**
      to serve as sanctioned C2M2 reference sets (e.g. OBI vs. BAO); criteria:_
      	* _how comprehensive is a CV's coverage of the relevant ontological space?_
      	* _how responsive are the CV owners to change requests?_
      * _detailed ETL-construction usage plan: should we pre-select sub-vocabularies of
      sanctioned CVs to distribute to ETL generators, updating these CFDE-blessed
      CV subsets on an ongoing basis (as new term requirements roll in from
      client metadata sources (DCCs) as they try to model their respective datasets)?_

#### Level 1 metadata submission examples: Data Package JSON Schema and example TSVs

A JSON Schema document -- implementing
[Frictionless Data](https://frictionlessdata.io/)'s
"[Data Package](https://frictionlessdata.io/data-package/)"
container meta-specification -- defining the Level 1 TSV collection is
[here](../draft-C2M2_JSON_Schema_datapackage_specs/C2M2_Level_1.datapackage.json);
an example Level-1-compliant TSV submission collection can be found
[here](../draft-C2M2_example_submission_data/HMP__sample_C2M2_Level_1_bdbag.contents/)
(as a bare collection of TSV files) and
[here](../draft-C2M2_example_submission_data/HMP__sample_C2M2_Level_1_bdbag.tgz)
(as a packaged BDBag archive).

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

The (**presently out-of-date**) JSON Schema document specifying the full Level 2 C2M2 TSV
collection is [here](../draft-C2M2_JSON_Schema_datapackage_specs/full_C2M2_datapackage_spec.json);
example Level-2-compliant TSV submissions will be found **here**.
