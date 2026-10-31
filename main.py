from textual import *
from textual.app import *
from textual.widgets import *
from pathlib import Path
from tkinter import filedialog
from mutagen import File
from functools import lru_cache

import os
import json
import vlc

from extension import extensions_audio 


with open("config.json", "r") as f:
    configRead = f.read()
    config = json.loads(configRead)
    path = config["PATH"]


if path != "":
    firstIndentList = sorted(os.listdir(path))
else:
    path = filedialog.askdirectory()
    if not path.endswith("/") : 
        path = path+"/"
    config["PATH"] = path
    with open("config.json", "w") as f:
        f.write(json.dumps(config))
    firstIndentList = sorted(os.listdir(path))

@lru_cache(maxsize=None)
def read_tags(path: Path):
    try:
        audio = File(path, easy=True)
    except Exception:
        return None, None          # <- toujours un tuple
    if audio is None:
        return None, None
    title = audio.get("title", [None])[0]
    track = audio.get("tracknumber", [None])[0]
    return title, track

def parse_track(track) -> int:
    if track:
        try:
            return int(str(track).split("/")[0])
        except ValueError:
            pass
    return 9999

def sort_info(path: Path):
    if path.suffix.lower() not in extensions_audio:
        return (0, path.name.lower())
    title, track = read_tags(path)
    return (parse_track(track), (title or path.name).lower())

'''def build_tree(node, folder: Path):
    entries = sorted(
        os.listdir(folder),
        key =lambda name: (
            not (folder / name).is_dir(),
            *sort_info( folder / name),
        )
    )
    for name in entries:
        full = folder / name
        ext = full.suffix.lower()
        if ext in extensions_audio:
            title = read_tags(full)[0]
            node.add_leaf(title or name, data=full)
        elif full.is_dir():
            child = node.add(name, data=full)
            build_tree(child, full)
'''

def scan_folder(folder: Path):
    result = []
    entries = sorted(
        os.listdir(folder),
        key=lambda name: (
            not (folder / name).is_dir(),
            *sort_info(folder / name),
        ),
    )
    for name in entries:
        full = folder / name
        if full.is_dir():
            result.append((name, full, scan_folder(full)))
        elif full.suffix.lower() in extensions_audio:
            title = read_tags(full)[0]
            result.append((title or name, full, None))
    return result

def add_nodes(node, items):
    for label, full, children in items:
        if children is None:
            node.add_leaf(label, data=full)
        else:
            child = node.add(label, data=full)
            add_nodes(child, children)

class TheCure(App):

    BINDINGS = [
        ("p", "toggle_expand_all", "Toggle expand All"),
        Binding("space", "play_pause", "Toggle play/pause", priority= True),
    ]

    def compose(self) -> ComposeResult:
        tree: Tree[str] = Tree("Music " + path)
        tree.root.expand()

        yield Header()
        yield Tree("Music " + path, id="tree")
        yield Footer()

        #build_tree(tree.root, Path(path))

    def action_toggle_expand_all(self) -> None:
        tree = self.query_one(Tree)
        tree.root.toggle_all()

    def action_play_pause(self) -> None:
        state = self.player.get_state()
        if state == vlc.State.Playing:
            self.player.pause()
        elif state in ( vlc.State.Paused, vlc.State.Stopped ):
            self.player.play()

    def on_mount(self):
        self.player = vlc.MediaPlayer()
        tree = self.query_one(Tree)
        tree.loading = True
        self.sub_title = "Library is loading"
        self.load_library()

    @work(thread=True)
    def load_library(self) -> None:
        data = scan_folder(Path(path))
        self.call_from_thread(self.show_library, data)

    def show_library(self, data) -> None:
        tree = self.query_one(Tree)
        add_nodes(tree.root, data)
        tree.root.expand()
        tree.loading = False
        self.sub_title = ""

    

    def on_tree_node_selected(self, event : Tree.NodeSelected):
        file_path = event.node.data

        if file_path is None:
            return

        file_path = Path(file_path)

        if file_path.is_file() and file_path.suffix.lower() in extensions_audio:
            self.player.stop()
            self.player.set_media(
                vlc.Media(str(file_path))
            )
            self.player.play()

    def on_unmount(self):
        self.player.stop()
        self.player.release()



if __name__ == "__main__":
    app = TheCure()
    app.run()


# controleur de volume
# waveform
# l'image de la musique
# musique suivante et precedente bouton( + pause )
# bar de progression musique