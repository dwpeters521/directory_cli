class Directory:
    """
    A class representing an individual directory within a file system
    """
    def __init__(self, name):
        self.name: str = name
        self.parent: Directory = None
        self.children: dict[str, Directory] = {}  

class FileSystem:
    """
    A class representing a file system with nested directories
    """
    def __init__(self):
        self.root: Directory = Directory("")

    def create(self, path: str):
        """
        Create a new directory, given a path name including slashes "/"
        """
        parts = path.strip('/').split('/')
        current = self.root
        for part in parts[:-1]:
            if part in current.children:
                current = current.children[part]
            else:
                print(f"Cannot create {path} - {part} does not exist")
                return

        # Add the new directory if it doesn't already exist
        new_dir_name = parts[-1]
        if new_dir_name in current.children:
            print(f"Cannot create {path} - {new_dir_name} already exists")
        else:
            current.children[new_dir_name] = Directory(new_dir_name)
            current.children[new_dir_name].parent = current
            print(f"CREATE {path}")

    def delete(self, path: str):
        """
        Delete a directory, given a path name including slashes "/"
        Returns "Cannot delete {path}" if not found
        """
        print(f"DELETE {path}")
        node = self._navigate_to_node(path)
        if node is None or node == self.root:
            print(f"Cannot delete {path} - {path.split('/')[0]} does not exist")
            return

        # Remove the directory from its parent's children
        parent = node.parent
        dir_name = node.name
        del parent.children[dir_name]

    def move(self, source_path: str, destination_path: str):
        """
        Moves a directory from source_path to destination_path
        """
        source_node = self._navigate_to_node(source_path)
        destination_node = self._navigate_to_node(destination_path)

        if source_node is None:
            print(f"Cannot move {source_path} - source does not exist")
            return

        if destination_node is None:
            print(f"Cannot move {source_path} - destination does not exist")
            return

        # Remove the source node from its current parent
        source_parent = source_node.parent
        del source_parent.children[source_node.name]

        # Add the source node to the destination's children
        source_node.parent = destination_node
        destination_node.children[source_node.name] = source_node
        print(f"MOVE {source_path} {destination_path}")

    def list(self):
        """
        Lists the full file system
        """
        print("LIST")
        self._list_recursive(self.root, level=0)

    def _list_recursive(self, directory: str, level: int):
        """
        Recursive helper function to list full file system
        """
        if directory != self.root:
            print("  " * (level - 1) + directory.name)
        for child_name in sorted(directory.children.keys()):
            self._list_recursive(directory.children[child_name], level + 1)

    def _navigate_to_node(self, path: str):
        """
        Helper method to navigate to a node, given a path name
        """
        parts = path.strip('/').split('/')
        current = self.root

        for part in parts:
            if part in current.children:
                current = current.children[part]
            else:
                return None
        return current
