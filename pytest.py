import os
import sys
import unittest
import redactor
import glob

class TestRedactor(unittest.TestCase):
    def test1(self):  # for names_red() function
        input_file = ".txt"
        text_files = glob.glob(input_file)
        for file in text_files:
            with open(file, "r", encoding="utf-8") as f:
                data = f.read()
                result = redactor.names_red(data)
                self.assertIsNotNone(result)            

    def test2(self):  # for red_date()
        text = " John Smith lives at 123 Main Street. He is a software engineer, and his phone number is (555) 555-1212. She was born on June 1st, 1990."    
        result = redactor.red_date(text)
        self.assertIsNotNone(result)

    def test3(self): # for red_gender()
        text = "John Smith lives at 123 Main Street. He is a software engineer, and his phone number is (555) 555-1212. She was born on June 1st, 1990."  
        result = redactor.red_gender(text)
        self.assertIsNotNone(result)  

    def test4(self): # for red_phnum
        text = "John Smith lives at 123 Main Street. He is a software engineer, and his phone number is (555) 555-1212. She was born on June 1st, 1990."
        result = redactor.red_phnum(text)
        self.assertIsNotNone(result)

    def test5(self): # for red_add()
        text = " John Smith lives at 123 Main Street. He is a software engineer, and his phone number is (555) 555-1212. She was born on June 1st, 1990."    
        result = redactor.red_add(text)
        self.assertIsNotNone(result)

    def test6(self): # for redaction()
        text = "John Smith lives at 123 Main Street. He is a software engineer, and his phone number is (555) 555-1212. She was born on June 1st, 1990." 
        res_lt1, cnt1 = redactor.names_red(text)
        res_lt2, cnt2 = redactor.red_date(text)
        res_lt3, cnt3 = redactor.red_gender(text)
        res_lt4, cnt4 = redactor.red_add(text)
        res_lt5, cnt5 = redactor.red_phnum(text)
        res_lt6, cnt6 = redactor.redaction(res_lt1,res_lt2,res_lt3,res_lt4,res_lt5,text)
        tcnt = cnt1+cnt2+cnt3+cnt4+cnt5
        if cnt6 == tcnt:
            result = 1
        else:
            result = None    


if __name__ == '__main__':
    unittest.main()

