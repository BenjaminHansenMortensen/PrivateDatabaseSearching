""" Permutes the encrypted database using bitonic sorting algorithm """

from math import log
from numpy import random
from Oblivious_Database_Query_Scheme.getters import get_database_size as database_size


def compare_init(client, index: int, permutation: list, descending: bool, mid_point: int):
    """  """

    index_a, index_b = index, index + mid_point

    swap = False
    # Compares them based on permutation
    permutation_a, permutation_b = permutation[index_a], permutation[index_b]
    if (permutation_a > permutation_b and not descending) or (permutation_b > permutation_a and descending):
        permutation_a, permutation_b = permutation_b, permutation_a
        swap = True

    # Updates indexing
    permutation[index_a], permutation[index_b] = permutation_a, permutation_b

    # Executes the mpc encryption and comparison
    client.send_indices_and_encrypt(swap, index_a, index_b)


def compare(client, index: int, permutation: list, descending: bool, mid_point: int):
    """

    :return:
    """

    # Client
    index_record_a, index_record_b = index, index + mid_point

    swap = False
    # Compares them based on permutation
    permutation_a, permutation_b = permutation[index], permutation[index + mid_point]
    if (permutation_a > permutation_b and not descending) or (permutation_b > permutation_a and descending):
        permutation_a, permutation_b = permutation_b, permutation_a
        swap = True

    # Updates indexing
    permutation[index], permutation[index + mid_point] = permutation_a, permutation_b

    # Executes the mpc encryption and comparison
    client.send_indices_and_reencrypt(swap, index_record_a, index_record_b)


def init(client, permutation: list):
    """

    :return:
    """

    partition_size = 2
    partition_mid_point = partition_size // 2

    descending = False
    for index in range(0, database_size(), partition_size):

        #   Parallelizable to log_2(n) processes
        compare_init(client, index, permutation, descending, partition_mid_point)

        descending = (descending + 1) % 2


def merge_partition(client, descending: bool, permutation: list, partition_index: int, partition_mid_point: int):
    """

    :return:
    """

    for value in range(partition_mid_point):
        index = partition_index + value

        #   Parallelizable to log_(partition_split)(n) processes
        compare(client, index, permutation, descending, partition_mid_point)


def merge(client, permutation: list, partition_size, partition_mid_point: int):
    """

    :return:
    """

    descending = False
    for partition_index in range(0, database_size(), partition_size):

        #   Parallelizable to log_(partition_size)(n) processes
        merge_partition(client, descending, permutation, partition_index, partition_mid_point)

        descending = (descending + 1) % 2


def sort_subpartition(client, permutation: list, descending: bool, partition_index: int,
                      subpartition_index: int, subpartition_mid_point: int):
    """

    :return:
    """

    for value in range(subpartition_mid_point):
        index = partition_index + subpartition_index + value

        #   Parallelizable to log_(partition_split)(n) processes
        compare(client, index, permutation, descending, subpartition_mid_point)


def sort_partition(client, permutation: list, descending: bool, partition_size: int, partition_index: int):
    """

    :return:
    """

    for sublevel in range(-int(log(partition_size, 2)) + 1, 0):
        subpartition_size = 2 ** (sublevel * -1)
        subpartition_mid_point = subpartition_size // 2

        for subpartition_index in range(0, partition_size, subpartition_size):

            #  Parallelizable to log_(subpartition_size)(n) processes
            sort_subpartition(client, permutation, descending, partition_index, subpartition_index, subpartition_mid_point)


def sort(client, permutation: list, partition_size: int):
    """

    :return:
    """

    descending = False
    for partition_index in range(0, database_size(), partition_size):

        #   Parallelizable to log_(partition_size)(n) processes
        sort_partition(client, permutation, descending, partition_size, partition_index)

        descending = (descending + 1) % 2


def bitonic_sort(client) -> dict[int, int]:
    """
    :param client:
    :param array_size:
    :param working_directory:
    :return:
    """

    if not log(database_size(), 2).is_integer():
        raise ValueError("Array size has to be of power 2.")

    # Creates new indexing of the shuffled database
    permutation = random.permutation(database_size()).tolist()
    permutation_indexing = dict(zip([str(i) for i in range(len(permutation))], permutation))

    # Initializes the encrypted databases and sorts the first level
    init(client, permutation)

    # Completes the sorting of the encrypted database
    for level in range(2, int(log(database_size(), 2) + 1)):  # Skip 2**1 as it was done in the initiation
        partition_size = 2 ** level
        partition_mid_point = partition_size // 2

        merge(client, permutation, partition_size, partition_mid_point)

        sort(client, permutation, partition_size)

    return permutation_indexing