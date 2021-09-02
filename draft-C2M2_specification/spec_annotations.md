`creation_time`

<ul>

<li>We are aware (and unconcerned) that the spec technically renders one particular
**`HH:MM:SS`** value -- "`00:00:00`" -- ambiguous. Forestalling this ambiguity
(by allowing select omissions of constituent sub-segments of `creation_time` string
values as an alternative mechanism to denote missing data, or by introducing
nonstandard and increasingly artificial special-case encodings like "`99:99:99`")
was determined to be of less immediate concern than maintaining the technical
advantages conferred by the (stronger) constraint of requiring a fixed-length
`creation_time` string that remains fully conformant with (a constrained subset
of) the RFC 3339 standard. The canonical C2M2 interpretation of "`00:00:00`" is
thus explicitly defined to be "**`HH:MM:SS`** information unknown" and not
"exactly midnight."</li>

<li>Re: `size_in_bytes` as "the **size of this `file` in bytes**:" this value varies
(even for "copies" of the same file) across differences in storage hardware and
operating system. CFDE does not require any particular method of byte computation
beyond "system-reported size in bytes" -- precise, reproducible file size integrity
metadata will instead be provided in the form of checksum data in the `sha256`
and/or `md5` fields.</li>

---

| `sha256` | **CFDE-preferred** file checksum string: the output of the SHA-256 cryptographic hash function after being run on this file. One or both of `sha256` and `md5` is required. |
| `md5` | **Permitted** file checksum string: the output of the MD5 message-digest algorithm after being run as a cryptographic hash function on this file. One or both of `sha256` and `md5` is required. |

CFDE recommends using SHA-256 for file checksums if feasible, but we recognize
the nontrivial cost involved in (re)computing these hash values for large
collections of files, so if MD5 values have already been generated, we will
accept those.

---

| `file_format` | An EDAM CV term ID identifying the digital format of this file (e.g. TSV or FASTQ). Pattern: `format:[0-9]+` |
| `data_type` | An EDAM CV term ID identifying the type of information stored in this file (e.g. RNA sequence reads). Pattern: `data:[0-9]+` |
| `assay_type` | An OBI CV term ID describing the type of experiment that generated the results summarized by this file. Pattern: `OBI:[0-9]+` |

* these will soon be URIs, not bare terms
* they will soon be expressed by association, not as fields embedded within entity tables

---

| `mime_type` | A MIME type describing this file. |

* we have draft guidance on selecting MIME types for files of various types: <amanda's thing>

---

* biosample

      * _C2M2 models_ `biosample`_s as abstract materials that are directly consumed
      by one or more analytic processes. Simple provenance relationships -- between each
      such_ `biosample` _and the_ `subject` _from which it was originally derived, as well
      as between each_ `biosample` _and any_ `file`_s analytically derived from it -- are
      represented using association tables, with one such table dedicated to each
      relationship type (cf. below, §"Association tables: inter-entity linkages").
      Actual DCC-managed provenance metadata will sometimes (maybe always) represent more complex and
      detailed provenance networks: in such situations, chains of "_`this` _produced_
      `that`_" relationships too complex to model in this C2M2 version will need to be
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
   	library preparation material). Future C2M2 expansions will offer metadata structures to model
   	this entire process in full detail, including representational support for all
   	intermediate_ `biosample`_s, and for the various preparatory processes involved.
   	At current complexity, on the other hand, only_ `subject` _<->_ `some_monolothic_stuff`
   	_<->_ `(FASTQ) file` _can and should be explicitly represented._
         * _The simplifications here are partially necessitated by the fact that
   	   event modeling has been deliberately deferred to future C2M2 versions: as a result,
   	   the notion of a well-defined "chain of provenance" is not modeled at
   	   this point. (More concretely: C2M2 in its current state does not represent
   	   inter-_`biosample` _relationships.)_
         * _The modeling of details describing experimental processes has also been
         assigned to future C2M2 versions._
         * _With both of these (more complex) aspects of experimental metadata
         masked at present, the most appropriate granularity at which a_
         `biosample` _entity should be modeled is as an abstract "material phase"
         (possibly masking what is in reality a chain of multiple distinct materials)
         that enables an analytic (or observational or other scientific) process (which
         originates at a_ `subject` _) to move forward and ultimately produce one or
         more_ `file`_s._  
      * _In practice, a C2M2 submission builder facing such a situation
   	might reasonably create one record for the originating_ `subject` _; create one_
   	`biosample` _entity record; create a_ `file` _record for the FASTQ file produced
   	by the sequencing process; and hook up_ `subject` _<->_ `biosample` _and_
   	`biosample` _<->_ `file` _relationships via the corresponding association tables
   	(cf. below, §"Association tables: inter-entity linkages")._
         * _In terms of deciding (in a well-defined way) specifically which native DCC
         metadata should be attached to this_ `biosample` _record, one
         might for example choose to import metadata (IDs, etc.) describing the
         final pre-sequencer material. The creation of specific rules governing maps
         from native DCC data to (simplified, abstracted) entity records
         is of necessity left up to the best judgment of the serialization staff
         creating each DCC's C2M2 ETL instance; we recommend consistency,
         but beyond that, custom solutions will have to be developed to handle
         different data sources. Real-life examples of solution configurations
	 will be published (as they are collected) to help inform decisionmaking,
	 and CFDE staff will be available as needed to help create mappings between
	 the native details of DCC sample metadata and the approximation that is
	 the C2M2_ `biosample` _entity._
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
         of current modeling, instead attaching a single (slightly upstream)_
         `biosample` _entity -- based on metadata describing_ `M` _-- to both_ `M1.fastq`
         _and_ `M2.fastq`_. As above, final decisions regarding detailed rules
         mapping native DCC data to C2M2 entities are necessarily left to
         DCC-associated investigators and serialization engineers; CFDE staff will be available as needed to offer
         feedback and guidance when navigating mapping issues._

---

* collection

    * words are too-often overloaded; we do not mean to imply here the usual mathematical
        meaning of 'collection' as a 'set of sets', but instead as "a set with no
        predetermined element type"

</ul>