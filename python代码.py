import random
class math_exam():
    operator={
        '1':lambda x,y,z:x+y+z,'2':lambda x,y,z:x-y-z,'3':lambda x,y,z:x*y*z,'4':lambda x,y,z:x/y/z,
        '5':lambda x,y,z:x+y-z,'6':lambda  x,y,z:x+y*z,'7':lambda x,y,z:x+y/z,'8':lambda x,y,z:x-y*z,
        '9':lambda x,y,z:x-y/z,'z':lambda x,y,z:x*y/z
    }
    def math_operation(self):
        count=0
        while count<=300:
            num_1 = random.randint(1, 100)
            num_2 = random.randint(1, 100)
            num_3 = random.randint(1, 100)
            map = random.choice('12346789z')
            if map=='1':
                b = int(self.operator[map](num_1,num_2,num_3))
                if 0<b<=100:
                    print(num_1,'+',num_2,'+',num_3,'=',b)
                    count=count+1
            elif map=='2':
                b = int(self.operator[map](num_1, num_2, num_3))
                if 0<b<=100:
                    print(num_1, '-', num_2, '-', num_3, '=', b)
                    count=count+1
            elif map == '3':
                b = int(self.operator[map](num_1,num_2,num_3))
                if 0<b<=100:
                    print(num_1, '*', num_2, '*', num_3, '=',b)
                    count=count+1
            elif map == '4':
                b = int(self.operator[map](num_1,num_2,num_3))
                if 0<b<=100:
                    print(num_1, '/', num_2, '/', num_3, '=', b)
                    count=count+1
            elif map == '5':
                b = int(self.operator[map](num_1,num_2,num_3))
                if 0<b<=100:
                    print(num_1, '+', num_2, '-', num_3, '=', b)
                    count=count+1
            elif map=='6':
                b =int(self.operator[map](num_1,num_2,num_3))
                if 0<b<=100:
                    print(num_1, '+', num_2, '*', num_3, '=', b)
                    count=count+1
            elif map=='7':
                b = int(self.operator[map](num_1,num_2,num_3))
                if 0<b<=100:
                    print(num_1, '+', num_2, '/', num_3, '=', b)
                    count=count+1
            elif map=='8':
                b = int(self.operator[map](num_1,num_2,num_3))
                if 0<b<=100:
                    print(num_1, '-', num_2, '*', num_3, '=', b)
                    count=count+1
            elif map=='9':
                b = int(self.operator[map](num_1,num_2,num_3))
                if 0<b<=100:
                    print(num_1, '-', num_2, '/', num_3, '=', b)
                    count=count+1
            elif map=='z':
                b = int(self.operator[map](num_1,num_2,num_3))
                if 0<b<=100:
                    print(num_1, '*', num_2, '/', num_3, '=', b)
                    count=count+1
a=math_exam()
a.math_operation()
