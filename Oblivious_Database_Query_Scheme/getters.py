""" The getters for the different variables used by the application. """

# Imports.
from pathlib import Path
from os import chdir


def working_directory_validation() -> None:
    """
        Validates the path to the Oblivious Database Query directory.

        Parameters:
            -

        Returns:
            :raises Exception
            -
    """

    global working_directory

    try:
        chdir(working_directory)
    except Exception as e:
        print(f'Error occurred in validating the working directory. {e}')


def mp_spdz_directory_validation() -> None:
    """
        Validates the path to the MP-SPDZ directory.

        Parameters:
            -

        Returns:
            :raises NotADirectoryError
            -
    """

    global mp_spdz_directory

    if not mp_spdz_directory.is_dir() or not mp_spdz_directory.exists():
        raise NotADirectoryError('The MP-SPDZ path is not valid.')


def get_encoding_base() -> int:
    """ Getter for the encoding_base variable. """
    encoding_base = 16
    return encoding_base


def get_number_of_bytes() -> int:
    """ Getter for the number_of_bytes variable. """
    block_size = get_block_size()
    number_of_bytes = block_size // 8
    return number_of_bytes


def get_max_file_length() -> int:
    """ Getter for the max_file_length variable. """
    max_file_length = 6016
    return max_file_length


def get_number_of_blocks() -> int:
    """ Getter for the number_of_blocks variable. """
    number_of_blocks = get_max_file_length() // get_encoding_base()
    return number_of_blocks


def get_database_size() -> int:
    """ Getter for the database_size variable. """
    database_size = 2**4
    return database_size


def get_number_of_records() -> int:
    """ Getter for the number_of_records variable. """
    number_of_records = 10
    return number_of_records


def get_number_of_dummy_items() -> int:
    """ getter for the number_of_dummy_items variable. """
    number_of_dummy_items = get_database_size() - get_number_of_records()
    return number_of_dummy_items


def get_working_directory() -> Path:
    """ Getter for the working_directory variable. """
    global working_directory
    return working_directory


def get_mp_spdz_directory() -> Path:
    """ Getter for the MP_SPDZ_directory variable. """
    global mp_spdz_directory
    return mp_spdz_directory


def get_supplementary_data_directory() -> Path:
    """ Getter for the supplementary_data_directory variable. """
    global working_directory
    supplementary_data_directory = working_directory / 'Server' / 'Utilities' / 'Data_Generation' / 'Supplementary_Data'
    return supplementary_data_directory


def get_block_size() -> int:
    """ Getter for the block_size variable. """
    block_size = 128
    return block_size


def get_records_directory() -> Path:
    """ Getter for the records_directory variable. """
    records_directory = get_working_directory() / 'Server' / 'PNR_Records'
    return records_directory


def get_excluded_records() -> list:
    """ Getter for the excluded_records variable. """
    excluded_records = ['Sample_Record.json']
    return excluded_records


def get_encrypted_records_directory() -> Path:
    """ Getter for the encrypted_records_directory variable. """
    global working_directory
    encrypted_records_directory = working_directory / 'Server' / 'Encrypted_PNR_Records'
    return encrypted_records_directory


def get_client_mp_spdz_input_directory() -> Path:
    """ Getter for the client_mp_spdz_input_directory variable. """
    global working_directory
    client_mp_spdz_input_directory = working_directory / 'Client' / 'MP_SPDZ_Inputs'
    return client_mp_spdz_input_directory


def get_client_mp_spdz_input_path() -> Path:
    """ Getter for the client_mp_spdz_input_file variable. """
    global working_directory
    client_mp_spdz_input_path = working_directory / 'Client' / 'MP_SPDZ_Inputs' / 'Client_Input'
    return client_mp_spdz_input_path


def get_client_mp_spdz_output_directory() -> Path:
    """ Getter for the client_mp_spdz_output_directory variable. """
    global working_directory
    client_mp_spdz_output_directory = working_directory / 'Client' / 'MP_SPDZ_Outputs'
    return client_mp_spdz_output_directory


def get_client_mp_spdz_output_path() -> Path:
    """ Getter for the client_mp_spdz_output_path variable. """
    global working_directory
    client_mp_spdz_output_path = working_directory / 'Client' / 'MP_SPDZ_Outputs' / 'Client_Output'
    return client_mp_spdz_output_path


def get_server_mp_spdz_input_directory() -> Path:
    """ Getter for the server_mp_spdz_input_directory variable. """
    global working_directory
    server_mp_spdz_input_directory = working_directory / 'Server' / 'MP_SPDZ_Inputs'
    return server_mp_spdz_input_directory


def get_server_mp_spdz_input_path() -> Path:
    """ Getter for the server_mp_spdz_input_path variable. """
    global working_directory
    server_mp_spdz_input_path = working_directory / 'Server' / 'MP_SPDZ_Inputs' / 'Server_Input'
    return server_mp_spdz_input_path


def get_server_mp_spdz_output_directory() -> Path:
    """ Getter for the server_mp_spdz_output_directory variable. """
    global working_directory
    server_mp_spdz_output_directory = working_directory / 'Server' / 'MP_SPDZ_Outputs'
    return server_mp_spdz_output_directory


def get_server_mp_spdz_output_path() -> Path:
    """ Getter for the server_mp_spdz_output_path variable. """
    global working_directory
    server_mp_spdz_output_path = working_directory / 'Server' / 'MP_SPDZ_Outputs' / 'Server_Output'
    return server_mp_spdz_output_path


def get_sort_and_encrypt_with_circuit_mpc_script_path() -> Path:
    """ Getter for the sort_and_encrypt_with_circuit variable. """
    global working_directory
    sort_and_encrypt_with_circuit_path = (working_directory.parent / 'MP_SPDZ_Scripts' /
                                          f'sort_and_encrypt_with_circuit.mpc')
    return sort_and_encrypt_with_circuit_path


def get_sort_and_reencrypt_with_circuit_mpc_script_path() -> Path:
    """ Getter for the sort_and_reencrypt_with_circuit_mpc_script_path variable. """
    global working_directory
    sort_and_reencrypt_with_circuit_mpc_script_path = (working_directory.parent / 'MP_SPDZ_Scripts' /
                                                       f'sort_and_reencrypt_with_circuit.mpc')
    return sort_and_reencrypt_with_circuit_mpc_script_path


def get_aes_128_with_circuit_mpc_script_path() -> Path:
    """ Getter for the aes_128_mpc_script_path variable. """
    global working_directory
    aes_128_ecb_with_circuit_mpc_script_path = (working_directory.parent / 'MP_SPDZ_Scripts' /
                                                'aes_128_ecb_with_circuit.mpc')
    return aes_128_ecb_with_circuit_mpc_script_path


def get_if_else_circuit_path() -> Path:
    """ Getter for the if_else_circuit_path variable. """
    global working_directory
    if_else_circuit_path = working_directory.parent / 'MP_SPDZ_Circuits' / f'if_else{get_block_size()}.txt'
    return if_else_circuit_path


def get_sort_and_encrypt_circuit_path() -> Path:
    """ Getter for the sort_and_encrypt_circuit variable. """
    sort_and_encrypt_circuit = working_directory.parent / 'MP_SPDZ_Circuits' / f'sort_and_encrypt{get_block_size()}.txt'
    return sort_and_encrypt_circuit


def get_sort_and_reencrypt_circuit_path() -> Path:
    """ Getter for the sort_and_reencrypt_circuit variable. """
    sort_and_reencrypt_circuit = (working_directory.parent / 'MP_SPDZ_Circuits' /
                                  f'sort_and_reencrypt{get_block_size()}.txt')
    return sort_and_reencrypt_circuit


def get_mp_spdz_scripts_directory() -> Path:
    """ Getter for the mp_spdz_scripts_directory variable. """
    global mp_spdz_directory
    mp_spdz_scripts_path = mp_spdz_directory / 'Programs' / 'Source'
    return mp_spdz_scripts_path


def get_mp_spdz_circuits_directory() -> Path:
    """ Getter for the MP_SPDZ_circuits_directory variable. """
    global mp_spdz_directory
    mp_spdz_circuits_path = mp_spdz_directory / 'Programs' / 'Circuits'
    return mp_spdz_circuits_path


def get_mp_spdz_compile_path() -> Path:
    """ Getter for the MP_SPDZ_compile_path variable. """
    global mp_spdz_directory
    mp_spdz_compile_path = mp_spdz_directory / 'compile.py'
    return mp_spdz_compile_path


def get_inverted_index_matrix_path() -> Path:
    """ Getter for the inverted_index_matrix_path variable. """
    global working_directory
    inverted_index_matrix_path = working_directory / 'Server' / 'Indexing' / 'Inverted_Index_Matrix.json'
    return inverted_index_matrix_path


def get_server_encrypted_inverted_index_matrix_path() -> Path:
    """ Getter for the encrypted_inverted_index_matrix_path variable. """
    global working_directory
    encrypted_inverted_index_matrix_path = (working_directory / 'Server' / 'Indexing' /
                                            'Encrypted_Inverted_Index_Matrix.json')
    return encrypted_inverted_index_matrix_path


def get_client_indexing_directory() -> Path:
    """ Getter for the client_indexing_directory variable. """
    global working_directory
    client_indexing_directory = working_directory / 'Client' / 'Indexing'
    return client_indexing_directory


def get_client_encrypted_inverted_index_matrix_path() -> Path:
    """ Getter for the client_encrypted_inverted_index_matrix_path variable. """
    client_encrypted_inverted_index_matrix_path = (get_client_indexing_directory() /
                                                   'Encrypted_Inverted_Index_Matrix.json')
    return client_encrypted_inverted_index_matrix_path


def get_permutation_indexing_path() -> Path:
    """ Getter for the permutation_indexing_path variable. """
    global working_directory
    permutation_indexing_path = working_directory / 'Client' / 'Indexing' / 'Permutation_Indexing.json'
    return permutation_indexing_path


def get_retrieved_records_directory() -> Path:
    """ Getter for the retrieved_records_directory variable. """
    global working_directory
    retrieved_records_directory = working_directory / 'Client' / 'Retrieved_Records'
    return retrieved_records_directory


def get_records_encryption_key_streams_directory() -> Path:
    """ Getter for the records_encryption_keys_directory variable. """
    global working_directory
    records_encryption_keys_directory = working_directory / 'Client' / 'Records_Encryption_Key_Streams'
    return records_encryption_keys_directory


def get_client_networking_directory() -> Path:
    """ Getter for the client_networking_directory variable. """
    client_networking_directory = working_directory / 'Client' / 'Networking'
    return client_networking_directory


def get_client_networking_key_path() -> Path:
    """ Getter for the client_networking_key_path variable. """
    client_networking_key_path = working_directory / 'Client' / 'Networking' / 'key.pem'
    return client_networking_key_path


def get_client_networking_certificate_path() -> Path:
    """ Getter for the client_networking_key_path variable. """
    client_networking_certificate_path = working_directory / 'Client' / 'Networking' / 'cert.pem'
    return client_networking_certificate_path


def get_server_networking_directory() -> Path:
    """ Getter for the server_networking_directory variable. """
    server_networking_directory = working_directory / 'Server' / 'Networking'
    return server_networking_directory


def get_server_networking_key_path() -> Path:
    """ Getter for the server_networking_key_path variable. """
    server_networking_key_path = working_directory / 'Server' / 'Networking' / 'key.pem'
    return server_networking_key_path


def get_server_networking_certificate_path() -> Path:
    """ Getter for the client_networking_key_path variable. """
    server_networking_certificate_path = working_directory / 'Server' / 'Networking' / 'cert.pem'
    return server_networking_certificate_path


def get_server_encryption_keys_directory() -> Path:
    """ Getter for the server_encryption_keys_directory variable. """
    server_encryption_keys_directory = working_directory / 'Server' / 'Encryption_Keys'
    return server_encryption_keys_directory


def get_inverted_index_matrix_encryption_key_path() -> Path:
    """ Getter for the inverted_index_matrix_encryption_key_path variable. """
    inverted_index_matrix_encryption_key_path = working_directory / 'Server' / 'Encryption_Keys' / 'Encryption_Key.txt'
    return inverted_index_matrix_encryption_key_path


def get_requested_indices_path() -> Path:
    """ Getter for the requested_indices_path variable. """
    global working_directory
    requested_indices_path = working_directory / 'Client' / 'Indexing' / 'Requested_Pointers.txt'
    return requested_indices_path


def get_server_indexing_files_directory() -> Path:
    """ Getter for the server_indexing_files_directory variable. """
    global working_directory
    server_indexing_files_directory = working_directory / 'Server' / 'Indexing'
    return server_indexing_files_directory


working_directory = Path.cwd()
mp_spdz_directory = Path.cwd().parent.parent.parent / 'mp-spdz-0.3.8'
