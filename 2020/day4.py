import re, pprint

input_file = open('./day4_input.txt', 'r')
lines = input_file.readlines()

required_fields = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}

valid_eye_colors = ['amb','blu','brn','gry','grn','hzl','oth']
valid_pp_count = 0


pp = ''
for line in lines: 
    if line.strip() == '':
        #process PP
        array = pp.strip().split(' ')
        pp_dict = {}
        #construct dict
        for item in array: 
            k,v = item.split(":")
            pp_dict[k] = v        
        #verify
        pp_key_set = set(pp_dict.keys())
        pp_key_set.discard('cid')
        try:
            assert len(pp_key_set & required_fields) == 7, 'MISSING REQUIRED FIELDS'
            assert 1920 <= int(pp_dict['byr']) <= 2002, 'byr'
            assert 2010 <= int(pp_dict['iyr']) <= 2020, 'iyr'
            assert 2020 <= int(pp_dict['eyr']) <= 2030, 'eyr'
            if pp_dict['hgt'][-2:] == 'cm':
                assert 150 <= int(pp_dict['hgt'][:-2]) <= 193, 'hgt'
            elif pp_dict['hgt'][-2:] == 'in':
                assert 59 <= int(pp_dict['hgt'][:-2]) <= 76, 'hgt'
            else:
                assert False, 'hgt'
            assert re.match(r'#[0-9a-f]{6}\b',pp_dict['hcl']), 'hcl'
            assert pp_dict['ecl'] in valid_eye_colors, 'ecl'
            assert re.match(r'\d{9}\b',pp_dict['pid']), 'pid'
            valid_pp_count += 1
        except AssertionError as ae:
            if str(ae) in (pp_dict.keys()):
                print(str(ae) + ":" + pp_dict[str(ae)])
            else:
                print(ae)
        pp=''
    else:
        pp += line.strip() + ' '
        #append this to previous line

print (valid_pp_count+1)
