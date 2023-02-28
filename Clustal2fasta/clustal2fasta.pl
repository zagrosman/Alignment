#!/usr/bin/perl
use strict;
use warnings;

# Get input and output file names from command line arguments
my $infile = shift;
my $outfile = shift;

# Open input file and skip header lines
open my $in, '<', $infile or die "Can't open input file: $!";
while (<$in>) {
    last unless /^CLUSTAL/ or /^#/;
}

# Parse alignment data
my %seqs;
while (<$in>) {
    next if /^\s*$/;
    my ($id, $seq) = split;
    $seqs{$id} .= $seq;
}

# Open output file and write sequences in Fasta format
open my $out, '>', $outfile or die "Can't open output file: $!";
foreach my $id (sort keys %seqs) {
    print $out ">$id\n$seqs{$id}\n";
}

