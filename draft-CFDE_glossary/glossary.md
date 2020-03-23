# CFDE Glossary

## Controlled Vocabulary

**Asset** - a sample or a file.

**Biospecimens** - a material collected from an organism, a cell culture or a material containing organisms, such as an environmental material 

**Data object** - a region of storage that contains a value or group of values. Each value can be accessed using its identifier or a more complex expression that refers to the object. In addition, each object has a unique data type.

**DATS** - [DAta Article Tag Suite](https://github.com/datatagsuite/README) is a data model for represented key information about datasets with an emphasis on data discovery and data findability, which has inspired the creation of the NIH-C2M2 model. The [DATS model is expressed as json schema](https://datatagsuite.github.io/docs/html/dats.html). Associated JSON-LD context files support search engine optimization owing to mapping into [schema.org](https://schema.org) and [dcat](://www.w3.org/TR/vocab-dcat-2/). Mappings into biological entities are also available via [obofoundry resources](http://www.obofoundry.org). 

**DERIVA** - Discovery Environment for Relational Information and Versioned Assets. A suite of tools and services that are designed to significantly reduce the overhead and complexity of creating and managing complex, big datasets. DERIVA provides a digital asset management system for scientific data to streamline the acquisition, modeling, management, and sharing of complex, big data, and provides interfaces so that these data can be delivered to diverse external tools for big-data analysis and analytic tools.

**Data-generating events** - a Process such as a data acquisition or a data transformation resulting in the creation of file (digital asset)

**Dataset** - A collection of data, published or curated by a single agent, and available for access or download in one or more formats.

**FAIR/FAIRness/FAIRshake** 

**Figshare** - an online open access repository where researchers can preserve and share their research outputs, including figures, datasets, images, and videos.

**File**

**Frictionless Data Package** - a format specification produced Open Knowledge Foundation supported Frictionless.io organization. It aims shortens the path from data to insight with a collection of specifications and software for the publication, transport, and consumption of data. This kills the cycle of find/improve/share that makes for a dynamic and productive data ecosystem.

**GUID**: Globally-Unique IDentifier is A 128-bit unique identifier used to uniquely identify entity is theory as mordern hashing functions used to generate those make identifier collisions (the event of the function producing the same sequence) highly unlikely (but not impossible).

**Globus Automate** - a distributed research automation platform that addresses the problem of securely and reliably automating, for many thousands of scientists, sequences of data management tasks that may span locations, storage systems, administrative domains, and timescales, and integrate both mechanical and human inputs.

**Insignia**

**Metadata** - a type of information entity usually defined as `data about the data`, understood as descriptors allowing to understand the context of a dataset. For instance, metadata about say an FASTQ file would be things such as `file size` or `file creator`. Metadata is often classified into `descriptive metadata`, `structural metadata`, `administrative metadata`, `provenance medata`, all of which provide context to the actual data|dataset.

**POC I/II**

**Project** 

**Organization** - an entity comprising multiple people, such as an institution or an association, that has a particular purpose. (from wikipedia)

**Sample** - see biospecimens.

**Subject** - a study participant (human, animal) from which samples may be obtained.

**Subject Group** - a set of study subjects, often grouped based on a set of criteria or the types of intervention study subjects will undergo.


## File formats and types - 

**CFDE Asset Manifest** is a collection of **asset**s described by the **CFDE Asset Specification**.

**CFDE Asset Specification** defines the set of attributes used to charaterize an **asset**.

**[CFDE Common Metadata Format](https://fair-research.org/deliverables/cfde-metadata-format.html)** specifies a minimal set of attributes (metadata) related to an **asset**

**[Core ER diagram](https://github.com/nih-cfde/cfde-deriva/blob/2019-08/diagrams/cfde-core-model.png)**

**[Core Table Schema](https://github.com/nih-cfde/cfde-deriva/blob/2019-08/table-schema/cfde-core-model.json)**

**[Entity-Relation diagram](https://github.com/nih-cfde/cfde-deriva/blob/2019-10/extractors_and_metadata.GTEx/cfde-core-model.2019.10.21.1430.png)**

**Inventory**

**Metadata manifest**


## Processes

**C2M2 Creation Flow**

**C2M2 Extractor Flow**

**FAIR assessment** - the process of evaluating the level of compliance of a dataset with the FAIR principles. The assessment may be performed with tools such as [FAIRshake](https://fairshake.cloud) or [FAIREvaluator](https://fairsharing.github.io/FAIR-Evaluator-FrontEnd/#!/)

**Globus Automate flow**

**Master Flow**

**metadata ingest**

**[Table Schema to Deriva translation](https://github.com/nih-cfde/cfde-deriva/blob/2019-08/examples/tableschema_to_deriva.py)**



## Software and Tools

**API**: stands for `application programmer interface` and allows developers to manipulate (query, update) remote data sources through specific protocols or specific standards for communication (e.g. REST,SOAP).

**C2M2** stands for `Cross Cut Metadata Model` 

**[CFDE Data Dashboard](https://cfde.derivacloud.org/deriva-webapps/plot/)**

**CFDE Portal**

**[Data citation rubric](https://github.com/nih-cfde/FAIR/blob/master/Demos/FAIRAssessment/data_citation_rubric.py)**

**DATS** - [DAta Article Tag Suite](https://github.com/datatagsuite/README) is a data model for represented key information about datasets with an emphasis on data discovery and data findability, which has inspired the creation of the NIH-C2M2 model. The [DATS model is expressed as json schema](https://datatagsuite.github.io/docs/html/dats.html). Associated JSON-LD context files support search engine optimization owing to mapping into [schema.org](https://schema.org) and [dcat](://www.w3.org/TR/vocab-dcat-2/). Mappings into biological entities are also available via [obofoundry resources](http://www.obofoundry.org). 

**DERIVA**  Discovery Environment for Relational Information and Versioned Assets. A suite of tools and services that are designed to significantly reduce the overhead and complexity of creating and managing complex, big datasets. DERIVA provides a digital asset management system for scientific data to streamline the acquisition, modeling, management, and sharing of complex, big data, and provides interfaces so that these data can be delivered to diverse external tools for big-data analysis and analytic tools.

**DERIVA Catalogue**

**FAIR insignia** 

**FAIRshake** - a tool produced for carrying out `FAIR assessment` [FAIRshake](https://fairshake.cloud). [Clarke et al. FAIRshake: Toolkit to Evaluate the FAIRness of Research Digital Resources, Cell Systems (2019),](https://doi.org/10.1016/j.cels.2019.09.011)

**Frictionless Data Package** - a format specification produced Open Knowledge Foundation supported Frictionless.io organization. It aims shortens the path from data to insight with a collection of specifications and software for the publication, transport, and consumption of data. This kills the cycle of find/improve/share that makes for a dynamic and productive data ecosystem.

**Jupyter notebook**

**NPM** 


## Other

# CFDE Glossary

**ASHG** - American Society of Human Genetics. They hold an annual conference that is the largest human genetics and genomics meeting and exposition in the world.


**C2M2** 

**CFDE** - Common Fund Data Ecosystem.

**CFDE Asset Manifest** - a collection of **Asset**s described by the **CFDE Asset Specification**.

**CFDE Asset Specification** - defines the set of attributes used to charaterize an **asset**.

![data asset specification](https://user-images.githubusercontent.com/40363469/66134046-ac16bc80-e5c5-11e9-9b30-66407a3446e5.png)

**CFDE Common Metadata Format** - specifies a minimal set of attributes (metadata) related to an **asset**

![common metadata format](https://user-images.githubusercontent.com/40363469/66134031-a8833580-e5c5-11e9-9cc8-5e4b275fa20c.png)

**CFDE Query Portal**

**Common Fund Programs**
  * 4D Nucleome
  * GTEx
  * HMP
  * KidsFirst
  * LINCS
  * Metabolomics
  * SPARC


**DRAFT-placeholder def stub to test anchor targets**<a name="dummy_def"></a>

