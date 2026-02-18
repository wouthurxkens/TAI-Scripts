STANDARD_TOKENS = [
    (0xCE, "If "), (0xCF, "Then"), (0xD0, "Else"), (0xD3, "For("), (0xD1, "While "),
    (0xD2, "Repeat "), (0xD4, "End"), (0xD8, "Pause "), (0xD8, "Pause"), (0xD6, "Lbl "),
    (0xD7, "Goto "), (0xDA, "IS>("), (0xDB, "DS<("), (0xE6, "Menu("), (0x5F, "prgm"),
    (0xD5, "Return"), (0xD9, "Stop"), (0xDC, "Input "), (0xDD, "Prompt "), (0xDE, "Disp "),
    (0xDF, "DispGraph"), (0xE5, "DispTable"), (0xE0, "Output("), (0xAD, "getKey"),
    (0xE1, "ClrHome"), (0xFB, "ClrTable"), (0xE8, "Get("), (0xE7, "Send("),
    (0xE9, "PlotsOn "), (0xEA, "PlotsOff "), (0x84, "Trace"), (0x86, "ZStandard"),
    (0x87, "ZTrig"), (0x88, "ZBox"), (0x89, "ZoomIn"), (0x8A, "ZoomOut"), (0x8B, "ZSquare"),
    (0x8C, "ZInteger"), (0x8D, "ZPrevious"), (0x8E, "ZDecimal"), (0x8F, "ZoomStat"),
    (0x90, "ZoomRcl"), (0x92, "ZoomSto"), (0x93, "Text("), (0x98, "StorePic"),
    (0x99, "RecallPic"), (0x9A, "StoreGDB"), (0x01, "->DMS"), (0x02, "->DEC"),
    (0x03, "->FRAC"), (0x04, "->"), (0x05, "BoxPlot"), (0x0A, "[radians]"),
    (0x0B, "[degrees]"), (0x0C, "^-1"), (0x0D, "^2"), (0x0E, "[transpose]"),
    (0x0F, "^3"), (0x12, "round("), (0x13, "pxl-Test("), (0x14, "augment("),
    (0x15, "RowSwap("), (0x16, "row+("), (0x17, "*row("), (0x18, "*row+("),
    (0x19, "max("), (0x1B, "min("), (0x1F, "median("), (0x20, "randM("),
    (0x21, "mean("), (0x22, "solve("), (0x23, "seq("), (0x24, "fnInt("),
    (0x25, "NDeriv("), (0x27, "FMin("), (0x28, "FMax("), (0x2E, "CubicReg "),
    (0x2F, "QuartReg "), (0x3C, " or "), (0x3D, " xor "), (0x40, "and"),
    (0x5B, "[theta]"), (0x5F, "prgm"), (0x64, "Radian"), (0x65, "Degree"),
    (0x66, "Normal"), (0x67, "Sci"), (0x68, "Eng"), (0x69, "Float"),
    (0x6D, "<="), (0x6E, ">="), (0x6F, "!="), (0x72, "Ans"), (0x73, "Fix "),
    (0x74, "Horiz"), (0x75, "Full"), (0x76, "Func"), (0x77, "Param"),
    (0x78, "Polar"), (0x79, "Seq"), (0x7A, "IndpntAuto"), (0x7B, "IndpntAsk"),
    (0x7C, "DependAuto"), (0x7D, "DependAsk"), (0x7F, "[box]"), (0x81, "[dot]"),
    (0x84, "Trace"), (0x85, "ClrDraw"), (0x86, "ZStandard"), (0x87, "ZTrig"),
    (0x88, "ZBox"), (0x89, "Zoom In"), (0x8A, "Zoom Out"), (0x8B, "ZSquare"),
    (0x8C, "ZInteger"), (0x8D, "ZPrevious"), (0x8E, "ZDecimal"), (0x8F, "ZoomStat"),
    (0x90, "ZoomRcl"), (0x91, "PrintScreen"), (0x92, "ZoomSto"), (0x93, "Text("),
    (0x94, "nPr"), (0x95, "nCr"), (0x96, "FnOn "), (0x97, "FnOff "),
    (0x98, "StorePic "), (0x99, "RecallPic "), (0x9A, "StoreGDB "), (0x9B, "RecallGDB "),
    (0x9C, "Line("), (0x9D, "Vertical "), (0x9E, "Pt-On("), (0x9F, "Pt-Off("),
    (0xA0, "Pt-Change("), (0xA1, "Pxl-On("), (0xA2, "Pxl-Off("), (0xA3, "Pxl-Change("),
    (0xA4, "Shade("), (0xA5, "Circle("), (0xA6, "Horizontal "), (0xA7, "Tangent("),
    (0xA8, "DrawInv "), (0xA9, "DrawF "), (0xAC, "[pi]"), (0xAD, "getKey"),
    (0xB0, "[neg]"), (0xB1, "int("), (0xB2, "abs("), (0xB3, "det("),
    (0xB4, "identity("), (0xB5, "dim("), (0xB6, "sum("), (0xB7, "prod("),
    (0xB8, "not("), (0xB9, "iPart("), (0xBA, "fPart("), (0xBC, "[root]^2"),
    (0xBD, "[root]^3"), (0xBE, "ln("), (0xBF, "e^"), (0xC0, "log("),
    (0xC1, "10^("), (0xC2, "sin("), (0xC3, "asin("), (0xC4, "cos("),
    (0xC5, "acos("), (0xC6, "tan("), (0xC7, "atan("), (0xC8, "sinh("),
    (0xC9, "asinh("), (0xCA, "cosh("), (0xCB, "acosh("), (0xCC, "tanh("),
    (0xCD, "atanh("), (0xD0, "Else"), (0xE2, "Fill("), (0xE3, "SortA("),
    (0xE4, "SortD("), (0xEB, "[list]"), (0xEC, "Plot1("), (0xED, "Plot2("),
    (0xEE, "Plot3("), (0xF1, "[root]^"), (0xF2, "1-Var Stats "), (0xF3, "2-Var Stats "),
    (0xF4, "LinReg(a+bx) "), (0xF5, "ExpReg "), (0xF6, "LnReg "), (0xF7, "PwrReg "),
    (0xF8, "Med-Med "), (0xF9, "QuadReg "), (0xFA, "ClrList "), (0xFB, "ClrTable"),
    (0xFC, "Histogram"), (0xFD, "xyLine"), (0xFE, "Scatter"), (0xFF, "LinReg(ax+b) "),
    (0xAB, "rand")
]

CALC_VARS = [
    (0x6CBB, "AsmPrgm"), (0x6DBB, "AsmPrgm"), (0x005C, "[A]"), (0x015C, "[B]"),
    (0x025C, "[C]"), (0x035C, "[D]"), (0x045C, "[E]"), (0x055C, "[F]"),
    (0x065C, "[G]"), (0x075C, "[H]"), (0x085C, "[I]"), (0x095C, "[J]"),
    (0x005D, "L1"), (0x015D, "L2"), (0x025D, "L3"), (0x035D, "L4"),
    (0x045D, "L5"), (0x055D, "L6"), (0x065D, "L7"), (0x075D, "L8"),
    (0x085D, "L9"), (0x095D, "L0"), (0x105E, "Y1"), (0x115E, "Y2"),
    (0x125E, "Y3"), (0x135E, "Y4"), (0x145E, "Y5"), (0x155E, "Y6"),
    (0x165E, "Y7"), (0x175E, "Y8"), (0x185E, "Y9"), (0x195E, "Y0"),
    (0x00AA, "STR1"), (0x01AA, "STR2"), (0x02AA, "STR3"), (0x03AA, "STR4"),
    (0x04AA, "STR5"), (0x05AA, "STR6"), (0x06AA, "STR7"), (0x07AA, "STR8"),
    (0x08AA, "STR9"), (0x09AA, "STR0"), (0x6ABB, "Asm(")
]

REPLACEMENTS = [
    ('"', 0x2A), ('\'', 0xAE), (',', 0x2B), ('?', 0xAF), (' ', 0x29),
    ('=', 0x6A), ('<', 0x6B), ('>', 0x6C), ('+', 0x70), ('-', 0x71),
    ('/', 0x83), ('*', 0x82), ('!', 0x2D), (':', 0x3E), ('\n', 0x3F),
    ('0', 0x30), ('1', 0x31), ('2', 0x32), ('3', 0x33), ('4', 0x34),
    ('5', 0x35), ('6', 0x36), ('7', 0x37), ('8', 0x38), ('9', 0x39),
    ('.', 0x3A), ('[', 0x06), (']', 0x07), ('{', 0x08), ('}', 0x09),
    ('(', 0x10), (')', 0x11), ('&', 0x40), ('|', 0x3C), ('~', 0x3D),
    ('^', 0xF0)
]

TOKEN_LOOKUP = {}
REVERSE_LOOKUP = {}
LONGEST_INPUT = 0

def initialize_tokens():
    """Builds the forward and reverse lookup tables."""
    global LONGEST_INPUT
    
    # Process 1-byte standard tokens
    for token_val, text in STANDARD_TOKENS:
        TOKEN_LOOKUP[text] = {'token': token_val, 'sz': 1}
        REVERSE_LOOKUP[token_val] = text
        LONGEST_INPUT = max(LONGEST_INPUT, len(text))
        
    # Process 2-byte variables
    for token_val, text in CALC_VARS:
        TOKEN_LOOKUP[text] = {'token': token_val, 'sz': 2}
        REVERSE_LOOKUP[token_val] = text
        LONGEST_INPUT = max(LONGEST_INPUT, len(text))
        
    # Process single-character replacements
    for char, token_val in REPLACEMENTS:
        TOKEN_LOOKUP[char] = {'token': token_val, 'sz': 1}
        REVERSE_LOOKUP[token_val] = char

def lookup_token_by_str(s):
    return TOKEN_LOOKUP.get(s)

def lookup_token_by_val(val):
    return REVERSE_LOOKUP.get(val)

initialize_tokens()
