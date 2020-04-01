# Glossary

##### Biospecimen
A material collected from an organism, a cell culture, or a material containing organisms, such as an environmental material. 

##### CFDE Asset Manifest
A collection of *Assets* described by the *CFDE Asset Specification*. The ecosystem will support the concept of a manifest that describes a collection of files. The manifests enable bundling lists of CFDE data assets into a machine-readable file using a common format. Manifests will also be used to publish the complete inventories of data from each DCC, and will enable uniform collection of asset metadata to support indexing of the assets in the CFDE portal.

##### CFDE Asset Specification
Defines the set of attributes used to charaterize an *Asset*. The specification simplifies the discovery of assets hosted at the DCCs with a minimal set of descriptors for each of these files. The types of files that are referenced (e.g., genomic sequence, metagenomic, RNA-Seq, physiological and metabolic data) are flexible and contain a small number of essential elements such as a *GUID*, originating institution (e.g., Broad Institute), assay type (e.g., whole genome/exome, transcriptome, epigenome), file type (e.g., fastq, alignment, vcf, counts), and tissue source and species name for the sample.

##### Dataset
A collection of data, published or curated by a single agent, and available for access or download in one or more formats.

##### DCC
Data Coordinating/Resource Center.

##### Digital File Assets
Digital objects that each of the DCCs host, such as genomic sequence, metagenomic, RNA-Seq, physiological, descriptive, and metabolic data.

##### Entity Relationship Model
Describes the interrelationships of metadata terms. It specifes both the entity (metadata term) and how that term is semantically related to all the other entities in the model. For example, we specify that each Biospecimen must come from a Subject.

##### Event
Specific instances of data gathering for a specific patient, as in a specific surgery or appointment

##### Metadata
A type of information entity usually defined as data about the data, understood as descriptors to understand the context of a dataset. For example, metadata about an FASTQ file may be file size or file creator. Metadata is often classified into descriptive metadata, structural metadata, administrative metadata, and provenance metadata, all of which provide context to the actual data/dataset.

##### Metadata Ingest
Assigning identifiers to the objects and then extracting or creating metadata for these objects.

##### Subject
A study participant (human, animal) from which samples may be obtained.

