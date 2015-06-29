from Bio.SeqUtils.ProtParam import ProteinAnalysis

regions = [
     # seq      # identifer
   ("MWTLVSWVALTAGLVAG", "N_"),
   ("TRCPDGQFCPVACCLDPGGASYSCCRPLLD", "P"),
   ("KWPTTLSRHL", "pg"),
   ("GGPCQVDAHCSAGHSCIFTVSGTSSCCPFPEAVACGDGHHCCPRGFHCSADGRSCF", "G"),
   ("QRSGNNSVG", "gf"),
   ("AIQCPDSQFECPDFSTCCVMVDGSWGCCPMPQASCCEDRVHCCPHGAFCDLVHTRCI", "F"),
   ("TPTGTHPLAKKLPAQRTNRAVALSSS", "fb"),
   ("VMCPDARSRCPDGSTCCELPSGKYGCCPMPNATCCSDHLHCCPQDTVCDLIQSKCL", "B"),
   ("SKENATTDLLTKLPAHTVG", "ba"),
   ("DVKCDMEVSCPDGYTCCRLQSGAWGCCPFTQAVCCEDHIHCCPAGFTCDTQKGTCE", "A"),
   ("QGPHQVPWMEKAPAHLSLPDPQALKRD", "ac"),
   ("VPCDNVSSCPSSDTCCQLTSGEWGCCPIPEAVCCSDHQHCCPQGYTCVAEGQCQ", "C"),
   ("RGSEIVAGLEKMPARRASLSHPRDI", "cd"),
   ("GCDQHTSCPVGQTCCPSLGGSWACCQLPHAVCCEDRQHCCPAGYTCNVKARSCE", "D"),
   ("KEVVSAQPATFLARSPHVGVK", "de"),
   ("DVECGEGHFCHDNQTCCRDNRQGWACCPYRQGVCCADRRHCCPAGFRCAARGTKCL", "E"),
   ("RREAPRWDAPLRDPALRQLL", "C_"),
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






