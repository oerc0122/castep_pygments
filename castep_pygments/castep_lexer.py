"""
CASTEP Lexer for Pygments
"""
import re

from pygments.lexer import RegexLexer, bygroups, include, words
from pygments.token import Comment, Keyword
from pygments.token import Literal as Lit
from pygments.token import Name, Number, Operator, String, Text

from ._cell_kw import CELL
from ._param_kw import PARAM

__all__ = ['ParamFileLexer', 'CellFileLexer']


CASTEP_UNITS = words(("bohr", "m", "cm", "nm", "ang", "me", "amu",
                      "kg", "g", "aut", "s", "ms", "mus", "ns", "ps", "fs", "e", "c",
                      "hartree", "mhartree", "ev", "mev", "ry", "mry", "kj/mol",
                      "kcal/mol", "j", "erg", "hz", "mhz", "ghz", "thz", "cm-1", "k",
                      "hartree/bohr", "ev/ang", "n", "auv", "ang/ps", "ang/fs", "bohr/ps",
                      "bohr/fs", "m/s", "hartree/bohr**3", "ev/ang**3", "pa", "mpa", "gpa",
                      "atm", "bar", "mbar", "1/bohr", "1/m", "1/nm", "1/ang", "a0", "ha",
                      "dyne", "ha/bohr**2", "ev/ang**2", "n/m", "dyne/cm", "bohr**3",
                      "m**3", "cm**3", "nm**3", "ang**3", "acu", "ampere", "acd",
                      "amperemetre2", "amfd", "tesla", "gauss", "agr", "radsectesla",
                      "mhztesla", "bohr**2", "fm**2", "barn", "adu", "debye", "e**2/me",
                      "e**2/amu", "debye**2/ang**2/amu", "km/mol", "hartree/bohr/e",
                      "ev/ang/e", "n/c", "tpa", "ppa", "j/mol/k", "c/mol/k", "r", "hbar/2",
                      "hbar", "mub", "magneton", "pm", "1/pm", "pm**3", "pm/v",
                      "bohre/hartree", "ang/v",)).get()

BOOLEAN = r"(?:FALSE|TRUE|.FALSE.|.TRUE.|[FT])"
INTEGER = r"\b[0-9]+\b"
REAL = r"(?:[+-]?(?:\d*\.\d+|\d+\.\d*)(?:[Ee][+-]?\d{{1,3}})?)"
NUMBER = rf"(?:{REAL}|{INTEGER})"


def get_root_block(kwdict: dict):
    """Construct standard form for cell/param KW with matching argument"""
    return [
        (rf"{kwdict['physical']}(\s*[ =:]\s*)({NUMBER})(\s*){CASTEP_UNITS}?",
         bygroups(Name.Variable, Operator, Number.Float, Text.Whitespace, Keyword.Constant)),

        (rf"{kwdict['real']}(\s*[ =:]\s*)({NUMBER})",
         bygroups(Name.Variable, Operator, Number.Float)),

        (rf"{kwdict['boolean']}(\s*[ =:]\s*)({BOOLEAN})",
         bygroups(Name.Variable, Operator, Keyword.Pseudo)),

        (rf"{kwdict['int']}(\s*[ =:]\s*)({INTEGER})",
         bygroups(Name.Variable, Operator, Number.Integer)),

        (kwdict['defined'], Name.Variable),

        (rf"{kwdict['string']}(\s*[ =:]\s*)([^#!\n]*)",
         bygroups(Name.Variable, Operator, String)),

        (rf'(?m)(%block)(\s+){kwdict["block"]}(?:(\n){CASTEP_UNITS}(?!\w))?',
         bygroups(Name.Builtin, Text.Whitespace, Name.Variable, Text.Whitespace,
                  Keyword.Constant), 'block'),
    ]


def get_block_block(kwdict: dict):
    """Construct standard form for cell/param blocks"""
    return [
        include('comment'),
        (rf'(%endblock)(\s+){kwdict["block"]}',
         bygroups(Name.Builtin, Text.Whitespace, Name.Variable), '#pop'),
        (REAL, Number.Float),
        (INTEGER, Number.Integer),
        (BOOLEAN, Keyword.Constant),
        (r'\w+', String),
        (r'\s+', Text.Whitespace)
    ]


class ParamFileLexer(RegexLexer):
    """Simple lexer for CASTEP param files"""

    name = "CASTEP Param"
    aliases = ["castep_param"]
    filenames = ["*.param"]
    flags = re.IGNORECASE

    tokens = {
        'comment': [
            (r'[!#].*', Comment)
        ],
        'devel_code_val': [
            (r'(\w+)(=)([TF]|[0-9.-]+|\w+|\s*\"[\w\s]+\")',
             bygroups(Name.Variable, Operator, Lit)),
        ],
        'devel_code_key': [
            include('comment'),
            include('devel_code_val'),
            (r'(:)(end)(\w+)', bygroups(Operator, Operator, Name.Variable), '#pop'),
            (r'\s+', Text.Whitespace)
        ],
        'devel_code': [
            include('comment'),
            include('devel_code_val'),
            (r'(%endblock)(\s+)(DEVEL_CODE)',
             bygroups(Name.Builtin, Text.Whitespace, Name.Variable), '#pop'),
            (r'(\w+)(:)', bygroups(Name.Variable, Operator), 'devel_code_key'),
            (r'\s+', Text.Whitespace)
        ],
        'block': get_block_block(PARAM),
        'root': [
            include('comment'),
            (r'(%block)(\s+)(devel_code)',
             bygroups(Name.Builtin, Text.Whitespace, Name.Variable), 'devel_code'),
            *get_root_block(PARAM),
        ],
    }


class CellFileLexer(RegexLexer):
    """Simple lexer for CASTEP cell files"""

    name = "CASTEP Cell"
    aliases = ["castep_cell"]
    filenames = ["*.cell"]
    flags = re.IGNORECASE

    tokens = {
        'comment': [(r'[!#].*', Comment)],
        'block': get_block_block(CELL),
        'root': [include('comment'), *get_root_block(CELL)]
    }
