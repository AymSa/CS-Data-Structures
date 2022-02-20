class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None #Instance du noeud parent
        
    def addChild(self,child):
        child.parent = self #On spécifie que le noeud actuel est le parent du child
        self.children.append(child)
        
    def getLevel(self):
        lvl = 0
        p = self.parent
        while(p):
            lvl+=1
            p = p.parent
        return lvl
    
    def summary(self):
        spaces = ' ' * self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.summary()


if __name__ == '__main__':
    root = TreeNode("User")

    desktop = TreeNode("Desktop")
    desktop.addChild(TreeNode("Games"))
    desktop.addChild(TreeNode("Work"))
    desktop.addChild(TreeNode("Series"))

    download = TreeNode("Download")
    download.addChild(TreeNode("Ressources"))
    download.addChild(TreeNode("Tutorial"))

    document = TreeNode("Document")
    document.addChild(TreeNode("Images"))
    document.addChild(TreeNode("Videos"))
    document.addChild(TreeNode("Music"))

    root.addChild(desktop)
    root.addChild(download)
    root.addChild(document)
    
    root.summary()