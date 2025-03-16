def clo():
    ict = dict()
    with open('C:/_project/refseq_transcript.fasta','r') as f:
      for line in f:
         m = line.strip()
         if len(m) != 0 and m[0] == '>':
           m = m.split()
           key = m[0][1:]
           ict[key] = ""
         else:
           ict[key] += m

      for key, value in ict.items():
         print(key, '*', value)

clo()
