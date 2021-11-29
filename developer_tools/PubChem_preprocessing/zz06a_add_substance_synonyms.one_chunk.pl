#!/usr/bin/perl

use strict;

$| = 1;

# ARGUMENTS

my $substanceTSV = shift;

my @xmlFiles = ();

while ( my $nextFile = shift ) {
   
   push @xmlFiles, $nextFile;
}

# PARAMETERS

my $outFile = "$substanceTSV.new";

my $unfoundFile = "$substanceTSV.unready_SIDs.tsv";

# $destroy <- 1 == Don't save intermediate state files:

my $destroy = 1;

# EXECUTION

my $currentFileCount = 0;

my $totalFileCount = scalar( @xmlFiles );

open MAIN, "<$substanceTSV" or die("Can't open $substanceTSV for reading.\n");

open OUT, ">$outFile" or die("Can't open $outFile for writing.\n");

chomp( my $mainLine = <MAIN> );

my ( $mainID, @theRest ) = split(/\t/, $mainLine);

my $missingLines = {};

chomp( my $date = `date` );

print STDERR "[$date] Beginning substitution pass...\n\n";

foreach my $xmlFile ( @xmlFiles ) {
   
   my $lineCount = 0;

   my $currentID = '';

   my $title = {};

   my $synonyms = {};

   my $listening = 0;

   my $cid = {};

   open IN, "zcat $xmlFile |" or die("Can't open $xmlFile for reading.\n");

   while ( chomp( my $line = <IN> ) ) {
      
      $lineCount++;

      if ( $line =~ /<PC\-ID_id>(\d+)<\/PC\-ID_id>/ ) {
         
         $currentID = $1;

      } elsif ( $line =~ /<PC\-ID_id>/ ) {
         
         die("ACK! $line\n");
      
      } elsif ( $line =~ /<PC\-Substance_synonyms_E>\s*(.*)\s*<\/PC\-Substance_synonyms_E>/ ) {
         
         my $synonym = $1;

         if ( $synonym =~ /\'/ ) {
            
            die("FATAL: Noncompliant synonym encoding, line $lineCount of $xmlFile: \"$synonym\"; aborting.\n");
         }

         if ( not exists( $synonyms->{$currentID} ) ) {
            
            $synonyms->{$currentID} = [];

            $title->{$currentID} = $synonym;
         }

         push @{$synonyms->{$currentID}}, $synonym;

      } elsif ( $line =~ /<PC\-Substance_synonyms_E>/ ) {
         
         die("OH NO! $line\n");

      } elsif ( $line =~ /<PC\-CompoundType_type value="standardized">1<\/PC\-CompoundType_type>/ ) {
         
         $listening = 1;

      } elsif ( $line =~ /<PC\-CompoundType_type value=/ ) {
         
         $listening = 0;

      } elsif ( $line =~ /<PC\-CompoundType_id_cid>(.+)<\/PC\-CompoundType_id_cid>/ ) {
         
         if ( $listening ) {
            
            $cid->{$currentID} = $1;
         }
      }

   } # end while ( line iterator on current input XML.gz )

   close IN;

   chomp( $date = `date` );

   print STDERR "   (" . ++$currentFileCount . "/" . $totalFileCount . ") [$date] loaded $xmlFile; inserting synonyms...";

   # Insert the new synonyms (in SID order) into the main table.

   foreach my $sid ( sort { $a <=> $b } keys %$title ) {
      
      while ( not eof(MAIN) and $mainLine ne '' and $mainID < $sid ) {
         
         print OUT "$mainLine\n";

         if ( chomp( $mainLine = <MAIN> ) ) {
            
            ( $mainID, @theRest ) = split(/\t/, $mainLine);

         } else {
            
            # We fell off the end of the file.

            $mainLine = '';
         }
      }

      if ( $mainID == $sid ) {
         
         my $currentCID = $theRest[3];

         print OUT "$sid\t$title->{$sid}\t\t['";

         print OUT join( "', '", @{$synonyms->{$sid}} );

         print OUT "']\t$currentCID\n";

         if ( $currentCID ne $cid->{$sid} ) {
            
            die("Good grief! [$sid] $currentCID != $cid->{$sid} ; aborting.\n");
         }

         # Advance to the next input line in substance.tsv to avoid record duplication (we just wrote a new version of the current line)

         if ( chomp( $mainLine = <MAIN> ) ) {
            
            ( $mainID, @theRest ) = split(/\t/, $mainLine);

         } else {
            
            # We fell off the end of the file.

            $mainLine = '';
         }

      } elsif ( $mainID > $sid ) {
         
         # This SID isn't in the input file.

         my $currentCID = 'NOT_ASSIGNED';

         if ( exists( $cid->{$sid} ) ) {
            
            $currentCID = $cid->{$sid};
         }

         $missingLines->{$sid} = "$sid\t$title->{$sid}\t\t['" . join( "', '", @{$synonyms->{$sid}} ) . "']\t$currentCID\n";

      } else {
         
         # We fell off the end of the input file.

         my $currentCID = 'NOT_ASSIGNED';

         if ( exists( $cid->{$sid} ) ) {
            
            $currentCID = $cid->{$sid};
         }

         $missingLines->{$sid} = "$sid\t$title->{$sid}\t\t['" . join( "', '", @{$synonyms->{$sid}} ) . "']\t$currentCID\n";
      }

   } # end foreach ( $sid for which synonyms were loaded from $xmlFile )

   chomp( $date = `date` );

   print STDERR "done. [$date]\n";
}

chomp( $date = `date` );

print STDERR "\n...done with substitution pass. [$date]\nCleaning up...";

# If we haven't yet fallen off the end of the input file, copy the rest of it.

if ( $mainLine ne '' ) {
   
   print OUT "$mainLine\n";
}

while ( $mainLine = <MAIN> ) {
   
   print OUT $mainLine;
}

close OUT;

close MAIN;

open OUT, ">$unfoundFile" or die("Can't open $unfoundFile for writing.\n");

foreach my $sid ( sort { $a <=> $b } keys %$missingLines ) {
   
   print OUT $missingLines->{$sid};
}

close OUT;

if ( $destroy ) {
   
   system("mv $outFile $substanceTSV");
}

chomp( $date = `date` );

print STDERR "done. [$date]\n";


