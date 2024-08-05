---
title: "Simple Sequence Similarity"
last_modified_at: 2015-01-15
categories:
  - Blog
tags:
  - "Old Blogger"
  - Code
---
I've mostly refrained from posting any of the code that I've been writing in the past months because the code seems scraped together in a "just get it done" method that wouldn't be particularly interesting or useful to anyone but me. The programs are simple scripts only applicable to the single task at hand. But I've finally gained enough confidence to show off a few lines that I've been using recently.<br />
<br />
How similar is the phrase "Get it finished" to "Finished get it"? Or in protein terminology, how homologous is GETITFINISHED to FINISHEDGETIT? Many similarity calculations assume sequence linearity, and therefore would not detect much likeness between these two phrases/sequences. The script below is a very simple way of detecting similarity in these sort of "mixed up" strings.<br />
<br />
<br />
<pre class="brush:python;">import numpy as np
from Bio import SeqIO
from itertools import product
from scipy.stats.stats import pearsonr

def k_mers(data, outfile,k):
    def occurrences(s,k1):
        dic = {} #Initialize dictionary
        c = 0 #Initialize counter
        while c+k1 &lt;= len(s): #Iterate through the sequence until the end
            k_mer = s[c:c+k1] #Kmer defined as a slice of sequence s and size k
            if k_mer not in dic: #If the kmer hasn't been seen before
                dic.update({k_mer:1}) #Add the kmer as a key to the dictionary. 
            elif k_mer in dic: #If the kmer has been seen before
                dic[k_mer] += 1 #Increment the kmer's value by one.
            c += 1 #Move over one letter in the sequence
        return dic #Return the full dictionary

    transcripts = SeqIO.parse(open(data, "r"),'fasta') #Open the fasta file
    c = 0 #Initialize a counter to determine size of storage array
    for i in transcripts: #For each transcript
        c+=1 #Add 1 to the counter
    transcripts = SeqIO.parse(open(data, "r"),'fasta') #Reopen the fasta file
    c_mat = np.zeros([c,4**k]) #Initialize array to store the counts   
    for i, rna in enumerate(transcripts): #For each transcript
        counts = occurrences(str(rna.seq),k) #Get the kmer counts for sequence       
        counts_ar = np.zeros([4**k]) #Initialize array to store all kmers
        for j, sub in enumerate(product("AGTC", repeat=k)): #Generate each kmer
            k_mer = "".join(sub) #Turn kmer list into a string
            if k_mer in counts: #If the kmer is in the transcript
                counts_ar[j] = counts[k_mer] #Add the proper kmer value
        c_mat[i] = counts_ar #Add new row of counts to count matrix
    np.savetxt(open(outfile, "w"),c_mat, delimiter=",") #Save the matrix
   
def k_mers_corr(c_mat, outfile):        
    c_mat = np.genfromtxt(open(c_mat,"r"), delimiter=",") #Open the count matrix
    corr_mat = np.zeros([c_mat.shape[0],c_mat.shape[0]]) #Initialize new matrix
    for i, row1 in enumerate(c_mat): #For each row in count matrix
        for j, row2 in enumerate(c_mat): #For each row in count matrix
            dist = pearsonr(row1,row2)[0] #Get the corr coeff between rows
            corr_mat[j][i] = dist #Add coeff to matrix
    np.savetxt(open(outfile, "w"),corr_mat, delimiter=",") #Save the matrix
    
p = "A:/Library2/Data/" #My directory containing all my working files
i = p+"gencode_lncRNA_overlap_m.txt" #My transcript file
o1 = p+"blogger1.csv" #Output file for the count data
o2 = p+"blogger2.csv" #Output file for the correlation data
k_mers(i,o1,4) #Call to first function
k_mers_corr(o1,o2) #Call to second function
</pre>
<br />
<br />
Even with the comments, this is a lot to digest at once, so let's go through it section by section.
<br />
<br />
The first section is pretty straightforward. It simply give Python access to the necessary tools that I'm going to need later on in the script.
<br />
<pre class="brush:python;">import numpy as np
from Bio import SeqIO
from itertools import product
from scipy.stats.stats import pearsonr
</pre>
<br />
<br />
The next section defines a couple of functions. "k_mers" takes the name of a data file (currently this must be a FASTA file, but it would be easy to generalize the function to be able to read other strings as well), the name of the file to which you would like to store your data, and the size of the substring/kmer you want to analyze. It will then produce a file telling you how many times each kmer appeared in each of the the sequences you want to compare. Notice that the "occurrences" function is defined exclusively inside of the "k_mers" function. It is the function that actually does the counting. If you know much of anything about Python, you probably want to point out that Python has a built in count method. The count method Python provides, however, does not count overlapping sub-strings. For example if you used the default count method on "AGTC" with a size of 2, it would return "AG" and "TC". "occurrences", on the other hand, will return "AG", "GT", and "TC"'. 
<br />
<pre class="brush:python;">def k_mers(data, outfile,k):
    def occurrences(s,k1):
        dic = {} #Initialize dictionary
        c = 0 #Initialize counter
        while c+k1 &lt;= len(s): #Iterate through the sequence until the end
            k_mer = s[c:c+k1] #Kmer defined as a slice of sequence s and size k
            if k_mer not in dic: #If the kmer hasn't been seen before
                dic.update({k_mer:1}) #Add the kmer as a key to the dictionary. 
            elif k_mer in dic: #If the kmer has been seen before
                dic[k_mer] += 1 #Increment the kmer's value by one.
            c += 1 #Move over one letter in the sequence
        return dic #Return the full dictionary
</pre>
<br />
<br />
Next, we need to know how many transcripts we are going to analyze. So, we open the file and read through it with a counter that adds one each time a new transcript is encountered. I'm not going to get into generators here, but Python needs to reopen a file to be able to read through it again, so I have to recall the same line.
<br />
<pre class="brush:python;">    transcripts = SeqIO.parse(open(data, "r"),'fasta') #Open the fasta file
    c = 0 #Initialize a counter to determine size of storage array
    for i in transcripts: #For each transcript
        c+=1 #Add 1 to the counter
    transcripts = SeqIO.parse(open(data, "r"),'fasta') #Reopen the fasta file
</pre>
<br />
<br />
Now we can make an 2-by-2 array that's eventually going to be filled with the number of kmers that are present in each transcript and begin cycling through them. For each transcript, we call the "occurrences" function we defined above. We send "occurrences" the current transcript we are working on as well as the size of the kmers we are looking for. It will return with a dictionary of the kmers and their corresponding counts.
<br />
<pre class="brush:python;">    c_mat = np.zeros([c,4**k]) #Initialize array to store the counts   
    for i, rna in enumerate(transcripts): #For each transcript
        counts = occurrences(str(rna.seq),k) #Get the kmer counts for sequence
</pre>
<br />
<br />
The next few lines might make more sense if you've looked ahead to what sort of statistical method we are eventually going to use for comparison of the sequences. But consider the trivial case where we want to compare "AGTA" to "CAAA" using a kmer size of 1. The first transcript is going to produce "A"=2, "G"=1, and "T"=1 while the second will be "A"=4 and "C"=1. But what is needed for "an apples-to-apples" comparison is the first "A"=2, "G"=1, "T"=1, "C"=0 while the second will now be "A"=3, "G"=0, "T"=0, and "C"=1. These next lines are producing those necessary placeholders.
<br />
<pre class="brush:python;">        for j, sub in enumerate(product("AGTC", repeat=k)): #Generate each kmer
            k_mer = "".join(sub) #Turn kmer list into a string
            if k_mer in counts: #If the kmer is in the transcript
                counts_ar[j] = counts[k_mer] #Add the proper kmer value
</pre>
<br />
<br />
The last two lines of this function are pretty self explanatory. It would have been a bit easier to keep the matrix in memory and continue on to the correlation calculations, but here is a natural breaking point which allows the user to do other things with the data if they wish. "k_mers_corr" is a fairly simple function, which takes the names of the file produced in the previous function, as well as another output file to store this new data. The new data will be a symmetric matrix where each transcript is compared to every other transcript in the file, and their similarity are saved. After getting things going by bringing in the data and creating a square matrix of the proper size, we start iterating through the rows of our data.
<br />
<pre class="brush:python;">def k_mers_corr(c_mat, outfile):        
    c_mat = np.genfromtxt(open(c_mat,"r"), delimiter=",") #Open the count matrix
    corr_mat = np.zeros([c_mat.shape[0],c_mat.shape[0]]) #Initialize new matrix
    for i, row1 in enumerate(c_mat): #For each row in count matrix
</pre>
<br />
<br />
For each row we go through all of the rows (including the row we are currently on) and compare their similarity via the <a href="http://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient">Pearson </a>correlation. Once we have that number, we store it in the proper cell in the matrix we initialized earlier. Once we have filled all of the cells, we save our data. 
<br />
<pre class="brush:python;">        for j, row2 in enumerate(c_mat): #For each row in count matrix
            dist = pearsonr(row1,row2)[0] #Get the corr coeff between rows
            corr_mat[j][i] = dist #Add coeff to matrix
    np.savetxt(open(outfile, "w"),corr_mat, delimiter=",") #Save the matrix
</pre>
<br />
<br />
And we're finished! The functions I've walked through here are actually stripped down versions of what I have been using recently (don't want to give away ALL my secrets!), so it would appear that I've made my first real Bioinformatics post. I hope I made it clear but if any clarifications are needed, feel free to ask a question in the comments below. Cheers! 