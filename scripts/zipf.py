import argparse
from collections import Counter
from matplotlib import pyplot as plt


def get_ranks_and_frequencies(infile):
    """Produces a list of rank, frequency pairs for each word in a text file
    :param infile: a text file
    :return: a list containing rank, frequency pairs for each word
    """
    with open(infile) as f:
        contents = f.read()
    c = Counter(contents.split())
    # TODO: create a list called ranks_and_frequencies that stores (rank,
    # frequency) pairs for each word in the file
    ranks_and_frequencies = [(rank, frequency) for rank, (word, frequency) in enumerate(c.most_common(), start=1)]
    print(ranks_and_frequencies[:3]) # a small sanity check for me
    return ranks_and_frequencies


def plot(infile):
    """
    Plots rank and frequency pairs to demonstrate Zipf's Law
    :param infile: a text file
    :return: None, produces a matplotlib plot
    """
    ranks_and_frequencies = get_ranks_and_frequencies(infile)

    # TODO: use the (rank, frequency) pairs to plot the data
    # and use a log scale on both axes
    # You will display the plot using plt.show(), which is already written
    
    ranks = [pair[0] for pair in ranks_and_frequencies]
    frequencies = [pair[1] for pair in ranks_and_frequencies]
    plt.plot(ranks, frequencies)
    plt.xscale("log")
    plt.yscale("log")
    plt.title("Nina Dukic")
    plt.show()

# My comment on the graph: The graph shows a very clear linear relationship between log of word rank and frequency, in line with Zipf's Law.
# The bottom of the graph, though, has a staircase-like shape, which is probably due to many words sharing the same frequency and that same
# frequency being expressed using a low, but whole number, which in turn causes clustering of this sort.


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Constructs a curve '
                                                 'demonstrating Zipf\'s Law '
                                                 'by plotting a rank, '
                                                 'frequency plot.')
    parser.add_argument('--path', type=str, required=True, help='Path to file')
    args = parser.parse_args()
    plot(args.path)
