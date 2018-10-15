
from __future__ import print_function
from IPython.core.magic import (Magics, 
                                magics_class, 
                                line_magic,
                                cell_magic, 
                                line_cell_magic)
import pexpect
import re

PIGPATH = 'pig -4 log4j.properties -x local '
PROMPT = 'grunt> '
CONTPROMPT = '>> '

@magics_class
class CodeMagic(Magics):

    def __init__(self, shell):
        super(CodeMagic, self).__init__(shell)
        self.child = pexpect.spawn(PIGPATH)
        self.child.expect(PROMPT, timeout=300)
        self.output(self.child.before.decode())

    @cell_magic
    def pig(self, line, cell):
        x = cell.split('\n')
        for y in x:
            self.child.sendline(y)
            self.child.expect(['\r\n'+CONTPROMPT, '\r\n'+PROMPT], timeout=300)
            self.output(self.child.before.decode()) 
        return None        
        
    def output(self, text):
        text = text.split('\r\n')
        for line in text:
            print(line)

       
        
    def output1(self, text):
        text = text.split('\r\n')
        filter = [' INFO ', ' WARN ', 'Total Length = ', 
                  'Input split', '   ',
                  '-----------------------',
                  '		',
                  'Job DAG:',
                  'Successfully ',
                  'MAP_ONLY',
                  'job_local',
                  'Total records proactively spilled',
                  'Total bags proactively spilled',
                  'HadoopVersion',
                  'UNKNOWN',
                  'AvgReduceTime',
                  'Total bytes written',
                  'Total records written :',
                  'File System Counters',
                  'Map-Reduce Framework',
                  'File Input Format Counters',
                  'File Output Format Counters',
                  'Input\(s\):',
                  'Output\(s\):',
                  'Counters:',
                  'JobId',
                  'Spillable Memory Manager spill count',
                  'Success!',
                  'Job Stats (time in seconds)'
                  
                 ]
        for line in text:
            if re.search('|'.join(filter), line):
                pass
            elif len(line.strip()) == 0:
                pass
            else:
                print(line)
        
        
__ip = get_ipython()
codemagic = CodeMagic(__ip)
__ip.register_magics(codemagic)
