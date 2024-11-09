[
    "sequenz",
    ["setzen", "x", 100],
    
    ["setzen", "outer", 
        ["func", [], 
            ["sequenz",
                ["setzen", "x", 50],
                ["setzen", "inner", 
                    ["func", [], 
                        ["sequenz", ["bekommen", "x"]]
                    ]
                ],
                ["call", "inner"]
            ]
        ]
    ],

    ["call", "outer"],
    ["bekommen", "x"]
]
