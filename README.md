# Documentation Overview

# Technical specifications and docs for the Cross Cut Metadata Model 



# Updating the Documentation in the Public Documentation Site

## Overview

This repo is a sub-module of https://github.com/nih-cfde/published-documentation which is rendered at https://docs.nih-cfde.org/en/latest/

To update https://docs.nih-cfde.org/en/latest/ you only need to update this repository. The published-documentation repo will automatically pull changes and do two major actions:

- attempt to render them as a preview site for your preview
- make a PR to incorporate your changes into the `stable` branch

You should use the preview site to check that the changes look the way you want. If they do, you should positively review the PR to the master branch so it can be merged in.

## Detailed Instructions for Updating the Published Documentation Website

### Make your desired changes

 All changes to files in this repo should be made in this repo (https://github.com/nih-cfde/C2M2). The published-documentation repo checks hourly for changes to the `master` branch of this repository.

 We recommend working in a personal branch, and pushing those changes to `master` once you are happy with them.

For changes to content, there are no special considerations except for linking.
 - if you are linking to other docs *within* this repo, use relative links
 - if you are linking to the *glossary*, you need to use a full link to the rendered version of the docs, for e.g. `[asset inventory](https://cfde-published-documentation.readthedocs-hosted.com/en/latest/CFDE-glossary/#asset-inventory)`

If you are adding or removing pages, or otherwise changing how the navigation of the pages should work, you do that using `.pages` files.

- Directories without a `.pages` file will have their contents rendered in alphabetical order, using the yaml header information for page titles if available, or the first header in the markdown file as the page title
- Directories with a `.pages` file will have their contents rendered according to the specifications in the `.pages` file:
  - `title: XXX` will render that folder navigation title as XXX
  - you can redundantly hide a folder and its contents with `hide: true`
  - you can order the contents of the directory with `nav:`
     - `nav:` should be followed by an ordered list of files as bullet points. Be sure to nest bullets with spaces. Tabs will cause it to fail.
     - It will render the file title from the yaml header or first header line as above. You can override this behavior by specifying a file title as in `First page: page1.md`
  - you can make a link to a different web address with `- Link Title: https://lukasgeiter.com`
- For more options and examples see [awesome pages documentation](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)

### Check the preview site

The published-documentation repo checks hourly for changes to the master branch of this repository. If it finds changes, it automatically:

- makes a branch called update-C2M2-preview with the changes
- makes a PR to merge that branch into C2M2preview
- runs a series of build checks

If those build checks all pass, it will then automatically merge update-C2M2-preview into C2M2preview, close the pull request, and build a preview site for you to browse at: https://cfde-published-documentation.readthedocs-hosted.com/en/C2M2preview/

If your preview site looks as expected, go to [Publishing your changes](#Publishing-your-changes)

If your preview site does not look right, continue making changes to https://github.com/nih-cfde/C2M2 or look at Troubleshooting below.

#### Troubleshooting

If this preview pull request runs and closes itself without you doing anything, then it worked as intended!

If the preview pull request does not merge and close itself, then there was a problem.

There are three possible reasons the PR might not automatically merge into C2M2preview:

- The most likely reason, is that the preview branch needs to be refreshed, that a stale preview was already in the C2M2preview branch and is clashing with yours. To fix it delete the C2M2preview branch and wait for the next hourly run
- If it's a fresh preview branch, your changes may have made the repos incompatible. Tag @Acharbonneau in your PR and she'll help
- Very occasionally, the github robot fails for server related reasons when there is otherwise no problem. Removing the C2M2preview branch so that the robot tries again generally fixes this. Or tag @Acharbonneau


### Publishing your changes

The published-documentation repo checks hourly for changes to the master branch of this repository. If it finds changes, it also automatically:

- makes a branch called update-c2m2 with the changes
- makes a PR to merge that branch into stable
- runs a series of build checks

Once you are happy with your preview site, approve this matching PR, and it will be merged in. An administrator has to merge this PR into the https://github.com/nih-cfde/published-documentation repository, and they are automatically tagged by the PR robot. However, if you find they are taking an excessively long time, please re-tag @Acharbonneau
