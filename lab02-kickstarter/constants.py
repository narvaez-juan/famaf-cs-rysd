# encoding: utf-8
# Revisión 2019 (a Python 3 y base64): Pablo Ventura
# Revisiones 2013-2014 Carlos Bederián
# Revisión 2011 Nicolás Wolovick
# Copyright 2008-2010 Natalia Bidart y Daniel Moisset
# $Id: constants.py 388 2011-03-22 14:20:06Z nicolasw $

DEFAULT_DIR = 'testdata'
DEFAULT_ADDR = '0.0.0.0'  # 0.0.0.0 representa todas las IPv4 del server
DEFAULT_PORT = 19500


EOL = '\r\n'

# CODES #
CODE_OK = 0
BAD_EOL = 100
BAD_REQUEST = 101
INTERNAL_ERROR = 199
INVALID_COMMAND = 200
INVALID_ARGUMENTS = 201
FILE_NOT_FOUND = 202
BAD_OFFSET = 203

# PARSER #
PARSER_STATUS_OK = "OK"
PARSER_STATUS_MALFORMED = "MALFORMED"
PARSER_STATUS_UNKNOWN = "UNKNOWN"
PARSER_ASCII_CARRIAGE_RETURN = 13
"""
\\r
"""
PARSER_ASCII_LINE_FEED = 10
"""
\\n
"""

# COMMAND #
MAX_LENGTH_COMMAND = 100
MAX_LENGTH_FILE_NAME = 200

# EXECUTE #
EXECUTE_STATUS_EXIT = "QUIT"
EXECUTE_STATUS_OK = "OK"
EXECUTE_INVALID_COMMAND = "INVALID_COMMAND"
EXECUTE_INVALID_ARGUMENTS = "INVALID_ARGUMENTS"


error_messages = {
    CODE_OK: "OK",
    # 1xx: Errores fatales (no se pueden atender más pedidos)
    BAD_EOL: "BAD EOL",
    BAD_REQUEST: "BAD REQUEST",
    INTERNAL_ERROR: "INTERNAL SERVER ERROR",
    # 2xx: Errores no fatales (no se pudo atender este pedido)
    INVALID_COMMAND: "NO SUCH COMMAND",
    INVALID_ARGUMENTS: "INVALID ARGUMENTS FOR COMMAND",
    FILE_NOT_FOUND: "FILE NOT FOUND",
    BAD_OFFSET: "OFFSET EXCEEDS FILE SIZE",
}


def valid_status(s):
    return s in list(error_messages.keys())


def fatal_status(s):
    assert valid_status(s)
    return 100 <= s < 200


VALID_CHARS = set(".-_")
for i in range(ord('A'), ord('Z') + 1):
    VALID_CHARS.add(chr(i))
for i in range(ord('a'), ord('z') + 1):
    VALID_CHARS.add(chr(i))
for i in range(ord('0'), ord('9') + 1):
    VALID_CHARS.add(chr(i))
