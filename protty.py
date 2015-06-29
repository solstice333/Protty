from Bio.SeqUtils.ProtParam import ProteinAnalysis

      # seq   # identifer
N_ = ("MWT",  "N_")
P =  ("TRC",  "P")
pg = ("KWP",  "pg")

regions = [N_, P, pg]

beg = 0
end = len(regions)
for i in range(end):
   for j in range(beg,end): 
      kitty = ""
      cat = ""

      for k in range(beg, j + 1):
         kitty += regions[k][0]   # seq
         cat += regions[k][1]   # identifier

      pappi = ProteinAnalysis(kitty)
      print("%s,%.3lf kda" %(cat, pappi.molecular_weight() / 1000))
   beg += 1






