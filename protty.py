#!/usr/bin/env python
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# Usage: Fill in the regions list below appropriately with a valid protein
# sequence and an identifier of your choosing. Open a terminal, cd to this
# directory with `cd Dropbox/<our shared folder>/protty`. Then run protty.py
# thus, `python protty.py`. To redirect the output to a csv file that can
# be viewed in Excel, do `python protty.py > drea.csv`.

regions = [
     # seq      # identifer
   ("MLPSQINQNSKHITKKNDVRIFFCILYFNIKYFSFHTFIAELDQTIIIIDRQVVSDKIGVLSVCPLHSSFSFIFSIKIMRLILLFLVFLCRVTA", "A"),
   ("HQCDAETECSDDETCCKLGDNTWGCCPMPNAVCCDDRSHCCPTGTTCDPQGARCI", "1"),
   ("GADEKHVPMKKKKPARKTVERNQFNE", "B"),
   ("VVCPDKASKCPDGSTCCLLEQGSYGCCPVPNAVCCADMLHCCPNGFTCHGQFCSQ", "2"),
   ("NFAMIPHLRKFASTSIHRKPAVEFLSEEEEDDDDEESTSSEDPESDVDP", "C"),
   ("IACGVGKTCPAKTTCCNVRGKNGEPKTMCCPLSNAICCENTCCPAGYHCVDGGKCE", "3"),
   ("KHAKTMRTRFWNVKDDEDEDQI", "D"),
  
]

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
      print("%s,%.3lf" %(cat, pappi.molecular_weight() / 1000))
   beg += 1






