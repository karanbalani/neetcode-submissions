class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "#"
        encoded_string = ""

        for s in strs:
            length = len(s)
            encoded_string += str(length) + delimiter + s
        
        print(encoded_string)
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_list = []
        cursor = 0

        while cursor < len(s):
            print("cursor", cursor)

            len_str = ""

            while s[cursor] != "#":
                len_str += s[cursor]
                cursor += 1
                print(len_str)
            
            length = int(len_str)

            cursor += 1
            
            word = ""
            for i in range (cursor, cursor+length):
                word += s[i]
            
            cursor += length

            decoded_list.append(word)
        
        return decoded_list
