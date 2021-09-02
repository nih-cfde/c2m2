#!/usr/bin/env python3

##########################################################################################
#                                SCRIPT PROVENANCE
##########################################################################################
# 
# Arthur Brady (Univ. of MD Inst. for Genome Sciences) wrote this script to automatically
# load and summarize (via term-tracking TSV files) controlled-vocabulary term usage across
# all core resource entity records in a given C2M2 submission instance to assist with
# submission preparation prior to ingestion into a central CFDE database.
# 
# Creation date: 2020-05-17
# Lastmod date unless I forgot to change it: 2021-03-16
# 
##########################################################################################

import os
import json
import re
import sys

##########################################################################################
##########################################################################################
##########################################################################################
#                                USER-DEFINED PARAMETERS
##########################################################################################
##########################################################################################
##########################################################################################

##########################################################################################
# Directory containing full CV reference info (see below, 'cvFile' dictionary, for file
# list).

cvRefDir = './external_CV_reference_files'

##########################################################################################
# Directory in which C2M2 core submission TSVs (for the purposes of this script,
# this means 'file.tsv' and 'biosample.tsv') have been built and stored, prior to running
# this script.

submissionDraftDir = './draft_C2M2_submission_TSVs'

##########################################################################################
# Directory into which new TSVs generated by this script will be written summarizing all
# controlled vocabulary term usage throughout this C2M2 instance.

outDir = './autogenerated_C2M2_term_tables'

##########################################################################################
##########################################################################################
##########################################################################################
#                          CONSTANT PARAMETERS: DO NOT MODIFY
##########################################################################################
##########################################################################################
##########################################################################################

##########################################################################################
# Map of CV names to reference files. These files should be present in cvRefDir before
# running this script.

cvFile = {
   
   'EDAM' : '%s/EDAM.version_1.25.tsv' % cvRefDir,
   'OBI' : '%s/OBI.version_2021-04-06.obo' % cvRefDir,
   'Uberon' : '%s/uberon.version_2021-02-12.obo' % cvRefDir
}

##########################################################################################
# TSV filenames to scan for term usage. These files should be present in
# submissionDraftDir before running this script.

targetTSVs = ( 'file.tsv', 'biosample.tsv' )

##########################################################################################
# Term-tracker data structure.

termsUsed = {
   
   'file_format': {},
   'data_type': {},
   'assay_type': {},
   'anatomy': {}
}

##########################################################################################
##########################################################################################
##########################################################################################
#                   SUBROUTINES (in call order, including recursion)
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

def identifyTermsUsed(  ):
   
   global termsUsed, submissionDraftDir, targetTSVs

   for basename in targetTSVs:
      
      inFile = submissionDraftDir + '/' + basename

      with open( inFile, 'r' ) as IN:
         
         header = IN.readline()

         colNames = re.split(r'\t', header.rstrip('\r\n'))

         currentColIndex = 0

         columnToCategory = dict()

         for colName in colNames:
            
            if colName in termsUsed:
               
               columnToCategory[currentColIndex] = colName

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

   for categoryID in termsUsed:
      
      if categoryID == 'anatomy' or categoryID == 'assay_type':
         
         cv = ''

         if categoryID == 'anatomy':
            
            cv = 'Uberon'

         elif categoryID == 'assay_type':
            
            cv = 'OBI'

         # end if ( categoryID type check )

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

                  else:
                     
                     currentTerm = ''

                     # (Recording is already switched off by default.)

               elif not( re.search(r'^\[Term\]', line) is None ):
                  
                  recording = False

               elif recording:
                  
                  if not ( re.search(r'^name:\s+(\S*.*)$', line) is None ):
                     
                     termsUsed[categoryID][currentTerm]['name'] = re.search(r'^name:\s+(\S*.*)$', line).group(1)

                  elif not ( re.search(r'^def:\s+\"(.*)\"[^\"]*$', line) is None ):
                     
                     termsUsed[categoryID][currentTerm]['description'] = re.search(r'^def:\s+\"(.*)\"[^\"]*$', line).group(1)

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

               ( termURL, name, synonyms, definition ) = re.split(r'\t', line)[0:4]

               currentTerm = re.sub(r'^.*\/([^\/]+)$', r'\1', termURL)

               currentTerm = re.sub(r'data_', r'data:', currentTerm)
               currentTerm = re.sub(r'format_', r'format:', currentTerm)

               if currentTerm in termsUsed[categoryID]:
                  
                  # There are some truly screwy things allowed inside
                  # tab-separated fields in this file. Clean them up.

                  name = name.strip().strip('"\'').strip()

                  definition = definition.strip().strip('"\'').strip()

                  definition = re.sub( r'\|.*$', r'', definition )

                  termsUsed[categoryID][currentTerm]['name'] = name;
                  termsUsed[categoryID][currentTerm]['description'] = definition;

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
         
         OUT.write( '\t'.join( [ 'id', 'name', 'description' ] ) + '\n' )

         for termID in termsUsed[categoryID]:
            
            termDesc = ''

            if 'description' in termsUsed[categoryID][termID]:
               
               termDesc = termsUsed[categoryID][termID]['description']

#            Uncomment the following line if you get a weird error: it'll report all the CV terms processed so far (as you're running the script), and should stop after the first one that causes an error. (If there are any.)
#            progressReport(termID)
            OUT.write( '\t'.join( [ termID, termsUsed[categoryID][termID]['name'], termDesc ] ) + '\n' )

# end sub writeTermsUsed(  )

##########################################################################################
##########################################################################################
##########################################################################################
#                                       EXECUTION
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

