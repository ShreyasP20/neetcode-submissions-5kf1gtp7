class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split("/")
        path_stck = []
        for i in split_path:
            if i == "..":
                if path_stck != []:
                    path_stck.pop()
            elif i != "." and i != "":
                path_stck.append(i)

        return "/" + "/".join(path_stck)
