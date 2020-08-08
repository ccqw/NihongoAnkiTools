#!/usr/bin/env python3
import config
import jq
import requests as r

def main():
    headers = {'Authorization': 'Bearer {}'.format(config.api_key)}
    levels = [x for x in range(config.min_level, config.max_level + 1)]
    uri = 'subjects?types=vocabulary&level='

    # TODO handle pagination of results

    for level in levels:
        level_uri = '{}{}'.format(uri, level)
        endpoint = config.root_url + level_uri
        response = r.get(endpoint, headers=headers).json()
        words = iter(jq.compile('.data[].data | {"word": .slug, "meanings": [.meanings[].meaning], "sentences": .context_sentences, "wk_level": %d}' % level).input(response))
        while True:
            try:
                print(next(words))
            except StopIteration:
                break

    # TODO output as tsv for import to Anki


if __name__ == '__main__':
    main()
