#!/usr/bin/perl

use strict;

$| = 1;

# ARGUMENTS

my $oldFile = shift;

my $newFile = shift;

die("Usage: $0 <old OBO file> <new OBO file>\n") if ( not -e $oldFile or not -e $newFile );

# PARAMETERS

# EXECUTION

open IN, "<$oldFile" or die("Can't open $oldFile for reading.\n");

my $getThis = 0;

my $oldSet = {};

my $oldSet_unfound = {};

my $lineCount = 0;

while ( chomp( my $line = <IN> ) ) {
   
   $lineCount++;

   if ( $getThis ) {
      
      if ( $line =~ /^id:\s+(\S+)/ ) {
         
         my $term = $1;

         $oldSet->{$term} = 1;
         $oldSet_unfound->{$term} = 1;

      } else {
         
         die("FATAL: Nonconformant post-[Term] line #$lineCount: \"$line\"; aborting.\n");
      }

      $getThis = 0;
   }

   if ( $line =~ /^\[Term\]/ ) {
      
      $getThis = 1;
   }
}

close IN;

my $oldSetCount = scalar( keys %$oldSet );

open IN, "<$newFile" or die("Can't open $newFile for reading.\n");

my $newSet = {};

$getThis = 0;

$lineCount = 0;

my $bothTermCount = 0;

my $newTermCount = 0;

while ( chomp( my $line = <IN> ) ) {
   
   $lineCount++;

   if ( $getThis ) {
      
      if ( $line =~ /^id:\s+(\S+)/ ) {
         
         my $term = $1;

         $newSet->{$term} = 1;

         if ( exists( $oldSet->{$term} ) ) {
            
            $bothTermCount++;

            if ( exists( $oldSet_unfound->{$term} ) ) {
               
               delete $oldSet_unfound->{$term};
            }

         } else {
            
            $newTermCount++;
         }

      } else {
         
         die("FATAL: Nonconformant post-[Term] line #$lineCount: \"$line\"; aborting.\n");
      }

      $getThis = 0;
   }

   if ( $line =~ /^\[Term\]/ ) {
      
      $getThis = 1;
   }
}

close IN;

my $newSetCount = scalar( keys %$newSet );

print "OLD SET\n$oldSetCount terms\nNEW SET\n$newSetCount terms\nBOTH SETS\n$bothTermCount terms\nNEW TERMS\n$newTermCount\n";

print "DROPPED\n";

foreach my $id ( sort { $a cmp $b } keys %$oldSet_unfound ) {
   
   print "$id\n";
}


