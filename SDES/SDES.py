class KeyGeneration:
    
    ten_bit_key = "1010000010"
    p10 = (3,5,2,7,4,10,1,9,8,6)
    p8 = (6,3,7,4,8,5,10,9)
    
    def generate_k1_k2(self):
        result_after_p10 = self.get_result_after_p10(self.ten_bit_key)
        left_shifted = self.left_shift_10_bit_keys(result_after_p10)
        k1 = self.get_result_after_p8(left_shifted)
        
        left_shifted = self.left_shift_10_bit_keys(left_shifted)
        left_shifted = self.left_shift_10_bit_keys(left_shifted)
        k2 = self.get_result_after_p8(left_shifted)
        
        return k1, k2
    
    def get_result_after_p10(self, value):
        result_after_p10 = ""
        for i in self.p10:
            result_after_p10 += value[i-1]
        return result_after_p10
    
    def get_result_after_p8(self, value):
        result_after_p8 = ""
        for i in self.p8:
            result_after_p8 += value[i-1]
        return result_after_p8
    
    def left_shift_10_bit_keys(self, value):
        left_shifted = ""
        left_half = list(value[:5])
        right_half = list(value[5:])
        
        temp = left_half[0]
        for i in range(len(left_half)):
            if i != 4:
                left_half[i] = left_half[i+1]
            else:
                left_half[i] = temp
    
        temp = right_half[0]
        for i in range(len(right_half)):
            if i != 4:
                right_half[i] = right_half[i+1]
            else:
                right_half[i] = temp
                
        return ''.join(left_half) + ''.join(right_half)

class SDES:
    
    IP = (2,6,3,1,4,8,5,7)
    IP_inv=(4,1,3,5,7,2,8,6)
    
    EP = (4,1,2,3,2,3,4,1)
    P4=(2,4,3,1)
    _xormap = {('0', '1'): '1', ('1', '0'): '1', ('1', '1'): '0', ('0', '0'): '0'}
    S0=[["01","00","11","10"],["11","10","01","00"],["00","10","01","11"],["11","01","11","10"]]
    S1=[["00","01","10","11"],["10","00","01","11"],["11","00","01","00"],["10","01","00","11"]]

    def xor(self, x, y):
        return ''.join([self._xormap[a, b] for a, b in zip(x, y)])
    
    def apply_IP(self, text):
        value_after_IP = ""
        for i in self.IP:
            value_after_IP += text[i-1]
        return value_after_IP
        
    def apply_IP_inv(self, text):
        value_after_IP_inv = ""
        for i in self.IP_inv:
            value_after_IP_inv += text[i-1]
        return value_after_IP_inv
        
    def apply_EP(self, text):
        value_after_EP = ""
        for i in self.EP:
            value_after_EP += text[i-1]
        return value_after_EP
    
    def apply_SBOXES(self, text):
        left_half = list(text[:4])
        right_half = list(text[4:])
        
        # SBOX0
        row = int(left_half[0]+left_half[3], 2)
        col = int(left_half[1]+left_half[2], 2)
        s0_val = self.S0[row][col]
        
        # SBOX1
        row = int(right_half[0]+right_half[3], 2)
        col = int(right_half[1]+right_half[2], 2)
        s1_val = self.S1[row][col]
        
        return s0_val+s1_val
    
    def apply_P4(self, text):
        value_after_P4 = ""
        for i in self.P4:
            value_after_P4 += text[i-1]
        return value_after_P4
        
    
    def get_cipher_text(self, k1, k2, text):
        value_after_IP = self.apply_IP(text)
        left_half = value_after_IP[:4]
        right_half = value_after_IP[4:]
        value_after_EP = self.apply_EP(right_half)
        value_after_XOR = self.xor(value_after_EP, k1)
        value_after_SBOXES = self.apply_SBOXES(value_after_XOR)
        value_after_P4 = self.apply_P4(value_after_SBOXES)
        value_after_XOR = self.xor(value_after_P4, left_half)
        
        new_text = right_half + value_after_XOR

        left_half = new_text[:4]
        right_half = new_text[4:]
        value_after_EP = self.apply_EP(right_half)
        value_after_XOR = self.xor(value_after_EP, k2)
        value_after_SBOXES = self.apply_SBOXES(value_after_XOR)
        value_after_P4 = self.apply_P4(value_after_SBOXES)
        value_after_XOR = self.xor(value_after_P4, left_half)
        
        new_text = value_after_XOR + right_half
        print(new_text)
        
        cipher_text = self.apply_IP_inv(new_text)
        return cipher_text
    

mKeyGen = KeyGeneration()
k1, k2 = mKeyGen.generate_k1_k2()
print(k1, k2)

mSDES = SDES()
eight_bit_plain_text = "01110010"
cipher_text = mSDES.get_cipher_text(k1,k2,eight_bit_plain_text)
print(cipher_text)

plain_text = mSDES.get_cipher_text(k2,k1,cipher_text)
print(plain_text)
        
        