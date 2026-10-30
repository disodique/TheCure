
'''
class StaticAndLabelApp(App):
    def compose(self):
        self.static = Static(
            "I am a [bold red] Static [/bold red] widget !",
        )
        yield self.static
        self.label = Label (
            "I am a [yellow italic]Label[/yellow italic] widget !",
        )
        yield self.label

    def on_mount(self):
        #Styling the static
        self.static.styles.background = "blue"
        self.static.styles.border = ("solid", "white")
        self.static.styles.text_align = "center"
        self.static.styles.padding = 1 , 1
        self.static.styles.margin = 4 , 4
        #Styling the label
        self.label.styles.background = "darkgreen"
        self.label.styles.border = ("double", "red")
        self.label.styles.padding = 1 , 1
        self.label.styles.margin = 4 , 4

class ButtonsAndInputsApp(App):
    def compose(self):
        # Buttons
        yield Button("Click me !")
        yield Button("Primary", variant="primary")
        yield Button.success("Success !")
        yield Button.warning("Warning !")
        yield Button.error("Error !")
        # Inputs
        yield Input(placeholder="Type your text here")
        yield Input(placeholder="Password", password=True)
        yield Input(
            placeholder="Type a number here",
            type="number",
            tooltip="Digits only please",
        )
'''


        # Loops to display folders
'''        for dirs in firstIndentList:
            ext = Path(dirs).suffix.lower()
            # First loop for first indentation
            if (ext in extensions_audio):
                tree.root.add_leaf("%s"%dirs,
                                    data=Path(path) / dirs)
                
            elif (ext in extensions_non_audio):
                pass
            else:
                languages = tree.root.add("%s"%dirs,
                                            data=Path(path) / dirs)
                
                SecondIndentList = sorted(os.listdir(Path(path) / dirs)) 
                for subdirs in SecondIndentList:
                    ext = Path(subdirs).suffix.lower()
                    if (ext in extensions_audio):
                        artists = languages.add_leaf(subdirs,
                                                        data=Path(path) / dirs / subdirs)
                        
                    elif (ext in extensions_non_audio):
                        pass
                    else:
                        artists = languages.add(subdirs,
                                                data = Path(path) / dirs / subdirs)
                        
                        ThirdIndentList = sorted(os.listdir(Path(path) / dirs / subdirs))
                        for secondSubDirs in ThirdIndentList:
                            ext = Path(secondSubDirs).suffix.lower()
                            if (ext in extensions_audio):
                                titles = artists.add_leaf(secondSubDirs,
                                                            data = Path(path) / dirs / subdirs / secondSubDirs)
                                
                            elif (ext in extensions_non_audio):
                                pass
                            else:
                                albums = artists.add(secondSubDirs,
                                                        data = Path(path) / dirs / subdirs / secondSubDirs)
                                
                                FourthIndentList = os.listdir(Path(path) / dirs / subdirs / secondSubDirs)
                                for thirdSubDirs in FourthIndentList:
                                    ext = Path(thirdSubDirs).suffix.lower()
                                    if (ext in extensions_audio):
                                        titles = albums.add_leaf(thirdSubDirs,
                                                                    data = Path(path) / dirs / subdirs / secondSubDirs / thirdSubDirs)

                                    elif (ext in extensions_non_audio):
                                        pass
                                    else:
                                        titlesSub = albums.add(thirdSubDirs,
                                                                data = Path(path) / dirs / subdirs / secondSubDirs / thirdSubDirs)
                                        
                                        FifthIndentList = os.listdir(Path(path) / dirs / subdirs / secondSubDirs / thirdSubDirs)
                                        for fourthSubDirs in FifthIndentList:
                                            ext = Path(fourthSubDirs).suffix.lower()
                                            if (ext in extensions_audio):
                                                titles = titlesSub.add_leaf(fourthSubDirs,
                                                                            data = Path(path) / dirs / subdirs / secondSubDirs / thirdSubDirs / fourthSubDirs)
                                                
                                            elif (ext in extensions_non_audio):
                                                pass
                                            else:
                                                ThirdAlbums = albums.add(fourthSubDirs,
                                                                            data = Path(path) / dirs / subdirs / secondSubDirs / thirdSubDirs / fourthSubDirs)
'''