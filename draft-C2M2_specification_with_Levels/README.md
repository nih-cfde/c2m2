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
C2M2 ecosystem. These alternative formats will be offered in
levels tiered according to increasing complexity, reflecting
anticipated differences in the relative richness of metadata
available to different DCCs at any one time. The general
expectation will be that the metadata submitted and managed by a
DCC will be able to transition, over time, through
increasingly rich formats -- enabling increasingly powerful downstream
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
iteratively change a complex model than it is to build
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
more operationally complex DCCs. Newer or smaller DCCs, in contrast, may
not have currently enough information readily available
to feasibly model their experimental resources using the
full model; CFDE aims to fully support cases like these by
offering simpler but still well-structured metadata
models, lowering barriers to entry into the data ecosystem.

Simpler C2M2 metadata models must be maintained by
CFDE in such a way as to maximize interoperability with
more complex C2M2 models, and the whole system should be
structured to minimize the negative side effects of model
changes. All of these considerations have led to the
notion of C2M2 [richness levels](../draft-CFDE_glossary/glossary.md#richness-levels):
canonical variants of C2M2 which are benchmarked at
increasing levels of model complexity.

In addition to the full C2M2 model, CFDE presently offers
two less-complex C2M2 variants: [Level 0](#level-0) (the simplest: 
basic metadata describing a collection of files) and
[Level 1](#level-1)
(which introduces core experimental resources like
samples and subjects; search targets like the anatomical
source for a given tissue sample; host species taxonomy;
and basic support for assigning experimental resources
to projects and sub-projects. (Proposals for Levels 2 and
3 are currently in [first-round rough draft](../draft-C2M2_Levels_spreadsheets/Level_definitions.csv).)

### Level 0

C2M2 Level 0 defines a minimal valid C2M2 instance; data submissions
at this richness level will be the easiest to produce, and will
support the most basic available functionality implemented by
downstream applications.

|_Level 0 model diagram_|
|:---:|
|![Level 0 model diagram](../draft-C2M2_ER_diagrams/Level-0-C2M2-model.png "Level 0 model diagram")|

#### Level 0 submission process: overview

Metadata submissions at Level 0 will consist of a single TSV
file with a header row, describing a collection of digital
files owned or managed by a DCC. The properties listed
for the Level 0 `file` entity (see next subsection for
definitions) will serve as the TSV's column headers; each
TSV row will represent a single file. The Level 0 TSV
itself thus represents a flat
[manifest](../draft-CFDE_glossary/glossary.md#CFDE-asset-manifest)
or inventory of the digital files that a DCC wants to
introduce into the C2M2 metadata ecosystem.

This level encodes only the most basic of file metadata
information; its use by downstream applications will be
limited to informing the least specific level of data
accounting and reports.

#### Level 0: `file` properties

* `id_namespace`
* `id`
* `size_in_bytes`
* `sha256`
* `md5`
* `uri`
* `filename`

#### Level 0 submissions: schema and example TSVs

The JSON Schema document specifying the Level 0 TSV can
be found **here**; example Level-0-compliant TSV submissions
can be browsed **here**, **here** and **here**.

### Level 1

(intro)

|_Level 1 model diagram_|
|:---:|
|![Level 1 model diagram](../draft-C2M2_ER_diagrams/Level-1-C2M2-model.png "Level 1 model diagram")|

(spec)

(defs)

#### Level 1 submissions: schema and example TSVs

The JSON Schema document specifying the Level 1 TSV
collection can be found **here**; example Level-1-compliant
TSV submissions can be browsed **here**, **here** and
**here**.
