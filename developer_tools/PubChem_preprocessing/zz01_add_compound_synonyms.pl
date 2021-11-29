#!/usr/bin/perl

use strict;

$| = 1;

# PARAMETERS

my $synFile = '000_raw_PubChem_files/Compound/CID-Synonym-filtered.gz';

my $outDir = '001_stupidly_large_reference_tables';

my $compoundTSV = "$outDir/compound.tsv";

my $tempFile = "$compoundTSV.tmp";

# $destroy <- 1 == Don't save intermediate state files:

my $destroy = 1;

# EXECUTION

# Note: this script (correctly, as of time of writing) assumes
# that the records being parsed from the PubChem input files listed above
# will appear sorted (ascending) by numeric CID, and further that the
# maximum CID found in the CID-Synonym-filtered file is less than or
# equal to the maximum CID found in the CID-Title file.

open DB_IN, "<$compoundTSV" or die("Can't open $compoundTSV for reading.\n");

open DB_OUT, ">$tempFile" or die("Can't open $tempFile for writing.\n");

my $header = <DB_IN>;

print DB_OUT $header;

chomp( my $nextDBline = <DB_IN> );

my ( $current_db_id, @someOtherStuff ) = split(/\t/, $nextDBline);

open IN, "zcat $synFile |" or die("Can't open $synFile for reading.\n");

my $synLineCount = 0;

my $insertionCount = 0;

my $current_syn_id = '';

my @current_synonyms = ();

print STDERR "Beginning sub pass...";

while ( chomp( my $line = <IN> ) ) {
   
   $synLineCount++;

   my ( $syn_id, $synonym ) = split(/\t/, $line);

   if ( $syn_id eq '' ) {
      
      die("FATAL: null record ID for synonym \"$synonym\" at $synFile line $synLineCount; aborting.\n");
   }

   if ( $current_syn_id eq '' ) {
      
      $current_syn_id = $syn_id;

      @current_synonyms = ( $synonym );

   } elsif ( $syn_id eq $current_syn_id ) {
      
      push @current_synonyms, $synonym;

   } else {
      
      # We have encountered a new CID that isn't the first record. Dump the previous one.

      while ( $current_db_id < $current_syn_id ) {
         
         print DB_OUT "$nextDBline\n";

         chomp( $nextDBline = <DB_IN> );
            
         ( $current_db_id, @someOtherStuff ) = split(/\t/, $nextDBline);
      }

      if ( $current_db_id != $current_syn_id ) {
         
         # Some compounds don't get titles. In this case, there's a default form:

         my $insertDBline = "$current_syn_id\tCID $current_syn_id\t\t[]";

         my $newSynString = '[\'' . join('\', \'', @current_synonyms) . '\']';

         $insertDBline =~ s/\[\]$/$newSynString/;

         # Need to print this now, because we still have $nextDBline buffered from the input $compoundTSV.

         print DB_OUT "$insertDBline\n";

         $insertionCount++;

      } else {
         
         # Now we're on the right record line. Swap in the loaded synonym set where we left an empty pair of brackets (in the final field).

         my $newSynString = '[\'' . join('\', \'', @current_synonyms) . '\']';

         $nextDBline =~ s/\[\]$/$newSynString/;

         # (The new line will be printed before the next dump.)
      }

      # Update the new block.

      $current_syn_id = $syn_id;

      @current_synonyms = ( $synonym );
   }
}

close IN;

# Process the final block.

while ( $current_db_id < $current_syn_id ) {
   
   print DB_OUT "$nextDBline\n";

   chomp( $nextDBline = <DB_IN> );

   ( $current_db_id, @someOtherStuff ) = split(/\t/, $nextDBline);
}

if ( $current_db_id != $current_syn_id ) {
   
   # Some compounds don't get titles. In this case, there's a default form:

   my $insertDBline = "$current_syn_id\tCID $current_syn_id\t\t[]";

   my $newSynString = '[\'' . join('\', \'', @current_synonyms) . '\']';

   $insertDBline =~ s/\[\]$/$newSynString/;

   # Need to print this now, because we still have $nextDBline buffered from the input $compoundTSV.

   print DB_OUT "$insertDBline\n";

   $insertionCount++;

} else {
   
   # Now we're on the right record line. Swap in the loaded synonym set where we left an empty pair of brackets (in the final field).

   my $newSynString = '[\'' . join('\', \'', @current_synonyms) . '\']';

   $nextDBline =~ s/\[\]$/$newSynString/;
}

# Finish updating $compoundTSV.

print DB_OUT "$nextDBline\n";

while ( my $line = <DB_IN> ) {
   
   print DB_OUT $line;
}

close DB_OUT;

close DB_IN;

print STDERR "done. Added $insertionCount new records.\n";

if ( $destroy ) {
   
   system("mv $tempFile $compoundTSV");
}


