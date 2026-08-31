def add(first_name: str,last_name: str):
    n_fname = first_name.upper()
    n_lname = last_name.upper()
    return n_fname + " " + n_lname

fname = "fasih"
lname = "dagia"

print(add(fname,lname))