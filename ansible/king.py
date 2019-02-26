import winrm

s = winrm.Session(‘https://windows-host:5986′,auth=(‘administrator’,’Passw0rd!’),transport=’ntlm‘)

r = s.run_cmd(‘ipconfig’)

print r.std_out
