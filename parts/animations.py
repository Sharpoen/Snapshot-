from time import sleep, perf_counter
from parts.esq import esq
from getkey import getkey

#default
d=esq.deft_bg+esq.white
#dark
b=esq.black_bg+esq.white
cutscenes={
  "start":{
    "title":"Darkness",
    "frames":[
      [
        "%s           00       "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s          %s        "%(b, esq.blue+"[>"),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
      ],
      [
        "%s           00       "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s            %s      "%(b, esq.blue+"[>"),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
      ],
      [
        "%s           00       "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s              %s    "%(b, esq.blue+"[>"),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
      ],
      [
        "%s           00       "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                %s  "%(b, esq.blue+"[>"),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
      ],
      [
        "%s           00       "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s      %sWhere am I? "%(b, esq.bright_blue+"  "),
        "%s                %s  "%(b, esq.blue+"\\/"),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
      ],
      [
        "%s           00       "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s      %sWhere am I? "%(b, esq.bright_blue+"  "),
        "%s                %s  "%(b, esq.blue+"<]"),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
      ],
      [
        "%s           00       "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s      %sWhere am I? "%(b, esq.bright_blue+"  "),
        "%s                %s  "%(b, esq.blue+"/\\"),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
      ],
      [
        "%s           00       "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s      %sWhere am I? "%(b, esq.bright_blue+"  "),
        "%s                %s  "%(b, esq.blue+"<]"),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
      ],
      [
        "%s           00       "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                %s  "%(b, esq.blue+"\\/"),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
      ],
      [
        "%s           00       "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                %s  "%(b, esq.blue+"[>"),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
      ],
      [
        "%s           00       "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                  %s"%(b, esq.blue+"[>"),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
      ],
      [
        "%s           00       "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s%s                  "%(b, esq.red+".."),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
      ],
      [
        "%s           00       "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s  %s                "%(b, esq.red+".."),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
      ],
      [
        "%s           00       "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s    %s              "%(b, esq.red+".."),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s%s                  "%(b, esq.blue+"[>"),
        "%s                    "%(b),
        "%s           00       "%(b),
        "%s          []        "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s  %s                "%(b, esq.blue+"[>"),
        "%s                    "%(b),
        "%s           00       "%(b),
        "%s          []        "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s    %s              "%(b, esq.blue+"[>"),
        "%s                    "%(b),
        "%s           00       "%(b),
        "%s          []        "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s%s     %s            "%(b, esq.red+".", esq.blue+"[>"),
        "%s                    "%(b),
        "%s           00       "%(b),
        "%s          []        "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s %s    %s           "%(b, esq.red+"..", esq.blue+"[>"),
        "%s                    "%(b),
        "%s           00       "%(b),
        "%s          []        "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s   %s   %s          "%(b, esq.red+"..", esq.blue+"[>"),
        "%s                    "%(b),
        "%s           00       "%(b),
        "%s          []        "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s     %s  %s         "%(b, esq.red+"..", esq.blue+"[>"),
        "%s                    "%(b),
        "%s           00       "%(b),
        "%s          []        "%(b),
        "%s                    "%(b),
      ],      
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s      %s %s         "%(b, esq.red+"..", esq.blue+"[>"),
        "%s                    "%(b),
        "%s           00       "%(b),
        "%s          []        "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s      %s %s         "%(b, esq.red+"..", esq.blue+"<]"),
        "%s                    "%(b),
        "%s           00       "%(b),
        "%s          []        "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s       %sYikes!     "%(b, esq.bright_blue+"  "),
        "%s      %s %s        "%(b, esq.red+"..~", esq.blue+"<]"),
        "%s                    "%(b),
        "%s           00       "%(b),
        "%s          []        "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s       %sYikes!     "%(b, esq.bright_blue+"  "),
        "%s      %s %s         "%(b, esq.red+"..", esq.blue+"<]"),
        "%s                    "%(b),
        "%s           00       "%(b),
        "%s          []        "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s     %s  %s         "%(b, esq.red+"..", esq.blue+"[>"),
        "%s                    "%(b),
        "%s         00         "%(b),
        "%s        []          "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                   0"%(b),
        "%s     %s  %s         "%(b, esq.red+"..", esq.blue+"[>"),
        "%s                   ["%(b),
        "%s       00           "%(b),
        "%s      []            "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                 000"%(b),
        "%s     %s  %s         "%(b, esq.red+"..", esq.blue+"[>"),
        "%s                 [] "%(b),
        "%s     00           []"%(b),
        "%s    []              "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s               000  "%(b),
        "%s     %s  %s         "%(b, esq.red+"..", esq.blue+"[>"),
        "%s               []   "%(b),
        "%s   00           []  "%(b),
        "%s  []                "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s             000    "%(b),
        "%s     %s  %s         "%(b, esq.red+"..", esq.blue+"[>"),
        "%s             []   []"%(b),
        "%s 00           []    "%(b),
        "%s[]                  "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s           000    []"%(b),
        "%s     %s  %s         "%(b, esq.red+"..", esq.blue+"[>"),
        "%s           []   []  "%(b),
        "%s0           []     ["%(b),
        "%s                    "%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s         000    []  "%(b),
        "%s     %s  %s         "%(b, esq.red+"..", esq.blue+"[>"),
        "%s         []   []  []"%(b),
        "%s          []     [] "%(b),
        "%s                   ["%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                    "%(b),
        "%s                    "%(b),
        "%s       000    []    "%(b),
        "%s     %s  %s         "%(b, esq.red+"..", esq.blue+"[>"),
        "%s       []   []  []  "%(b),
        "%s        []     []   "%(b),
        "%s                 []["%(b),
        "%s                    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s                   0"%(b),
        "%s                    "%(b),
        "%s     000    []    0 "%(b),
        "%s     %s  %s         "%(b, esq.red+"..", esq.blue+"[>"),
        "%s     []   []  []  []"%(b),
        "%s      []     []     "%(b),
        "%s               [][] "%(b),
        "%s                  []"%(b),
      ],
      [
        "%s                    "%(b),
        "%s                 0  "%(b),
        "%s                    "%(b),
        "%s   000    []    0   "%(b),
        "%s      %s %s         "%(b, esq.red+"..", esq.blue+"[>"),
        "%s   []   []  []  [][]"%(b),
        "%s    []     []      ["%(b),
        "%s             [][]   "%(b),
        "%s                [][]"%(b),
      ],
      [
        "%s                    "%(b),
        "%s               0    "%(b),
        "%s                    "%(b),
        "%s 000    []    0    ["%(b),
        "%s      %s %s         "%(b, esq.red+"..", esq.blue+"[>"),
        "%s []   []  []  [][]  "%(b),
        "%s  []     []      [] "%(b),
        "%s           [][]   []"%(b),
        "%s              [][]/ "%(b),
      ],
      [
        "%s                    "%(b),
        "%s             0      "%(b),
        "%s                    "%(b),
        "%s00    []    0    [] "%(b),
        "%s      %s%s         "%(b, esq.red+"..~", esq.blue+"\\/"),
        "%s]   []  []  [][]    "%(b),
        "%s[]     []      []   "%(b),
        "%s         [][]   []  "%(b),
        "%s            [][]/   "%(b),
      ],
      [
        "%s                    "%(b),
        "%s              0    "%(b),
        "%s                    "%(b),
        "%s0    []    0    []  "%(b),
        "%s        %s         "%(b, esq.red+"..-"),
        "%s   []  []%s[][]     "%(b, esq.blue+"\\/"+b),
        "%s]     []      []   0"%(b),
        "%s        [][]   []   "%(b),
        "%s           [][]/    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s              0    "%(b),
        "%s                    "%(b),
        "%s0    []    0    []  "%(b),
        "%s          %s       "%(b, esq.red+"..~"),
        "%s   []  []  [][]     "%(b),
        "%s]     [] %s   []   0"%(b, esq.blue+"\\/"+b),
        "%s        [][]   []   "%(b),
        "%s           [][]/    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s              0    "%(b),
        "%s                    "%(b),
        "%s0    []    0    []  "%(b),
        "%s            %s     "%(b, esq.red+"..-"),
        "%s   []  []  [][]     "%(b),
        "%s]     [] %s   []   0"%(b, esq.blue+"\\/"+b),
        "%s     %s*CRACK*%s]   "%(b, esq.magenta+"  ", b+" ["),
        "%s           [][]/    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s              0    "%(b),
        "%s                    "%(b),
        "%s0    []    0    []  "%(b),
        "%s              %s    "%(b, esq.red+".."),
        "%s   []  []  [][]     "%(b),
        "%s]     [] %s   []   0"%(b, esq.blue+"\\/"+b),
        "%s     %s*CRACK*%s]   "%(b, esq.magenta+"  ", b+" ["),
        "%s           [][]/    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s              0    "%(b),
        "%s                    "%(b),
        "%s0    []    0    []  "%(b),
        "%s                %s  "%(b, esq.red+".."),
        "%s   []  []%s! no!    "%(b, esq.bright_blue+"Oh"),
        "%s]     [] %s   []   0"%(b, esq.blue+"\\/"+b),
        "%s        [][]   []   "%(b),
        "%s           [][]/    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s              0    "%(b),
        "%s                    "%(b),
        "%s0    []    0    []  "%(b),
        "%s                  %s"%(b, esq.red+".."),
        "%s   []  []%s! no!    "%(b, esq.bright_blue+"Oh"),
        "%s]     [] %s   []   0"%(b, esq.blue+"\\/"+b),
        "%s        [][]   []   "%(b),
        "%s           [][]/    "%(b),
      ],
      [
        "%s                    "%(b),
        "%s              0    "%(b),
        "%s                    "%(b),
        "%s0    []    0    []  "%(b),
        "%s                    "%(b),
        "%s   []  []  [][]     "%(b),
        "%s]     [] %s   []   0"%(b, esq.blue+"\\/"+b),
        "%s  %sMy flashlight is"%(b, esq.bright_blue+"  "),
        "%s   %sbroken!%s][]/    "%(b, esq.bright_blue+"  ", b),
      ],
      [
        "%s                    "%(b),
        "%s              0    "%(b),
        "%s                    "%(b),
        "%s0    []    0    []  "%(b),
        "%s                    "%(b),
        "%s   []  []  [][]     "%(b),
        "%s]     [] %s   []   0"%(b, esq.blue+"\\/"+b),
        "%s  %sMy flashlight is"%(b, esq.bright_blue+"  "),
        "%s   %sbroken!%s][]/    "%(b, esq.bright_blue+"  ", b),
      ],
      [
        "%s                    "%(b),
        "%s              0    "%(b),
        "%s                    "%(b),
        "%s0    []    0    []  "%(b),
        "%s                    "%(b),
        "%s   []  []  [][]     "%(b),
        "%s]     [] %s   []   0"%(b, esq.blue+"\\/"+b),
        "%s  %sMy flashlight is"%(b, esq.bright_blue+"  "),
        "%s   %sbroken!%s][]/    "%(b, esq.bright_blue+"  ", b),
      ],
      [
        "%s                    "%(b),
        "%s              0    "%(b),
        "%s                    "%(b),
        "%s0    []    0    []  "%(b),
        "%s                    "%(b),
        "%s   []  []  [][]     "%(b),
        "%s]     [] %s   []   0"%(b, esq.blue+"\\/"+b),
        "%s  %sMy flashlight is"%(b, esq.bright_blue+"  "),
        "%s   %sbroken!%s][]/    "%(b, esq.bright_blue+"  ", b),
      ],
    ]
  }
  
}


def cutscene(scene, **args):
  title = cutscenes[scene]["title"]
  frames = cutscenes[scene]["frames"]
  print(esq.clear+esq.top+esq.reset+d+title)
  
  for frame in frames:
    print("\n".join(frame))
    sleep(0.5)
    print(end=d+esq.top+esq.sdown, flush=True)
    # getkey()
  # getkey()
  
  
  