# The Common Fund Data Ecosystem Crosscut Metadata Model (CFDE C2M2)

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
two less-complex C2M2 variants: Level 0 (the simplest: 
basic metadata describing a collection of files) and Level
1 (which introduces core experimental resources like
samples and subjects; search targets like the anatomical
source for a given tissue sample; host species taxonomy;
and basic support for assigning experimental resources
to projects and sub-projects. (Proposals for Levels 2 and
3 are currently in first-round rough draft.)