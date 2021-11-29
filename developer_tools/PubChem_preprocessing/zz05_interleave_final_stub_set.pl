#!/usr/bin/perl

use strict;

$| = 1;

# PARAMETERS

my $inDir = '001_stupidly_large_reference_tables';

my $failFile = "$inDir/substance.failed_CID_lookups.tsv";

my $compoundFile = "$inDir/compound.tsv";

my $compoundTemp = "$inDir/compound.tsv.new";

my $debugCidsFound = 'cids_loaded.txt';

my $debugCidsAdded = 'cids_added.txt';

my $debug = 0;

# $destroy <- 1 == Don't save intermediate state files:

my $destroy = 1;

# EXECUTION

print STDERR "Loading missing values...";

open IN, "<$failFile" or die("Can't open $failFile for reading.\n");

my $header = <IN>;

my $compoundLineHash = {};

my $substanceLineHash = {};

while ( chomp( my $line = <IN> ) ) {
   
   my ( $sid, $cid ) = split(/\t/, $line);

   # id	name	description	synonyms

   $compoundLineHash->{$cid} = "$cid\tCID $cid\t\t[]\n";

   # id	name	description	synonyms	compound

   $substanceLineHash->{$sid} = "$sid\t\t\t\t$cid\n";
}

close IN;

my @cidLines = ();

if ( $debug ) {
   
   open OUT, ">$debugCidsFound" or die("Can't open $debugCidsFound for writing.\n");
}

foreach my $cid ( sort { $a <=> $b } keys %$compoundLineHash ) {
   
   push @cidLines, $compoundLineHash->{$cid};

   if ( $debug ) {
      
      print OUT "$cid\n";
   }
}

if ( $debug ) {
   
   close OUT;
}

my @sidLines = ();

foreach my $sid ( sort { $a <=> $b } keys %$substanceLineHash ) {
   
   push @sidLines, $substanceLineHash->{$sid};
}

print STDERR "done.\n";

chomp( my $date = `date` );

print STDERR "Updating $compoundFile... [$date]\n\n";

open IN, "<$compoundFile" or die("Can't open $compoundFile for reading.\n");

open OUT, ">$compoundTemp" or die("Can't open $compoundTemp for writing.\n");

if ( $debug ) {
   
   open ADD, ">$debugCidsAdded" or die("Can't open $debugCidsAdded for writing.\n");
}

my $nextCidLine = shift @cidLines;

my ( $nextCid, @theRest ) = split(/\t/, $nextCidLine);

my $newCidCount = 0;

my $header = <IN>;

print OUT $header;

while ( my $line = <IN> ) {
   
   my ( $currentCid, @currentRest ) = split(/\t/, $line);

   while ( $nextCid != -1 and $currentCid > $nextCid ) {
      
      if ( $nextCidLine ne '' ) {
         
         print OUT $nextCidLine;

         $newCidCount++;

         if ( $debug ) {
            
            print ADD "$nextCid\n";
         }
      }

      if ( scalar( @cidLines ) > 0 ) {
         
         $nextCidLine = shift @cidLines;

         ( $nextCid, @theRest ) = split(/\t/, $nextCidLine);

      } else {
         
         $nextCidLine = '';

         $nextCid = -1;
      }
   }

   print OUT $line;
}

# There might still be some CIDs left to add on the end of the sorted target list.

if ( $nextCidLine ne '' ) {
   
   print OUT $nextCidLine;

   $newCidCount++;

   if ( $debug ) {
      
      print ADD "$nextCid\n";
   }
}

if ( scalar( @cidLines ) > 0 ) {
   
   foreach my $line ( @cidLines ) {
      
      print OUT $line;

      $newCidCount++;

      if ( $debug ) {
         
         ( $nextCid, @theRest ) = split(/\t/, $line);

         print ADD "$nextCid\n";
      }
   }
}

if ( $debug ) {
   
   close ADD;
}

close OUT;

close IN;

if ( $destroy ) {
   
   system("mv $compoundTemp $compoundFile");
}

print STDERR "\n...done updating $compoundFile; added $newCidCount new CIDs (sanity: " . scalar( keys %$compoundLineHash ) . ").\n";

=pod

# Update substance data -- DELETE THIS BLOCK AFTER INITIAL FIX, THE GENERATOR SCRIPT WAS ADJUSTED

print STDERR "Updating substance files... [$date]\n\n";

my $fileIndex = 0;

my $nextSidLine = shift @sidLines;

( my $nextSid, @theRest ) = split(/\t/, $nextSidLine);

my $newSidCount = 0;

while ( -e "$inDir/substance.tsv.$fileIndex.sorted" ) {
   
   my $inFile = "$inDir/substance.tsv.$fileIndex.sorted";

   my $outFile = "$inDir/substance.tsv.$fileIndex.sorted.new";

   open IN, "<$inFile" or die("Can't open $inFile for reading.\n");

   open OUT, ">$outFile" or die("Can't open $outFile for writing.\n");

   while ( my $line = <IN> ) {
      
      my ( $currentSid, @currentRest ) = split(/\t/, $line);
   
      while ( $nextSid != -1 and $currentSid > $nextSid ) {
         
         if ( $nextSidLine ne '' ) {
            
            print OUT $nextSidLine;
   
            $newSidCount++;
         }
   
         if ( scalar( @sidLines ) > 0 ) {
            
            $nextSidLine = shift @sidLines;
   
            ( $nextSid, @theRest ) = split(/\t/, $nextSidLine);
   
         } else {
            
            $nextSidLine = '';
   
            $nextSid = -1;
         }
      }
   
      print OUT $line;
   }

   close IN;

   close OUT;

   if ( $destroy ) {
      
      system("mv $outFile $inFile");
   }

   print STDERR "   pass" . ( $fileIndex + 1 ) . " complete\n";

   $fileIndex++;
}

# There might still be some SIDs left to add on the end of the sorted target list.

if ( $nextSidLine ne '' ) {
   
   my $newFile = "$inDir/substance.tsv.$fileIndex.sorted";

   my $outFile = "$inDir/substance.tsv.$fileIndex.sorted.new";

   open OUT, ">$outFile" or die("Can't open $outFile for writing.\n");

   print OUT $nextSidLine;

   $newSidCount++;

   if ( scalar( @sidLines ) > 0 ) {
      
      foreach my $line ( @sidLines ) {
         
         print OUT $line;

         $newSidCount++;
      }
   }

   close OUT;

   if ( $destroy ) {
      
      system("mv $outFile $newFile");
   }

} elsif ( scalar( @sidLines ) > 0 ) {
   
   my $newFile = "$inDir/substance.tsv.$fileIndex.sorted";

   my $outFile = "$inDir/substance.tsv.$fileIndex.sorted.new";

   open OUT, ">$outFile" or die("Can't open $outFile for writing.\n");

   foreach my $line ( @sidLines ) {
      
      print OUT $line;

      $newSidCount++;
   }

   close OUT;

   if ( $destroy ) {
      
      system("mv $outFile $newFile");
   }
}

print STDERR "\n...done updating substance files; added $newSidCount new SIDs (sanity: " . scalar( keys %$substanceLineHash ) . ").\n";

=cut

if ( $destroy ) {
   
   system("rm $failFile");
}


