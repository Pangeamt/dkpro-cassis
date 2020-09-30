from tests.fixtures import *

SENTENCE_NS = 'de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Sentence'
TOKEN_NS = 'de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Token'


def test_offsets_rewrite():
    # Text='Hello! 😈. \nYes, I do 😈.\n'
    gold_sentences = [
        "Hello!",
        "😈.",
        "Yes, I do 😈."
    ]
    gold_sentences_offsets = [
        (0, 6),
        (7, 9),
        (11, 23)
    ]

    gold_tokens = [
        ['Hello', '!'],
        ['😈', '.'],
        ['Yes', ',', 'I', 'do', '😈', '.']
    ]

    with open('test_files/typesystems/offsets_rewrite.xml', 'rb') as f:
        ts = load_typesystem(f)

    with open('test_files/xmi/offsets_rewrite.xmi', 'rb') as f:
        cas = load_cas_from_xmi(f, typesystem=ts)
        for i, sentence in enumerate(cas.select(SENTENCE_NS)):
            assert sentence.get_covered_text() == gold_sentences[i]
            assert sentence.begin == gold_sentences_offsets[i][0]
            assert sentence.end == gold_sentences_offsets[i][1]

            for j, token in enumerate(cas.select_covered(TOKEN_NS, sentence)):
                assert token.get_covered_text() == gold_tokens[i][j]















