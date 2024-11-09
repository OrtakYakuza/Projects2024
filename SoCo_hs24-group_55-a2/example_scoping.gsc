[
    "sequenz",
    ["setzen", "x", 100],
    
    ["setzen", "set_local_x", 
        ["func", [], 
            ["sequenz",
                ["setzen", "x", 42],
                ["bekommen", "x"]
            ]
        ]
    ],

    ["setzen", "get_global_x", 
        ["func", [], 
            ["sequenz",
                ["bekommen", "x"]
            ]
        ]
    ],

    ["call", "set_local_x"],
    ["call", "get_global_x"],
    ["bekommen", "x"]
]
