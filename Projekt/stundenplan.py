import subprocess
import operator
# executes clingo
p = subprocess.Popen([r'C:\Users\Cuauhtechalotl\Anaconda3\Library\bin\clingo.exe', r'plan.lp'],shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# reads output
output = list()
for line in p.stdout.readlines():
    output.append(line)
# checks if result was satisfiable
string = ""
string2 = "SATISFIABLE"
for char in output[5]:
    string += chr(char)
string = string.split()[0]
if string != string2:
    exit()
#converts output into a result matrix
results = []
buffer = ""
for char in output[4]:
    buffer += chr(char)
    if chr(char)==')':
        results.append(buffer)
        buffer = ""
for x in range (0,len(results)):
    results[x] = results[x].split('(')[1]
    results[x] = results[x].split(')')[0]
    results[x] = results[x].split(',')
retval = p.wait()
#print for testing
results = sorted(results, key=operator.itemgetter(0,1,2))
for x in range (0,len(results)):
    out = ""
    for y in range (0,len(results[x])):
        out += results[x][y] + " "
    print(out)
# results[x][i] contains x results with i Parameters, given by the executed programm
# at date 10.12: slot, day, room, class, group, subject