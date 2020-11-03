# Documentation Overview

Technical specs and docs for CFDE-CC products

This repository hosts all of the documentation and specifications for CFDE-CC products relevant to DCC members of the CFDE.

Currently, it houses the C2M2 technical documentation. Eventually it will also contain documentation for other products.


# Updating the documentation in the public documentation site

This repo is a sub-module of https://github.com/nih-cfde/published-documentation which is rendered at https://cfde-published-documentation.readthedocs-hosted.com/en/latest/

To update https://cfde-published-documentation.readthedocs-hosted.com/en/latest/ you only need to update this repository. The published-documentation repo will automatically pull changes and do two major actions:

- attempt to render them as a preview site for your preview
- make a PR to incorporate your changes into the master branch

You should use the preview site to check that the changes look the way you want. If they do, you should positively review the PR to the master branch so it can be merged in.

## Detailed instructions for updating the

### Preview site

The published-documentation repo checks hourly for changes to the master branch of this repository. If it finds changes, it automatically:

- makes a branch called update-specsdocs-preview with the changes
- makes a PR to merge that branch into specspreview
- runs a series of build checks

If those build checks all pass, it will then automatically merge update-specsdocs-preview into specspreview, and will build a preview site visible at: https://cfde-published-documentation.readthedocs-hosted.com/en/specspreview/

There are three possible reasons the PR might not automatically merge:

- The most likely reason, is that the preview branch needs to be refreshed.


creates a PR in published-documentation from update-specsdocs-preview

https://cfde-published-documentation.readthedocs-hosted.com/en/preview/
