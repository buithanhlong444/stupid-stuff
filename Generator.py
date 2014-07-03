import sys

s_n = 0
un = ''
pw = ''
out = ''
str = ''
helpme = \
       '''-u, --user  <filename>  |   File Contain Victim's Emails
-p, --pass  <filename>  |   File Contain Victim's Passwords 
-o, --out   <filename>  |   File Contain Output 
-h, --help              |   Print Help
         '''

for arg in sys.argv:
    try:
        if arg.lower() == '-u' or arg.lower() == '--user':
            un = sys.argv[int(sys.argv[1:].index(arg)) + 2]
        elif arg.lower() == '-p' or arg.lower() == '--pass':
            pw = sys.argv[int(sys.argv[1:].index(arg)) + 2]
        elif arg.lower() == '-o' or arg.lower() == '--out':
            out = sys.argv[int(sys.argv[1:].index(arg)) + 2]
        elif arg.lower() == '-h' or arg.lower() == '--help':
            print helpme
    except IOError:
        exit
    except NameError:
        exit
    except IndexError:
        exit
    
        

def a_p(v_1):
    global s_n
    f = open(pw, 'r')
    for line in f:
        l1 = line.replace('\n', '')
        if l1.strip() <> '':
            f2 = open(out, 'a')
            f2.write('\n' + v_1 + '|' + l1)
            s_n += 1
            print 'Combined : <' + v_1 + '|' + l1 + '> . String %i' % s_n
            
        
def main():
    global un, pw, out
    f = open(un, 'r')
    for line in f:
        str = line.replace('\n', '')
        if str.strip() <> '':
            a_p(str)
                   
if __name__ == '__main__':
    main()

