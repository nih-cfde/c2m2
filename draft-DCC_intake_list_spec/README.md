# Introductory notes

This specification describes the structure of a minimal, basic list
of core experimental resources (at the moment, just files) managed
by a DCC.

Our primary purpose in creating this specification is to define a simple
data-description space which can be used by any DCC to build a basic
structured inventory of experimental resources of potential interest
to external investigators, while requiring only minimal effort overhead
from a DCC (beyond conducting the inventory itself). Beyond facilitating
DCC onboarding into and adoption of the CFDE technologies, this
inventory will serve as a preliminary survey of available
data files managed by each DCC, will help guide future CFDE-DCC
interactions as more detailed metadata modeling and ingestion
progresses, and will also immediately serve as a data substrate
for administrative (dashboard) reporting of basic stats describing
DCC file asset collections (prior to construction of a corresponding
full C2M2 instance).

We will accept intake data as a pair of TSVs: one TSV will encode
metadata for individual files, and the other will describe metadata
associated with the entire asset list object. These TSVs will
be described by a frictionless.io JSON Schema spec, itself defined
by the following model:

# Specification details

```
Xs indicate required fields.

X' (X-prime) means 'one or the other of these two fields is required.'

INTAKE LIST object specification:
X   organization                                 # URL-friendly string unambiguously identifying this DCC
X   contact_name
X   contact_email
X   list_completion_date                         # YYYY-MM-DD
    data_release_version                         # optional tie-in to DCC data release versioning system
X   [list of resource records]                   # TSV format: 'intake_list.tsv' metadata table (describing
                                                 # this block of fields) plus separate 'file_assets.tsv'
                                                 # (describing the fields listed below)

INTAKE FILE ASSET object specification:

   # The first field, here, can serve as a unique identifier for this file.
   
   X uri                                         # A Tag URI instance (cf. http://www.faqs.org/rfcs/rfc4151.html and
                                                 # https://en.wikipedia.org/wiki/Tag_URI_scheme) constructed by
                                                 # concatenating the following two components:

      * project_containment                      # PATH-like '/'-separated list of DCC-assigned project IDs (or
                                                 # any other tree-like sorting system) unambiguously locating this
                                                 # file asset within the DCC's accounting hierarchy. (Can e.g. just be a
                                                 # filesystem path, if all the DCC's assets are stored on the
                                                 # same filesystem, then this might be the simplest solution.)
      * filename                                 # (no preceding path info)

   # ...so a fully-built URI according to this scheme would conform to:
   # 
   #          tag:organization,list_completion_date:project_containment/filename
   # 
   # ...where all the string tokens (except "tag") named above are copies of
   # the same-named fields in this specification.

   # The next two fields together are meant to comprise the philosophical equivalent to
   # a "MIME/media type" specification for bioinformatics data files (although sadly none exists),
   # answering both "how is this file physically formatted?" (e.g. TSV, BAM, FASTQ), and
   # "what is the semantic context within which the data in this file should be processed?"
   # (e.g. sequence reads, allele variant reports, relative abundance estimates).
   
   X    file_format                              # CV: EDAM
   X    data_type                                # CV: EDAM

   X    size_in_bytes                            # (integer)

   # Files may not be network-accessible at any given moment, so the next field is optional
   # (at least with respect to this intake list).

        url                                      # A network-resolvable URL pointing to this file

   # The next field is really a metadata stub -- chosen to be nearly universally applicable
   # to human-medicine-centered bioinformatics data assets -- so we have something on which
   # we can structure, e.g., a pie chart or two in the admin/dashboard display (which should
   # be immediately able to render summary reports using this asset collection).

        body_site_or_product                     # CV: UBERON

   X'   sha256                                   # output of recommended checksum algorithm
   X'   md5                                      # output of alternative checksum algorithm
```

# PFAQ

**Please note that the information below is presently out of date.**

("Probably frequently asked questions": we only received a few so far, so
in the interests of frank disclosure, please note that no reliable estimates
of question frequency have actually been made.)

--------------------------------------------------------------------------------

Q. Are we modeling anything about protocols, subjects or experiments?

A. No, not at the intake list level. We can optionally store metadata
about protocol description documents of arbitrary detail (as file resources),
but anything beyond that in terms of experimental process modeling is out
of scope for this level of information interchange. It is our initial
guess that storing anything at all about subjects will lead immediately
to a dbGaP-style policy chokepoint, which would violate our mandate to
make this initial inventory process as easy as possible. We believe we
can get a decent first-pass sense of the scope of a DCC's local data
ecosystem by asking for an inventory limited to files and samples. Downstream
iterations between the CFDE and DCCs can populate more complex data
or protected-access materials requiring extra processing.

--------------------------------------------------------------------------------

Q. Why sample IDs and not file IDs?

A. Based on our experience serving as a DCC, we're guessing that
typical internal DCC systems will assign unambiguous labels to samples,
but that the same assumption will not hold true for files (which
already come with properties like fully-qualified paths or URLs,
obviating any first-blush need to create a new ID layer within a
given DCC). Our tentative expectation is that each file resource can
be labeled (by us, during intake list processing) in an unambiguous
way which is uniform across all DCCs, facilitating reporting while
not requiring DCCs to create new ID layers for their files that
won't be used for anything but internal CFDE tracking and indexing.
Again: we're trying to minimize the necessary overhead that will be
imposed on each DCC during the inventory process, and this seemed
like the right combination.

--------------------------------------------------------------------------------

Q. When are DCCs expected to begin working on these inventories?

A. Not until after they receive their OT awards.

--------------------------------------------------------------------------------

Q. This is a really simple model; why include three URL fields?

A. The CFDE will be a cloud-based ecosystem: we believe that
drawing attention to the potential for cloud storage, from the
very beginning of the DCC/CFDE integration process, will encourage
DCCs who might be further behind in cloud-service deployment to
maintain a beneficial focus on the relevant technological environment.
For those with already-existing cloud distributions, we want to
preserve -- and promote -- any useful cloud file storage information
that has already been set up, since access info is fundamental to
describing files, and because real examples of instantiated cloud
distros can be used to encourage compliance across the board.

--------------------------------------------------------------------------------

Q. How are you modeling projects, studies, and other administrative
divisions of work and resources within local DCC ecosystems?

A. The proposed project_containment field is designed to allow
DCCs to create arbitrarily deep subdivisions of the scope and purview
of well-defined research groups; to link every inventoried resource with
whatever project or sub-project that resource is natively associated with
within the DCC's local accounting system without having to modify the
overall accounting structure; and to allow DCCs to use whatever native
identifiers they're already using to track project divisions.

The main potential drawback to the proposed pathlike structure is that
it enforces a tree hierarchy on project subdivisions, as opposed to the
'dataset' model in C2M2 which allows fully arbitrary and possibly
weirdly-intersecting set associations. We hope and expect that this
constraint won't pose a problem, but we're keeping an eye out for results.

We do hope the proposed field evades most of the complexity that seems
to arise when trying to more closely model project structures and
substructures.

--------------------------------------------------------------------------------

Q. Precisely who will receive these inventories, specifically how will
they be processed, and who will be available to DCCs if they have
questions while building their inventories?

A. These questions are all fully open as of this writing.

--------------------------------------------------------------------------------

Q. Why not enforce any controlled vocabularies for fields
like 'body_site_or_product'?

A. Again: dead-simple inventory procedure. We mean to avoid (at least
during the intake list generation phase) a processing layer in which DCCs are
forced to translate local descriptive terms into a target CV specified
by us. Some DCCs already use their own CVs; others may store more
free-form data descriptors. Our idea is to first canvas whatever local
description vocabulary that a DCC uses now, and then in subsequent feedback
iterations move (as needed) toward harmonization or conversion to a central
CV system (which we'll ultimately need in order to support cross-DCC querying).

--------------------------------------------------------------------------------

Q. What if a DCC wants to contribute more information? Can you take TSVs
that they already have but that have other info? Or are you only taking
this at this time?

A. We're only looking for this info at this time; we conceive of this
dataset as being the input to a fairly standardized inventory-evaluation
process that informs downstream engagement, so in this context extra data
is likely to simply be ignored. If a DCC has existing metadata that
contains all of this information as a subset and conforms to the
specification as written, then it should be a fairly trivial process
to turn that data into a spec-compliant submission.

--------------------------------------------------------------------------------

Q. You're storing data about files and samples, which are often linked
to one another. Are you modeling these links in any way?

A. No: we're leaving that for the full C2M2 database. Inventories are flat
lists, and are relatively easy to produce; linkages turn flat lists into
relationship-constrained network systems, and we don't want to impose any
unnecessary modeling steps on DCC staff during the intake/inventory phase. We
believe that a list of minimal descriptions of samples and files from a
DCC, as described in this specification, will suffice to give us decent
initial estimates of relative DCC data management experience levels,
dataset complexity, and other indicators that will be needed for us to
formulate an engagement plan for downstream data integration with that DCC.

--------------------------------------------------------------------------------

Q. It looks like the TSV examples have all columns, even if the column
is never used (e.g. s3_url in file_assets); but s3_url is left out of
the json when it isn't used. Is that on purpose?

A. Yes; that was a (possibly lame) attempt to demonstrate our input
flexibility by showing multiple ways of expressing the same null data.
Regardless, the version of the specification presented in this document
is an abstract one and is not formally unified or fully described down to
all implementation-level details (note e.g. that the 'type' field on
resources isn't specifically modeled in the TSV data variants, instead
being encoded in the relevant filenames); once the comment process
has concluded, we'll publish formal (probably frictionless.io, unless
we discover some unexpected reason not to) JSON Schema specs describing
the encoding systems precisely and unambiguously, including
explicit directives on how to encode null data.

--------------------------------------------------------------------------------

Q. At least one DCC hosts their data in-house and has no real intention
of changing that. Does that still fit in your primary_url spec?

A. Sure. In this case they could either share a URL on their in-house
HTTP/FTP/whateverServer, or they could just make up their own url
protocol string and use it to reflect whatever internally consistent system they
want to represent a very abstract version of 'file location', like
exampleDCC://here/is/how/we/organize/this/file.data

Long-term data (and FAIRness) concerns like URL permanence and actual
accessibility of files are out of scope for this inventory. What we're
after here is an internally consistent system for identifying files,
ideally built by directly mapping whatever the DCC is already doing to
organize files, without creating an extra annotation layer during this phase
of data collection.

--------------------------------------------------------------------------------

**Please note in particular** that a bunch of the answers above rely explicitly
on the assumption that the DCC data integration process, at least for
the medium-term future, cannot be fully automated, and will be shepherded
by technical staff within the CFDE core, requiring a few iterations of
discussion between us and a given DCC before full integration is
achieved.

We don't think this is an unreasonable assumption to make at this stage
in the development of the CFDE process model, but we would like to
actively solicit discussion of any objections to this particular
(critical) assumption (while of course also remaining open to any other
criticisms that arise).

