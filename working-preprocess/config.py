import logging
import re

class Config() :
    CLASSIFIED_COLUMNS = ['원문', '현상', '원인', '조치', '요망']

    LANG_THRESHOLD = 6
    LANG_REGEX = {
        'kor' : re.compile(r"[ㄱ-ㅣ가-힣]"),
        'etc' : re.compile(r"[^\x00-\x7F]+")
    }

    SPLIT_REGEX = re.compile(r"[1-4][.][가-힣 ]+\s+:\s+")

    SEARCH_REGEX = [
        {
            'a' : r"1([,.]|[ ]|[:;]|현상){2,}\s*[:;]?",
            'b' : r"2([,.]|[ ]|[:;]|((점검[가-힣 ]*)|([가-힣 ]*원인))){2,}[:;]?",
            'c' : r"3([,.]|[ ]|[:;]|조치(내용)?){2,}[:;]?",
            'd' : r"4([,.]|[ ]|[:;]|요망(사항)?){2,}[:;]?"
        },
        {
            'a' : r"현상\s*[:;\)]",
            'b' : r"(점검[가-힣 ]*|[가-힣 ]*원인)\s*[:;\)]",
            'c' : r"조치\s*[:;\)]",
            'd' : r"요망\s*[:;\)]"
        },
        {
            'a' : r"^\[[A-Z]\]1[.,]",
            'b' : r"\s+2[.,]",
            'c' : r"\s+3[.,]",
            'd' : r"\s+4[.,]"
        },
        {
            'a' : r"^\[[A-Z]\]현상[ ]+",
            'b' : r"[ ]+원인[ ]+",
            'c' : r"[ ]+조치[ ]+",
            'd' : r"[ ]+요망[ ]+"
        }
    ]

def get_logger() :
    def get_handler(kind) :
        handler = None
        if kind == 'stream' :
            handler = logging.StreamHandler()
        elif kind == 'file' :
            handler = logging.FileHandler()
        return handler
    def get_formatter(custom = None) :
        fmt = '%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s'
        if custom :
            fmt = custom
        formatter = logging.Formatter(fmt)
        return formatter

    logger = logging.getLogger() # root logger
    handler = get_hanlder('stream')
    formatter = get_formatter()
    
    handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger
