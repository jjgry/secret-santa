import random
import string
import urllib.parse
import argparse


def choose_receiver(giver, receivers):
    viable_receivers = receivers.copy()
    if giver in viable_receivers:
        viable_receivers.remove(giver)

    if len(viable_receivers) == 0:
        return (False, giver)
    else:
        return (True, random.choice(viable_receivers))


def make_pairs(names):
    givers = names.copy()
    receivers = givers.copy()

    pairs = []
    for giver in givers:
        (is_successful, receiver) = choose_receiver(giver, receivers)

        if is_successful:
            pairs.append((giver, receiver))
            receivers.remove(receiver)
        else:
            return make_pairs(names)
    return pairs


def random_url(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def create_webpages(group_name, group_name_url, pairs):
    with open('./template.shtml') as template:
        text = template.read()
        text = text.replace('GROUP_NAME', group_name)

    for (giver, receiver) in pairs:
        if giver == 'index':
            raise Exception("'{}' is not an acceptable name".format(giver))
        giver_safe = urllib.parse.quote(giver).lower()
        new_filepath = './{}/{}-{}.shtml'.format(
            group_name_url, giver_safe, random_url(20))

        modified_text = text.replace('RECEIVER', receiver)

        with open(new_filepath, 'w') as new_file:
            new_file.write(modified_text)


def main():
    # group_name = 'Girl Gang'
    # group_name_url = 'girl-gang'
    # names = ['Balint', 'Benjamin', 'Izzy', 'JJ', 'Sid']
    # pairs = make_pairs(names)
    # create_webpages(group_name, group_name_url, pairs)

    group_name = 'Ladingtons'
    group_name_url = 'test'
    names = ['Andrew', 'Brad', 'JJ', 'Joe', 'Grant', 'Dmitry']
    pairs = make_pairs(names)
    create_webpages(group_name, group_name_url, pairs)

    CLI = argparse.ArgumentParser()
    CLI.add_argument(
        "names",  # name on the CLI - drop the `--` for positional/required parameters
        nargs="*",  # 0 or more values expected => creates a list
        type=str,
        default=None,  # default if nothing is provided
    )
    CLI.add_argument(
        "--name-urls",
        nargs="*",
        type=str,  # any type/callable can be used here
        default=None,
    )
    CLI.add_argument(
        "--group",
        nargs="*",
        type=str,  # any type/callable can be used here
        default=None,
    )
    CLI.add_argument(
        "--group-url",
        nargs="*",
        type=str,  # any type/callable can be used here
        default=None,
    )


if __name__ == "__main__":
    main()
