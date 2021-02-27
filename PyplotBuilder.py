import typing as tp
import matplotlib.pyplot as plt
import numpy as np

class PyplotBuilder:
    def __init__(self) -> None:
        return
        

    def build(self, elem, pycode: str, canvas=None):
        _globals = globals()
        _globals["np"] = np

        self.vars = {}

        exec(pycode, _globals, self.vars)

        self.fig = plt.figure() if canvas is None else canvas
        
        return self._build(elem)


    def _build(self, elem):
        name, children, args = elem

        fn_name = f"_build_{name}"
       
        if not hasattr(self, fn_name):
            raise Exception(fn_name)
        
        return getattr(self, fn_name)(children, args)


    def _build_Root(self, children, args):
        self.ax = self.fig.gca()

        for child in children:
            self._build(child)

        if "title" in args.keys():
            self.fig.suptitle(args["title"])
      
        if "xlabel" in args.keys():
            self.ax.set_xlabel(args["xlabel"])
        if "ylabel" in args.keys():
            self.ax.set_ylabel(args["ylabel"])

        if "legend" in args.keys():
            label_pos=args["legend"]
        else:
            label_pos="best"



        plt.legend(loc=label_pos)

        return self.fig


    def _build_Line(self, children, args):
        x = self.vars[args["x"].name]
        y = self.vars[args["y"].name]

        linewidth = args["width"] if "width" in args.keys() else None
        label = args["label"] if "label" in args.keys() else None

        self.ax.plot(x, y, linewidth=linewidth, label=label)

    def _build_Scatter(self, children, args):
        x = self.vars[args["x"].name]
        y = self.vars[args["y"].name]

        linewidth = args["width"] if "width" in args.keys() else None
        marker = args["marker"] if "marker" in args.keys() else None
        size = args["size"] if "size" in args.keys() else None
        label = args["label"] if "label" in args.keys() else None

        self.ax.scatter(x, y, linewidth=linewidth, s=size, marker=marker.name, label=label)

