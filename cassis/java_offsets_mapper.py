from typing import Dict


class JavaOffsetsMapper:
    """
    To deal with Java string offsets.
    """
    def __init__(self, text: str):
        self.text = text
        self.python_to_java_begin_map: Dict[int, int] = {}
        self.python_to_java_end_map: Dict[int, int] = {0: 0}

        accumulated_length = 0
        for i, char in enumerate(text):
            # Python to java begin
            self.python_to_java_begin_map[i] = accumulated_length

            # Calculate java char length
            char_length = JavaOffsetsMapper.java_text_length(char)
            accumulated_length += char_length

            # Python to java end
            self.python_to_java_end_map[i+1] = accumulated_length

        # Java to python begin
        self.java_to_python_begin_map: Dict[int, int] = \
            {v: k for k, v in self.python_to_java_begin_map.items()}

        # Java to python end
        self.java_to_python_end_map: Dict[int, int] = \
            {v: k for k, v in self.python_to_java_end_map.items()}

    @staticmethod
    def java_text_length(text: str):
        return len(text.encode('utf-16-le')) // 2  # le (little indian) to avoid BOM mark

    def java_to_python_begin(self, java_begin: int):
        return self.java_to_python_begin_map[java_begin]

    def java_to_python_end(self, java_end: int):
        return self.java_to_python_end_map[java_end]

    def python_to_java_begin(self, begin: int):
        return self.python_to_java_begin_map[begin]

    def python_to_java_end(self, end: int):
        return self.python_to_java_end_map[end]