import dns.resolver

for TLD in open("tlds-alpha-by-domain.txt").read().split("\n"):
  TLD = TLD.strip()
  if len(TLD) == 0:
    continue
  if TLD.startswith("#"):
    continue
  try:
    answer = dns.resolver.resolve(TLD, "CAA", raise_on_no_answer = False)
  except Exception as e:
    print(TLD, "failed", e)
  if answer.rrset is None:
    print(TLD, "none")
  else:
    for rr in answer.rrset:
      print(TLD, rr)
