import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar
nav = Navbar()
body = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.Blockquote(
                                [
                                    html.H4("Hiring Workflow"),
                                    html.Footer(html.Small("Complete Hiring Solution", className="text-muted")),
                                ],
                                className="blockquote",
                                style={
                                    "align": "center"
                                }
                            )
                        ]
                    )
                ),
                width = 4
            ),
            justify = "center"
        )
    ],
className="mt-4",
)

def Homepage():
    layout = html.Div([nav,body])
    return layout
