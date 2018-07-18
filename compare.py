import subprocess

def run_shell_command(cmd, output=None, raise_on_error=True, under_dir='.'):
    if output is True:
        output = subprocess.PIPE

    sub = subprocess.Popen(cmd, stdout=output, stderr=output, cwd=under_dir)
    out = sub.communicate()
    if raise_on_error and sub.returncode:
        raise RuntimeError("%s returned %d" % (cmd, sub.returncode))

    if out[0] is not None:
        return out[0].strip().decode()


output = run_shell_command(['ls', '-a'], output=True, under_dir='./my/')
lists = output.split()
my_debian_pkgs = []
for e in lists:
  if '.deb' in e:
    my_debian_pkgs.append(e)

output = run_shell_command(['ls', '-a'], output=True, under_dir='./rbe/')
lists = output.split()
rbe_debian_pkgs = []
for e in lists:
  if '.deb' in e:
    rbe_debian_pkgs.append(e)

my_debian_pkgs.sort()
rbe_debian_pkgs.sort()

if len(my_debian_pkgs) != len(rbe_debian_pkgs):
  raise Error('the length is not the same')

for i in range(len(my_debian_pkgs)):
  my_sha256 = run_shell_command(['sha256sum', my_debian_pkgs[i]], output=True, under_dir='./my/').split()[0]
  rbe_sha256 = run_shell_command(['sha256sum', rbe_debian_pkgs[i]], output=True, under_dir='./rbe/').split()[0]
  if my_sha256 != rbe_sha256:
    print my_debian_pkgs[i]
