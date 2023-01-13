from model.DictEntry import DictEntry
from model.Meaning import Meaning
from functools import reduce


def to_html(dict_entry: DictEntry) -> str:

    return f"""
            <h1>{dict_entry.word.capitalize()}</h1>
            {reduce(lambda a,b:a+b, [meaning_to_html(m, i+1) for i, m in enumerate(dict_entry.meanings)])}
            """


def meaning_to_html(m: Meaning, index: int) -> str:

    return f"""
            <h2>Meaning {index}</h2>
            <p>{m.word_type.name}</p>
            <p>{m.definition}</p>
            <h3>Examples:</h3>
            {m.tags}
            """
