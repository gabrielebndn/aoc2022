import typing as tp
from dataclasses import dataclass

TESTFILE = "../resources/test_7.txt"
FILENAME = "../resources/input_7.txt"

FILESYSTEM_SIZE = 70000000
UNUSED_NEEDED   = 30000000

class Entry:
    pass

class FileSystemObject(Entry):
    pass

@dataclass
class File(FileSystemObject):
    size: int
    name: str

    def __str__(self) -> str:
        return f"{self.size} {self.name}"

class Directory(FileSystemObject):
    def __init__(self, name: str, parent: 'Directory' = None):
        self.name: str = name
        self.contents: tp.List[tp.Union[File, 'Directory']] = []
        self.parent: 'Directory' = parent

    @property
    def size(self):
        return sum([content.size for content in self.contents])

    def add(self, obj: tp.Union[File, 'Directory']):
        self.contents.append(obj)
        if obj.__class__ == self.__class__:
            obj.parent = self
    
    def __str__(self):
        return f"dir {self.name}"

class Command(Entry):
    pass

class LsCommand(Command):
    pass

    def __str__(self):
        return "$ ls"

@dataclass
class CdCommand(Command):
    folder: str

    def __str__(self):
        return f"$ cd {self.folder}"

def parse_command(s: str) -> Command:
    assert s[:2] == "$ "
    s = s[2:].strip()
    if s == 'ls':
        return LsCommand()
    else:
        assert s[:3] == 'cd '
        s = s[3:].strip()
        return CdCommand(s)

def parse_filesystem_object(s: str) -> FileSystemObject:
    if s[:4] == 'dir ':
        return Directory(s[4:])
    else:
        entry = s.split()
        return File(int(entry[0]), entry[1])

def parse_entry(s: str) -> Entry:
    if s[0] == '$':
        return parse_command(s)
    else:
        return parse_filesystem_object(s)

def exec_cd(root: Directory, current_dir: Directory, cmd: CdCommand) -> Directory:
    if cmd.folder == "/":
        return root
    elif cmd.folder == "..":
        assert current_dir.parent is not None
        return current_dir.parent
    else:
        for d in current_dir.contents:
            if isinstance(d, Directory) and d.name == cmd.folder:
                return d
        assert False, f'Folder not found: \"{cmd.folder}\" in \"{current_dir.name}\"'

def parse_file(filename: str, verbose: bool = False):
    root = Directory("/")
    current_dir = root
    with open(filename) as f:
        while line := f.readline():
            line = line.strip()
            entry = parse_entry(line)
            if verbose:
                print(entry)
            if isinstance(entry, CdCommand):
                current_dir = exec_cd(root, current_dir, entry)
            elif isinstance(entry, LsCommand):
                pass
            else:
                current_dir.add(entry)
    return root

def print_filesytem(obj: FileSystemObject, level: int = 0):
    s = '  ' * level + '- '
    s += str(obj)
    print(s)
    if isinstance(obj, Directory):
        for c in obj.contents:
            print_filesytem(c, level+1)

# efficient algo never computing same dir twice
# return list of folders as files
def recurse_sizes(d: Directory) -> tp.List[File]:
    size = 0
    list_ = []
    for c in d.contents:
        if isinstance(c, File):
            size += c.size
        else:
            sublist = recurse_sizes(c)
            list_ += sublist
            size += sublist[0].size
    obj = File(size, d.name)
    list_.insert(0, obj)
    return list_

def exo_1():
    root = parse_file(FILENAME)
    list_ = recurse_sizes(root)
    assert list_[0].size == root.size
    return sum([elem.size for elem in list_ if elem.size < 100000])


def exo_2():
    root = parse_file(FILENAME)
    list_ = recurse_sizes(root)
    assert list_[0].size == root.size

    full = root.size
    min_ = list_[0]
    max_size = FILESYSTEM_SIZE - UNUSED_NEEDED
    for f in list_:
        if full-f.size < max_size:
            if f.size < min_.size:
                min_ = f
    return min_


if __name__ == "__main__":
    print(exo_1())
    print(exo_2())
