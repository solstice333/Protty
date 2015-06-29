from Bio.SeqUtils.ProtParam import ProteinAnalysis


A = "1"
B = "2"
C = "3"

regions = [A, B, C]

beg = 0
end = len(regions)
for i in range(end):
   for j in range(beg,end): 
      kitty = ""
      kitty = kitty.join(regions[beg:j + 1])
      print(kitty)
   beg += 1







