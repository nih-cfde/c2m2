This document defines C2M2 Level 0, which is the simplest
of several increasingly complex variants of the Crosscut
Metadata Model (C2M2).

## Background
### The Common Fund Data Ecosystem's Crosscut Metadata Model (CFDE C2M2)

The Common Fund Data Ecosystem group is creating a new
software system centered around the Crosscut
Metadata Model (C2M2), a flexible technical standard
for describing biomedical experimental resources and data
at any of several pre-defined levels of model complexity.
The purpose of this new system is to support powerful
cross-dataset searches, custom aggregation of experimental
data, and scale-powered statistical analysis methods for the
biomedical research community at an unprecedented scope.

Using this system, data coordinating centers
([DCCs](../draft-CFDE_glossary/glossary.md#DCCs)) can
share structured information ([metadata](../draft-CFDE_glossary/glossary.md#metadata))
about their experimental resources with the research
community, dramatically widening access to usable
observational data and accelerating discovery.

### DCC metadata submissions

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

## C2M2 Level 0
#### A basic metadata manifest describing a collection of digital file assets

C2M2 Level 0 defines a **minimal valid C2M2 instance.** Data submissions
at this level of metadata richness will be the easiest to produce, and will
support the simplest available functionality implemented by
downstream applications.

### Level 0 submission process: overview

Metadata submissions at Level 0 will consist of two TSV
files.

The first (named `file.tsv`) will represent a
**[manifest](../draft-CFDE_glossary/glossary.md#CFDE-asset-manifest) or inventory
of digital file assets** that a DCC wants to introduce into
the C2M2 metadata ecosystem. The properties listed for the
`file` entity in the C2M2 Level 0 model (see below for a model
diagram and property definitions) will serve as the column
headers for `file.tsv`; each TSV row will represent a
single `file`. `file.tsv` will be prepared by the DCC based
on the collection of digital files within their purview.

The second TSV (named `namespace.tsv`) will serve as a formal
structural placeholder for a `id_namespace` identifier,
which will be assigned to each DCC by CFDE. CFDE will
create and furnish a `namespace.tsv` file for each DCC
to be used for Level 0 submissions.

C2M2 Level 0 encodes the most basic file metadata:
its use by downstream applications will be
limited to informing the least specific level of data
accounting, querying and reporting.

|_Level 0 model diagram_|
|:---:|
|![Level 0 model diagram](../draft-C2M2_ER_diagrams/Level-0-C2M2-model.png "Level 0 model diagram")|

### Level 0 technical specification: properties of the `file` entity

**Required: `id_namespace` `id` `sha256|md5`**

|property|description|
|:---:|:---|
| `id_namespace` | String **identifier assigned by CFDE to the DCC managing this `file`**. The value of this property will be used together with `id` (assigned to each `file` by the DCC that owns it) as a **paired-key structure formally identifying Level 0 `file` entities** within the total C2M2 data space.|
| `id` | Unrestricted-format **string identifying this `file`, assigned by the DCC managing it**. Can be any string as long as it **uniquely identifies each `file`** within the scope of a single Level 0 metadata submission. |
| `size_in_bytes` | The **size of a `file` in bytes**. This varies (even for "copies" of the same `file`) across differences in storage hardware and operating system. CFDE does not require any particular method of byte computation: file size integrity metadata will be provided in the form of checksum data in the `sha256` and/or `md5` properties. `size_in_bytes` will instead underpin automatic reporting of basic storage statistics across different C2M2 collections of DCC metadata.|
| `sha256` | **CFDE-preferred** file checksum string: the output of the SHA-256 cryptographic hash function after being run on this `file`. One or both of `sha256` and `md5` is required. |
| `md5` | **Permitted** file checksum string: the output of the MD5 message-digest algorithm after being run as a cryptographic hash function on this `file`. One or both of `sha256` and `md5` is required. (CFDE recommends SHA-256 if feasible, but we recognize the nontrivial overhead involved in recomputing these hash values for large collections of files, so if MD5 values have already been generated, CFDE will accept them.) |
| `uri` | **A persistent, resolvable URI generated by a DCC** (using, e.g., our minid server) **and permanently attached to this `file`**, to serve as a permanent address to which landing pages (which summarize metadata associated with this `file`) and other relevant decorations can eventually be attached to this `file`, including (optionally) resolution to a network location from which the `file` can be downloaded. **Actual network locations must not be embedded directly within this identifier**: one level of indirection is required to guard against changes in specific network-location data over time as files are moved around. |
| `filename` | A filename with no prepended PATH information. |

### Level 0 metadata submission examples: schema and example TSVs

The JSON Schema document specifying the Level 0 TSV is
[here](../draft-C2M2_JSON_Schema_datapackage_specs/Level_0_datapackage_spec.json);
example Level-0-compliant TSV submissions can be found **here**, **here** and **here**.

