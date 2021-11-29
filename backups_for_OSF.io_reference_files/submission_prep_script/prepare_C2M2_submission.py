#!/usr/bin/env python3

##########################################################################################
#                                          SCRIPT PROVENANCE
##########################################################################################
# 
# Arthur Brady (University of Maryland Institute for Genome Sciences) wrote this script to
# scan and summarize (via term-tracking TSV files) controlled-vocabulary term usage across
# a C2M2 instance to assist with datapackage preparation prior to submission for
# publication in the CFDE portal.
# 
# Creation date: 2020-05-17
# Lastmod date unless I forgot to change it: 2021-11-29
# 
##########################################################################################

import os
import json
import re
import sys
import gzip
from pathlib import Path

##########################################################################################
##########################################################################################
##########################################################################################
#                                          USER-DEFINED PARAMETERS
##########################################################################################
##########################################################################################
##########################################################################################

##########################################################################################
# Directory containing full CV reference info (see below, 'cvFile' dictionary, for file
# list).

cvRefDir = 'external_CV_reference_files'

##########################################################################################
# Directory in which C2M2 core submission TSVs (for the purposes of this script,
# this means 'file.tsv' and 'biosample.tsv') have been built and stored, prior to running
# this script.

submissionDraftDir = 'draft_C2M2_submission_TSVs'

##########################################################################################
# Directory into which new TSVs generated by this script will be written summarizing all
# controlled vocabulary term usage throughout this C2M2 instance.

outDir = 'autogenerated_C2M2_term_tables'

##########################################################################################
##########################################################################################
##########################################################################################
#                                  CONSTANT PARAMETERS: DO NOT MODIFY
##########################################################################################
##########################################################################################
##########################################################################################

##########################################################################################
# Map of CV names to reference files. These files should be present in cvRefDir before
# running this script.

cvFile = {
    
    'EDAM' : '%s/EDAM.version_1.25.tsv' % cvRefDir,
    'NCBI' : '%s/ncbi_taxonomy.tsv.gz' % cvRefDir,
    'OBI' : '%s/OBI.version_2021-08-18.obo' % cvRefDir,
    'OBI_provisional' : '%s/OBI.provisional_terms.2021-08-04.tsv' % cvRefDir,
    'Uberon' : '%s/uberon.version_2021-11-12.obo' % cvRefDir,
    'DO' : '%s/doid.version_2021-10-12.obo' % cvRefDir,
    'Ensembl' : '%s/ensembl_genes.tsv' % cvRefDir,
    'PubChem_compound' : '%s/compound.tsv.gz' % cvRefDir,
    'PubChem_substance' : '%s/substance.tsv.gz' % cvRefDir
}

##########################################################################################
# TSV filenames to scan for term usage. These files should be present in
# submissionDraftDir before running this script.

targetTSVs = ( 'file.tsv', 'biosample.tsv', 'biosample_disease.tsv', 'biosample_gene.tsv', 'biosample_substance.tsv', 'subject_disease.tsv', 'subject_role_taxonomy.tsv', 'subject_substance.tsv' )

##########################################################################################
# Term-tracker data structure.

termsUsed = {
    
    'anatomy': {},
    'assay_type': {},
    'data_type': {},
    'disease': {},
    'file_format': {},
    'ncbi_taxonomy': {},
    'gene': {},
    'substance': {}
}

##########################################################################################
##########################################################################################
##########################################################################################
#                         SUBROUTINES (in call order, including recursion)
##########################################################################################
##########################################################################################
##########################################################################################

####### progressReport ###################################################################
# 
# CALLED BY: main execution thread
# 
# Print a logging message to STDERR.
# 
#-----------------------------------------------------------------------------------------

def progressReport( message ):
    
    print('%s' % message, file=sys.stderr)

#-----------------------------------------------------------------------------------------
# end sub: progressReport( message )
##########################################################################################

####### die ##############################################################################
# 
# CALLED BY: [everything....]
# Halt program and report why.
# 
#-----------------------------------------------------------------------------------------

def die( errorMessage ):
   
   print('\n   FATAL: %s\n' % errorMessage, file=sys.stderr)

   sys.exit(-1)

#-----------------------------------------------------------------------------------------
# end sub: die( errorMessage )
##########################################################################################

def identifyTermsUsed(  ):
    
    global termsUsed, submissionDraftDir, targetTSVs

    for basename in targetTSVs:
        
        inFile = submissionDraftDir + '/' + basename

        if Path(inFile).is_file():
            
            with open( inFile, 'r' ) as IN:
                
                header = IN.readline()

                colNames = re.split(r'\t', header.rstrip('\r\n'))

                currentColIndex = 0

                columnToCategory = dict()

                for colName in colNames:
                    
                    if colName in termsUsed:
                        
                        columnToCategory[currentColIndex] = colName

                    elif basename == 'subject_role_taxonomy.tsv' and colName == 'taxonomy_id':
                        
                        columnToCategory[currentColIndex] = 'ncbi_taxonomy'

                    elif basename == 'file.tsv' and colName == 'compression_format':
                        
                        columnToCategory[currentColIndex] = 'file_format'

                    currentColIndex += 1

                for line in IN:
                    
                    fields = re.split(r'\t', line.rstrip('\r\n'))

                    for colIndex in columnToCategory:
                        
                        currentCategory = columnToCategory[colIndex]

                        if fields[colIndex] != '':
                            
                            termsUsed[currentCategory][fields[colIndex]] = {}

# end sub: identifyTermsUsed(  )

def decorateTermsUsed(  ):
    
    global termsUsed, cvFile

    categories = list(termsUsed.keys())

    for categoryID in categories:
        
        if categoryID == 'substance':
            
            # Initialize 'compound' now; it wasn't created with the others because it's
            # wholly derived from the 'substance' values (thus not directly used by
            # submitters), so there was nothing to scan for in the drafted tables.
            # Also note 'compound' should not appear in the 'categories' list we're
            # iterating through, for the same reason -- hence the list copy above.
            
            termsUsed['compound'] = {}

            if len(termsUsed[categoryID]) > 0:
                
                progressReport("[heads up -- this is going to take a few minutes longer than it otherwise would, due to the presence of PubChem IDs]")

                cv = 'PubChem_substance'

                refFile = cvFile[cv]

                progressReport("[processing substance file]")

                with gzip.open( refFile, mode='rt' ) as IN:
                    
                    header = IN.readline()

                    for line in IN:
                        
                        line = line.rstrip('\r\n')

                        ( currentSID, currentName, currentDesc, currentSyn, currentLinkedCID ) = re.split(r'\t', line)

                        if currentSID in termsUsed[categoryID]:
                            
                            termsUsed[categoryID][currentSID]['name'] = currentName
                            termsUsed[categoryID][currentSID]['description'] = currentDesc
                            termsUsed[categoryID][currentSID]['synonyms'] = currentSyn
                            termsUsed[categoryID][currentSID]['compound'] = currentLinkedCID

                            # Initialize linked CID record for second-pass scan.

                            termsUsed['compound'][currentLinkedCID] = {}

                        # end if ( we loaded this SID during our input scan )

                    # end for ( line iterator on substance TSV )

                # end with ( open substance TSV for reading )

                progressReport("[done]")
                progressReport("[processing compound file]")

                # Load linked CID records.

                cv = 'PubChem_compound'

                refFile = cvFile[cv]

                with gzip.open( refFile, mode='rt', encoding="latin-1" ) as IN:
                    
                    header = IN.readline()

                    for line in IN:
                        
                        line = line.rstrip('\r\n')

                        ( currentCID, currentName, currentDesc, currentSyn ) = re.split(r'\t', line)

                        if currentCID in termsUsed['compound']:
                            
                            termsUsed['compound'][currentCID]['name'] = currentName
                            termsUsed['compound'][currentCID]['description'] = currentDesc
                            termsUsed['compound'][currentCID]['synonyms'] = currentSyn

                        # end if ( we loaded this CID during our SID processing scan )

                    # end for ( line iterator on compound TSV )

                # end with ( open compound TSV for reading )

                progressReport("[done]")

            # end if ( we have at least one substance term loaded )

        elif categoryID == 'ncbi_taxonomy':
            
            cv = 'NCBI'

            refFile = cvFile[cv]

            with gzip.open( refFile, mode='rt' ) as IN:
                
                header = IN.readline()

                for line in IN:
                    
                    line = line.rstrip('\r\n')

                    ( currentTerm, currentClade, currentName, currentDesc, currentSyn ) = re.split(r'\t', line)

                    if currentTerm in termsUsed[categoryID]:
                        
                        termsUsed[categoryID][currentTerm]['clade'] = currentClade
                        termsUsed[categoryID][currentTerm]['name'] = currentName
                        termsUsed[categoryID][currentTerm]['description'] = currentDesc
                        termsUsed[categoryID][currentTerm]['synonyms'] = currentSyn

                    # end if ( current NCBI taxon ID was used in this submission )

                # end for ( each line in the NCBI Taxonomy DB TSV )

            # end with open( [taxonomy reference TSV], 'r' ) as IN

        elif categoryID == 'gene':
            
            cv = 'Ensembl'

            refFile = cvFile[cv]

            with open( refFile, 'r' ) as IN:
                
                header = IN.readline()

                for line in IN:
                    
                    line = line.rstrip('\r\n')

                    ( currentTerm, currentName, currentDesc, currentSyn, currentTaxID ) = re.split(r'\t', line)

                    if currentTerm in termsUsed[categoryID]:
                        
                        # Ensembl allows null term names; we do not. Auto-copy ID into name field if none exists.

                        if currentName == '':
                            
                            currentName = currentTerm

                        termsUsed[categoryID][currentTerm]['name'] = currentName
                        termsUsed[categoryID][currentTerm]['description'] = currentDesc
                        termsUsed[categoryID][currentTerm]['synonyms'] = currentSyn
                        termsUsed[categoryID][currentTerm]['organism'] = currentTaxID

                    # end if ( current Ensembl gene ID was used in this submission )

                # end for ( each line in the (CFDE-preprocessed-by-species) Ensembl gene DB TSV )

            # end with open( [gene reference TSV], 'r' ) as IN

        elif categoryID == 'anatomy' or categoryID == 'assay_type' or categoryID == 'disease':
            
            cv = ''

            if categoryID == 'anatomy':
                
                cv = 'Uberon'

            elif categoryID == 'assay_type':
                
                # Load the provisional term map first for this one; afterward we'll
                # load the main ontology with destructive overwrites for any conflicts
                # (to defer to published term versions).

                cv = 'OBI_provisional'

            elif categoryID == 'disease':
                
                cv = 'DO'

            # end if ( categoryID type check )

            if cv == 'OBI_provisional':
                
                refFile = cvFile[cv]

                with open( refFile, 'r' ) as IN:
                    
                    header = IN.readline()

                    for line in IN:
                        
                        line = line.rstrip('\r\n')

                        ( termRequester, termStatus, currentTerm, termLabel, termDefinition, termSynonyms ) = re.split(r'\t', line)

                        if currentTerm in termsUsed[categoryID]:
                            
                            termsUsed[categoryID][currentTerm]['name'] = termLabel
                            termsUsed[categoryID][currentTerm]['description'] = termDefinition

                            if termSynonyms == '':
                                
                                termSynonyms = '[]'

                            termsUsed[categoryID][currentTerm]['synonyms'] = termSynonyms

                        # end if ( term was seen )

                    # end for ( each line in provisional OBI term TSV )

                # end with ( open [provisional OBI term TSV] as IN

                cv = 'OBI'

            # end if cv == 'OBI_provisional'

            refFile = cvFile[cv]

            with open( refFile, 'r' ) as IN:
                
                recording = False

                currentTerm = ''

                for line in IN:
                    
                    line = line.rstrip('\r\n')
                
                    matchResult = re.search(r'^id:\s+(\S.*)$', line)

                    if not( matchResult is None ):
                        
                        currentTerm = matchResult.group(1)

                        if currentTerm in termsUsed[categoryID]:
                            
                            recording = True

                            # Wipe out any synonyms we already loaded from a provisional term list, if we did that.
                            # (During EDAM processing (below), a destructive overwrite already happens by default
                            # for this case, so no extra deletion is required.)

                            if 'synonyms' in termsUsed[categoryID][currentTerm]:
                                
                                del termsUsed[categoryID][currentTerm]['synonyms']

                        else:
                            
                            currentTerm = ''

                            # (Recording is already switched off by default.)

                    elif not( re.search(r'^\[Term\]', line) is None ):
                        
                        recording = False

                    elif not( re.search(r'^\[Typedef\]', line) is None ):
                        
                        break

                    elif recording:
                        
                        if not ( re.search(r'^name:\s+(\S*.*)$', line) is None ):
                            
                            termsUsed[categoryID][currentTerm]['name'] = re.search(r'^name:\s+(\S*.*)$', line).group(1)

                        elif not ( re.search(r'^def:\s+\"(.*)\"[^\"]*$', line) is None ):
                            
                            parsedDesc = re.search(r'^def:\s+\"(.*?)(?<!\\)\".*$', line).group(1)

                            if currentTerm == 'UBERON:4300002':
                                
                                # Until this is fixed in the ontology, a typo involving unpaired brackets
                                # makes this one impossible to parse properly.

                                parsedDesc = re.sub(r'\]$', r'', parsedDesc)

                            parsedDesc = re.sub(r'\s*\[[^\]]+\]', r'', parsedDesc)

                            # Remove newline codes and replace with space characters.

                            parsedDesc = re.sub(r'\\n', r' ', parsedDesc)

                            # Trim remaining extremal whitespace.

                            parsedDesc = re.sub(r'^\s+', r'', parsedDesc)
                            parsedDesc = re.sub(r'\s+$', r'', parsedDesc)

                            termsUsed[categoryID][currentTerm]['description'] = parsedDesc

                        elif not ( re.search(r'^synonym:\s+"[^\"]+"\s+EXACT', line) is None ):
                            
                            newSyn = re.search(r'^synonym:\s+"([^\"]+)"\s+EXACT', line).group(1)

                            newSyn = re.sub(r'\\n', r' ', newSyn)

                            newSyn = newSyn.strip().strip('"\'').strip()

                            newSyn = re.sub(r'\"', r'', newSyn)

                            if re.search(r'\|', newSyn) is None:
                                
                                if 'synonyms' in termsUsed[categoryID][currentTerm]:
                                    
                                    termsUsed[categoryID][currentTerm]['synonyms'] = termsUsed[categoryID][currentTerm]['synonyms'] + '|"' + newSyn + '"'

                                else:
                                    
                                    termsUsed[categoryID][currentTerm]['synonyms'] = '"' + newSyn + '"'

                        elif not ( re.search(r'^synonym:\s+"[^\"]+"\s+BROAD', line) is None ):

                            newSyn = re.search(r'^synonym:\s+"([^\"]+)"\s+BROAD', line).group(1)

                            newSyn = re.sub(r'\\n', r' ', newSyn)

                            newSyn = newSyn.strip().strip('"\'').strip()

                            newSyn = re.sub(r'\'', r'', newSyn)

                            if re.search(r'\|', newSyn) is None:

                                if 'synonyms' in termsUsed[categoryID][currentTerm]:
                                    
                                    termsUsed[categoryID][currentTerm]['synonyms'] = termsUsed[categoryID][currentTerm]['synonyms'] + '|"' + newSyn + '"'

                                else:
                                    
                                    termsUsed[categoryID][currentTerm]['synonyms'] = '"' + newSyn + '"'

                        elif not ( re.search(r'^def:\s+', line) is None ):
                            
                            die('Unparsed def-line in %s OBO file: "%s"; aborting.' % ( cv, line ) )

                    # end if ( line-type selector switch )

                # end for ( input file line iterator )

            # end with ( open refFile as IN )

        elif categoryID == 'file_format' or categoryID == 'data_type':
            
            cv = 'EDAM'

            refFile = cvFile[cv]

            with open( refFile, 'r' ) as IN:
                
                header = IN.readline()

                for line in IN:
                    
                    line = line.rstrip('\r\n')

                    ( termURL, name, synonymBlock, definition ) = re.split(r'\t', line)[0:4]

                    currentTerm = re.sub(r'^.*\/([^\/]+)$', r'\1', termURL)

                    currentTerm = re.sub(r'data_', r'data:', currentTerm)
                    currentTerm = re.sub(r'format_', r'format:', currentTerm)

                    if currentTerm in termsUsed[categoryID]:
                        
                        # There are some truly screwy things allowed inside
                        # tab-separated fields in this file. Clean them up.

                        name = name.strip().strip('"\'').strip()

                        synonymBlock = synonymBlock.strip().strip('"\'').strip()

                        synonymField = ''

                        if synonymBlock == '':
                            
                            synonymField = '[]'

                        else:
                            
                            synonyms = re.split(r'\|+', synonymBlock)

                            synonymField = '['

                            first = 1

                            for synonym in synonyms:
                                
                                synonym = re.sub(r'"', r'', synonym)

                                if first == 1:
                                    
                                    synonymField = synonymField + '"' + synonym + '"'

                                    first = 0

                                else:
                                    
                                    synonymField = synonymField + ',"' + synonym + '"'

                            synonymField = synonymField + ']'

                        definition = definition.strip().strip('"\'').strip()

                        definition = re.sub( r'\|.*$', r'', definition )

                        if categoryID == 'file_format' and not( re.search(r'^format', currentTerm) is None ):
                            
                            termsUsed[categoryID][currentTerm] = {}

                            termsUsed[categoryID][currentTerm]['name'] = name
                            termsUsed[categoryID][currentTerm]['description'] = definition
                            termsUsed[categoryID][currentTerm]['synonyms'] = synonymField

                        elif categoryID == 'data_type' and not( re.search(r'^data', currentTerm) is None ):
                            
                            termsUsed[categoryID][currentTerm] = {}

                            termsUsed[categoryID][currentTerm]['name'] = name
                            termsUsed[categoryID][currentTerm]['description'] = definition
                            termsUsed[categoryID][currentTerm]['synonyms'] = synonymField

                    # end if ( currentTerm in termsUsed[categoryID] )

                # end for ( input file line iterator )

            # end with ( refFile opened as IN )

        # end if ( switch on categoryID )

    # end foreach ( categoryID in termsUsed )

# end sub decorateTermsUsed(  )

def writeTermsUsed(  ):
    
    global outDir, termsUsed

    for categoryID in termsUsed:
        
        outFile = '%s/%s.tsv' % ( outDir, categoryID )

        with open(outFile, 'w') as OUT:
            
            if categoryID == 'substance':
                
                OUT.write( '\t'.join( [ 'id', 'name', 'description', 'synonyms', 'compound' ] ) + '\n' )

            elif categoryID == 'compound':
                
                OUT.write( '\t'.join( [ 'id', 'name', 'description', 'synonyms' ] ) + '\n' )

            elif categoryID == 'ncbi_taxonomy':
                
                OUT.write( '\t'.join( [ 'id', 'clade', 'name', 'description', 'synonyms' ] ) + '\n' )

            elif categoryID == 'gene':
                
                OUT.write( '\t'.join( [ 'id', 'name', 'description', 'synonyms', 'organism' ] ) + '\n' )

            else:
                
                OUT.write( '\t'.join( [ 'id', 'name', 'description', 'synonyms' ] ) + '\n' )

            for termID in sorted( termsUsed[categoryID] ):
                
                termDesc = ''

                termSynonyms = '[]'

                # If 'name' is blank, this is a universe-level error!

                if 'name' in termsUsed[categoryID][termID]:
                    
                    if 'description' in termsUsed[categoryID][termID]:
                        
                        termDesc = termsUsed[categoryID][termID]['description']

                    if 'synonyms' in termsUsed[categoryID][termID]:
                        
                        termSynonyms = termsUsed[categoryID][termID]['synonyms']

                        # Synonyms for the categories excluded here are preprocessed by us in advance and shouldn't need help.

                        if categoryID != 'ncbi_taxonomy' and categoryID != 'gene' and categoryID != 'substance' and categoryID != 'compound':
                            
                            if termSynonyms != '' and re.search(r'\|', termSynonyms) is None and re.search(r'^\[', termSynonyms) is None:
                                
                                termSynonyms = '[' + termSynonyms + ']'

                            elif termSynonyms != '' and not(re.search(r'\|', termSynonyms) is None):
                                
                                synonyms = re.split(r'\|+', termSynonyms)

                                termSynonyms = '['

                                first = 1

                                for synonym in synonyms:
                                    
                                    if first == 1:
                                        
                                        termSynonyms = termSynonyms + synonym

                                        first = 0

                                    else:
                                        
                                        termSynonyms = termSynonyms + ',' + synonym

                                termSynonyms = termSynonyms + ']'

                    # end field preprocessing

                    # Uncomment the following line if you get a weird error: it'll report all the CV terms processed so far
                    # (as you're running the script), and should stop after the first one that causes an error. (If there are any.)

                    # progressReport(termID)

                    if categoryID == 'ncbi_taxonomy':
                        
                        OUT.write( '\t'.join( [ termID, termsUsed[categoryID][termID]['clade'], termsUsed[categoryID][termID]['name'], termDesc, termSynonyms ] ) + '\n' )

                    elif categoryID == 'gene':
                        
                        OUT.write( '\t'.join( [ termID, termsUsed[categoryID][termID]['name'], termDesc, termSynonyms, termsUsed[categoryID][termID]['organism'] ] ) + '\n' )

                    elif categoryID == 'substance':
                        
                        OUT.write( '\t'.join( [ termID, termsUsed[categoryID][termID]['name'], termDesc, termSynonyms, termsUsed[categoryID][termID]['compound'] ] ) + '\n' )

                    else:
                        
                        OUT.write( '\t'.join( [ termID, termsUsed[categoryID][termID]['name'], termDesc, termSynonyms ] ) + '\n' )

                else:
                    
                    die('Term \'%s\' has no name: aborting, please check integrity of \'%s\' reference file(s).' % ( termID, categoryID ) )

                # end if ( 'name' in termsUsed[categoryID][termID] )

            # end for ( termID in termsUsed[categoryID] )

        # end with ( open(outFile, 'w') as OUT )

    # end for ( categoryID in termsUsed )

# end sub writeTermsUsed(  )

##########################################################################################
##########################################################################################
##########################################################################################
#                                                    EXECUTION
##########################################################################################
##########################################################################################
##########################################################################################

# Create the output directory if need be.

if not os.path.isdir(outDir) and os.path.exists(outDir):
    
    die('%s exists but is not a directory; aborting.' % outDir)

elif not os.path.isdir(outDir):
    
    os.mkdir(outDir)

# Find all the CV terms used in the draft C2M2 submission in "submissionDraftDir".

identifyTermsUsed()

# Load data from CV reference files to fill out needed columns in C2M2
# term-tracker tables.

decorateTermsUsed()

# Write the term-tracker tables.

writeTermsUsed()


