import subprocess
import operator
import csv
<<<<<<< Updated upstream
# executes clingo
p = subprocess.Popen([r'clingo.exe', r'plan.lp'],shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
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
#data ouput
with open('output.csv', mode='w',newline='') as output_file:
    writer = csv.writer(output_file, delimiter=";",dialect='excel')
    writer.writerow(["Slot","Day","Room","Class","Subclass","Course"])
    writer.writerows(results)
# results[x][i] contains x results with i Parameters, given by the executed programm
# at date 10.12: slot, day, room, class, group, subject
=======
import datetime
import urllib.parse as urlparse
from urllib.parse import parse_qs

# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8082

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
		
        parameters = parse_qs(urlparse.urlparse(self.path).query)
            
        self.wfile.write(bytes("<html><head><title>intelligente Ressourcenplanung</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        
        if self.path == "/output":
            with open('../../INN1-Frontend/src/assets/output.csv') as file:
                lines = file.readlines()
            for line in lines:
                self.wfile.write(bytes("<p>%s</p>" % line, "utf-8"))
        else:    
            self.wfile.write(bytes("<form action=\"\" method=\"GET\">", "utf-8"))
            self.wfile.write(bytes("<table><tr><td>Raeume: </td><td><input type=\"text\" name=\"roomNo\"></td></tr>", "utf-8"))
            self.wfile.write(bytes("<tr><td>davon Uebungsraeume: </td><td><input type=\"text\" name=\"roomNoSmall\"></td></tr>", "utf-8"))
            self.wfile.write(bytes("<tr><td>Faecher: </td><td><input type=\"text\" name=\"subjNo\"></td></tr>", "utf-8"))
            self.wfile.write(bytes("<tr><td>Klassen: </td><td><input type=\"text\" name=\"classNo\"></td></tr>", "utf-8"))
            self.wfile.write(bytes("<tr><td>Einheiten pro Tag: </td><td><input type=\"text\" name=\"slotNo\"></td></tr>", "utf-8"))
            self.wfile.write(bytes("<tr><td><input type=\"submit\" value=\"Submit\"></td></tr></table></form>", "utf-8"))
            
            if len(parameters) == 5:
                # write plan.temp
                with open('template.lp', 'r') as template:
                        lines = template.readlines()
                with open('plan.lp', 'w') as file:
                    for key, value in parameters.items():
                        file.write("#const %s = %s.\n" % (key,value[0]))
                    for line in lines:
                        file.write(line)
                        
				# executes clingo
                p = subprocess.Popen([r'clingo.exe', r'plan.lp'],shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
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
                results = sorted(results, key=operator.itemgetter(3,4,1,0))
                for x in range (0,len(results)):
                    out = ""
                    for y in range (0,len(results[x])):
                        out += results[x][y] + " "
                    print(out)
				#data ouput
                with open('../../INN1-Frontend/src/assets/output.csv', mode='w',newline='') as output_file:
                    writer = csv.writer(output_file, delimiter=";",dialect='excel')
                    writer.writerow(["Slot","Day","Room","Class","Subclass","Course"])
                    writer.writerows(results)
				# results[x][i] contains x results with i Parameters, given by the executed programm
				# at date 10.12: slot, day, room, class, group, subject
                self.wfile.write(bytes("<p>csv created at time %s</p>" % str(datetime.datetime.now()).split('.')[0], "utf-8"))               
        
        self.wfile.write(bytes("</body></html>", "utf-8"))
	
	
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
>>>>>>> Stashed changes
