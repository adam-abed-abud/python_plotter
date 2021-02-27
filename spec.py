SPEC = {
    "Root": {
        "fields": {
            "title": "str",
            "xlabel": "str",
            "ylabel": "str",
            "legend": "str",
           
        },
        "required_fields": [],
        "allowed_children": ["Line", "Scatter"],
    },
    "Line": {
        "fields": {
            "x": "data",
            "y": "data",
            "width": "length",
            "label": "label",
        },
        "required_fields": ["x", "y"],
        "allowed_children": [],
    },
    "Scatter": {
        "fields": {
            "x": "data",
            "y": "data",
            "width": "length",
            "size" : "length",
            "marker": "marker",
            "label": "label",
        },
        "required_fields": ["x", "y"],
        "allowed_children": [],
    },
}

