## $\textcolor{green}{Description}$
This Python script reads a Clustal Omega alignment output file (.aln) and converts it to a Fasta file (.fasta).


## $\textcolor{green}{Executing\ clustal2fasta.py\ script}$
1. Creat a directory for this python script and your clustal output file.
2. Run the script using the following command:

```
python clustal2fasta.py input.aln output.fasta
```

**input.aln:** clustal output file. 
**output.fasta:** the output of this script. 


You can also use `clustal2fasta.pl` to convert clustalO file to fasta file. To use this script, run the following command:

```
perl clustal2fasta.pl input.aln output.fasta
```

## $\textcolor{green}{Note}$
Make sure that all steps run correctly, if you get an error while running this script. To run the given scripts here, you need python > 3.0 versions and Perl tools. Both scripts have been checked and they work fine. Go ahead!


## $\textcolor{green}{Online\ conversion}$
 You can also convert `.aln` file to `.fasta` file using the following converting tools.
 1. [CFSC](http://sequenceconversion.bugaco.com/converter/biology/sequences/clustal_to_fasta.php)
 2. [Seqret](https://www.ebi.ac.uk/Tools/sfc/emboss_seqret/)
