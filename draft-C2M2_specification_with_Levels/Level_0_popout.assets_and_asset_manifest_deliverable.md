# Asset Manifest Specification
## Introduction
### Technical Specification for CFDE Data Assets and Instructions for Preparing Data Asset Manifests
This document reviews the technical details for the Common Fund _Data Asset Specification_, explains how to build formal _Data Asset Manifests_ describing collections of experimental data files, and describes how to prepare and submit these manifests to the CFDE database. To understand this process, we will review the Crosscut Metadata Model (C2M2), which is used to describe experimental resources. C2M2 is divided into numbered "levels" that reflect increasing degrees of complexity of data and metadata descriptions. C2M2 Level 0 (the subject of this document and in which _data assets_ and the _data asset manifest_ are defined) is the minimum information needed to describe a basic inventory of all of a DCC's digital files; higher C2M2 levels will be useful in supporting queries based on more complex experimental metadata via the CFDE portal.

## Background
### The CFDE Crosscut Metadata Model (C2M2)

The Common Fund Data Ecosystem group is creating a new software system centered around the Crosscut Metadata Model (C2M2), a flexible technical standard for modeling biomedical experimental resources and data at any of the several predefined levels of model complexity. This system is designed to support powerful cross-dataset and cross-institute searches, custom aggregation of experimental data, and scale-powered statistical analysis methods for the biomedical research community, all at an unprecedented scope.

Using the C2M2 system, Common Fund Data Coordinating Centers ([DCCs](./draft-C2M2_specification_with_Levels_glossary.md#dcc)) will be able to share structured information ([metadata](./draft-C2M2_specification_with_Levels_glossary.md#metadata)) about their experimental resources with the research community, widening and deepening access to usable observational data and accelerating discovery.

### DCC Metadata Submissions

DCCs will collect and provide metadata to the CFDE describing experimental resources within their purview. Each metadata submission will take the form of a collection of tab-separated value (TSV) files. Precise formatting requirements for these TSV collections will be specified by JSON schema documents implementing the [Data Package](http://frictionlessdata.io/docs/data-package/) meta-specification published by the [Frictionless Data](http://frictionlessdata.io/) group. These schemas will be used by the CFDE software infrastructure to automatically validate submission format compliance and metadata integrity during the [metadata ingestion](./draft-C2M2_specification_with_Levels_glossary.md#metadata-ingest) process.

The CFDE will offer the DCCs several alternative metadata submission formats, all of which will be automatically interoperable with the
C2M2 system. These alternative formats are arranged in levels tiered by increasing complexity and reflecting anticipated differences in the relative richness of metadata producible by different DCCs at any time. The expectation will be that the metadata submitted and managed by a DCC will be able to transition, over time, through increasingly rich C2M2 modeling levels as the life cycle of the DCC/CFDE technical interaction progresses, which will enable increasingly powerful downstream applications.

## Technical Specification
### C2M2 Level 0: A Basic Metadata Manifest of Digital File Assets

This C2M2 Level 0 specification defines a **minimal valid C2M2 instance.** DCC metadata submissions at this level of model complexity will be the easiest to produce and will support the simplest available functionality implemented by downstream C2M2-driven applications.

### Level 0 Submission Process Overview

Metadata submissions by the DCCs to the CFDE that are compliant with C2M2 Level 0 will consist of two TSV files:

- `file.tsv` will be a **[manifest](./draft-C2M2_specification_with_Levels_glossary.md#cfde-asset-manifest) of [digital file assets](./draft-C2M2_specification_with_Levels_glossary.md#digital-file-assets)** that a DCC wants to introduce into the C2M2 metadata ecosystem. The properties of the `file` entity in the C2M2 Level 0 model (see below for the model
diagram and a list of property definitions) will serve as column headers for `file.tsv` and each TSV row will represent a
single `file`. DCCs will prepare `file.tsv` using data describing digital files within their management purview.

- `namespace.tsv` will serve as a formal structural placeholder for a `namespace` identifier, which will be assigned to each DCC by the CFDE. The CFDE will create and furnish a `namespace.tsv` file for each DCC to include with Level 0 submissions.

C2M2 Level 0 encodes the most basic file metadata; its use by downstream applications will be limited to informing the least specific level of data accounting, querying, and reporting.

|_Level 0 Model Diagram_|
|:---:|
|![Level 0 model diagram](../draft-C2M2_ER_diagrams/Level-0-C2M2-model.png "Level 0 model diagram")|

### Level 0 Technical Specification: Properties of the `file` Entity

**Required: `id_namespace` `id` `sha256|md5`**

|Property|Description|
|:---:|:---|
| `id_namespace` | String identifier assigned by the CFDE to the DCC managing this `file`. The value of this property will be used together with `id` (assigned to each `file` by the DCC that owns it) as a paired-key structure formally identifying Level 0 `file` entities within the total C2M2 data space.|
| `id` | Unrestricted-format string identifying this `file`, assigned by the DCC managing it. Can be any string as long as it uniquely identifies each `file` within the scope of a single Level 0 metadata submission. |
| `size_in_bytes` | The size of this `file` in bytes. This varies, even for "copies" of the same `file`, across differences in storage hardware and operating systems. The CFDE does not require any particular method of byte computation; file size integrity metadata will be provided in the form of checksum data in the `sha256` and/or `md5` properties. `size_in_bytes` will instead underpin automatic reporting of basic storage statistics across different C2M2 collections of DCC metadata.|
| `sha256` | CFDE-preferred file checksum string--the output of the SHA-256 cryptographic hash function after being run on this `file`. One or both of `sha256` and `md5` is required. |
| `md5` | Permitted file checksum string--the output of the MD5 message-digest algorithm after being run as a cryptographic hash function on this `file`. One or both of `sha256` and `md5` is required. The CFDE recommends using the SHA-256 algorithm if feasible, but we recognize the nontrivial overhead involved in recomputing these hash values for large collections of files, so if MD5 hashes have already been generated, then the CFDE will accept them. |
| `persistent_id` | A persistent, resolvable URI generated by a DCC (e.g., using the CFDE minid server) and permanently attached to this `file`. It serves as a permanent address to which landing pages, which summarize metadata associated with this `file`, and other relevant annotations and functions can eventually be attached, including (optionally) resolution to a network location from which the `file` can be downloaded. Actual network locations must not be embedded directly within this identifier; one level of indirection is required to allow network addresses to change over time as files are moved around. |
| `filename` | A filename with no prepended PATH information. |

## Schema
### Level 0 Metadata Submission: frictionless.io `datapackage.json` Schema Specification

The JSON schema document formally specifying all data constraints on Level 0 TSVs is located
[here](../draft-C2M2_JSON_Schema_datapackage_specs/Level_0_datapackage_spec.json), and
an example Level-0-compliant TSV submission can be found [here](../draft-C2M2_example_submission_data/HMP__sample_C2M2_Level_0_bdbag.contents/file.tsv) (just the `file.tsv` portion) and [here](../draft-C2M2_example_submission_data/HMP__sample_C2M2_Level_0_bdbag.tgz) (as a full BDBag archive).
