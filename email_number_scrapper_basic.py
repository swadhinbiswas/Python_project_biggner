import re

class Parser:
    def __init__(self,text):
        self.text=text 
    
    def emails(self):
        match=re.search(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]',self.text)
        if match:
            return match.group(0)
        return None
    def phone(self):
        match = re.search(r'\d{3}-\d{3}-\d{4}', self.text)
        if match:
            return match.group(0)
        return None
    
    def parse(self):
        return {
            'email':self.emails(),
            'phone':self.phone()
        }
    

if __name__ == '__main__':
    s = 'Contact us via 408-205-5663 or email@test.com'
    parser = Parser(s)
    print(parser.parse())
    print(parser.parse())
