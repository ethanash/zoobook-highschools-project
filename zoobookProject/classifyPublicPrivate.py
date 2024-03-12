from thefuzz import fuzz

f = open('publicPrivateList.txt', 'w')
with open("us-public-schools.csv", 'r') as public_schools:
    with open("privateSchoolFullNames.csv", 'r') as private_schools:
        with open("zoobookSchoolFullNames.csv", 'r') as zoobook:
            public_schools = [line.rstrip() for line in public_schools]
            private_schools = [line.rstrip() for line in private_schools]
            i = 0
            for zoo_school_line in zoobook:
                found = False
                zoo_line = zoo_school_line.lower().replace('"', '').strip()
                for public_school_line in public_schools:
                    public_line = public_school_line.split(",")[0].lower().replace('"', '').strip()
                    similarity = fuzz.token_sort_ratio(zoo_line, public_line)
                    if similarity > 75:
                        f.write(zoo_school_line.strip() + ",public\n")
                        found = True
                        break
                if not found:
                    for private_school_line in private_schools:
                        private_line = private_school_line.lower()
                        similarity = fuzz.token_sort_ratio(zoo_line, private_line)
                        if similarity > 75:
                            f.write(zoo_school_line.strip() + ",private\n")
                            found = True
                            break
                if not found:
                    f.write("unknown\n")
                i += 1
            zoobook.close()
        private_schools.close()
    public_schools.close()
f.close()
