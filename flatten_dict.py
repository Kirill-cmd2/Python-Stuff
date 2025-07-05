
def get_key_and_value(given_dict: dict):
    for key, value in zip(given_dict.keys(), given_dict.values()):
        yield key, value


def flatten_dict(given_dict: dict, *, sep='_') -> dict:
    # :)
    big_d = dict()

    for outer_key, outer_value in get_key_and_value(given_dict):
        if isinstance(outer_value, dict):
            small_d: dict = flatten_dict(outer_value, sep=sep)

            for inner_key, inner_value in get_key_and_value(small_d):
                big_d.update([(outer_key + sep + inner_key, inner_value)])

        else:
            big_d.update([(outer_key, outer_value)])

    return big_d



print(flatten_dict({'vowels': {'a': 1, 'e': 4}, 'sometitle': {'consonants': {'z': 2, 'v': 3}}, 'ZA': 'sev', 'AZ': 'gi', 'A': {'Z': {'Sev': 'gi'}}}))
