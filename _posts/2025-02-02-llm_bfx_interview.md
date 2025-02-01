---
title: "Reasoning LLM: A Bioinformatics Coding Interview"
last_modified_at: 2025-02-02
categories:
  - Blog
tags:
  - AI
---

Here's the question I used to use at Invitae to interview bioinformatics engineering candidates, how it's solved by two reasoning LLMs, and a few conclusions. 

## Interview Question

I have a fasta file that has the following format:

```
>SEQ1
AGTCTGCTACGCTAGC
>SEQ2
GGTGCGATCGATCGTG
>SEQ3
TTCCCATGCTACGTCG
>SEQ4
TCAAACGCATCGCGAC
```

You can assume that:
* the fasta file is well formatted
* there is only one sequence line per header line
* each sequence in the file is the same length

Your task is to replace the `pass` portions of this code with functioning code, according to the name and docstring:

```python
def read_fasta(input_fasta_path):
    """Given the location of a fasta file, return a list of sequences"""
    pass


def are_similar(seq1, seq2, threshold=3):
    "Given two sequences, using a Hamming distance metric to return a bool indicating whether or not the two sequences are similar"
    pass


def build_graph(sequences):
    """Given a list of sequences, return a graph representation of sequences that are similar via Hamming distance"""
    pass


def are_second_degree_neighbors(graph, seq1, seq2):
    """Given a graph and two sequences, return a bool indicating if they're second degree neighbors""" 
    pass


def main():
   pass

```

Please create any tests and data you need in order to feel confident that the code you write is correct. Similarly, structure `main` in any way you see fit to demonstrate correctness of the code.

Lastly, imagine we want this code to go into production. Please attempt to make coding decisions that produce production-level code.

## ChatGPT-o1

(Thought for 29s)

```python
#!/usr/bin/env python3
"""
FASTA Similarity Checker

This module provides functionality to:
1. Read sequences from a FASTA file.
2. Compute a Hamming-based similarity check between two sequences.
3. Build a graph (adjacency list) of sequences considered "similar."
4. Determine whether two sequences are second-degree neighbors within that graph.

Author: Your Name
Date: 2025-01-31
"""

from itertools import combinations
import sys


def hamming_distance(seq1: str, seq2: str) -> int:
    """
    Compute the Hamming distance between two equal-length sequences.
    
    :param seq1: First sequence (string).
    :param seq2: Second sequence (string).
    :return: The Hamming distance (integer).
    :raises ValueError: If the sequences are not the same length.
    """
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be of equal length to compute Hamming distance.")
    return sum(ch1 != ch2 for ch1, ch2 in zip(seq1, seq2))


def read_fasta(input_fasta_path: str) -> list[str]:
    """
    Given the location of a fasta file, return a list of sequences.
    Assumptions:
      - The FASTA file is well-formatted.
      - There is only one sequence line per header line.
      - Each sequence is of the same length.
    
    :param input_fasta_path: Path to input FASTA file.
    :return: A list of sequences (strings).
    """
    sequences = []
    
    with open(input_fasta_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Skip headers that start with '>'
            if line.startswith(">"):
                continue
            sequences.append(line)

    return sequences


def are_similar(seq1: str, seq2: str, threshold: int = 3) -> bool:
    """
    Given two sequences, use a Hamming distance metric to return a bool
    indicating whether the two sequences are 'similar.'
    
    :param seq1: First sequence (string).
    :param seq2: Second sequence (string).
    :param threshold: Maximum Hamming distance for which sequences are considered similar.
    :return: True if Hamming distance <= threshold, False otherwise.
    """
    dist = hamming_distance(seq1, seq2)
    return dist <= threshold


def build_graph(sequences: list[str], threshold: int = 3) -> dict[str, set[str]]:
    """
    Given a list of sequences, return a graph (adjacency list) of sequences
    that are similar with respect to a given Hamming distance threshold.
    
    :param sequences: A list of sequences (strings).
    :param threshold: Maximum Hamming distance allowed to declare two sequences connected.
    :return: A dict where keys are sequences and values are sets of adjacent (similar) sequences.
    """
    graph = {seq: set() for seq in sequences}
    
    for seq1, seq2 in combinations(sequences, 2):
        if are_similar(seq1, seq2, threshold):
            graph[seq1].add(seq2)
            graph[seq2].add(seq1)

    return graph


def are_second_degree_neighbors(graph: dict[str, set[str]], seq1: str, seq2: str) -> bool:
    """
    Given a graph (as returned by build_graph) and two sequences, return a bool
    indicating if they are second-degree neighbors.
    
    Here, "second-degree neighbors" means that seq1 is not directly connected to seq2,
    but there exists some intermediate neighbor 'n' such that seq1 -> n -> seq2 is a path.
    
    :param graph: The adjacency list (dict of sets) of sequences.
    :param seq1: The first sequence (string).
    :param seq2: The second sequence (string).
    :return: True if seq2 can be reached from seq1 by exactly two "hops." 
    """
    # If either sequence is not in the graph, cannot be neighbors
    if seq1 not in graph or seq2 not in graph:
        return False
    
    # If they're first-degree neighbors, they're not strictly second-degree neighbors
    if seq2 in graph[seq1]:
        return False

    # Check for an intermediate neighbor
    for neighbor in graph[seq1]:
        if seq2 in graph[neighbor]:
            return True
    
    return False


def test_all():
    """
    A simple test suite to ensure correctness of the code.
    """
    # Test Hamming distance
    assert hamming_distance("AAAA", "AAAT") == 1
    assert hamming_distance("AAAA", "AAAA") == 0
    try:
        _ = hamming_distance("AAA", "AAAA")
    except ValueError:
        pass  # expected

    # Test are_similar
    assert are_similar("AAAA", "AAAT", threshold=1) is True
    assert are_similar("AAAA", "AATT", threshold=1) is False
    
    # Build a small graph and test adjacency
    seqs = ["AAAA", "AAAT", "AATT", "TTTT"]
    g = build_graph(seqs, threshold=1)
    # neighbors of "AAAA" should only be "AAAT"
    assert g["AAAA"] == {"AAAT"}
    # neighbors of "AAAT" should be "AAAA" and "AATT"
    assert g["AAAT"] == {"AAAA", "AATT"}
    
    # Test are_second_degree_neighbors
    # "AAAA" -> "AAAT" -> "AATT" => second-degree neighbors
    assert are_second_degree_neighbors(g, "AAAA", "AATT") is True
    # But "AAAA" and "TTTT" are not even close (distance=4 each from "AAAA")
    assert are_second_degree_neighbors(g, "AAAA", "TTTT") is False
    
    print("All tests passed!")


def main():
    """
    Demonstration of how to use the above functions in practice.
    """
    # 1. Run tests to ensure code works correctly
    test_all()
    
    # 2. Example usage with a sample FASTA file (replace 'example.fasta' with a real file path)
    fasta_file = "example.fasta"

    try:
        sequences = read_fasta(fasta_file)
    except FileNotFoundError:
        print(f"Error: FASTA file '{fasta_file}' not found.")
        sys.exit(1)
    
    print("Sequences read from FASTA file:")
    for s in sequences:
        print(s)
    
    # 3. Build the similarity graph
    graph = build_graph(sequences, threshold=3)
    
    # 4. Demonstrate neighbor checks (customize seq1, seq2 to your input)
    if len(sequences) >= 2:
        seq1 = sequences[0]
        seq2 = sequences[1]
        print(f"\nChecking if '{seq1}' and '{seq2}' are similar (threshold=3): {are_similar(seq1, seq2, 3)}")
        print(f"Are '{seq1}' and '{seq2}' second-degree neighbors? {are_second_degree_neighbors(graph, seq1, seq2)}")
    else:
        print("Not enough sequences to demonstrate neighbor checks.")


if __name__ == "__main__":
    main()
```

### Running the script

I used the following test file as `example.fasta`:

```
>SEQ1
AAAAAAATTTTTTTCCCCCCGGGGGGG
>SEQ2
AAAAAAATTTTTTTCCCCCCGGGTTTT
>SEQ3
GGGGGGGTTTTTTTCCCCCCGGGGGGG
>SEQ4
AAAAAAATTTTTTTCCCCCCGGGGGTT
>SEQ5
AAAAAAATTTTTTTCCCCCCGGGGGGC
```

I'd expect the o1 script to say that the first two sequences are neighbors.

```
❯ python chatGPT_o1.py
All tests passed!
Sequences read from FASTA file:
AAAAAAATTTTTTTCCCCCCGGGGGGG
AAAAAAATTTTTTTCCCCCCGGGTTTT
GGGGGGGTTTTTTTCCCCCCGGGGGGG
AAAAAAATTTTTTTCCCCCCGGGGGTT
AAAAAAATTTTTTTCCCCCCGGGGGGC

Checking if 'AAAAAAATTTTTTTCCCCCCGGGGGGG' and 'AAAAAAATTTTTTTCCCCCCGGGTTTT' are similar (threshold=3): False
Are 'AAAAAAATTTTTTTCCCCCCGGGGGGG' and 'AAAAAAATTTTTTTCCCCCCGGGTTTT' second-degree neighbors? True
```

## Deepseek R1

(Thought for 176s)

```python
from collections import defaultdict


def read_fasta(input_fasta_path):
    """Given the location of a fasta file, return a list of sequences"""
    sequences = []
    with open(input_fasta_path, "r") as f:
        for line in f:
            if line.startswith(">"):
                # Read the next line as the sequence
                seq = next(f).strip()
                sequences.append(seq)
    return sequences


def are_similar(seq1, seq2, threshold=3):
    """Given two sequences, return True if their Hamming distance is <= threshold."""
    if len(seq1) != len(seq2):
        return False
    hamming_distance = sum(c1 != c2 for c1, c2 in zip(seq1, seq2))
    return hamming_distance <= threshold


def build_graph(sequences):
    """Given a list of sequences, return a graph where keys are sequences and values are lists of similar sequences."""
    graph = defaultdict(list)
    n = len(sequences)
    for i in range(n):
        for j in range(i + 1, n):
            if are_similar(sequences[i], sequences[j]):
                graph[sequences[i]].append(sequences[j])
                graph[sequences[j]].append(sequences[i])
    return graph


def are_second_degree_neighbors(graph, seq1, seq2):
    """Return True if seq1 and seq2 are connected via exactly two edges in the graph."""
    if seq1 == seq2:
        return False  # A sequence cannot be a neighbor of itself in this context

    # Check if they are direct neighbors
    if seq2 in graph.get(seq1, []):
        return False

    # Check if there's any common neighbor that connects them
    for neighbor in graph.get(seq1, []):
        if seq2 in graph.get(neighbor, []):
            return True
    return False


def main():
    # Example test case with a small FASTA file
    test_fasta = [">SEQ1", "AAAA", ">SEQ2", "AAAT", ">SEQ3", "AATT", ">SEQ4", "ATTT"]
    # Writing test data to a temporary file
    with open("test.fasta", "w") as f:
        f.write("\n".join(test_fasta))

    # Read the sequences
    sequences = read_fasta("test.fasta")
    print(f"Read {len(sequences)} sequences: {sequences}")

    # Build the graph
    graph = build_graph(sequences)
    print("Graph edges:")
    for seq, neighbors in graph.items():
        print(f"{seq}: {neighbors}")

    # Test are_similar
    print("\nTesting are_similar:")
    print("SEQ1 and SEQ2 (threshold=1):", are_similar(sequences[0], sequences[1], 1))  # True
    print("SEQ1 and SEQ3 (threshold=1):", are_similar(sequences[0], sequences[2], 1))  # False

    # Test are_second_degree_neighbors
    print("\nTesting are_second_degree_neighbors:")
    print("SEQ1 and SEQ3:", are_second_degree_neighbors(graph, sequences[0], sequences[2]))  # True
    print("SEQ1 and SEQ4:", are_second_degree_neighbors(graph, sequences[0], sequences[3]))  # False


if __name__ == "__main__":
    main()
```

It's clever that it chooses to write out then read in a file in `main`. 

If we just run the script, we get the output:

```
❯ python deepseek_R1.py
Read 4 sequences: ['AAAA', 'AAAT', 'AATT', 'ATTT']
Graph edges:
AAAA: ['AAAT', 'AATT', 'ATTT']
AAAT: ['AAAA', 'AATT', 'ATTT']
AATT: ['AAAA', 'AAAT', 'ATTT']
ATTT: ['AAAA', 'AAAT', 'AATT']

Testing are_similar:
SEQ1 and SEQ2 (threshold=1): True
SEQ1 and SEQ3 (threshold=1): False

Testing are_second_degree_neighbors:
SEQ1 and SEQ3: False
SEQ1 and SEQ4: False
```

## Conclusions

* Both of these models pass the test. By comparison, probably 1/3 people I interviewed would pass. Many bioinformaticians get bogged down in even simple data structure / algorithm style questions. 
* There's a little room for ambiquity in the question. I used to spend a lot of time in the interviews answering questions and clarifying that ambiquity. Both models make reasonable choices.
* I like to see both `itertools` and `collections` utilized, as a demonstration of knowledge of the standard library. It's interesting that each model uses one but not the other.
* o1's tests were a little more robust, IMO.
* R1 took 6x the time to solve the problem. 
* I have a slight qualitative preference for o1's code. 

// TODO Comment on the set approach for 2nd degree neighbors

And finally:

* The next time I interview a BFX role, I should come up with another question. This one is "solved". 