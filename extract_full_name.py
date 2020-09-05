def extract_name(name):
  inits = name.split()
  new_name = ""
  for n in range(len(inits)-1):
    name = inits[n]
    new_name += (name[0].upper()+'.').title()
    # new_name += inits[-1].title() 
  return new_name

name = input("enter full name ==>")
print(extract_name(name))