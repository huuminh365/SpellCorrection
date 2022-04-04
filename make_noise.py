import pandas as pd
import numpy as np
import unidecode
import re

chars_regrex = '[aàảãáạăằẳẵắặâầẩẫấậAÀẢÃÁẠĂẰẲẴẮẶÂẦẨẪẤẬoòỏõóọôồổỗốộơờởỡớợOÒỎÕÓỌÔỒỔỖỐỘƠỜỞỠỚỢeèẻẽéẹêềểễếệEÈẺẼÉẸÊỀỂỄẾỆuùủũúụưừửữứựUÙỦŨÚỤƯỪỬỮỨỰiìỉĩíịIÌỈĨÍỊyỳỷỹýỵYỲỶỸÝỴnNvVmMCG]'
same_chars = {
    'a': ['á', 'à', 'ả', 'ã', 'ạ', 'ấ', 'ầ', 'ẩ', 'ẫ', 'ậ', 'ắ', 'ằ', 'ẳ', 'ẵ', 'ặ'],
    'A': ['Á','À','Ả','Ã','Ạ','Ấ','Ầ','Ẩ','Ẫ','Ậ','Ắ','Ằ','Ẳ','Ẵ','Ặ'],
    'O': ['Ó','Ò','Ỏ','Õ','Ọ','Ô','Ố','Ồ','Ổ','Ỗ','Ộ','Ơ','Ớ','Ờ','Ở','Ỡ','Ợ','Q'],
    'o': ['ó', 'ò', 'ỏ', 'õ', 'ọ', 'ô', 'ố', 'ồ', 'ổ', 'ỗ', 'ộ', 'ơ','ớ', 'ờ', 'ở', 'ỡ', 'ợ', 'q'],
    'e': ['é', 'è', 'ẻ', 'ẽ', 'ẹ', 'ế', 'ề', 'ể', 'ễ', 'ệ', 'ê'],
    'E': ['É', 'È', 'Ẻ', 'Ẽ', 'Ẹ', 'Ế', 'Ề', 'Ể', 'Ễ', 'Ệ', 'Ê'],
    'u': ['ú', 'ù', 'ủ', 'ũ', 'ụ', 'ứ', 'ừ', 'ử', 'ữ', 'ự', 'ư'],
    'U': ['Ú', 'Ù', 'Ủ', 'Ũ', 'Ụ', 'Ứ', 'Ừ', 'Ử', 'Ữ', 'Ự', 'Ư'],
    'i': ['í', 'ì', 'ỉ', 'ĩ', 'ị'],
    'I': ['Í', 'Ì', 'Ỉ', 'Ĩ', 'Ị'],
    'y': ['ý', 'ỳ', 'ỷ', 'ỹ', 'ỵ', 'v'],
    'Y': ['Ý', 'Ỳ', 'Ỷ', 'Ỹ', 'Ỵ', 'V'],
    'n': ['m'],
    'N': ['N'],
    'v': ['y'],
    'V': ['Y'],
    'm': ['n'],
    'M': ['N'],
    'C': ['G'],
    'G': ['C']
}


#sai dấu
def remove_random_accent(df_text, ratio=0.15):
        data = []
        for text in df_text:
            words = text.split()
            mask = np.random.random(size=len(words)) < ratio
            for i in range(len(words)):
                if mask[i]:
                    words[i] = unidecode.unidecode(words[i])
                    break
            data.append(' '.join(words))
            
        return data

#sai khoảng cách
def remove_random_space(df_text):
    data = []
    for text in df_text:
        words = text.split()
        n_words = len(words)
        start = np.random.randint(low=0, high=n_words, size=1)[0]
        
        if start + 3 < n_words:
            end = np.random.randint(low=start, high=start + 3, size=1)[0]
        else:
            end = np.random.randint(low=start, high=n_words, size=1)[0]

        out = ' '.join(words[:start])  + ' ' + ''.join(words[start:end + 1]) + ' ' + ' '.join(words[end + 1:])

        data.append(out.strip())
    return data

#sai từ 
def _char_regrex(text):
    match_chars = re.findall(chars_regrex, text)
    return match_chars

def _random_replace(text, match_chars):
    replace_char = match_chars[np.random.randint(low=0, high=len(match_chars), size=1)[0]]
    insert_chars = same_chars[unidecode.unidecode(replace_char)]
    insert_char = insert_chars[np.random.randint(low=0, high=len(insert_chars), size=1)[0]]
    text = text.replace(replace_char, insert_char, 1)

    return text

def change(text):
    match_chars = _char_regrex(text)
    if len(match_chars) == 0:
        return text

    text = _random_replace(text, match_chars)

    return text

def replace_accent_chars(df_text, ratio=0.15):
    data = []
    for text in df_text:
        words = text.split()
        mask = np.random.random(size=len(words)) < ratio

        for i in range(len(words)):
            if mask[i]:
                words[i] = change(words[i])
                break          
        data.append(' '.join(words))
    return data



