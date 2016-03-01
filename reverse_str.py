def reverse_str(input_str):
     ss = input_str.split(' ')
     result = []
     for s in ss:
         r = []
         for i in range(len(s)-1, -1, -1):
             r.append(s[i])
         r = ''.join(r)
         result.append(r)
     print ' '.join(result)
