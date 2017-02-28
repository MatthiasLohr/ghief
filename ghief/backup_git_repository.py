
import tempfile
import shutil
import subprocess


def backup_git_repository(source, target):
    gitdir = tempfile.mkdtemp(suffix='.git')
    subprocess.call(['git', 'clone', '--bare', source, gitdir])
    subprocess.call(['git', 'remote', 'add', 'backup', target], cwd=gitdir)
    subprocess.call(['git', 'push', '--all', '--prune', 'backup'], cwd=gitdir)
    shutil.rmtree(gitdir)
